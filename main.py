import converter

option = 3

while option!=0:
    print("press 1 to convert string to morse\nPress 2 to convert morse to string\nPress 0 to quit")
    option = input(": ")
    string = input("Enter a phrase: ")

    if option == "1":
        print(converter.text_to_morse(string))
    elif option == "2":
        print(converter.morse_to_text(string))
    else:
        print('invalid option')