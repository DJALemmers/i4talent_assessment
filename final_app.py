from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Load the trained RSF model
print("Loading model...")
rsf = joblib.load("rsf_model.pkl")
print("Model loaded successfully!")

@app.route("/predict_survival_model", methods=["POST"])
def predict_survival():
    print("Running predict_survival")
    try:
        # Parse input JSON
        input_data = request.get_json()
        compute_ci = input_data.get("compute_ci", False)  # Optional CI flag (default: False)

        # Convert input data to DataFrame
        df = pd.DataFrame(input_data["data"])

        # Ensure required columns exist
        required_columns = {"geboortedatum", "lengte_dienst"}
        if not required_columns.issubset(df.columns):
            return jsonify({"error": f"Missing required columns: {required_columns - set(df.columns)}"}), 400

        # Compute 'age' based on 'geboortedatum'
        df["geboortedatum"] = pd.to_datetime(df["geboortedatum"], errors="coerce")
        df["leeftijd"] = datetime.now().year - df["geboortedatum"].dt.year  # Convert birthdate to age

        # Use only the features the model was trained on
        model_input = df[["lengte_dienst", "leeftijd"]]

        print("*** Predicting survival functions...")
        # Predict survival functions for all employees
        survival_predictions = rsf.predict_survival_function(model_input)

        # Define time range (0-25 years)
        years = range(0, 25)

        # Store survival odds for each individual
        survival_odds = {}
        people_left = []
        ci_lower = []
        ci_upper = []
        n_bootstraps = 1000  # Bootstrap iterations

        # Compute outflow projections
        for time_point in years:
            survival_at_time = [fn(time_point) for fn in survival_predictions]
            survival_at_time = pd.Series(survival_at_time)

            # Compute number of people still in company
            still_in_company = (survival_at_time > 0.5).sum()
            predicted_people_left = len(model_input) - still_in_company
            people_left.append(predicted_people_left)

            # Compute 95% CI if requested
            if compute_ci:
                bootstrap_samples = []
                for _ in range(n_bootstraps):
                    sample = survival_at_time.sample(frac=1, replace=True)
                    still_in_company_boot = (sample > 0.5).sum()
                    predicted_people_left_boot = len(model_input) - still_in_company_boot
                    bootstrap_samples.append(predicted_people_left_boot)

                ci_lower.append(int(np.percentile(bootstrap_samples, 2.5)))
                ci_upper.append(int(np.percentile(bootstrap_samples, 97.5)))
            else:
                ci_lower.append(None)
                ci_upper.append(None)

        # Convert results to appropriate types
        people_left = [int(val) for val in people_left]
        ci_lower = [None if val is None else float(val) for val in ci_lower]
        ci_upper = [None if val is None else float(val) for val in ci_upper]

        # Return results as JSON
        return jsonify({
            "est_people_left": people_left,
            "ci_lower": ci_lower if compute_ci else "Not Computed",
            "ci_upper": ci_upper if compute_ci else "Not Computed",
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Run the app
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
