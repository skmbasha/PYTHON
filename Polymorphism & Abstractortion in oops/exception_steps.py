#step:1
try:
    a=int(input("enter a number "))
    b=int(input("enter a number "))
    division=a/b
#step:2
except TypeError:
    print ("TypeError,pllease do not entre  0 as denominatr")
#step:3
else:
   print ("division is:division")
#step:4
finally:
    print ("mandetary stmnt")
 # we need to handle exception to progrmm strong & secur