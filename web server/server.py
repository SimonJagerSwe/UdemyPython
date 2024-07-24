from flask import Flask, render_template
app = Flask(__name__)
# print(__name__)

@app.route('/')
def hello_world():
   return 'Hello, Simon!'

@app.route('/blog')
def blog():
   return 'These are my thoughts on blogs'

@app.route('/blog/2020/dogs')
def blog2():
   return 'My dog is actually a cat'

@app.route('/about.html')
def about():
   return render_template('about.html')