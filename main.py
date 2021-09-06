from dotenv import load_dotenv
import os
from NotionClient import NotionClient

if __name__ == "__main__":
    load_dotenv()
    notion_token = os.getenv("NOTION_TOKEN")
    notion_client = NotionClient(notion_token)
    notion_client.get_database(os.getenv("DATABASE_ID"))
