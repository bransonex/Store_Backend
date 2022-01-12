from flask import Flask
from mock_data import catalog
import json

app = Flask (_name_)

me = {
    'name': 'Kvon',
    'last': 'Smith',
    'age': 29,
    'hobbies': [],
    'address': {
        'street': 'Windy Hill',
        'number': 32,   
        'city': 'Madison'
        }
}
@app.route("/", methods=['GET'])
def home():
    return "Hi There"

@app.route("/test")
def home():
    return "Hello from Python"

@app.route("/about")
def about():
return me["name"] + "" + me["last"]

@app.route("/api/catalog")
def get_catalog
# TODO: read the catalog form a database
return json.dumps(catalog)

@app.route("/api/catalog", methods=["post"])
def save_product():
product = request.get_json()
print(product)

return "OK"


@app.route("/api/cheapest")
def get_cheapest():
    # find the cheapest proudct on the catalog list
    # 1 - travel the list
    # 2 - print the price on the console
    cheap = catalog[0]
    for product in catalog:
        print(product["price"]) < cheap["price"]:
        cheap = product 

    #  return it as json
    return json.dumps(cheap)

@app.route("/api/product/<id>")
def get_product(id)

for product in catalog:
    if proudct["_id"] == id:
        return json.dumps(product)

return "NOT FOUND"


@app.route("/api/catalog/<category>")
def get_by_category(category):
    result = []
    for product in catalog:
        if proudct["category"].lower() == category:
            result.append(product)
           
            return json.dumps(result)

app.run(debug=True)