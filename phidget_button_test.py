from Phidget22.Phidget import *
from Phidget22.Devices.DigitalInput import *
import time

def DigitalInput0_StateChange(self, state):
        print("Ready to start [" + str(self.getChannel()) + "]: " + str(state))
        if(state):
              print ("Ready")
        else:
              print ("Running")
def DigitalInput1_StateChange(self, state):
	print("Stop - shoe size =  [" + str(self.getChannel()) + "]: " + str(state))
        if(state):
              print ("Measured")
        else:
              print ("Measuring")

def main():
        digitalInput0 = DigitalInput()
        digitalInput1 = DigitalInput()

        digitalInput0.setChannel(0)
        digitalInput1.setChannel(1)

        digitalInput0.setOnStateChangeHandler(DigitalInput0_StateChange)
        digitalInput1.setOnStateChangeHandler(DigitalInput1_StateChange)

        digitalInput0.openWaitForAttachment(5000)
        digitalInput1.openWaitForAttachment(5000)

        try:
                input("Press Enter to Stop\n")
        except (Exception, KeyboardInterrupt):
                pass

        digitalInput0.close()
        digitalInput1.close()

main()

