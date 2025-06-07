#Build a simple jounral that runs in terminal
#Warm up with python syntax again and OOP

#Imports
from entry import Entry
import time

class Journal:
    def __init__(self, filepath):
        self.filepath = filepath
        self.entries = []

    def add_entry(self):
        print("Enter the title of the entry: ")
        entry_title = input()
        print("Enter the content of the journal entry: ")
        entry_content = input()
        #Create the new entry
        self.entries.append(Entry(entry_title,entry_content))
    
    def display_entries(self):
        for entry in self.entries:
            print("--------------------------------------------------------------\n")
            entry.display()

    def save_to_file(self):
        print(f"Saving Jounral to {self.filepath}")

        with open (self.filepath, 'w') as file:
            for entry in self.entries:
                file.write(f"{entry.timestamp.isoformat()}|~|{entry.title}|~|{entry.content.replace('\n', '<br>')}\n")

    def load_jounral(self):
        print(f"Loading Jounral from {self.filepath}")
        try:
            with open(self.filepath, "r") as file:
                for line in file:
                    parts = line.strip().split("|~|")
                    if len(parts) == 3:
                        title = parts[1]
                        content = parts[2].replace('<br>', '\n')

                        loaded_entry = Entry(title, content)
                        loaded_entry.timestamp = parts[0]
                        self.entries.append(loaded_entry)
            print("Journal Loaded Successfuly!\n")
        except FileNotFoundError:
            print(f"File {self.filepath} does not exist")