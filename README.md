## NewsAPI

## Author
Raphael Nyangenya

## About the application
 This is a simple web application that displays a list of several news sources and articles from across various media outlets. This application achieves its functionality by using the [News API](https://newsapi.org/).


## SetUp / Installation Requirements
### Prerequisites
* python3.6/3.7/3.8
* pip
* virtualenv

### Cloning
* In your terminal:

        $ git clone https://github.com/rmautia/news.git
        $ cd into the project

## Running the Application
* Creating the virtual environment

        $ python3.7 -m venv --without-pip virtual
        $ source virtual/bin/env
        $ curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Flask and other Modules

        $ python3.7 -m pip install Flask
        $ python3.7 -m pip install Flask-Bootstrap
        $ python3.7 -m pip install Flask-Script

* Setting up the API Key

        To get the news articles, you will require an Api.

        Worry not, getting one is easy
        follow the following steps
        * head on to https://newsapi.org/ and register for an API key.
        * within the root directory of the project folder create a file: start.sh
        * Input the below information into the start.sh

                export NEWS_API_KEY='<Your-Api-Key>'
                python3 manage.py server

        * Insert the API Key you received from News Api where <Your-Api-Key> is.
        * make sure to exclude the < > symbols. example 'sbdzgtsshb'

* To run the application, in your terminal:

        * prerequisite
        $ chmod +x start.sh

        then run the command
        $ ./start.sh

## Testing the Application
* To run the tests for the class files:

        $ python3 manage.py tests to test for all tests

## Technologies Used
* Python3.7
* Flask
* Bootstrap

## contact
* email- raphaelnyangenya@gmail.com
* phone - +254704445630
* Github - rmautia

## License
- MIT
- Copyright (c) 2020 Raphael Nyangenya

------------

### Permission
- Permission is hereby granted for further use of the application for development purposes. 



