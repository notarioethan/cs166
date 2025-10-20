def frequencyCount(ciphertext):
    if len(ciphertext) <= 0:
        print("Empty string")
        return
    frequencyArr = [0.0] * 26
    sumLetters = 0.0
    for ch in ciphertext:
        if ord(ch.lower()) < 97 or ord(ch.lower()) > 122:
            print("Invalid character: " + ch)
            break
        frequencyArr[ord(ch.lower()) - 97] += 1
    # print("Key letter frequency: " + frequencyArr)
    for i in range(26):
        print(chr(i + 97).upper() + ": " + str(frequencyArr[i]), end="   ")
    print()

ciphertext = input("Enter ciphertext: ")
frequencyCount(ciphertext)
keyfound = False
while keyfound == False:
    keyguess = input("Guess key(26 unique uppercase letters): ")
    
    keyfound = True