import json

def load_movies(file_path):
    with open(file_path, 'r') as file:
        movies = json.load(file)
    return movies

def get_recommendations(movies, query):
    recommendations = [movie for movie in movies if query.lower() in movie['title'].lower() or query.lower() in movie['genre'].lower()]
    return recommendations

def display_recommendations(recommendations):
    if recommendations:
        print("Here are some movie recommendations based on your search:")
        for movie in recommendations:
            print(f"- {movie['title']} ({movie['genre']}) ({movie["Eric's Rating"]})")
    else:
        print("No recommendations found for your query.")

def main():
    movies = load_movies('data/movies.json')
    while True:
        query = input("Enter a letter, word, or movie genre (Action, Drama, Sci-Fi) \n(or 'exit' to quit): ").strip()
        if query.lower() == 'exit':
            break
        recommendations = get_recommendations(movies, query)
        display_recommendations(recommendations)

if __name__ == "__main__":
    main()
