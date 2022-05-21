def send_messages(messages , empty_messages):
    while messages:
        message=messages.pop()
        print(message.title())
        empty_messages.append(message)

messages=['harry potter', 'vol de mort', 'hagrid']
empty_messages=[]
print(messages)
print(empty_messages)
send_messages(messages[:], empty_messages)
print(messages)
print(empty_messages)