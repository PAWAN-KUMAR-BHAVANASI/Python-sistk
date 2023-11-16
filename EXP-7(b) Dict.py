#Operations on Dict
d1={'name':'vasu','age':30,'class':'cse',7:10}
#Prints type of d1
print(type(d1))
#Prints the d1 contents
print('The dictionary d1 is',d1)
#Prints the length of the d1
print('Length of the dictionary d1 is',len(d1))
#Prints the value of the key name in d1
print('Value of key name is',d1['name'])
#Prints the value of the key 7 in d1
print('Value of key 7 is',d1[7])
print('string representation is',str(d1))
d2={}
print(type(d2))
#Inset keys and values
d2['name1']='hi'
print(d2)
d1['age']=35
print('d1 is',d1)
d1.update(d2)
print('updated d1 is',d1)
print(d1.copy())
d1['college']='siddartha'
print('after adding new entry d1 is',d1)
del d1['name1']
print('after deleting',d1)
print('Items in dictionary are',d1.items())
print('Keys in dictionary d1 are',d1.keys())
print('Values in dictionary d1 are',d1.values())
print(d1.get('class'))
seq=['age','roll']
d3={}
d3=d3.fromkeys(seq,10)
print(d3)
#delete operation
d2.clear()
print('d2 is',d2)
del d2
print('d2 is',d2)