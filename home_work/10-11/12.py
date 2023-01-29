import csv
def open_db():
    with open('db_market.csv', encoding='utf-8') as file_db:
        db = list(csv.DictReader(file_db))
        print(db)
        print(type(db))
        return db
open_db()