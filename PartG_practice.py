import csv
import json
with open("practice.csv","r",encoding="utf-8")as f:
    products=csv.DictReader(f)
    rows=[row for row in products]
items=[row["item"]for row in rows]
prices=[float(row["price"])for row in rows]
stocks=[int(row["stock"])for row in rows]
total_stock=sum(stocks)
average_price=sum(prices)/len(prices)
print("products",products)
print("rows",rows)
print("item",items)
print("price",prices)
print("stock",stocks)
print("total stock",total_stock)
print("average price",average_price)

rooms = {
    "living": {
        "capacity": 2,
        "people": ["James"],
        "exits": {"north": "kitchen", "outside": "garden"}
    },
    "kitchen": {
        "capacity": 1,
        "people": [],
        "exits": {"south": "living"}
    },
    "garden": {
        "capacity": 3,
        "people": ["Sue"],
        "exits": {"inside": "living"}
    }
}
with open("rooms.json","w",encoding="utf-8")as f1:
    json.dump(rooms,f1,indent=4)
with open("rooms.json","r",encoding="utf-8")as f1:
    loaded_room=json.load(f1)
    room=[row for row in loaded_room]
    print("room:",room)

print("How many rooms:",len(room))

capacity=[loaded_room[room]["capacity"]for room in loaded_room]
print("total capacity:",sum(capacity))

room_with_people=[room for room,info in loaded_room.items() if info["people"]]
print("room with people",room_with_people)
