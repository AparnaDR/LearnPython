condition = ""
started = False
#stopped = False
while True:
    text = input("> ").lower()
    if text == 'help':
        print("""
start - to start the car
stop -  to stop the car
quit - to exit
        """)
    elif text == "start" and started == False:
        print("car started")
        started = True
    elif text == "start" and started == True:
        print("car has already started")
    elif text == "stop":
        if not started:
       # if stopped:
            print(" car is already stopped")
        else:
            started = False
            print("car stopped")
    elif text == "quit":
        break
else:
    print("invalid type")

