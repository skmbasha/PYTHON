class X:
    a=2000
    __b=5000    # wth __ we can secure properties
    def m1(self):
        print ("m1 is open mehtod anyone can access")
        print (X.a),#X.b)= we canot acces it it is in abstraction
x1=X()
x1.m1()
x1.a
#x1.b