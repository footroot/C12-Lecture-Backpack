# Class Definition for Participants in Survey
class Participant:
    # Constructor with attributes
    # (add in functionality to allow for responses to be provided as well)
    def __init__(self, name, age, email, responses={}):
        self.name = name
        self.age = age
        self.email = email
        self.responses = responses

    # Methods
    def update_response(self, question, answer):
        self.responses[question] = answer

    # Method to validate an email address
    # We'll make this very simple, checking that there's an @ and a .
    # Note that this alone is not sufficient but suffices in this example
    def validate_email(self):
        return (("@" in self.email) and ("." in self.email))

    # Method for printing out a participant
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Email: {self.email}, Responses: {self.responses}"


myParticipant = Participant("Jane Doe", 56, "jane@doe.com", {
    "name": "Jake",
    "age": 78
})

print(myParticipant)
# Helper Functions for I/O
# Read data


def read_data(filename):
    participants = {}
    try:
        # Add in functionality to retrieve responses
        with open(filename, "r") as file:
            for line in file:
                data = line.strip().split(',')

                name = data.pop(0)
                age = data.pop(0)
                email = data.pop(0)
                responses = {}

                while (len(data) > 0):
                    q, a = data.pop[0].split(':')
                    responses[q] = a

                participants[name] = Participant(
                    name, int(age), email, responses)

    except FileNotFoundError:
        print("File not found. Starting with an empty list.")
    return participants

# Write data


def save_data(filename, participants):
    with open(filename, 'w') as file:
        for participant in participants.values():
            # Add functionality to save responses
            line = f"{participant.name},{participant.age},{participant.email}"

            for q in participant.responses:
                line += f",{q}:{participant.responses[q]}"

            file.write(line + "\n")


# Function to analyse survey responses
# Display the average age and number of participants
def analyse_participants(participants):
    num_participants = len(participants)

    total_age = 0
    for participant in participants.values():
        total_age += participant.age
    average_age = total_age/num_participants

    print(f"Number of participants: {num_participants}")
    print(f"Average age of participants: {average_age:.2f}")


# Main program code
# Extra functionality that can be added:
# print out all participants,
# print out responses for specific participant
def main():
    participants = read_data("participants.txt")
    while True:
        print("\n--- Survey Data Manager ---")
        print("1. Add Participant")
        print("2. Update Responses")
        print("3. Participant Statistics")
        print("4. Save and Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            email = input("Enter email: ")
            participant = Participant(name, age, email)

            # Add in to validate email address before adding to list
            if participant.validate_email():
                participants[name] = participant
                print("Participant added successfully.")
            else:
                print("Invalid email address. Please try again.")

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

        # Extra choice for participant statistics
        elif choice == "3":
            analyse_participants(participants)

        elif choice == "4":
            save_data("participants.txt", participants)
            print("Data saved. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
