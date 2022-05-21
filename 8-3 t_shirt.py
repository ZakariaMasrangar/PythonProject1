def make_shirt(size, message):
    print(f"the message is {message}\n of size is {size}")
s=10
m="Lakers"

make_shirt(s, m) # positional argument
make_shirt(size=s,message=m) # keyword argument