import datetime

#Entry Class
class Entry:
    def __init__(self, title : str, content : str) -> None:
        self.content = content
        self.title = title
        self.timestamp = datetime.datetime.now()
        #Set time to when the entry in initialized

    def display(self):
        print(f"Entry Title: {self.title}\n")
        print(f"Entry Content: {self.content}\n")
        print(f"Entry Time: {self.timestamp}\n")


