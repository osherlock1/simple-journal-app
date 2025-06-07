#Main 
from journal import Journal
from entry import Entry


def main():
    
    #List of Journals
    filepath = "journal.txt"
    journal = Journal(filepath)


    #While Loop
    while True:

        print("1: Create new Entry")
        print("2; Display Entroes")
        print("3: Save Jounral")
        print("4: Load Jounral")
        print("5: Exit")
        #Get User Input
        user_input = input()

        if user_input == '1':
            print("Adding new entry: ")
            journal.add_entry()

        elif user_input == '2':
            print("Displaying Entries: ")
            journal.display_entries()

        elif user_input == '3':
            print("Saving jounral")
            journal.save_to_file()

        elif user_input == '4':
            print("Loading Jounral")
            journal.load_jounral()
            
        elif user_input == '5':
            break

        else:
            print("Please enter a valid input...")

if __name__ == "__main__":
    main()
