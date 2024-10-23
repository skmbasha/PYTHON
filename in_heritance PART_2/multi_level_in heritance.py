class X: # we can acces X in y but not y in x
    a=1000
    def m1(self):
        print ("in m1 of x")
class Y(X):
    b=2000
    def m2(self):
        print ("in m2 of y")
class Z(Y):
    c=3000
    def m3(self):
        print ("in m3 of Z")
x2=Y
x2.m1
x3=Z
x3.m2
