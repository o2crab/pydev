from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    DATABASE_URL = os.environ['DATABASE_URL']
    return DATABASE_URL
    #return 'Hello, World!!!'

if __name__ == '__main__':
    app.run()
