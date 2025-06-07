#Build a simple jounral that runs in terminal
#Warm up with python syntax again and OOP

#Imports
from entry import Entry
import time

class Journal:
    def __init__(self):
        self.entries = []

    def add_entry(self):
        print("Enter the title of the entry: ")
        entry_title = input()
        print("Enter the content of the journal entry: ")
        entry_content = input()
        entry_time = time.time()
        #Create the new entry
        self.entries.append(Entry(entry_title,entry_content,entry_time))
    
    def display_entries(self):
        for entry in self.entries:
            print("--------------------------------------------------------------\n")
            entry.display()






