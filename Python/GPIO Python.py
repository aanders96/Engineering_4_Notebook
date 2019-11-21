import RPi.GPIO as GPIO #Import Rasberry Pi GPIO library
from time import sleep #Import the sleep function from the time module

GPIO.setwarnings(False) #Ignore warning for now
GPIO.setmode(GPIO.BCM) # use physical pin numbering
GPIO.setup(17,GPIO.OUT,initial=GPIO.LOW) # Set pin 17 to be an output pin and set intial value to low (off)

while True: # Run forever
    GPIO.output (17,GPIO.HIGH) # Turn on
    sleep(1) # sleep for 1 second
    GPIO.output(17,GPIO.LOW) #Turn Off
    sleep(1) #sleep for 1 second
