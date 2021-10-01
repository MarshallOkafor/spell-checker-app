--------------------------------------------------------------
#     DICTIONARY: ITS A COLLECTION OF KEYS AND VALUES
-------------------------------------------------------------

d1={}

d1 = dict()
type(d1)

d1={'a':1,'b':2}
d2={'name':'jai','Age':24,'location':'chennai'}
d3={1:1,2:4,3:9}

len(d1)

d1.keys()
d1.valus()



c=d1.keys()
type(c)
d=d1.values()
type(d)


for i in d1:
	print i


d1['c']=3
d1['d']=4

d1.update({'e':5,6:7})

d1.copy()

d1.clear()

-----------------------------------------------------
# Dictionary with Iterations
-----------------------------------------------------
# Eg.1

for k,v in d1.items():
    print k,v


# Eg. 2    
for k,v in d1.items():
    print(k,v**2)
