import RPi.GPIO as GPIO
import time
# Use port numbering
GPIO.setmode(GPIO.BCM)
# Declare output ports
out1 = 16
out2 = 19
out3 = 13
# Declare input ports
in1 = 21
in2 = 20
# Set out1, out2, and out3 as output ports
GPIO.setup(out1, GPIO.OUT)
GPIO.setup(out2, GPIO.OUT)
GPIO.setup(out3, GPIO.OUT)
# Set in1 and in2 as input ports and activate pull down
GPIO.setup(in1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(in2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# Make threaded callback function
def LEDwithButton(pin):
  if GPIO.input(in1)==0:
    GPIO.output(out1, 0)
    time.sleep(.5)
    GPIO.output(out1, 1)
    time.sleep(.5)
    GPIO.output(out1, 0)
  elif GPIO.input(in2)==0:
    GPIO.output(out2, 0)
    time.sleep(.5)
    GPIO.output(out2, 1)
    time.sleep(.5)
    GPIO.output(out2, 0)

GPIO.add_event_detect(in1, GPIO.FALLING, callback=LEDwithButton, bouncetime=100)
GPIO.add_event_detect(in2, GPIO.FALLING, callback=LEDwithButton, bouncetime=100)

try:
  while True:
    GPIO.output(out3, 0)
    time.sleep(0.5)
    GPIO.output(out3, 1)
    time.sleep(.5)
except KeyboardInterrupt:
  print('\nExiting')
except Exception as e:
  print('\ne')

GPIO.cleanup()