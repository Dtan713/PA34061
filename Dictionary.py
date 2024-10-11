import json

# Initialize the movie database
movies = {}

def load_movies(filename):
    global movies
    try:
        with open(filename, 'r') as file:
            movies = json.load(file)
            print("Movies loaded successfully.")
    except FileNotFoundError:
        print("No saved movie database found. Starting fresh.")
    except json.JSONDecodeError:
        print("Error reading the movie database file.")

def save_movies(filename):
    with open(filename, 'w') as file:
        json.dump(movies, file, indent=4)
        print("Movies saved successfully.")

def add_movie():
    title = input("Enter movie title: ")
    genre = input("Enter genre: ")
    director = input("Enter director: ")
    year = input("Enter release year: ")
    actors = input("Enter actors (comma-separated): ").split(",")
    
    movies[title] = {
        "year": int(year),
        "genre": genre,
        "director": director,
        "actors": [actor.strip() for actor in actors]
    }
    print(f"Movie '{title}' added successfully.")

def edit_movie():
    title = input("Enter the title of the movie you want to edit: ")
    if title in movies:
        print("Current details:", movies[title])
        genre = input("Enter new genre (leave blank to keep current): ")
        director = input("Enter new director (leave blank to keep current): ")
        year = input("Enter new release year (leave blank to keep current): ")
        actors = input("Enter new actors (comma-separated, leave blank to keep current): ")

        if genre:
            movies[title]["genre"] = genre
        if director:
            movies[title]["director"] = director
        if year:
            movies[title]["year"] = int(year)
        if actors:
            movies[title]["actors"] = [actor.strip() for actor in actors.split(",")]
        
        print(f"Movie '{title}' updated successfully.")
    else:
        print("Movie not found.")

def delete_movie():
    title = input("Enter the title of the movie you want to delete: ")
    if title in movies:
        del movies[title]
        print(f"Movie '{title}' deleted successfully.")
    else:
        print("Movie not found.")

def view_movies():
    if movies:
        for title, details in movies.items():
            print(f"\nTitle: {title}")
            for key, value in details.items():
                print(f"{key.capitalize()}: {value}")
    else:
        print("No movies in the database.")

def search_movies():
    criteria = input("Enter title, genre, director, or actor to search: ").lower()
    results = {title: details for title, details in movies.items() if (
        criteria in title.lower() or
        criteria in details["genre"].lower() or
        criteria in details["director"].lower() or
        any(criteria in actor.lower() for actor in details["actors"])
    )}

    if results:
        for title, details in results.items():
            print(f"\nTitle: {title}")
            for key, value in details.items():
                print(f"{key.capitalize()}: {value}")
    else:
        print("No movies found matching the criteria.")

def main():
    filename = "movies.json"
    load_movies(filename)

    while True:
        print("\nMovie Database Management System")
        print("1. Add a new movie")
        print("2. Edit a movie")
        print("3. Delete a movie")
        print("4. View all movies")
        print("5. Search movies")
        print("6. Save changes")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == '1':
            add_movie()
        elif choice == '2':
            edit_movie()
        elif choice == '3':
            delete_movie()
        elif choice == '4':
            view_movies()
        elif choice == '5':
            search_movies()
        elif choice == '6':
            save_movies(filename)
        elif choice == '7':
            save_movies(filename)
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
