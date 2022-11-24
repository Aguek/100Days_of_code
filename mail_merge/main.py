# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# get the names
with open("./Input/Names/invited_names.txt", "r") as names:
    list_of_names = names.readlines()
    # looping through the names list to get every name.
    for name in list_of_names:
        with open("./Input/Letters/starting_letter.txt") as letter_file:
            letter_body = letter_file.read()
            stripped_name = name.strip()
            # replace [name] with the name of the person
            individual_letters = letter_body.replace("[name]", stripped_name)
            new_letter = open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w")
            new_letter.write(individual_letters)
