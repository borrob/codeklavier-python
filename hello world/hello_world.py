import time
import rtmidi

# Use trick to import from parrentdir
import sys
import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from CodeKlavier.Setup import Setup
from CodeKlavier.Mapping import Mapping_HelloWorld
from CodeKlavier.Mapping import Mapping_HelloWorld_NKK
from CodeKlavier.Callback import Callback

# Start the CodeKlavier
codeK = Setup()
myPort = codeK.perform_setup()
codeK.open_port(myPort)
device_id = codeK.get_device_id()
print('your device id is: ', device_id, '\n')

# Use your favourite mapping of the keys
print("Which keyboard map do you want to use?")
print("  1. Hello World (normal)")
print("  2. Hello World (NKK)")
choice_ok = False
while not(choice_ok):
    map_number = input("__?")
    if(int(map_number) == 1):
        mapping = Mapping_HelloWorld()
        choice_ok = True
        break
    elif(int(map_number) ==2 ):
        mapping = Mapping_HelloWorld_NKK()
        choice_ok = True
        break
    else:
        print("Please type 1 or 2.")

# class to handle the midi input and map it to characters
callback = Callback(device_id, myPort, mapping)

print("\nCodeKlavier is ready and ON.")
print("You are performing: HELLO WORLD")
print("\nPress Control-C to exit.")

codeK.set_callback(callback)

# Loop to program to keep listening for midi input
try:
    timer = time.time()
    while True:
        time.sleep(0.01)
except KeyboardInterrupt:
    print('')
finally:
    print("Bye-Bye :(")
    codeK.end()
