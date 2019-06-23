import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
LED = 11
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, False)
status = 0
while True:
    cmd = input('Enter your command as "ON" , "OFF" or "Q": ')
    cmd = cmd.lower()
    if cmd == "on":
        if status == 1 :
            print('The LED is already "ON". Use "OFF" or "Q" to change the status of the LED.')
        else:
            GPIO.output(LED, True)
            print("The LED has been switched ON.")
            status = 1
    elif cmd == "off" :
        if status == 0:
            print('The LED is already OFF. Switch the LED ON by "ON" command or quit using "Q" command.')
        else:
            GPIO.output(LED, False)
            status = 0
            print("The LED has been switched OFF.")
    elif cmd == "q":
        ans = input("Do you really want to quit(Y/N): ")
        ans = ans.lower()
        if ans == "y":
            print("The LED will be turned OFF before leaving the control")
            time.sleep(2)
            GPIO.output(LED, False)
            status = 0
            break
        elif ans == 'no':
            continue
        else:
            print('Invalid entry!!!')
            continue
    else:
        print("Command not recognised!!!")
        continue
GPIO.cleanup()

