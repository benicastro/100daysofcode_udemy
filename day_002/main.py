print("Welcome to the Tip Calculator!")


def calculate_tip(total_cost, num_people, tip_percentage):
    # This function calculates the share of a single individual from the total bill cost including the tip amount
    # Calculate the amount to be paid by each person
    person_share = total_cost / num_people
    # Add corresponding tip amount
    person_share *= 1 + tip_percentage/100
    return person_share


# Ask user to provide info about the bill
total_cost = float(input("Please provide total bill cost: $"))
num_people = int(input("How many people should share the expense?: "))
tip_percentage = int(input("Please provide the percentage tip agreed upon: "))

print(f"Each individual should pay: ${calculate_tip(total_cost, num_people, tip_percentage):.2f}")
