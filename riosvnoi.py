a=int(input("Pretend You Bought Something: How Much  Does It Cost?"))
b=int(input("Ok, now pretend you sell it. What do you get for it?"))
c=a-b
d = b-a
if a > b:
    print ("You just earnt", c, "Dollars!")
elif a == b:
    print ("You just did nothing.")
else:
    print ("You just lost", d, "Dollars!")