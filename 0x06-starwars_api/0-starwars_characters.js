#!/usr/bin/node

import requests
import sys

def get_movie_characters(movie_id):
    base_url = "https://swapi.dev/api/"

    film_url = f"{base_url}films/{movie_id}/"
    film_response = requests.get(film_url)
    film_data = film_response.json()

    character_urls = film_data.get('characters', [])

    characters = []
    for character_url in character_urls:
        character_response = requests.get(character_url)
        character_data = character_response.json()
        characters.append(character_data['name'])

    return characters

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <Movie ID>")
        sys.exit(1)

    movie_id = sys.argv[1]

    try:
        characters = get_movie_characters(movie_id)
        print(f"Characters in Star Wars Episode {movie_id}:")
        for character in characters:
            print(character)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
