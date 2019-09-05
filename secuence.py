n = int(input("Enter the length of the sequence: ")) 

one=1
two=2
three=3


for i in range(1,n+1):
    print(one)
    one,two,three = two,three,one+two+three

