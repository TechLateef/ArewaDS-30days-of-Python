
# let's import the flask
from flask import Flask, render_template
import os # importing operating system module
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pymongo
MONGODB_URI = 'mongodb+srv://lateef:u2ws9q7EM7FyHpAA@cluster0.qdu7f0n.mongodb.net/?retryWrites=true&w=majority'
# client = pymongo.MongoClient(MONGODB_URI)
client = MongoClient(MONGODB_URI,server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
# Creating database
db = client.thirty_days_of_python
# Creating students collection and inserting a document
db.students.insert_one({'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250})
print(client.list_database_names())

students = [
        {'name':'David','country':'UK','city':'London','age':34},
        {'name':'John','country':'Sweden','city':'Stockholm','age':28},
        {'name':'Sami','country':'Finland','city':'Helsinki','age':25},
    ]
for student in students:
    db.students.insert_one(student)

app = Flask(__name__)
if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)