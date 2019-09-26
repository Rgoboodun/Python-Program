p = input("Enter your password: ")
for x in p:
    get_ascii = ord(x)
    s = get_ascii + 3
    var = chr(s)
    print (var)