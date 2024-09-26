from utils.parsers import parse_author, parse_book
import datetime

class Exerices:
    
    def __init__(self, db):
        self.db = db
    
    def run(self):
        print('adding new book\n---')
        self.add_new_book()
        print('editing book price\n---')
        self.edit_book_price('The Alchemist', 'price', 9.99)
        print('deleting book\n---')
        self.delete_book('Le Petit Prince')
        print('finding books before 1900\n---')
        self.find_books_before("1900")
        print('finding books after 1980\n---')
        self.find_books_after("1980")
        print('searching for books with title containing "the"\n---')
        self.search_title('le')    
    
    def add_new_book(self):
        new_book = {
            "title": "The Alchemist",
            "author": "Paulo Coelho",
            "year": 1988,
            "category": "Fiction",
            "price": 7.99
        }
        
        author = self.db['authors'].find_one({'name': 'Paulo Coelho'})
        if author is None:

            author = {
                "name": "Paulo Coelho",
                "country": "Brazil",
                "birth": datetime.datetime(1947, 8, 24)
            }
            parse_author(author, self.db)
            
        parse_book(new_book, self.db)

    def edit_book_price(self, title, attribute, value):
        self.db['books'].update_one({'title': title}, {'$set': {attribute: value}})
        
    def delete_book(self, title):
        self.db['books'].delete_one({'title': title})
        
    def find_books_before(self, year):
        books = self.db['books'].find({'year': {'$lt': datetime.datetime.strptime(year, "%Y")}})
        
        for book in books:
            print(book)

    def find_books_after(self, year):
        books = self.db['books'].find({'year': {'$gt': datetime.datetime.strptime(year, "%Y")}})
        
        for book in books:
            print(book)
            
    def search_title(self, title):
        books = self.db['books'].find({'title': {'$regex': title, '$options': 'i'}})
        
        for book in books:
            print(book)