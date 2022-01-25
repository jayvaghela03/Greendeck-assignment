# This module provides helper method dumps that wrap the native json methods and provide BSON conversion to & from JSON
from bson.json_util import dumps

# Importing flask,jsonify and request for performing required requests and provide jsonified output
from flask import Flask, jsonify, request

# Importing flask_pymongo which will run our flask app with mongodb support
from flask_pymongo import PyMongo

# Using bson.objectid() to get an ObjectId for user, so we can reference it later on in our code without having to worry
# about collisions or duplicates when inserting new users into MongoDB
from bson.objectid import ObjectId

# Creating instance of flask called app, This instance will be used for all requests made in this program
app = Flask(__name__)
# Configuring the app with a MONGO_URI, This is the address of MongoDB,It will be used to store data in this application
app.config['MONGO_URI'] = "mongodb://localhost:27017/JAY_VAGHELA"
# Created a variable called mongo that is set to point at our PyMongo class from flask-pymongo library
mongo = PyMongo(app)


# The first request is for '/'
# This function is used to handle the HTTP requests that come in
# Defining a function called welcome().
@app.route('/')
def welcome():
    # Printing a welcome message and showing all the functionalities and methods for interacting with the database.
    message = {'0. >': 'Welcome to this REST API, You can perform CRUD operations here',

               # The second request is for '/create' It will call the POST method of our product class which we
               # defined later in order to create new products.
               '1. To Add new product       ': '/create',

               # The third request is for '/products'. It will call the GET method of our product class which we
               # defined later in order to get all the products from our collection.
               '2. For list of products     ': '/products',

               # The fourth request is for '/delete/<provide product id here>'. This will delete any given product
               # from our collection using its ID number provided by us when calling this route.
               '3. To delete any product    ': '/delete/<provide product id here>',

               # The fifth request is for '/update/<provide product id here>'. This will update any given product's
               # details using its ID number provided by us when calling this route using PUT method.
               '4. To update product details': '/update/<provide product id here>',

               # The sixth request is for '/count_discounted_products'. This returns total number of discounted products
               # present in our collection based on discount percentage value provided by us when calling this route.
               '5. How many products have a discount on them?           ': '/count_discounted_products',

               # The seventh request is for '/list_unique_brands'. This will return the list of all the unique brands
               # present in our database.
               '6. How many unique brands are present in the collection?': '/list_unique_brands',

               # The eighth request is for '/count_high_offer_price'. This will give us the number of products having
               # offer price greater than 300 using GET method.
               '7. How many products have offer price greater than 300? ': '/count_high_offer_price',

               # The ninth request is for '/count_high_discount'. This will give us the number of products having
               # discount percentage greater than 30%.
               '8. How many products have discount % greater than 30%?  ': '/count_high_discount'}

    # Storing our message into variable resp and jasonifying it to display it in a json format
    resp = jsonify(message)
    # Returning the resp variable
    return resp


# Using POST method to add new products to our database,which means that it will be sending the request as a JSON object
# Defining a function add_data inside which all the required fields are declared using json format
@app.route('/create', methods=['POST'])
def add_data():
    # Requesting to convert the data into json objects.
    _json = request.json
    # The name of the product being created is pulled from the JSON object sent by the user.
    _name = _json['name']
    # brand_name and currency are also pulled from this same JSON object.
    _brand_name = _json['brand_name']
    _currency = _json['currency']
    # regular price value and offer price value are both pulled from this same JSON object.
    _regular_price_value = _json['regular_price_value']
    _offer_price_value = _json['offer_price_value']
    # Classifications L1-L4 are all taken from this same JSON object as well
    _classification_l1 = _json['classification_l1']
    _classification_l2 = _json['classification_l2']
    _classification_l3 = _json['classification_l3']
    _classification_l4 = _json['classification_l4']
    # Image URL is also taken out of this same JSON Object (image_url).
    _image_url = _json['image_url']

    # All the field are stored in a list Mydata
    Mydata = [{'name': _name,
               'brand_name': _brand_name,
               'regular_price_value': _regular_price_value,
               'offer_price_value': _offer_price_value,
               'currency': _currency,
               'classification_l1': _classification_l1,
               'classification_l2': _classification_l2,
               'classification_l3': _classification_l3,
               'classification_l4': _classification_l4,
               'image_url': _image_url}]

    # This if statement checks that desired values are provided in the fields by the user and also checks for
    # the request method weather it is POST or not.
    if _name and _brand_name and _currency and _regular_price_value and _offer_price_value and request.method == 'POST':
        # Data provided by user is inserted into mongodb through this command storing it with a new product ID.
        id = mongo.db.NEW.insert_many(Mydata)
        # If details are provided correctly new object will be created and the following success message will be shown
        # with the success code 200.
        resp = jsonify("Product details added successfully")
        resp.status_code = 201

        return resp
    # In case of proper details not provided in defined fields, this command will be executed which contains an error
    # handling function not_found() it will show the error message.
    else:
        return not_found()


