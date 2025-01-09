"""
Event Planner System - Educational Version

This program implements an event planning system with both user and admin functionalities.
It demonstrates key programming concepts including:
- Object-Oriented Programming (using classes and methods)
- Data structures (dictionaries for storing rates and options)
- User input handling and validation
- Basic authentication (admin mode)
- Menu-driven interface

Student Exercise:
1. Complete the 'modify' and 'remove' functions in _modify_venue_rates()
2. Implement similar modification functions for meal rates and entertainment options
3. Add input validation to prevent negative prices or invalid inputs
4. Add a feature to save modified rates to a file
5. Implement a more secure authentication system for admin mode

"""


class EventPlanner:
    def __init__(self):
        # Initialize our pricing data using dictionaries
        # Dictionaries are perfect for this as they allow us to store key-value pairs
        # where keys are the options and values are the prices
        self.venue_rates = {
            "wedding": 100,
            "birthday": 50,
            "corporate": 75
        }
        self.meal_rates = {
            "basic": 20,
            "standard": 40,
            "luxury": 60
        }
        self.entertainment_options = {
            "dj": 500,
            "live band": 500,
            "photo booth": 300
        }

    def admin_mode(self):
        # Admin mode provides a separate menu for modifying prices and options
        # This demonstrates menu-driven interface design and user input handling
        while True:
            print("\n ----Admin Mode---")
            print("1. Modify venue rates")
            print("2. Modify meal rates")
            print("3. Modify entertainment options")
            print("4. Modify add-on costs")
            print("5. Exit admin mode")

            choice = input("Enter your choice (1-5): ")

            # Simple menu routing based on user input
            if choice == '1':
                self._modify_venue_rates()
            # TODO: Implement other menu options (2-4)

    def _modify_venue_rates(self):
        # Display current rates for reference
        # This helps the admin see what they're about to modify
        print("\nCurrent venue rates: ")
        for venue, rate in self.venue_rates.items():
            print(f"{venue}: ${rate}")

        # Get the desired action from the admin
        action = input(
            "Would you like to (add/modify/remove) a venue type? ").lower()

        if action == 'add':
            # Adding a new venue type with error checking
            venue_type = input('Enter the new venue type: ').lower()
            if venue_type in self.venue_rates:
                print('Venue already exists')
                return
            rate = float(input("Enter the rate per person: $"))
            self.venue_rates[venue_type] = rate

        elif action == "modify":
            # TODO: Student exercise - Implement modify functionality
            # 1. Get venue type from admin
            # 2. Check if it exists
            # 3. If it exists, get new rate and update
            pass

        elif action == "remove":
            # TODO: Student exercise - Implement remove functionality
            # 1. Get venue type from admin
            # 2. Check if it exists
            # 3. If it exists, remove it from the dictionary
            pass

    def venue_cost(self, event_type, attendees):
        # Calculate venue cost with potential bulk discount
        # The .get() method is used to safely get dictionary values with a default
        per_person_rate = self.venue_rates.get(event_type.lower(), 0)
        total = per_person_rate * attendees

        # Apply 10% discount for large groups (over 100 people)
        if attendees > 100:
            total *= 0.9  # Multiply by 0.9 to apply 10% discount
        return total

    def catering_cost(self, attendees, meal_plan):
        # Calculate catering cost including optional add-ons
        # Get user preferences for beverages and desserts
        beverages = input("Include beverages? (yes/no): ").lower() == "yes"
        desserts = input("Include desserts? (yes/no): ").lower() == "yes"

        # Calculate base meal cost using the selected plan
        total = attendees * self.meal_rates.get(meal_plan.lower(), 20)

        # Add costs for optional items if selected
        if beverages:
            total += attendees * 5  # Add beverage cost per person
        if desserts:
            total += attendees * 7  # Add dessert cost per person
        return total

    def entertainment_cost(self):
        # Handle entertainment options selection and cost calculation
        print("\nAvailable entertainment options:")
        # Display all available options and their costs
        for option, cost in self.entertainment_options.items():
            print(f"{option}: ${cost}")

        selected = []  # List to store costs of selected options
        # Keep asking for options until user is done
        while True:
            choice = input(
                "Enter an entertainment option (or 'done' to finish): ").lower()
            if choice == "done":
                break
            if choice in self.entertainment_options:
                selected.append(self.entertainment_options[choice])
            else:
                print("Invalid option. Please choose from the list.")
        return sum(selected)  # Return total cost of all selected options


def main():
    # Create an instance of our EventPlanner class
    planner = EventPlanner()

    # Main program loop
    while True:
        print("\nWelcome to the Event Planner Calculator!")
        print("1. Plan an event")
        print("2. Admin mode")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            # Event planning workflow
            print("Welcome to the Event Planner Calculator!")
            # Collect event details from user
            event_type = input(
                "Enter the event type (wedding, birthday, corporate): ")
            attendees = int(input("Enter the number of attendees: "))
            meal_plan = input(
                "Enter the meal plan (basic, standard, luxury): ")
            budget = float(input("Enter your total event budget: "))

            # Calculate costs using our class methods
            venue = planner.venue_cost(event_type, attendees)
            catering = planner.catering_cost(attendees, meal_plan)
            entertainment = planner.entertainment_cost()
            total = venue + catering + entertainment

            # Display itemized costs and total
            print("\n--- Event Cost Breakdown ---")
            print(f"Venue Cost: ${venue:.2f}")
            print(f"Catering Cost: ${catering:.2f}")
            print(f"Entertainment Cost: ${entertainment:.2f}")
            print(f"Total Event Cost: ${total:.2f}")

            # Compare with budget and provide feedback
            if total <= budget:
                print("Great! The event is within your budget!")
            else:
                print(
                    f"Oops! The event exceeds your budget by ${total - budget:.2f}.")
                print("Consider adjusting your plans to reduce costs.")

        elif choice == "2":
            # Simple admin authentication
            # TODO: Student exercise - Implement more secure authentication
            password = input("Enter admin password: ")
            if password == "admin123":  # Basic password check
                planner.admin_mode()
            else:
                print("Invalid password!")

        elif choice == "3":
            print("Thank you for using our platform")
            break

        else:
            print("Invalid choice. Please try again.")


if (__name__ == "__main__"):
    main()
