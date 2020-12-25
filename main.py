adminuser = "admin"
adminpass = "superduperpassword"


word = "Orange"
tries = 3

while True:
    print("Welcome! What do you want to do today?")
    print("1 - Play!")
    print("2 - Modify game settings.")
    print("3 - Close the game.")
    action = input("->")

    if action == "1":
        #If first action is chosen
        win = False

        i = 1

        while i <= int(tries):
            text = input("What's the word? ->")

            if text == word:
                win = True
                break
            else:
                print("Nope, wrong!")
            i = i + 1

        if win == True:
            print("Yay, you won!")
        else:
            print("You lost! Game over!")

    if action == "2":
        #If second action is chosen
        print("Welcome to the admin pannel! Please log in!")
        username = input("Username ->")
        password = input("Password ->")
        if username == adminuser and password == adminpass:
            print("Welcome, " + adminuser + "! What do you want to modify?")
            print("1 - The word. Current word: " + word)
            print("2 - Number of tries. Current number: " + str(tries))
            print("3 - Log out")
            setting = input("->")
            if setting == "1":
                word = input("New word ->")
                print("Word changed!")
            if setting == "2":
                tries = input("New number ->")
                print("Number of tries changed!")
        else:
            print("Incorrect username or password!")

    if action == "3":
        #If third action is chosen
        break
