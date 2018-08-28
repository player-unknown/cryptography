def vigenereCipher(key,message):
    output=""
    print(message)
    print(key)
    for i in range(len(message)):
        print("the char is:",chr(ord(key[i%len(key)])))
       #print(chr(((ord(message[i])+ord(key[i%len(key)])-ord("a")))))
        output=output+(chr(((ord(message[i])+ord(key[i%len(key)])-ord("a")))))
       # print(output)
    print("theputis:",output)

vigenereCipher("kkkss","mohantejaisagoodboy")