from pydantic import BaseModel

class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int

class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def get_book_by_id(self, book_id: int) -> Book:
        for book in self.books:
            if book.id == book_id:
                return book
        return None

    def update_book(self, book_id: int, new_book: Book):
        for i, book in enumerate(self.books):
            if book.id == book_id:
                self.books[i] = new_book
                return True
        return False

    def delete_book(self, book_id: int) -> bool:
        for i, book in enumerate(self.books):
            if book.id == book_id:
                del self.books[i]
                return True
        return False

# Create a book manager instance
book_manager = BookManager()