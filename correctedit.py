from gingerit.gingerit import GingerIt
print("Enter the Text")
data=open("C:\python\demo.txt").read()
list=[]
result = GingerIt().parse(data)
corrections = result['corrections']
correctText = result['result']

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
        
print(list, file=open("output.txt", "a"))