def outter():
    
    def inner():
        print("i am inner")
    return inner
result=outter()
result()

