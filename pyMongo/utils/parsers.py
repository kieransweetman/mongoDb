import json
import datetime
import dateparser

def parse_data(json_path, coll_names, db):
    with open(json_path, 'r') as file:
        json_data = json.load(file)
    
    for name in coll_names:
        collection = json_data[name]
        
        for item in collection:
            if name == 'books':
                parse_book(item, db)
            if name == 'authors':
                parse_author(item, db)
    

def parse_book(book, db):
    book['year'] = datetime.datetime.strptime(str(book['year']), "%Y")
    author = db['authors'].find_one({'name': book['author']})
    
    book['author'] = author['_id']
    db['books'].insert_one(book)    
    
    
def parse_author(author, db):
    if type(author['birth']) == str:
        author['birth'] = dateparser.parse(author['birth'], languages=['fr'])
    
    db['authors'].insert_one(author)
