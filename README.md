# Greendeck-assignment
Assignment Software Engineer-Data/ETL for Greendeck(Cliff.ai)

Folder structure:

JAY_VAGHELA
     >Task  
            1. app.py      (This is the main API code file which contains all the working codes)

            2. json_loader (This piece of code will load data from Task1 json file to Mongodb database JAY_VAGHELA )

            3. Task.json       (This is json file provided by greendeck contains 5000 product details)

       
      >screenshots : It contains all the related screenshots of project input and outputs.
      >Readme.txt

Aim : The task is to create a Rest API using using flask and python libraries that allows user to do basic CRUD operations on the data. 
REST API :- A REST API or RESTful API is an architectural style for an application program interface (API) that uses HTTP requests to 
            access and use data. That data can be used to GET, PUT, POST and DELETE data types, which refers to the reading, updating, 
            creating and deleting of operations concerning resources. It is based on representational state transfer (REST), which is an 
            architectural style and approach to communications often used in web services development.

Inserting json data file into mongodb database:
  The json_loader file is used to perform this operation, this file contains a json.load(file) function which sends all the data to mongodb
 database.   
    Database   : JAY_VAGHELA
    Collection : NEW 

After inserting data into database i started learnng about REST APIs, Docker and contanerization there uses and operations performed on it, 
i have installed flask, jsonify, pymongo and all other required libraries.

Then i used pymongo and Mongoclient to connect my code to mongodb database and then imported several libraries like:
1. from bson.json_util import dumps - This module provides helper method dumps that wrap the native json methods and provide BSON conversion 
                                      to & from JSON.
2. from flask import Flask, jsonify, request- Importing flask in which Flask, jsonify and request are used to create a functional API.
3. from flask_pymongo import PyMongo - Responsible for flask interacting with mongodb using python.
4. from bson.objectid import ObjectId- Using bson.objectid() to get an ObjectId for user, so we can reference it later on in our code without 
                                       having to worry about collisions or duplicates when inserting new users into MongoDB.

After configuring and connecting all the things, i started to create routes inside my API which are the basic operations performed on the 
  database.

i have created 11 routes which contains 8 GET methods and 3 other methods i.e delete, post and  put.

Starting with Welcome function which will be working on home page it will show all the functionalites and operations which can be performed
 through our API.

 The code starts by defining a function called welcome().
- This function is used to handle the HTTP requests that come in.
- The first request is for '/'.

- The second request is for '/create'.
- It will call the create() method of our product class which we defined later in order to create new products.

- The third request is for '/products'.
- It will call the GET method of our product class which we defined later in order to get all the products from our collection.

- The fourth request is for '/delete/<provide product id here>'.
- This will delete any given product from our collection using its ID number provided by us when calling this route.

- The fifth request is for '/update/<provide product id here>'.
- This will update any given product's details using its ID number provided by us when calling this route.

- The sixth request is for '/count_discounted_products'.
- This returns how many discounted products are present in our collection based on their discount percentage value provided by us when calling this route

- The seventh request is for '/list_unique_brands'. 
- This will return the list of all the unique brands present in our database.

- The eighth request is for '/count_high_offer_price'. 
- This will give us the number of products having offer price greater than 300 using GET method.
             
- The ninth request is for '/count_high_discount'. 
- This will give us the number of products having discount percentage greater than 30%.

After this methods i have set a error handler class which contains a not_found() function will be encountered whenever valid information is not provided
and if the api can't fetch the url. it will show message "error 404 and please provide valid details".

Docker :- Docker is an open source containerization platform. It enables developers to package applications into containers—standardized executable 
components combining application source code with the operating system (OS) libraries and dependencies required to run that code in any environment.
     Containers simplify delivery of distributed applications, and have become increasingly popular as organizations shift to cloud-native development 
and hybrid multicloud environments.
     Developers can create containers without Docker, but the platform makes it easier, simpler, and safer to build, deploy and manage containers.
Docker is essentially a toolkit that enables developers to build, deploy, run, update, and stop containers using simple commands and work-saving 
automation through a single API.
 
::::Docker-problem::::
"I have learned docker theory and then proceed to install it but rather than installing correctly it crashed my windows,i tried several times to install
docker on my system but it didn't work. then i tried installing it in other PCs but its not installed in any of them and this thing took my lots of time 
effort but my effort didn't bring any result as i am not able to make it work. Finally tried installing it using virtualBox son linux OS but i did not 
succeed."
I am really sorry to inform this but i tried all the means to install it but it didn't work.


Then i installed 'Postman' to test my API endpoints and i gave several inputs using it and my code is working correctly and data creation, updation and
deletion is successfully done using API endpoints by providing product IDs.

Related screenshots and outputs are present in the folder. i have tried my best to complete this assignment but i have came this far.

Thank you so much for giving me this assignment

Regards
Jay Vaghela
B.Tech(CSE)
IPS Academy Indore 



