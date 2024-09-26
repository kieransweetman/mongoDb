from pymongo import MongoClient
from pymongo.collection import Collection

from utils.Exerices import Exerices
from utils.parsers import parse_data

client = MongoClient('localhost', 27017)


   
book_validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["title", "author", "year", "category", "price"],
        "properties": {
            "title": {
                "bsonType": "string",
                "description": "must be a string and is required"
            },
            "author": {
                "bsonType": "objectId",
                "description": "must be an ObjectId referencing an author and is required"
            },
            "year": {
                "bsonType": "date",
                "description": "must be a date and is required"
            },
            "category": {
                "bsonType": "string",
                "description": "must be a string"
            },
            "price": {
                "bsonType": "double",
                "description": "must be a double greater than 0 and \
                is required",
                "minimum": 0
            }
        }
    }
}

author_validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["name", "country", "birth"],
        "properties": {
            "name": {
                "bsonType": "string",
                "description": "must be a string and is required"
            },
            "country": {
                "bsonType": "string",
                "description": "must be an array and is required",
            },
            "birth": {
                "bsonType": "date",
                "description": "must be a date and is required"
            }
        }
    }
}

book_pipelines = {
    "books_by_cat_pipeline":  [
        {
            '$group': {
                '_id': '$category',
                'count': {'$sum': 1}
            }
        }
    ],
    "avg_price_per_cat_pipeline": [
        {
            '$group': {
                '_id': '$category',
                'avg_price': {'$avg': '$price'}
            }
        }
    ],
    
    "count_by_year_desc_pipeline": [
        {
            '$group': {
                '_id': {'$year': '$year'},
                'count': {'$sum': 1}
            }
        },
        {
            '$sort': {'count': -1}
        }
    ],
    
    "cat_with_highest_avr_price_pipeline": [
        {
            '$group': {
                '_id': '$category',
                'avg_price': {'$avg': '$price'}
            },
        },
        {
            '$sort': {'avg_price': -1}
        },
        {
            '$limit': 1
        }
    ],
    "num_books_per_author_pipeline_desc": [
         {
            '$group': {
                '_id': '$author',
                'num_books': {'$sum': 1}
            }
        },
        {
            '$sort': {'num_books': -1}
        }
    ]
}




try:
    db = client['library']

   
    book_collection = db.create_collection('books')
    author_collection = db.create_collection('authors')
    
    db.command("collMod", 'books', validator=book_validator)
    db.command("collMod", 'authors', validator=author_validator)
    
    json_path = "./tp3_library_en.json"
    parse_data(json_path, ['authors', 'books'], db) 
    
    Exerices(db).run()
    
    def aggregate(collection: Collection, pipelines):
        for p in pipelines:
            result = collection.aggregate(p).to_list()
            print(result)
    
    aggregate(book_collection, book_pipelines.values())
    
    
    
    
    
    

except Exception as e :
    print(e)
    
finally:
    db.drop_collection('books')
    db.drop_collection('authors')







