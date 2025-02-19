from dataclasses import dataclass
from typing import List


@dataclass
class Connection():
    SnowflakeDatabaseConn: str
    AirflowConnection:str

@dataclass
class Person:
    name: str
    age: int
    email: str = None  # Optional field
    friends: list[str] = None  # List of friends
