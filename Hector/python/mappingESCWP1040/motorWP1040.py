# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
def AngleToDuty(ang):
  duty = float(pos)/10.+5.
  return duty
  
servoPin=12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPin,GPIO.OUT)
pwm=GPIO.PWM(servoPin,100)
depart =100
arrivee=130
DELAY=0.5
incStep=5
pos=depart

if __name__ == '__main__' :
    pwm.start(AngleToDuty(pos)) #star pwm
    i=''
    while i != 'y':
        print("--------------------------run {}".format(i)) 
        for pos in range(depart,arrivee,incStep):
            duty=AngleToDuty(pos)
            pwm.ChangeDutyCycle(duty)
            #print('¿Ya comenzó a girar?')
            #i = input("y)Ya, n)No")
            if i == 'y':
                print('Pwm:', pos)
                break
            else:
                pass
            print(pos)
            time.sleep(DELAY)
        print("position: {}° -> duty cycle : {}%".format(pos,duty))
      
    pwm.stop()
    GPIO.cleanup()
