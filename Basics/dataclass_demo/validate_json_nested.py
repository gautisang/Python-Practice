
import json
from  my_class import Connection,Person
from dacite import from_dict
from dataclasses import dataclass


def validate_json():
    json_data = '''{
            "Person":[
            {
                "name": "Alice",
                "age": 30,
                "email": "alice@example.com",
                "friends": ["Bob", "Charlie"]
               
            }
            ],
            "test":"test123"
            }
            '''
    data = json.loads(json_data)
    print(data['Person'])
    # Use dacite's from_dict to map the dictionary to the Person dataclass
    try:
        # person = from_dict(data_class=list[Person], data=data["Person"])
        # print(person)
        person_list = [from_dict(data_class=Person, data=person_data) for person_data in data["Person"]]
        print("Parsed data:", person_list)
    except Exception as e:
        print(f"Error: {e}")

validate_json()