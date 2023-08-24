print("Wellcome to The Space Travel Calculator!")

distance =  int(input("Enter a distance in light years!"))

speed = int(input("Please enter a spacecraft speed in fraction of the speed of light!"))

time = (distance/speed)

print("It will take", time ,"hours to reach your desired location!")