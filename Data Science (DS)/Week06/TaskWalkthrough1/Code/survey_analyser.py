# Class Definition for Participants in Survey
class Participant:
# Constructor with attributes
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        self.responses = {}

# Methods
    def update_response(self, question, answer):
        self.responses[question] = answer
    

# Helper Functions for I/O
# Read data
def read_data(filename):
    participants = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                name, age, email = line.strip().split(',')
                participants[name] = Participant(name, int(age), email)
    except FileNotFoundError:
        print("File not found. Starting with an empty list.")
    return participants 

# Write data
def save_data(filename, participants):
    with open(filename, 'w') as file:
        for name in participants:
            participant = participants[name]
            file.write(f"{participant.name},{participant.age},{participant.email}\n")


# Function to analyse survey responses


# Main program code
def main():
    participants = read_data("participants.txt")
    while True:
        print("\n--- Survey Data Manager ---")
        print("1. Add Participant")
        print("2. Update Responses")
        print("3. Save and Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            email = input("Enter email: ")
            participants[name] = Participant(name, age, email)
        
        elif choice == "2":
            name = input("Enter the name of the participant to update: ")
            if name in participants:
                    question = input("Enter survey question: ")
                    answer = input("Enter response: ")
                    participants[name].update_response(question, answer)
                    print("Response updated.")
                    found = True
            else:
                print("Participant not found.")
        
        elif choice == "3":
            save_data("participants.txt", participants)
            print("Data saved. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")



if __name__ == "__main__":
    main()
