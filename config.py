import json

class Config:
    config = None
    def __init__(self):
        pass

    @classmethod
    def load_config(cls, path):
        with open(path,"r") as f:
            cls.config = json.load(f)

