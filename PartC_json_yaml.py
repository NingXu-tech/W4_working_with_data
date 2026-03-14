import json
person={
    "name":"Ning",
    "age":23,
    "skills":["python","git","data analysis"],
    "student":True
    }
with open("person.json","w",encoding="utf-8")as f:
    json.dump(person,f,indent=4)
with open("person.json","r",encoding="utf-8")as f:
    loaded_person=json.load(f)
print("loaded person:",loaded_person)
print("name:",loaded_person["name"])
print("age:",int(loaded_person["age"]))
print("skills:",loaded_person["skills"])
print("student:",loaded_person["student"])