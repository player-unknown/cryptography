def vigenereCipher(key,message):
    output=""
    print(key)
    print()
    print(message)
    for i in range(len(message)):
       # print("the char is:",chr(ord(key[i%len(key)])))
       #print(chr(((ord(message[i])+ord(key[i%len(key)])-ord("a")))))
       #what does it do
       # print(message[i] +"=" + str(ord(message[i])))
        output=output+(chr(((ord(message[i])+ord(key[i%len(key)])-2*ord("a")))%26+ord("a")))
        #print(output)
    #print("the output is:",output)
    return output


def vigenereDeCipher(key,encryptedMessage):
    print("key : " + key)
    print("encrypted message is:"+ encryptedMessage)
    message=""
    for i in range(len(encryptedMessage)):
        print(chr(ord("a")+i))
        print(encryptedMessage[i],str(ord(encryptedMessage[i])))
        print(key[i%len(key)] , str(ord(key[i%len(key)])))
        n=ord(encryptedMessage[i])-(ord(key[i%len(key)])-ord("a"))
       
        if(n<ord("a")):
            n=ord("a")+(ord("a")-n)

        print(n)
        print(chr(n))
        print()
        message=message + chr(n) 
    print(message)    
output=vigenereCipher("hjikl","abcdefghijklmnopqrstuvwxyz")
print(output)
print()
vigenereDeCipher("hjikl",output )
