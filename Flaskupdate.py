from gingerit.gingerit import GingerIt   #Initiates the Ginger IT
from flask import Flask, render_template, request  #Initiates the Flask function

app = Flask(_name_)   #Initiates the reference

@app.route('/')               
def index():
    return render_template("index.html")    #renders the index .html file template

@app.route('/', methods=['post'])
def check():
    text = request.form['takeinput']          #transfer the out put from the Front end to the inout function in this backend file
    iwords = text.strip().lower().split()   # splits , lowers and transforms the inout text into list for better time complexity
    list=[]                       
    result = GingerIt().parse(iwords)                 #Initiates the Ginger IT comparing the text to the database
    corrections = result['corrections']
    correctText = result['result']
    for d in corrections:
       if d['text'] == d['correct']:
           print()
       else:
           print("________________")    
           print("Previous:",d['text'])  
           print("Correction:",d['correct'])
           list.append(d['correct'])        
    return render_template('index.html', output= list)    #returns the outputs to the front end



if _name_ == '_main_':      #main function
    app.run(debug=True)