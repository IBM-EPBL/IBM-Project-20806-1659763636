import RPi.GPIO as GPIO
import time
import mysql.connector
TRIG=21
ECHO=20
dusbinLevelInper=0

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(19, GPIO.OUT)

def DataBaseCon():

    mydb = mysql.connector.connect(

        host="192.168.143.95",
        user="",
        password="",
        database="IbmDataBase"
    )
    mycursor = mydb.cursor()

    sql = "UPDATE dsbn SET dusLevel = "+str(dusbinLevelInper)+" WHERE dusId = '1'"
    mycursor.execute(sql)
    mydb.commit()

    print(mycursor.rowcount, "record(s) affected")


def ledblinkon():
      GPIO.output(19, GPIO.HIGH)

def ledblinkoff():
      GPIO.output(19, GPIO.LOW)

while True:
    print("distance measurement in progress")
    GPIO.output(TRIG,False)
    print("waiting for sensor to settle")
    time.sleep(0.2)
    GPIO.output(TRIG,True)
    time.sleep(0.00001)
    GPIO.output(TRIG,False)
    while GPIO.input(ECHO)==0:
        pulse_start=time.time()
    while GPIO.input(ECHO)==1:
        pulse_end=time.time()
    pulse_duration=pulse_end-pulse_start
    distance=pulse_duration*17150
    distance=round(distance,2)
    print("distance:",distance,"cm")
    time.sleep(2)


    if(distance>=60):
        dusbinLevelInper=0
        ledblinkoff()
    elif(distance<=60 and distance>=45):
        dusbinLevelInper=25
        ledblinkoff()
    elif(distance<=45 and distance>=30):
        dusbinLevelInper=50
        ledblinkoff()
    elif(distance<=30 and distance>=10):
        dusbinLevelInper=80
        ledblinkoff()
 
    else:
        dusbinLevelInper=100
        ledblinkon()
    
    DataBaseCon()

