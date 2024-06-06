from fastapi import FastAPI, HTTPException, Path
from models import Book, book_manager
from typing import List

app = FastAPI()

def create_book(book: Book):
    book_manager.add_book(book)
    return book

@app.get("/books/", response_model=List[Book])
def get_all_books():
    return book_manager.books

@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, new_book: Book):
    if not book_manager.update_book(book_id, new_book):
        raise HTTPException(status_code=404, detail="Book not found")
    return new_book

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    if not book_manager.delete_book(book_id):
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)