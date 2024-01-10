from morse_code import text_to_morse, morse_to_text

if __name__ == '__main__':
    is_continue = True
    while is_continue:
        option = input("Enter 1 for text to morse, or enter 2 for morse to text, or 3 for exit : ")

        if option == "1":
            text = input("Enter the message : ").upper()
            result = text_to_morse(text)
            print(f"Converted :\nText : {text}\nMorse code : {result}")
        elif option == "2":
            code = input("Enter the morse code : ")
            result = morse_to_text(code)
            print(f"Converted :\nMorse code : {code}\nText : {result}")
        elif option == "3":
            is_continue = False
        else:
            print("Invalid command...")
