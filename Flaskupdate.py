# Python file to conduct the spell check. Comparison is done using the gingerit library which also checks for context spellings
# Import flask, gingerit and dotenv modules

from gingerit.gingerit import GingerIt   
from flask import Flask, render_template, request, jsonify, make_response  
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# Initializes Flask app
app = Flask(__name__)   
CORS(app)

# Pyhton method collects the user text as JSON and parses it to GingerIt for spell checking
@app.route('/api/v1/check', methods=['post'])
def checkText():
    try:
        text = request.get_json()["text"]          # Get text from front end as a JSON string
        corrected_text = GingerIt().parse(text)    # Text is compared with GingerIT library
        return make_response(jsonify({
        "status": "success", "data": corrected_text    # Returns corrected text
        }), 200)
    except:
        return make_response(jsonify({
        "status": "error", "message": "An error occur"     # Catches any error that occurs during comparison
        }), 400)

# main function
if __name__ == '__main__':      
    app.run(debug = True) # run our Flask app
