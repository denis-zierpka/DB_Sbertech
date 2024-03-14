from pymongo import MongoClient
import csv
from pprint import pprint


def fast_p(data):
    print()
    for i in data:
        pprint(i)
    print()


host = 'localhost' 
port = 27017
username = 'root' 
password = 'example' 
db_name = 'database' 

mongo_uri = f"mongodb://{username}:{password}@{host}:{port}"
with MongoClient(mongo_uri) as client:
    db = client[db_name]
    t = db.titanic

    with open('./titanic.csv', 'r') as input_file:
        answer = [i for i in csv.DictReader(input_file)]

    t.delete_many({})
    result = t.insert_many(answer)
    print('Insert: ', True if result else False)


    # Запросы на выборку
    first_class_passengers = t.find({'Pclass': '1'}).limit(3)
    fast_p(first_class_passengers)

    passenger_by_name = t.find_one({'Name': 'Mr. William Henry Allen'})
    print(passenger_by_name)

    survivors = t.find({'Survived': '1', 'Sex': 'male'}).limit(3)
    fast_p(survivors)


    # Запросы на обновление
    t.update_one({'Name': 'Mr. William Henry Allen'}, {'$set': {'Survived': '1'}})
    t.update_many({'Fare': {'$gt': 50}}, {'$set': {'Pclass': '1'}})

    # Запросы на удаление
    t.delete_one({'Name': 'Mr. William Henry Allen'})
    t.delete_many({'Survived': '0'})
    t.delete_many({'Age': {'$lt': '18'}})


