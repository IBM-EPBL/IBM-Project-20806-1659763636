import random
import time

i=0
while(i<=20):

    temp=random.randint(1,100)

    humidity=random.randint(1,100)

    if(temp>=40 and humidity<=40):
        print("Temp ==> {} humidity ==> {}".format(temp,humidity))
        print("<><><><><><><> Alarm Activated <><><><><><><>")

    else: 
        print("Temp ==> {} humidity ==> {}".format(temp,humidity))
        print("Alarm Deactivated")

    time.sleep(2)
    i+=1
    
