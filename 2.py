# Wroyte a program to greet all the list memebers starting with s 
l = ["Harry","Shubham","Swapnil","Sagar","Vivek"]
for name in l:
    if(name.startswith("S")):
        print(f"Hello {name}")
    else:
        print("None")