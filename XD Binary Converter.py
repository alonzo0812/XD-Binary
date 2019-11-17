# WELCOME TO XD BINARY BY JOHN LEOMARC ALONZO
print("")
print("Hi there! I'm a program made by John Leomarc M. Alonzo.")
print("Allow me to convert your text to XD and vice versa!")
print("Why do plain old binary when you can do it in XD!")
print("Uses ASCII")
print("")
print("")
run = True
while run:
    try:
        text = input("""Type your text or binary here:""")
        print("""If you want to convert to text type 'text'(Only works for XD binary)""")
        act = input("""If you want to convert to XD binary type 'XD':""")
                    
    except:
        print('Please do this properly.')
        
    if act.lower() == 'xd':
        porkchap = str('')
        for char in text:
            porkchap = porkchap + bin(ord(char))[2:].zfill(8)
        plop = porkchap
        porkchap = porkchap.replace('1', 'X')
        porkchap = porkchap.replace('0', 'D')

        print("")            
        print("Here it is in binary")
        print(plop)
        print("")
        print("Here it is in XD binary")
        print(porkchap)

    elif act.lower() == 'text':
        
        porkchap = text.replace('X', '1')
        porkchap = porkchap.replace('D', '0')
        binary = porkchap
        porkchap = ''.join(chr(int(porkchap[i*8:i*8+8],2)) for i in range(len(porkchap)//8))
        print("")
        print("Here it is in binary")
        print("")
        print(binary)
        print("")
        print("This is what the text says")
        print("")
        print(porkchap)
        print("")
        

    else:
        print("")
        print("I told you to type 'xd' or 'text'")
        print("humans.. ugh")
        print("")
        
