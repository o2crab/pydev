from flask import Flask

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/entry/<q_id>')
def echo(q_id):
    return q_id

if __name__ == "__main__":
    app.run(debug=True)
