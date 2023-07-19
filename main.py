#decimal to binary converter
bina_arr=[]
inp=input("Enter an integer:")
if inp.isnumeric():
    inp=int(inp)
    while inp>0:
        if inp%2==0:
            bina_arr.append("0")
            inp=inp/2
        if inp%2==1:
            bina_arr.append("1")
            inp=(inp-1)/2
else:
    print("Invalid")
bina_arr.reverse()
print("".join(bina_arr))