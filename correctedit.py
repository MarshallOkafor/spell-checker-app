from gingerit.gingerit import GingerIt #Gingerit is used to ease the file collection of dictionaries and to compare the data to the database.
print("Enter the Text")
data=open("C:\python\demo.txt").read() #sources the input text from input file and can be changed to automated input string by Flask
list=[]
result = GingerIt().parse(data) #method to compare the text to the database and lets the miss spelt words.
corrections = result['corrections'] #return the misspelt words
correctText = result['result'] #return the  corrected misspelt words

print("Correct Text:",correctText) 
print()
print("CORRECTIONS")                           
for d in corrections:
  if d['text'] == d['correct']: 
        print()
  else:
        print("________________")    
        print("Previous:",d['text'])  
        print("Correction:",d['correct'])
        list.append(d['correct'])        
        
print(list, file=open("output.txt", "a")) #returns the output to the external file
