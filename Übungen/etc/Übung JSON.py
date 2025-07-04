import sys
sys.path.append('./')
# Aufgabe 1
dict1= {
  "library": {
    "books": [
      { "title": "The Great Gatsby", "author": "F. Scott Fitzgerald" },
      { "title": "1984", "author": "George Orwell" },
      { "title": "Moby-Dick", "author": "Herman Melville" }
    ]
  }
}
# Antwort: 3
 
# Aufgabe 2
print(dict1["library"]["books"][2]["author"])

# Aufgabe 3
import json
school = {
    "classroom" : {
        "teacher": "Mrs. Smith",
        "subject": "Mathematics",
        "students": [
            { "name": "John Doe", "age":20, "major":"Physics"},
            { "name": "John Smith", "age":22, "major":"Mathematics"},
        ]
    }
}

school["classroom"]["students"].append ({ "name": "Alex mayer", "age":23, "major":"Biology"})

do = open ("./Exports/students.json", "w")
json.dump (school["classroom"]["students"], do, indent= 5)
do.close ()

# Aufgabe 4
do = open ("./Exports/students.json", "r")
stud_dict = json.load (do)
do.close ()

print (stud_dict[2])

# Aufgabe 5
json_string = json.dumps(dict1, indent= 5)

# Aufgabe 6
dict2 = json.loads(json_string)
