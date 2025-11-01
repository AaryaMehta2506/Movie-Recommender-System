Data Science Beginners Project
# Movie Recommender System

A content-based Movie Recommender System built with Python, Pandas, Scikit-learn, and Streamlit. It recommends similar movies based on genres, cast, crew, and keywords from movie metadata.

##  Features
Content-based movie recommendations using cosine similarity
Intelligent parsing of genres, cast, crew, and keywords
Streamlit interactive web interface
Clean, fast, and user-friendly design
Optimized for medium-sized datasets

## Tech Stack
Python 3.10+
Streamlit
Pandas
NumPy
Scikit-learn
Ast / JSON

## Dataset
This system uses The Movies Dataset 
Link : https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?select=movies_metadata.csv

Required files:
- movies_metadata.csv
- credits.csv
Both must be placed in the same project directory as app.py

## Installation & Run
git clone https://github.com/AaryaMehta2506/Movie-Recommender-System.git

cd movie-recommender-system
python -m venv venv
venv\Scripts\activate         # For Windows
# source venv/bin/activate    # For Mac/Linux
pip install -r requirements.txt
streamlit run app.py

## Project Structure
movie-recommender-system/
│
├── app.py                        # Streamlit app
├── movie_recommender_system.ipynb # Model building notebook
├── movies_metadata.csv            # Movie metadata
├── credits.csv                    # Cast & crew metadata
├── requirements.txt               # Dependencies
└── README.md                      # Documentation

## requirements.txt
streamlit
pandas
numpy
scikit-learn
tqdm
ast

## How To Use
1. Run the app
2. Enter a movie name (e.g. "Avatar" or "The Dark Knight")
3. Click Recommend
4. Instantly get similar movies displayed

## Example Movie Names
Avatar
The Dark Knight
Inception
Interstellar
Iron Man
Pulp Fiction
Forrest Gump

## Contributing
Contributions are welcome!
Feel free to fork the repository, improve the game, and open a pull request. Let's grow this classic game together!

## License
This project is licensed under the [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)

## Author
**Aarya Mehta**  
🔗 [GitHub Profile](https://github.com/AaryaMehta2506)
