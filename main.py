from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/about/<username>')
def about_page(username):
  return f'<h1>This is the about Page of {username} </h1>'

if __name__ == '__main__':
  app.run(debug=True)