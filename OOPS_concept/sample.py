class X:
    a=4000
    b=5000
    def modify(self):
        X.a+=2000
        X.b-=1000
    def display(self):
        print (X.a)
        print (X.b)
x1=X()
x1.display()
print ("******************")
x1.modify()
x1.display()
print ("*************")
x2=X()
x2.display()
x2.modify()