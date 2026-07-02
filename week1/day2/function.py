def personal_info(*args,**kwargs):
    print(type(args))
    print(type(kwargs))
    for arg in args:
        print(arg)
    for k,v in kwargs.items():
        print(f"{k}:{v}")

personal_info("sanskar","vaishya","asdfg",state="maharashtra")
