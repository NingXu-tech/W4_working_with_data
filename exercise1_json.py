import json
group = {
    "Jill": {
        "age": 26,
        "job": "biologist",
        "relations": {
            "Zalika": "friend",
            "John": "partner"
        }
    },
    "Zalika": {
        "age": 28,
        "job": "artist",
        "relations": {
            "Jill": "friend"
        }
    },
    "John": {
        "age": 27,
        "job": "writer",
        "relations": {
            "Jill": "partner"
        }
    },
    "Nash": {
        "age": 34,
        "job": "chef",
        "relations": {
            "John": "cousin",
            "Zalika": "landlord"
        }
    }
}
with open("ex1.json","w",encoding="utf-8")as f:
    json.dump(group,f,indent=4)
with open("ex1.json","r",encoding="utf-8")as f:
    ex1_group=json.load(f)
print("ex1 group:",ex1_group)
ages=[int(r["age"])for r in ex1_group.values()]
jobs=[r["job"]for r in ex1_group.values()]
relations=[r["relations"]for r in ex1_group.values()]
print("ages",ages)
print("jobs",jobs)
print("relations",relations)
