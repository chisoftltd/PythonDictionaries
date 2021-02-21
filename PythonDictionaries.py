import os
os. system('cls')

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#Dictionary Items

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

#Duplicates Not Allowed
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

#Dictionary Length
print(len(thisdict))

#Dictionary Items - Data Types
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(thisdict)
print(type(thisdict))

#Python - Access Dictionary Items
thisdict = {
  "brand" : "Ford",
  "model" : "Volvo",
  "year" : 2017
}

x = thisdict
print(x)

#Accessing Items
y = thisdict.get("model")
print(y)

#Get Keys
z = thisdict.keys()
print(z)

#Get Values
v = thisdict.values()
print(v)

thisdict["year"] = 2021
print(v)

#Add Key/value
thisdict["color"] = "black"
print(z)
print(v)
print(x)

#Get Items
i = thisdict.items()
print(i)
thisdict["year"] = 2022
print(i)
thisdict["Made in Sweden"] = "Sweden"
print(i)

#Check if Key Exists
if "year" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

#Update Dictionary
thisdict.update({"color": "darkblue"})
print(thisdict)

#Removing Items
thisdict.pop("model")
print(thisdict)

thisdict.popitem()
print(thisdict)

#delete Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#del thisdict
print(thisdict)
thisdict.clear()
print(thisdict)

#Python - Loop Dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)
  print(thisdict[x])
print()

for x in thisdict.values():
  print(x)
print()

for x in thisdict.keys():
  print(x)
print()

for x, y in thisdict.items():
  print(x, y)
print()

#Copy a Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(thisdict)
print(mydict)
mydict["Country"] = "Sweden"
print(mydict)
thisdict = mydict
print(thisdict)
bendict = dict(mydict)
print(bendict)

#Python - Nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "Tobechukwu",
    "year" : 2018
  },
  "child2" : {
    "name" : "Chukwuebuka",
    "year" : 2014
  },
  "child3" : {
    "name" : "Chinaecherem",
    "year" : 2012
  }
}

print(myfamily)
for x, y in myfamily.items():
  print(x, y)
  for y in x:
    print(y)


child11 = {
  "name" : "Emil",
  "year" : 2004
}
child12 = {
  "name" : "Tobias",
  "year" : 2007
}
child13 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily1 = {
  "child11" : child11,
  "child12" : child12,
  "child13" : child13
}

print(myfamily1)