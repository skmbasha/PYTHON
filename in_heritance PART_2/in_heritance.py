class X:
    a=1000
    def m1(self):
        print ("in m1 of x")
class Y(X): # in () getting in heritance from X
    b=2000
    def m2(self):
        print ("in m2 of y")
y1=Y()
y1.m2
print (y1.b)
y1.m1()
print (y1.a)