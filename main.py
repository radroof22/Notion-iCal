from dotenv import load_dotenv
import os
from NotionClient import NotionClient

if __name__ == "__main__":
    load_dotenv()
    notion_token = os.getenv("NOTION_TOKEN")
    notionClient = NotionClient(notion_token)