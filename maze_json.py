import json
import yaml
maze = {
    "living": {
        "exits": {
            "north": "kitchen",
            "outside": "garden",
            "upstairs": "bedroom"
        },
        "people": ["James"],
        "capacity": 2
    },
    "kitchen": {
        "exits": {
            "south": "living"
        },
        "people": [],
        "capacity": 1
    },
    "garden": {
        "exits": {
            "inside": "living"
        },
        "people": ["Sue"],
        "capacity": 3
    },
    "bedroom": {
        "exits": {
            "downstairs": "living",
            "jump": "garden"
        },
        "people": [],
        "capacity": 1
    }
}
with open("maze.json","w",encoding="utf-8")as f:
    json.dump(maze,f,indent=4)
with open("maze.json","r",encoding="utf-8")as f:
    maze_loaded=json.load(f)
print("living capacity:",maze_loaded["living"]["capacity"])
print("kitchen exist:",maze_loaded["kitchen"]["exits"])
print("garden people:",maze_loaded["garden"]["people"])
print("bedroom exits jump:",maze_loaded["bedroom"]["exits"]["jump"])

with open("maze.yaml","w",encoding="utf-8")as f1:
    yaml.dump(maze,f1)
with open("maze.yaml","r",encoding="utf-8")as f1:
    maze_yaml=yaml.safe_load(f1)
print(maze_yaml)
print(type(maze_yaml))

