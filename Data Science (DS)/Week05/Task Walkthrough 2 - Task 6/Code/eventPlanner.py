def venue_cost(event_type, attendees):
    rates = {"wedding": 100, "birthday": 50, "corporate": 75}
    per_person_rate = rates.get(event_type.lower(), 0)
    total = per_person_rate * attendees
    if attendees > 100:
        total *= 0.9  # 10% discount for large groups
    return total

def catering_cost(attendees, meal_plan):
    meal_rates = {"basic": 20, "standard": 40, "luxury": 60}
    beverages = input("Include beverages? (yes/no): ").lower() == "yes"
    desserts = input("Include desserts? (yes/no): ").lower() == "yes"
    total = attendees * meal_rates.get(meal_plan.lower(), 20)
    if beverages:
        total += attendees * 5  # ￡5 per person for beverages
    if desserts:
        total += attendees * 7  # ￡7 per person for desserts
    return total

def entertainment_cost():
    options = {"DJ": 500, "live band": 1500, "photo booth": 300}
    print("\nAvailable entertainment options:")
    for option, cost in options.items():
        print(f"{option}: ${cost}")
    selected = []
    while True:
        choice = input("Enter an entertainment option (or 'done' to finish): ").lower()
        if choice == "done":
            break
        if choice in options:
            selected.append(options[choice])
        else:
            print("Invalid option. Please choose from the list.")
    return sum(selected)


def main():
    print("Welcome to the Event Planner Calculator!")
    event_type = input("Enter the event type (wedding, birthday, corporate): ")
    attendees = int(input("Enter the number of attendees: "))
    meal_plan = input("Enter the meal plan (basic, standard, luxury): ")
    budget = float(input("Enter your total event budget: "))


    # Call function to calculate total cost
    venue = venue_cost(event_type, attendees)
    catering = catering_cost(attendees, meal_plan)
    entertainment = entertainment_cost()
    total = venue + catering + entertainment

    # Display results
    print("\n--- Event Cost Breakdown ---")
    print(f"Venue Cost: ${venue:.2f}")
    print(f"Catering Cost: ${catering:.2f}")
    print(f"Entertainment Cost: ${entertainment:.2f}")
    print(f"Total Event Cost: ${total:.2f}") 

    # Budget Comparison
    if total <= budget:
        print("Great! The event is within your budget!")
    else:
        print(f"Oops! The event exceeds your budget by ${total - budget:.2f}.")
        print("Consider adjusting your plans to reduce costs.")

        # Go through each expense and suggest way to decrease cost


if (__name__ == "__main__"):
    main()