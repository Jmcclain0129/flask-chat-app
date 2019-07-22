import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello There There!</h1>"

# app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)

if __name__ == '__main__':
 app.run(host=os.environ.get('IP', '127.0.0.1'),
         port=int(os.environ.get('PORT', '8080')),
         debug=True)

