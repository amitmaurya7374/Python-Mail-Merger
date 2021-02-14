"""Mail Challenge"""
# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
# Read a Name from a invited_names file.
list_of_invitation = []
list_of_names = []
with open("./Input/Names/invited_names.txt", mode="r") as file:
    guest_name_list = file.readlines()  # This method return all lines in a file
# print(guest_name_list)

for name in guest_name_list:
    striped_names = name.strip()
    list_of_names.append(striped_names)
    with open("./Input/Letters/starting_letter.txt", ) as file:
        content = file.read()
    new_letter = content.replace("[name]", f"{name}")
    list_of_invitation.append(new_letter)

for letter in range(len(list_of_invitation)):
    with open(f"./Output/ReadyToSend/letter_for {list_of_names[letter]}.txt", mode="w") as file:
        file.write(f"{list_of_invitation[letter]}")
