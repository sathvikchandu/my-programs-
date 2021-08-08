for i in range(-26,26):           #like the key can be forward or nackward to +25 forward or -25 backward, all possiblities are checked
    for i in range(0,26):

        shift = i 

        text = "ZICVTWQNGKZEIIGASXSTSLVVWLA"

        encryption = ""

        for c in text:

            
            if c.isupper():       #since we have to take an approach, i only took capital letters as input

                
                

                idx = ord(c) - ord("A")

                
                idx = (idx + shift) % 26

                
                new = idx + ord("A")

                cha = chr(new)

                
                encryption = encryption + cha

            else:

                
                encryption += c       #for spaces in between the text
                
        print("Plain text:",text)

        print("Encrypted text:",encryption)