# This is GET method used to retrieve a list of all the product details in a json format
@app.route('/products', methods=['GET'])
def products():
    # Find method is used to fetch all the object and details
    products = mongo.db.NEW.find()
    # Using dumps function for getting all the data and storing it in the resp variable
    resp = dumps(products)
    # Returning the response using resp variable
    return resp


# This GET method is created to retrieve details of a particular product using its ID
@app.route('/product/<id>', methods=['GET'])
def product(id):
    # Using find one method to find the particular product using its ID
    product = mongo.db.NEW.find_one({'_id': ObjectId(id)})
    resp = dumps(product)
    return resp


# Using DELETE method to delete any object using its id
@app.route('/delete/<id>', methods=['DELETE'])
def delete_product(id):
    # delete one method is used to delete the target object
    mongo.db.NEW.delete_one({'_id': ObjectId(id)})
    # Upon successful deletion the following message is displayed with success code 203
    resp = jsonify("Product removed successfully")
    resp.status_code = 203
    return resp


# Using PUT method to update details of any existing product using its ID
@app.route('/update/<id>', methods=['PUT'])
def update_product(id):
    # All the object fields are pulled as a json object
    _id = id
    _json = request.json
    _name = _json['name']
    _brand_name = _json['brand_name']
    _currency = _json['currency']
    _regular_price_value = _json['regular_price_value']
    _offer_price_value = _json['offer_price_value']
    _classification_l1 = _json['classification_l1']
    _classification_l2 = _json['classification_l2']
    _classification_l3 = _json['classification_l3']
    _classification_l4 = _json['classification_l4']
    _image_url = _json['image_url']

    # Storing all fields in a Dict Mydata
    Mydata = {'name': _name,
              'brand_name': _brand_name,
              'regular_price_value': _regular_price_value,
              'offer_price_value': _offer_price_value,
              'currency': _currency,
              'classification_l1': _classification_l1,
              'classification_l2': _classification_l2,
              'classification_l3': _classification_l3,
              'classification_l4': _classification_l4,
              'image_url': _image_url}

    # Checking that the request is PUT and catching other values to update in the fields
    if _name or _brand_name or _currency or _regular_price_value or _offer_price_value or _classification_l1 or \
            _classification_l2 or _classification_l3 or _classification_l4 or _image_url and _id and request.method == 'PUT':
        mongo.db.NEW.update_one({'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, {'$set': Mydata})
        # Showing this message with success code 200 on successful update of details
        resp = jsonify("Details are updated successfully")
        resp.status_code = 200

        return resp
    # Details not provided properly will result in returning this
    else:
        return not_found()


# Using GET method to retrieve the count of discounted products
@app.route('/count_discounted_products', methods=['GET'])
def discounted_products():
    # Find() function will search for the required data. The condition here is if regular price value is greater than
    # offer price value than discount is given on that product, and the list is retrieved
    discounted_products = mongo.db.NEW.find({"$expr": {"$gt": ["$regular_price_value", "$offer_price_value"]}})
    # We are printing only the length of that retrieved list which will give us the number discounted products present
    resp = jsonify("Number of products having discount: ", len(list(discounted_products)))
    resp.status_code = 200
    return resp


# unique brands present in the database
@app.route('/list_unique_brands', methods=['GET'])
def unique_brands():
    # Determined simply using distinct() function and then printed the whole list
    unique_brands = mongo.db.NEW.distinct("brand_name")
    resp = jsonify("List of Unique brands: ", list(unique_brands))
    resp.status_code = 200
    return resp


# Mathematical operator used for getting the products with offer price value greater than 300
@app.route('/count_high_offer_price', methods=['GET'])
def high_offer_price():
    # Our code will search for products having offer price value greater than 300 through find() funtion
    high_offer_price = mongo.db.NEW.find({"offer_price_value": {"$gt": 300}})
    # printing the number of such products using len
    resp = jsonify("Number of products have offer price greater than 300:", len(list(high_offer_price)))
    resp.status_code = 200
    return resp


# This route method will pull number of products having discount percentage greater than 30%
@app.route('/count_high_discount', methods=['GET'])
def high_discount():
    # methamatical operations used to calculate the discount percentage and after than $gt is checking if it is greater
    # than 30 or not.
    high_discount = mongo.db.NEW.find({
        "$expr": {
            "$gt": [{
                "$multiply": [{
                    "$divide": [{
                        "$subtract": [
                            "$regular_price_value", "$offer_price_value"]},
                        "$regular_price_value"]},
                    100]},
                30]}})
    # Printing length of the list of products having more tha 30% discount.
    resp = jsonify("Number of products have discount greater than 30%:", len(list(high_discount)))
    resp.status_code = 200
    return resp

# Defining a function to handle the errors
@app.errorhandler(404)
# not_found() function will basically takes error as parameter and provide the response as 404, if correct information
# is not provided by the user for products this will encounter an error and the error message will be shown
def not_found(error=None):
    # Message for error conditions
    message = {
        'status': 404,
        'message': 'Please provide valid details'
    }
    # this will jsonify the message
    resp = jsonify(message)
    resp.status_code = 404
    return resp

# This code will check if the __name__ is present in the __main__ and then run the app
if __name__ == "__main__":
    app.run(debug=True)
