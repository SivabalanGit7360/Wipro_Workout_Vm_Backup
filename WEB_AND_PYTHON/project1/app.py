from flask import Flask, render_template

# create an flask instance

app = Flask(__name__)

# flask will by default start at port 5000
# http://127.0.0.1:5000  - ('/' is the top level url of the application)

# create a route for '/'

@app.route('/')
def hello():
   # message = "this is the content from hello"
   # return render_template("hello.html",msg=message)
   
   # list
   #list_of_names = ['bob','pot','alice','sam']
   #return render_template("hello.html",names = list_of_names)
   
   # dictonary
   list_of_names = [{'name':'bob'},{'name':'pot'},{'name':'alice'},{'name':'sam'}]
   return render_template("hello.html",names = list_of_names)
    # return "<h1>Hello world<h1>"

# http://127.0.0.1:5000/exampleurl 
# create a route for '/exampleurl'
@app.route('/exampleurl')
def example():
    return render_template("example.html")
   # return "<h1> from example url</h1>"

if __name__ == '__main__':
    app.run() # starts the application at port number 5000