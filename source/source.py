#import the required modules
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

def socket_setup():
    # set the pins numbering mode
    GPIO.setmode(GPIO.BOARD)

    # Select the GPIO pins used for the encoder K0-K3 data inputs
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)

    # Select the signal to select ASK/FSK
    GPIO.setup(18, GPIO.OUT)

    # Select the signal used to enable/disable the modulator
    GPIO.setup(22, GPIO.OUT)

    # Disable the modulator by setting CE pin lo
    GPIO.output (22, False)

    # Set the modulator to ASK for On Off Keying 
    # by setting MODSEL pin lo
    GPIO.output (18, False)

    # Initialise K0-K3 inputs of the encoder to 0000
    GPIO.output (11, False)
    GPIO.output (15, False)
    GPIO.output (16, False)
    GPIO.output (13, False)

def socket_on(socket):
    print('ON SOCKET {}'.format(socket))
    d3 = None
    d2 = None
    d1 = None
    d0 = None

    if socket == 1:
        d3 = True
        d2 = True
        d1 = True
        d0 = True

    elif socket == 2:
        d3 = True
        d2 = True
        d1 = True
        d0 = False
    # Set K0-K3
    print("sending code {}{}{}{} Socket {} on".format(int(d3), int(d2), int(d1), int(d0), socket))
    GPIO.output (11, d0)
    GPIO.output (15, d1)
    GPIO.output (16, d2)
    GPIO.output (13, d3)
    # let it settle, encoder requires this
    time.sleep(0.1) 
    # Enable the modulator
    GPIO.output (22, True)
    # keep enabled for a period
    time.sleep(0.25)
    # Disable the modulator
    GPIO.output (22, False)

    return "SOCKET {} ON".format(socket)

def socket_off(socket):
    d3 = None
    d2 = None
    d1 = None
    d0 = None

    if socket == 1:
        d3 = False
        d2 = True
        d1 = True
        d0 = True

    elif socket == 2:
        d3 = False
        d2 = True
        d1 = True
        d0 = False
        
    # Set K0-K3
    print ("sending code {}{}{}{} Socket {} off".format(int(d3), int(d2), int(d1), int(d0), socket))
    GPIO.output (11, d0)
    GPIO.output (15, d1)
    GPIO.output (16, d2)
    GPIO.output (13, d3)
    # let it settle, encoder requires this
    time.sleep(0.1)
    # Enable the modulator
    GPIO.output (22, True)
    # keep enabled for a period
    time.sleep(0.25)
    # Disable the modulator
    GPIO.output (22, False)
    return "SOCKET {} OFF".format(socket)
    
def socket_clean():
    GPIO.cleanup()
    return "CLEANUP"

'''
# The On/Off code pairs correspond to the hand controller codes.
# True = '1', False ='0'
print ("The program will now loop around sending codes as follows when you")
print ("hit a key:")
print ("socket 1 on")
print ( "socket 1 off")
print ("socket 2 on")
print ("socket 2 off")
print ("all sockets on")
print ("all sockets off")
print ("Hit CTL C for a clean exit")
try:
    # We will just loop round switching the units on and off
    while True:
        input('hit return key to send socket 1 ON code')
        # Set K0-K3
        print ("sending code 1111 socket 1 on")
        GPIO.output (11, True)
        GPIO.output (15, True)
        GPIO.output (16, True)
        GPIO.output (13, True)
        # let it settle, encoder requires this
        time.sleep(0.1) 
        # Enable the modulator
        GPIO.output (22, True)
        # keep enabled for a period
        time.sleep(0.25)
        # Disable the modulator
        GPIO.output (22, False)

        input('hit return key to send socket 1 OFF code')
        # Set K0-K3
        print ("sending code 0111 Socket 1 off")
        GPIO.output (11, True)
        GPIO.output (15, True)
        GPIO.output (16, True)
        GPIO.output (13, False)
        # let it settle, encoder requires this
        time.sleep(0.1)
        # Enable the modulator
        GPIO.output (22, True)
        # keep enabled for a period
        time.sleep(0.25)
        # Disable the modulator
        GPIO.output (22, False)

        input('hit return key to send socket 2 ON code')
        # Set K0-K3
        print ("sending code 1110 socket 2 on")
        GPIO.output (11, False)
        GPIO.output (15, True)
        GPIO.output (16, True)
        GPIO.output (13, True)
        # let it settle, encoder requires this
        time.sleep(0.1) 
        # Enable the modulator
        GPIO.output (22, True)
        # keep enabled for a period
        time.sleep(0.25)
        # Disable the modulator
        GPIO.output (22, False)

        input('hit return key to send socket 2 OFF code')
        # Set K0-K3
        print ("sending code 0110 socket 2 off")
        GPIO.output (11, False)
        GPIO.output (15, True)
        GPIO.output (16, True)
        GPIO.output (13, False)
        # let it settle, encoder requires this
        time.sleep(0.1)
        # Enable the modulator
        GPIO.output (22, True)
        # keep enabled for a period
        time.sleep(0.25)
        # Disable the modulator
        GPIO.output (22, False)

        input('hit return key to send ALL ON code')
        # Set K0-K3
        print ("sending code 1011 ALL on")
        GPIO.output (11, True)
        GPIO.output (15, True)
        GPIO.output (16, False)
        GPIO.output (13, True)
        # let it settle, encoder requires this
        time.sleep(0.1)
        # Enable the modulator
        GPIO.output (22, True)
        # keep enabled for a period
        time.sleep(0.25)
        # Disable the modulator
        GPIO.output (22, False)

        input('hit return key to send ALL OFF code')
        # Set K0-K3
        print ("sending code 0011 All off")
        GPIO.output (11, True)
        GPIO.output (15, True)
        GPIO.output (16, False)
        GPIO.output (13, False)
        # let it settle, encoder requires this
        time.sleep(0.1) 
        # Enable the modulator
        GPIO.output (22, True)
        # keep enabled for a period
        time.sleep(0.25)
        # Disable the modulator
        GPIO.output (22, False)

# Clean up the GPIOs for next time
except KeyboardInterrupt:
    GPIO.cleanup()
'''
