import cv2
import requests
from Book.BookModel import BookModel

cap = cv2.VideoCapture(0)
# initialize the cv2 QRCode detector
detector = cv2.barcode.BarcodeDetector()


def scan_barcode():
    isbn = ''
    while True:
        _, img = cap.read()

        # detect and decode
        data, bbox, _ = detector.detectAndDecode(img)
        # check if there is a QRCode in the image
        if data:
            isbn = data
            break

        cv2.imshow("Barcode Scanner", img)
        if cv2.waitKey(1) == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
    return isbn


def get_book_information():
    isbn = scan_barcode()
    url = "https://www.googleapis.com/books/v1/volumes?q=isbn:" + str(isbn)
    # b = webbrowser.open(str(URL))
    r = requests.get(url=url)

    data = r.json()

    if not data:
        print("Could not fetch data. Try again!")

    else:
        book = BookModel()
        book.title = data["items"][0]["volumeInfo"]["title"]

        # todo add this option to book model
        # book.authors = data["items"][0]["volumeInfo"]["authors"][0]
        # book.publisher = data["items"][0]["volumeInfo"]["publisher"]
        # book.publishedDate = data["items"][0]["volumeInfo"]["publishedDate"]
        # book.desc = data["items"][0]["volumeInfo"]["description"]
        # book.pageCount = data["items"][0]["volumeInfo"]["pageCount"]
        # book.avgRating = data["items"][0]["volumeInfo"]["averageRating"]
        # book.image = data["items"][0]["volumeInfo"]["imageLinks"]["thumbnail"]
        return book
