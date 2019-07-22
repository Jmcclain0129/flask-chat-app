import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    """Main page with instructions"""
    return "To send a message use /USERNAME/MESSAGE"

@app.route('/username')
def user(username):
    return "hi" + username

@app.route('/<username>/<message>')
def send_message(username, message):
    return"{0}: {1}".format(username, message)






# app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)

if __name__ == '__main__':
 app.run(host=os.environ.get('IP', '127.0.0.1'),
         port=int(os.environ.get('PORT', '8080')),
         debug=True)

