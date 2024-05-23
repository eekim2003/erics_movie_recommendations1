from flask import Flask, render_template, request
import json

app = Flask(__name__)

def load_movies(file_path):
    with open(file_path, 'r') as file:
        movies = json.load(file)
    return movies

def get_recommendations(movies, query):
    recommendations = [movie for movie in movies if query.lower() in movie['title'].lower() or query.lower() in movie['genre'].lower()]
    return recommendations

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommendations', methods=['POST'])
def recommendations():
    query = request.form['query']
    movies = load_movies('data/movies.json')
    recommendations = get_recommendations(movies, query)
    return render_template('recommendations.html', recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)
