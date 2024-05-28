from flask import Flask, render_template, request, jsonify
import json
import random

app = Flask(__name__, static_folder='static')

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
    random_recommendations = random.sample(recommendations, min(3, len(recommendations)))
    return render_template('recommendations.html', recommendations=random_recommendations, query=query)

@app.route('/shuffle', methods=['POST'])
def shuffle():
    query = request.json['query']
    movies = load_movies('data/movies.json')
    recommendations = get_recommendations(movies, query)
    random_recommendations = random.sample(recommendations, min(3, len(recommendations)))
    return jsonify(random_recommendations)

if __name__ == "__main__":
    app.run(debug=True)
