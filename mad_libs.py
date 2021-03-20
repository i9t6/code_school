#!/home/paco/ubuntu/py3/bin/python
# Loop back to this point once code finishes
loop = 1

while (loop < 2):
    # All the questions that the program asks the user
    noun = input("Choose a noun: ")
    p_noun = input("Choose a plural noun: ")
    noun2 = input("Choose a noun: ")
    place = input("Name a place: ")
    adjective = input("Choose an adjective (Describing word): ")
    noun3 = input("Choose a noun: ")

    print (f" \n \
------------------------------------------ \n \
Be kind to your {noun} - footed {p_noun}  \n \
For a duck may be somebody's {noun2}, \n \
Be kind to your {p_noun} in {place}, \n \
Where the weather is always {adjective}.\n \
             \n \
You may think that is this the {noun3},\n \
Well it is \n \
------------------------------------------\n   ---------- Gracias ----------- ")
    # Loop back to "loop = 1"
    loop = loop + 1