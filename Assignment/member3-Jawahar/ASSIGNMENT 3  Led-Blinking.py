import RPi.GPIO as GPIO 
from time import sleep 

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(8, GPIO.OUT) 

while True: 
   print("LED IS ON")
   GPIO.output(8, GPIO.HIGH)
   sleep(1) 
   print("LED IS OFF")
   GPIO.output(8, GPIO.LOW) 
   sleep(1) 
