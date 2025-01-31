# i4talent_assessment

Deze repository bevat de oplossing voor de i4talent-assessment.

## Inhoudsopgave

- [Projectoverzicht](#projectoverzicht)  
- [Bestandsstructuur](#bestandsstructuur)  
- [Installatie](#installatie)  
- [Gebruik](#gebruik)  
- [Dependencies](#depedencies)  


## Projectoverzicht

Dit project richt zich op de vereisten zoals beschreven in `data_science_(junior)_case.pdf`.  
De oplossing omvat data-analyse, modelontwikkeling en een Flask-applicatie om de resultaten te demonstreren.

## Bestandsstructuur

- **`data_science_(junior)_case.pdf`** - De assessment-opdracht met projectvereisten.  
- **`i4talent.csv`** - De dataset die wordt gebruikt voor analyse.  
- **`main.ipynb`** - Het Jupyter-notebook met data-exploratie en modelontwikkeling.  
- **`Flask_test.ipynb`** - Een Jupyter-notebook voor het testen van de Flask-applicatie.  
- **`final_app.py`** - Het script van de Flask-applicatie.  
- **`requirements.txt`** - Een lijst met Python-pakketten die nodig zijn om het project uit te voeren.  
- **`rsf_model.pkl`** - Het geserialiseerde modelbestand.  
- **`Scratchbook.ipynb`** - Een aanvullend notebook voor verkennende analyse.  
- **`.gitignore`** - Bepaalt welke bestanden en mappen door git genegeerd moeten worden.  

## Installatie

1. **Clone de repository:**

   ```bash
   git clone https://github.com/DJALemmers/i4talent_assessment.git
   cd i4talent_assessment

2. **Instaleer vereiste packages:**
   ```bash
   pip install -r requirements.txt	

## Gebruik

1. Data-analyse en modelontwikkeling

Open en voer main.ipynb notebook uit om de data te verkennen en het model te ontwikkelen.

2. Flask-applicatie

Start de Flask-applicatie met:
   ``` bash
   python final_app.py

De API kan dan lokaal benaderd worden, voor een voorbeeld zie `Flask_test.ipynb`

## Depedencies

Het project maakt gebruik van verschillende Python-packages die vermeld staan in requirements.txt.
Belangrijke dependencies zijn onder andere:

    Flask
    Pandas
    Scikit-learn
    Jupyter

