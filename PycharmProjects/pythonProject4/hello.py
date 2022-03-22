from flask import Flask
app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return "<b>"+function()+"</b>"
    return wrapper
def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper(*args):
        return "<u>" + function() + "</u>"
    return wrapper

@app.route('/hello')
def hello():
    return '<h2>Hello, World</h2>'
@app.route('/')
def index():
    return 'Index Page'

@app.route("/bye")
@make_bold

@make_emphasis
def bye():
    return "Bye!"


@app.route("/test/<search_query>/<int:number>") #if variable is passed
@make_underlined
def search(search_query,number):
    return f"Hello {search_query} and {number}"

if __name__ == '__main__':
    app.run(debug=True) #reload without restarting and helps in debugging

