import requests

from barcodeScanner import get_book_information


def add_book_to_collection():
    URL = "https://www.googleapis.com/books/v1/mylibrary/bookshelves"
    r = requests.get(url=URL)

    data = r.json()
    book = get_book_information()