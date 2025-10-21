def frequencyCount(ciphertext):
    if len(ciphertext) <= 0:
        print("Empty string")
        return
    frequencyArr = [0.0] * 26
    sumLetters = 0.0
    for ch in ciphertext:
        if ord(ch.lower()) < 97 or ord(ch.lower()) > 122: #'a' to 'z'
            print("Invalid character: " + ch)
            return 1
        frequencyArr[ord(ch.lower()) - 97] += 1
        sumLetters += 1
    # print("Key letter frequency: " + frequencyArr)
    for i in range(26):
        freq = frequencyArr[i]/sumLetters * 100
        print(chr(i + 97).upper() + f": {freq: .2f}%", end="   ")
    print()

def decrypt(ciphertext, keyMap):
    decryptText = []
    for ch in ciphertext:
        decryptText.append(keyMap[ch.lower()])
    return "".join(decryptText)

def main():
    ciphertext = input("Enter ciphertext: ")
    if frequencyCount(ciphertext) == 1:
        return
    currentKeyMap = {chr(i + 97): chr(i + 65) for i in range(26)}# a-z to A-Z; plain to cipher
    while True:
        print("Current decryption: ")
        print(decrypt(ciphertext, currentKeyMap))
        
        userIn = input("Enter 'KEY' to guess full key, 'SUB' to map cipher char to plaintext char, or 'QUIT': ")
        
        if userIn == "QUIT":
            break
        
        elif userIn == 'KEY':
            keyGuess = input("Enter full key (26 unique uppercase letters): ").upper()
            alphaSet = set()
            success = True
            if len(keyGuess) == 26 and keyGuess.isalpha():
                for i in range(26):
                    pchar = chr(i + 97)
                    cchar = keyGuess[i]
                    if cchar in alphaSet:
                        print("Invalid key: duplicate character: " + cchar)
                        success = False
                        break
                    else:
                        currentKeyMap[pchar] = cchar
                        alphaSet.add(cchar)
                if success: print("Key success")
                else: print("Key failure")
            else:
                print("Invalid key: wrong size or nonalphabetic character")
        
        elif userIn == 'SUB':
            subGuess = input("Enter substitution in format C=a (CIPHERTEXT=plaintext)")
            if len(subGuess) != 3: print("Invalid format")
            elif ord(subGuess[0]) < 65 or ord(subGuess[0]) > 90: print("Invalid character: " + subGuess[0])
            elif ord(subGuess[1]) != '=': print("Invalid input: '=' not found where expected")
            elif ord(subGuess[2]) < 97 or ord(subGuess[2]) > 122: print("Invalid character: " + subGuess[2])
            else:
                pchar = subGuess[2]
                cchar = subGuess[0]
                tkey = pchar
                tval = currentKeyMap[pchar]
                for key, value in currentKeyMap.items():
                    if value == cchar: tkey = key
                currentKeyMap[pchar] = cchar
                currentKeyMap[tkey] = tval
                print(f"Substitution successful; values for {pchar} and {tkey} swapped")
        
        else:
            print("Invalid input")
            

if __name__ == "__main__":
    main()