# summer time project:
temp = int(input("enter your tempreture near your house - in celcius: "))
if temp > 13:
    print("the wether outside your home in summer is below the minimum in summer")
else:
    print("your wether outside your home is above minimum")
y = ("yes")
v = input("are you going to vacation this summer? ")

dtt = 3
if v == y:
    print("nice hope you enjoy")
else:
    print("its allright")
opt2 = input("are you going on a drive insted? ")
if opt2 == y:
    print("oh thats nice")
else:
    print("maybe try to going next next time")
    exit()
  
dt = float(input("how long is the drive? -in hours: ")) 
if dtt>dt:
    print("have a nice and safe drive")
else:
    print(" have a nice and safe drive to your destination :)")        
