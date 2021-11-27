# Python file to conduct the spell check. Comparison is done using the gingerit library for English which also checks for context spellings
# Import flask, gingerit, irishspell and dotenv modules
# The check function does the Irish spell checking

import re # Regular Expressions
from collections import Counter
import string
from gingerit.gingerit import GingerIt   
from flask import Flask, render_template, request, jsonify, make_response  
from flask_cors import CORS
from dotenv import load_dotenv
from irishspell import correct_spelling, unique_words, word_probability

# Initializes Flask app
app = Flask(__name__)   
CORS(app)

# Pyhton method collects the user text as JSON and parses it to GingerIt for English spell checking
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


# Pyhton method collects the user text as JSON and parses it to the Irish spell checker for Irish spell checking
@app.route('/api/v1/check/irish', methods=['post'])
def check():
    text = request.get_json()["text"]            # Get text from front end as a JSON string
    iwords = text.strip().lower().split()
    guesses = []
    r = []
    corrections = []
    
    for word in iwords:
        guesses = correct_spelling(word, unique_words, word_probability)   # guesses contain a word and its probability
        if len(guesses) != 0:
            cor_word, num = map(list, zip(*guesses))  # breaking guesses list to 2 lists
            n = num.index(max(num))      # finding index of max probability
            r.append(cor_word[n])
            correction = {"correct":cor_word[n],"start": n, "text":word } 
            corrections.append(correction)
        else:
            r.append(word)

        res = " "
        res = r
    print(corrections)
    return make_response(jsonify({
        "status": "success", "data": { "corrections": corrections }    # Returns corrected text
        }), 200)

# main function
if __name__ == '__main__':      
    app.run(debug = True) # run our Flask app
