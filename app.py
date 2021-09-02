##
## For putting data onto the website
##

# Set up Flask and data
from flask import Flask, jsonify
from data import getData

app = Flask(__name__)

# Run it
if __name__ == '__main__':
    app.run(debug=True)