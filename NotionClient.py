import requests

class NotionClient:

    def __init__(self, _token):
        
        self.TOKEN = _token
        print(self.TOKEN)