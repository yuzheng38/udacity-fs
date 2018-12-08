# Catalog application
Udacity fullstack nanodegree project #4
> This is a RESTful web application using the Flask web framework along with implementing Google Oauth2 authentication, backed by a sqlite database.
>

## File structure
The catalog folder is structured as below:
```
|--README.md
|--database_setup.py
|--run.py
|--catalog_app [package]
|   |--__init__.py
|   |--catalog.db
|   |--models.py
|   |--routes.py
|   |--static
|   |   |--css
|   |   |   |--main.css
|   |   |--profile_pics
|   |   |   |--default.jpg
|   |--templates
|   |   |--about.html
|   |   |--account.html
|   |   |--catalog.html
|   |   |--item.html
|   |   |--main.html
|   |   |--new_toon.html
|   |   |--errors
|   |   |   |--403.html
|   |   |   |--404.html
|   |   |   |--500.html
```

## Major design decisions
* A user is not required to register. The first time a user logs in via Google Oauth, a user's account is created.
* Three models were created - Player, Class, Toon. Explanations for these classes are in the docstring. 
* 3 API endpoints are made available. 
    * `/api/v1/classes`
    * `/api/v1/toons/<int:toon_id>`
    * `/api/v1/toons`
* Custom error handlers are created for 403, 404, and 500 response codes.
* Basic CSRF protection implemented for login route.


## Python and Pypi packages
Note: these packages are included in the Vagrant VM provided by Udacity FSND.
* Python 2.7
* flask
* flask-sqlalchemy
* requests


## Instructions
* Set up the development environment.

  * Follow the instructions in <a href="https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0">this</a> Udacity lesson to install and start Vagrant. Stop at the 'Logged In!' step, as the remaining steps are not needed for this project.

  * `cd` into the /vagrant directory, and save the project folder there. 

* Create and setup the sqlite database
  * `cd` into the project directory, where `catalog_app` folder is located. 
  * Type `python` to start the python terminal, then run the following: 
    * `from catalog_app import db`
    * `db.create_all()`
  * Ctrl-D to exit python terminal and run ```python database_setup.py``` to populate the database with some required data to render the pages. 


* Run the project

    In the project directory, run
    ```py
    python run.py
    ```
    and visit <a href="http://0.0.0.0:5000">http://0.0.0.0:5000</a> to see the application.


## Reference
Some of the HTML and CSS are code snippets from:
https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Flask_Blog/snippets

