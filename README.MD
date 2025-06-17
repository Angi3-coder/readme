# THIS IS THE MAIN TITLE

## Project Overview
What your project is about, features of your project and importance of project.
    1.
    2.
    3.


## Prerequisties
Before you install dependencies activate a virtual environment. run this in your terminal
```
cd server
python3 -m venv venv
source venv/bin/activate
```
To install backend dependencies run this code

```
pip install -r requirements.txt
```

To install frontend dependencies open another teminal and run this

```
cd client
npm install
```


## Set up database

run
```
flask db init
flask db migrate -m "Message"
flask db upgrade
```

Seed your database by running
```
python3 seed.py
```


## How to run app
To start the server run the following in the server directory

```
python3 app.py
```

To start the client run the following in the client directory/terminal
```
npm start
```


## Routes
Explain different end points

