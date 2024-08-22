def hello():
    print('Hello, User!')

def pack(arg1, arg2, arg3):
    return [arg1, arg2, arg3]

def eat_lunch(my_lunch):
    if len(my_lunch) == 0:
        print("My lunchbox is empty!")
    else:
        print(f"First I eat {my_lunch[0]}")
        for item in my_lunch[1:]:
            print(f"Next I eat {item}")

hello()
print(pack("sandwich", "chips", "apple"))
eat_lunch(["sandwich", "chips", "apple"])
eat_lunch([])

