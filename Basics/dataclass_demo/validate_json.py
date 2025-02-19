
import json
from  my_class import Connection,Person
from dacite import from_dict
def validate_json():
    json_data = '''
            {
                "name": "Alice",
                "age": 30,
                "email": "alice@example.com",
                "friends": ["Bob", "Charlie"]
            }
            '''
    data = json.loads(json_data)
    print(data)
    # Use dacite's from_dict to map the dictionary to the Person dataclass
    try:
        person = from_dict(data_class=Person, data=data)
        print(person)
    except Exception as e:
        print(f"Error: {e}")

validate_json()