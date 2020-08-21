import string,random
capta=''
words=''.join((string.ascii_letters,string.digits))
for i in range(6):
    capta+=random.choice(words)
print(capta)
input()
