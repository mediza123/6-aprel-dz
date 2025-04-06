from typing import List, Dict, Optional

class Movie:
    genre_categories: List[str] = ["Action", "Comedy", "Drama", "Horror", "Sci-Fi"]
    rating_system: Dict[str, str] = {"G": "General", "PG": "Parental Guidance", "R": "Restricted"}

    def __init__(self, title: str, director: str, year: int, duration: int, rating: str) -> None:
        self.title = title
        self.director = director
        self.year = year
        self.duration = duration
        self.rating = rating
        self.reviews: List[str] = []
    
    def __str__(self) -> str:
        return f"{self.title} ({self.year}), directed by {self.director}"
    
    def add_review(self, review: str) -> None:
        self.reviews.append(review)
    
    def get_age(self, current_year: int) -> int:
        return current_year - self.year
    
    def is_long(self) -> bool:
        return self.duration > 120
    
    def update_rating(self, new_rating: str) -> None:
        if new_rating not in self.rating_system:
            raise ValueError("Invalid rating")
        self.rating = new_rating

