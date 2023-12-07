temp = int(input("What is your room temperature?:"))
if not(temp>=0 and temp<=30):
    print("Thats normal")
elif not(temp<0 or temp >30):
    print("its bad go in")
