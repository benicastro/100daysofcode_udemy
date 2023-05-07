# Create a greeting
print("Welcome to the Band Name Generator!")

# Ask the user for the city they grew up in and their pet's name
# Make the input cursor show on a new line
city = input("What's the name of the city you grew up in?:\n")
pet_name = input("What's your pet's name?:\n")

# Create a function to take the user inputs and combine them to make it their band name


def band_name(city_input, pet_input):
    # This function generates a band name from the user's inputs
    return f"Your band name could be {city_input} {pet_input}!"


print(band_name(city, pet_name))
