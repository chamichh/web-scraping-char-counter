import socket
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
symbolCount = 0
try:
    url = input("Enter url:")
    domain = url.split("/")[2]
    mysocket.connect((domain, 80))
    texts = "GET " +url+ " HTTP/1.0\r\n\r\n"
    cmd = texts.encode()
    mysocket.send(cmd)
    while True:
        data = mysocket.recv(4096)
        if (len(data) < 1):
            break
        listOfCharacters = list(data.decode())
        for symbol in listOfCharacters:
            if symbolCount >= 2200:
                print("Max character limit reached.")
                break
            print(symbol, end="")
            symbolCount = symbolCount + 1
    mysocket.close()
except:
    print("url entered was improperly formatted or non-existent")
    quit()
print("Character count:", symbolCount)