## POST-HOME
* live site: 
### Python app made with django framework.A showcase for personal gallery.

### Description
* Main function is to show photos. Users get to view photos updated by the site admin. Users can see photos based on the location, by clicking on the listed locations in the menu. They can also copy the link to a photo to share with friends. The search functionality will search photos based on the categories.


### Set Up and Installations
## Prerequisites
* Ubuntu Software
* Python3.6
* Postgres
* python virtualenv
* Clone the Repo
 Run the following command on the terminal: git clone https://github.com/Jeffmusa/Post-Home && cd Post-Home

 Activate virtual environment
 Activate virtual environment using python3.6 as default handler

 virtualenv -p /usr/bin/python3.6 venv && source venv/bin/activate
* Install dependancies
* Install dependancies that will create an environment for the app to run pip3 install -r requirements.txt

# Create the Database
* psql
# CREATE DATABASE gallery;
* .env file
# Create .env file and paste paste the following filling where appropriate:

* SECRET_KEY = '<Secret_key>'
* DBNAME = 'gallery'
* USER = '<Username>'
* PASSWORD = '<password>'
* DEBUG = True
## Run initial Migration
python3.6 manage.py makemigrations gall;
python3.6 manage.py migrate
Run the app
python3.6 manage.py runserver
Open terminal on localhost:8000

Known bugs
No known bugs

Technologies used
- Python 3.6
- HTML
- Bootstrap 4
- JavaScript
- Heroku
- Postgresql
Support and contact details
Contact me on jeffmusa05@gmail.com for any comments, reviews or advice.

License
* MIT
Copyright (c) Jeff Musa
