"""
Mail Merge by Benedict Z. Castro | benedict.zcastro@gmail.com
"""


# Extract the names of the people needed for the invitations
with open("Input/Names/invited_names.txt", mode="r") as file:
    names_raw = file.readlines()

# Clean the data and retain only the names
names_cleaned = []
for name in names_raw:
    names_cleaned.append(name.replace("\n", ""))

# Extract the letter body to be edited
with open("Input/Letters/starting_letter.txt", mode="r") as letter:
    letter_body = letter.read()

# Replace the [name] placeholder in the letter body with the names of the people invited
for name in names_cleaned:
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="a") as output:
        output.write(letter_body.replace("[name]", f"{name}"))
