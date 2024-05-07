# Import Flask module
from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route and its corresponding request handler
@app.route("/")
def hello():
    # Return a response
    return "Hello World!"

# Run the application
if __name__ == '__main__':
    app.run(debug=True)


