letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
        'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
plaintext = input("input the text to be ciphered: ")
key = int(input("shift number? "))
def encode(plaintext,key):
    cipher = ""
    text = plaintext.lower()
    for lettersintext in text:
        if lettersintext ==" ":
            cipher+=" "
        else:
            for i in range(len(letter)):
                if letter[i] == lettersintext:
                    cipher += letter[i+key]
                    break
    return cipher

print(encode(plaintext,key))
