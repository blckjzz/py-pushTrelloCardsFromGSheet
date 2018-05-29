# A Python app that helps transform recieved Projects bills from Mudamos plataform into a database

# Main functions

  - Download files and transform CSV files into Petition objects
  - Query Petition Objects into Database
  - Push petitions into a Trello board in cards format

### Installation and Requirements 
- This application requires  requires [Python 2.7.*](https://www.python.org/download/releases/2.7/) 
- pip

# Dependencies
- requests==2.18.4
- peewee==3.4.0
- python-dotenv==python-dotenv-0.7.1

### Installing PIP
```
pip install pip
```
# Install App

Clone this repo to your directory

```
$ git clone https://github.com/se3k/py-pushTrelloCardsFromGSheet
$ cd py-pushTrelloCardsFromGSheet
```

### Install the dependencies 
 
```
$ pip install -r requirements.txt
```

### Setup and Run
You must setup keys and tokens to integrate multiple applications in `.env` file
Keys you must setup:
- GOOGLE_SHEET_URL = url where is place your csv file
- TRELLO_KEY 
- TRELLO_TOKEN 
- TRELLO_URL  
- TRELLO_BOARD_ID 
- TRELLO_LIST_ID  
- DATABASE_NAME = 

For more information about api and endpoint must check [Trello documentation](https://trello.readme.io/docs/api-introduction)
```
$ cd py-pushTrelloCardsFromGSheet
$ cp .env.exemple .env
```

# Setting up database
To create tables and database structure run
```
$ python model/schema.py
``` 

the application are based in two tables
- log = witch logs every sync event
- petition = where the petitions are stored

# Run application

Once you setup all you keys and tokens in `.env` file, you can interact with the application with the following commands:

```
$ python main.py
```
