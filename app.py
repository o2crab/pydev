from flask import Flask
app = Flask(__name__)

@app.route('/')
def Hello_world():
    return 'Hello, World!!!'

if __name__ == 'main':
    Hello_world()