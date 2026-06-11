import os
import json

class Movie:
    def __init__(self, title, year, genre, rating, watched=False):
        
        if rating < 0 or rating > 10:
            raise ValueError("Rating must be between 0 and 10") 
        
        self.title = title
        self.year = year
        self.genre = genre
        self.__rating = rating
        self.watched = watched

    def get_rating(self):
        return self.__rating
    
    def set_rating(self, new_rating):
        if new_rating <0 or new_rating>10:
            raise ValueError("Rating must be between 0 and 10")
        self.__rating = new_rating
        
    def mark_as_watched(self):
        self.watched = True  # Override the watched method to return True
    
    def mark_as_unwatched(self):
        self.watched = False  # Override the watched method to return False

    def to_dict(self):
        return {
            "title": self.title,
            "year": self.year,
            "genre": self.genre,
            "rating": self.__rating,
            "watched": self.watched         
        }

    def __str__(self):
        status = "[WATCHED]" if self.watched else "[UNWATCHED]"
        return f"{self.title} ({self.year}) - {self.genre} - {self.__rating}/10- {status}"

class Watchlist:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        """Add a Movie object to the watchlist."""
        self.movies.append(movie)
        print(f"✓ Added: {movie.title}")

    def remove_movie(self, title):
        """Remove a movie by title. If not found, print a message."""
        for m in self.movies:
            if m.title.lower() == title.lower():
                self.movies.remove(m)
                print(f"✓ Removed: {title}")
                return
        print(f"⚠️ Movie '{title}' not found")

    def mark_as_watched(self, title):
        """Mark a movie as watched by title."""
        for m in self.movies:
            if m.title.lower() == title.lower():
                m.mark_as_watched()
                print(f"✓ Marked as watched: {m.title}")
                return
        print(f"⚠️ Movie '{title}' not found")

    def mark_as_unwatched(self, title):
        """Mark a movie as unwatched by title."""
        for movie in self.movies:
            if movie.title.lower() == title.lower():
                movie.mark_as_unwatched()
                print(f"✓ Marked as unwatched: {title}")
                return
        print(f"⚠️ Movie '{title}' not found")

    def show_all(self):
        """Print all movies in the watchlist."""
        if not self.movies:
            print("Your watchlist is empty.")
            return
        for i,m in enumerate(self.movies,start=1):
            print(f"{i}.{m}")
            
    def show_watched(self):
        """Return list of movies that are marked as watched."""
        watched_movies= [m for m in self.movies if m.watched]
        if not watched_movies:
            print("No movies watched yet.")
            return
        for i, m in enumerate(watched_movies, start =1):
            print(f"{i}.{m}")
    
    def show_unwatched(self):
        """Return list of movies that are marked as unwatched."""
        unwatched_movies= [m for m in self.movies if not m.watched]
        if not unwatched_movies:
            print("No unwatched movies.")
            return
        for i, m in enumerate(unwatched_movies, start =1):
            print(f"{i}.{m}")
    
    def average_rating(self):
        """Calculate and return the average rating of all movies in the watchlist."""
        if not self.movies:
            return 0
        return sum(m.get_rating() for m in self.movies) / len(self.movies)
    
    def find_by_genre(self, genre_query):
        """Return list of movies whose genre contains genre_query (case-insensitive)."""
        return [m for m in self.movies if genre_query.lower() in m.genre.lower()]   
    
    def find_by_min_rating(self, min_rating):
        """Return list of movies with rating >= min_rating."""
        return [m for m in self.movies if m.get_rating() >= min_rating]
    
    def save_to_file(self, movielist):
        with open(movielist, "w") as file:
            json.dump([p.to_dict() for p in self.movies], file, indent=4)
        print(f"✓ Saved {len(self.movies)} movies to {movielist}")

    def load_from_file(self, movielist):
        if not os.path.exists(movielist):
            print(f"(No existing file '{movielist}' — starting empty.)")
            return
        try:
            with open(movielist, "r") as file:
                data = json.load(file)
        except json.JSONDecodeError:
            print(f"(File '{movielist}' is empty or corrupt — starting empty.)")
            return
        for d in data:
            movie = Movie(d["title"], d["year"], d["genre"], d["rating"], d["watched"])
            self.movies.append(movie)
        print(f"✓ Loaded {len(self.movies)} products from {movielist}")

    
#Test code
FILENAME = "movies.json"
wl = Watchlist()

wl.add_movie(Movie("Inception", 2010, "Sci-Fi", 8.8))
wl.add_movie(Movie("The Godfather", 1972, "Crime", 9.2))
wl.add_movie(Movie("Toy Story", 1995, "Animation", 8.3))
wl.add_movie(Movie("Interstellar", 2014, "Sci-Fi", 8.6))

print("\n--- ALL MOVIES ---")
wl.show_all()

# Mark a couple as watched
wl.mark_as_watched("Inception")
wl.mark_as_watched("Toy Story")

print("\n--- WATCHED ---")
wl.show_watched()

print("\n--- UNWATCHED ---")
wl.show_unwatched()

print("\n--- SCI-FI MOVIES ---")
for m in wl.find_by_genre("Sci-Fi"):
    print(m)

print("\n--- HIGHLY RATED (>= 8.5) ---")
for m in wl.find_by_min_rating(8.5):
    print(m)

print(f"\nAverage rating: {wl.average_rating():.2f}")

# Try invalid rating
try:
    Movie("Bad Movie", 2020, "Drama", 15)
except ValueError as e:
    print(f"\n⚠️ {e}")

# Remove a movie
wl.remove_movie("The Godfather")

print("\n--- AFTER REMOVAL ---")
wl.show_all()

# Try removing missing
wl.remove_movie("Avatar")

print("\n=== TEST PERSISTENCE ===")
wl.save_to_file(FILENAME)

# Restart with new Watchlist
wl2 = Watchlist()
wl2.load_from_file(FILENAME)

print("\n--- After 'restart', loaded watchlist: ---")
wl2.show_all()

print("\n--- Verify watched state survived: ---")
wl2.show_watched()