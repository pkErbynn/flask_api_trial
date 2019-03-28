import flask
from flask import request, jsonify

app = flask.Flask(__name__)     #  Creates the Flask application object, which contains data(vars) about the application and also methods (functions) that tell the application to do certain actions.
app.config["DEBUG"] = True

# creating a working API with test data that we’ve provided right in our application
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

def go_r():
    return 'go return'
def go_p():
    print('go print')
@app.route('/', methods=['GET'])    # methods are keyword argument letting Flast know the kind of HTTP requests are allowed
def home():
    print('debug in console')
    print(go_r()) # if returning, print
    go_p() # if printing, call
    return '''<h1>Distant Reading Archive</h1>
            <p>/hooooh....This site is a prototype API for distant
            reading of science fiction novels.</p>'''


# route to return all available entries in catalog
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all_data():
    return jsonify(books)


@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    # This part of the code determines if there is a query parameter, like ?id=0, and then assigns the provided ID to a variable.
    if 'id' in request.args:    # holds query parameters   # if 'id' appears in url
        id = int(request.args['id'])    # convert whats typed outside an integer 
    else:
        return 'Error: No id field provided. Please specify an id'
    
    # create an empty list for our results
    results = []

    for book in books:
        if book['id'] == id:    # if values of id,in int, in db == id comming, converted to int
            results.append(book)    # if yes, push that book detail to the list

    # print(request.args) # understanding the request

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)   


app.run()  # flask obj run() run the server

# flask maps HTTP request to functions. 
# the process of mapping URLs to functions is called routing 
# in this case, URL path ("/") mapped to one function, home

# to debug the script small small, go to python mode and import it as a file and debug in contents