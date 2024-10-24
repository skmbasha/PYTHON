class X:
    def m1(self):
        print ("in m1 of x")
    def m4(self):
        print("in m4 of x")
class Y(X):
    def m1(self):
        print("in m1 of y")
    def m3(self):
        print("in m3 of y")
y1=Y()
y1.m1()
y1.m4()