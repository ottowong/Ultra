import base64, sys
arg = sys.argv[1]
with open(str(arg),"rb") as image:
    encoded = base64.b64encode(image.read())

print(str(encoded)[2:][:-1])
input()
