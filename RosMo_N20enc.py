"""
******************************************************************
                         RosMo_N20enc.py
       a class for controlling N20 motors with encoders

Dec 2024  Alex Just-Alex
******************************************************************

Derived from encoder_N20_esp.py by rakesh-i
found here https://github.com/rakesh-i/MicroPython-Encoder-motor/blob/main/encoder_N20_esp.py

which contained the following copyright notice:

MIT License

Copyright (c) 2022 rakesh-i

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from time import sleep_ms, ticks_us
from machine import Pin, PWM, disable_irq, enable_irq
from RosMo_Motors import DCMotor

class EncodedMotor:
    
    # Instance variable for keeping the record of the encoder position
    pos = 0
    reverse = False #motors on RHS move in opposite direction
    # Interrupt handler
    def handle_interrupt(self,pin):
        a = self.px.value()
        if self.reverse:
            a = 1 - a
        if a > 0:
            self.pos = self.pos+1
        else:
            self.pos = self.pos-1
    
    # Constructor for initializing the motor pins
    def __init__(self,fwdPin, bwdPin, rvse, encA, encB):
        self.px = Pin(encA, Pin.IN)
        self.py = Pin(encB, Pin.IN)
        self.freq = 50
        self.reverse = rvse
        self.motor = DCMotor(fwdPin,bwdPin)
        # Interrupt initialization
        self.py.irq(trigger=Pin.IRQ_RISING, handler=self.handle_interrupt)
    
    # Arduino's map() function implementation in python 
    def convert(self, x, i_m, i_M, o_m, o_M):
        return max(min(o_M, (x - i_m) * (o_M - o_m) // (i_M - i_m) + o_m), o_m)

    # A function for speed control without feedback(Open loop speed control)
    def speed(self,M):
        #expects -1000 to +1000, DCMotor class expects -1 to +1 
        self.motor.speed(M/1000)

# A class for closed loop speed and postion control
class PID:
    
    # Instance variable for this class
    posPrev = 0

    # Constructor for initializing PID values
    def __init__(self, M, kp=1, kd=0, ki=0, umaxIn=990, eprev=0, eintegral=0):
        self.kp = kp
        self.kd = kd
        self.ki = ki
        self.M = M                   # Motor object
        self.umaxIn  =umaxIn
        self.eprev = eprev
        self.eintegral = eintegral

    # Function for calculating the Feedback signal. It takes the current value, user target value and the time delta.
    def evalu(self,value, target, deltaT):
        
        # Propotional
        e = target-value 

        # Derivative
        dedt = (e-self.eprev)/(deltaT)

        # Integral
        self.eintegral = self.eintegral + e*deltaT
        
        # Control signal
        u = self.kp*e + self.kd*dedt + self.ki*self.eintegral
        
        # Direction and power of  the control signal
        if u > 0:
            if u > self.umaxIn:
                u = self.umaxIn
            else:
                u = u
        else:
            if u < -self.umaxIn:
                u = -self.umaxIn
            else:
                u = u 
        self.eprev = e
        return u
    
    # Function for closed loop position control
    def setTarget(self,target):
        
        # Time delta is predefined as we have set a constat time for the loop.(Initial dealy is 
        # very high,interfers with response time)(Integral part becomes very high due to huge deltaT value at the beginning)
        # Use tick_us() to calculate the delay manually(remove slee_ms() if you use realtime delay)
        deltaT = .01

        # Disable the interrupt to read the position of the encoder(encoder tick)               
        state = disable_irq()
        step = self.M.pos

        # Enable the intrrupt after reading the position value
        enable_irq(state)

        # Control signal call
        x = int(self.evalu(step, target, deltaT))
        
        # Set the speed 
        self.M.speed(x/10)
        print(step, target) # For debugging
        
        # Constant delay 
        sleep_ms(10)
        
    # Function for closed loop speed control
    def setRPM(self, target):
        state = disable_irq()
        posi = self.M.pos
        enable_irq(state)

        # Delta is high because small delta causes drastic speed stepping.
        deltaT = .05

        # Target RPM
        vt = target 

        # Current encoder tick rate
        velocity = (posi - self.posPrev)/deltaT
        
#         if self.posPrev != posi:
#             print(posi,self.posPrev,posi - self.posPrev)
#         
        
        self.posPrev = posi
        # Converted to RPM
        # 350 ticks per revolution of output shaft of the motor 
        # For different gearing differnt values
        # Run the function without setting the motor speed and calculate the ticks per revolution by manually rotaing the motor  
        v = velocity/690*60

        # Call for control signal
        x = int(self.evalu(v, vt, deltaT))

        # Set the motor speed
        self.M.speed(x)
        print("speed: " + str(x))
        print(v, vt)   # For debugging

        # Constant delay
        sleep_ms(50)

    