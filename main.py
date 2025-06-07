#Main 
from journal import Journal
from entry import Entry


def main():
    
    #List of Journals
    journal = Journal()


    #While Loop
    while True:

        print("1: Create new Entry")
        print("2; Display Entroes")
        print("3: Exit")
        #Get User Input
        user_input = input()

        if user_input == '1':
            print("Adding new entry: ")
            journal.add_entry()

        elif user_input == '2':
            print("Displaying Entries: ")
            journal.display_entries()
        elif user_input == '3':
            break
        
        else:
            "Please enter a valid input..."

if __name__ == "__main__":
    main()
