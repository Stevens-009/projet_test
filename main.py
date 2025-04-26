import sys
import os
from encryption_utilities import loadPasswordFile, savePasswordFile, passwordEncrypt, passwordDecrypt


passwords = [["yahoo", "XqffoZeo"], ["google", "CoIushujSetu"]]


passwordFileName = "samplePasswordFile.csv"


encryptionKey = 16

while True:
    print("What would you like to do:")
    print(" 1. Open password file")
    print(" 2. Lookup a password")
    print(" 3. Add a password")
    print(" 4. Save password file")
    print(" 5. Print the encrypted password list (for testing)")
    print(" 6. Quit program")
    print("Please enter a number (1-6)")
    choice = input()

    if choice == '1':  # Load the password list from a file
        try:

            passwords = loadPasswordFile(passwordFileName)

            if passwords:
                print("Password file loaded successfully.")
                for site, encrypted in passwords:
                    print(f"Website: {site}, Encrypted password: {encrypted}")
            else:
                print("No passwords found in the file.")

        except Exception as e:
            print(f"An error occurred: {e}")
            passwords = []


    elif choice == '2':

        print("Which website do you want to lookup the password for?")

        for keyvalue in passwords:
            print(keyvalue[0])

        passwordToLookup = input()

        found = False

        for entry in passwords:

            if entry[0] == passwordToLookup:
                encrypted_password = entry[1]

                decrypted_password = passwordDecrypt(encrypted_password, encryptionKey)

                print(f"The password for {passwordToLookup} is: {decrypted_password}")

                found = True

                break

        if not found:
            print(f"No password found for {passwordToLookup}.")

    elif choice == '3':
        print("What website is this password for?")
        website = input()
        print("What is the password?")
        unencryptedPassword = input()

        encryptedPassword = passwordEncrypt(unencryptedPassword, encryptionKey)
        new_entry = [website, encryptedPassword]
        passwords.append(new_entry)
        print(f"Password for {website} added successfully.")

    elif choice == '4':
        savePasswordFile(passwords, passwordFileName)
        print("Passwords saved.")

    elif choice == '5':
        for keyvalue in passwords:
            print(', '.join(keyvalue))

    elif choice == '6':
        print("Exiting program.")
        sys.exit()

    else:
        print("Invalid input. Please enter a number from 1 to 6.")

    print()
