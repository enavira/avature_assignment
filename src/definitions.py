from pydantic import BaseModel
from typing import List
import hashlib

class Job(BaseModel):
    name: str
    salary: int
    country: str
    skills: List[str]

    def get_id_hash(self):
        self.skills = sorted(self.skills)
        _hash = hashlib.md5(self.json().encode()).hexdigest()
        return _hash
