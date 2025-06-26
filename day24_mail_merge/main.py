#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

# Read the template letter lines
letter = open("Input/Letters/starting_letter.txt", "r").readlines()

# Read the list of names
names = open("Input/Names/invited_names.txt", "r")

for name in names:
    name = name.strip("\n")           # Remove newline from the name
    new_letter = letter[:]            # Make a copy of the template lines
    new_letter[0] = new_letter[0].replace("[name]", name)  # Replace placeholder in the first line

    # Write the personalized letter to a new file
    with open(f"Output/ReadyToSend/{name}_invited.txt", "w") as file:
        for line in new_letter:
            file.write(line)