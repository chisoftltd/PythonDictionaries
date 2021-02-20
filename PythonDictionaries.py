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