import requests
from datetime import datetime
from icalendar import Calendar, Event
import tempfile, os

class NotionClient:

    def __init__(self, _token):
        self.cal = Calendar()
        self.TOKEN = _token
    
    def get_database(self, database_id):
        url = f"https://api.notion.com/v1/databases/{database_id}/query"
        headers = {
            "Authorization": f"Bearer {self.TOKEN}",
            "Notion-Version": "2021-08-16",
            "Content-Type": "application/json"
        }
        data = {
            "query": "Class Deadlines",
            "sort": {
                "direction":"ascending",
                "timestamp":"last_edited_time"
            }
        }

        events = []

        items = requests.post(url, headers=headers).json()["results"]
        for item in items:
            type_ = item["properties"]["Type"]["select"]["name"] # if its Assignment | Exam -> Make `title` all CAPS
            class_name = item["properties"]["Class"]["select"]["name"]
            title = item["properties"]["Name"]["title"][0]["plain_text"]
            if type_ == "Assignment" or type_ == "Exam":
                title.upper()
            date = item["properties"]["Date"]["date"]["start"]
            date = datetime.strptime(date, '%Y-%m-%d')
            
            url = item["url"]
            events.append(
                {
                    "title": f"{title} [{class_name}]",
                    "date": date,
                    "url": url,
                }
            )
        
        self.export_ical(events)
    
    def export_ical(self, items):
        # Add events to ical
        for item in items:
            event = Event()
            event.add("summary", item["title"])
            event.add("dtstart", item["date"].date())
            self.cal.add_component(event)

        # Write to disk
        with open("Notion.ics", "wb") as f:
            f.write(self.cal.to_ical())
            print("Completely Wrote to Disk")