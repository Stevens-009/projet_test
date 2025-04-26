import csv

# Caesar Cypher Encryption
def passwordEncrypt(unencryptedMessage, key):
    encryptedMessage = ''
    for symbol in unencryptedMessage:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            encryptedMessage += chr(num)
        else:
            encryptedMessage += symbol
    return encryptedMessage

def passwordDecrypt(encryptedMessage, key):
    return passwordEncrypt(encryptedMessage, -key)

def loadPasswordFile(fileName):
    try:
        passwordList = []
        with open(fileName, newline='') as csvfile:
            passwordreader = csv.reader(csvfile)
            for row in passwordreader:
                if len(row) == 2:
                    passwordList.append(row)
                else:
                    print(f"Skipping malformed row: {row}")
        print(f"Loaded passwords: {passwordList}")
        return passwordList
    except FileNotFoundError:
        print(f"File '{fileName}' not found.")
        return []
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return []

def savePasswordFile(passwordList, fileName):
    print(f"Saving passwords: {passwordList}")
    with open(fileName, 'w', newline='') as csvfile:
        passwordwriter = csv.writer(csvfile)
        passwordwriter.writerows(passwordList)
