from flask import Flask, request, json
import pymongo

mongo_client = pymongo.MongoClient("localhost", 27017)
database = mongo_client.mietteet
app = Flask(__name__)

@app.route("/mietteet", methods = ["GET", "POST"])
def mietteet():
    print(f"Received a request {request.remote_addr}: {request.method} /mietteet")
    if request.method == "POST":
        payload = json.loads(request.data.decode("iso-8859-1"))
        database.mietteet.insert_one(payload)
        return f"Inserted: {payload} into the database!"
    elif request.method == "GET":
        data = list(map(lambda x: str(x), database.mietteet.find({})))
        return data

if __name__ == "__main__":
    print(f"Database connection.. {database.command('ping')}")
    app.run(debug = True)