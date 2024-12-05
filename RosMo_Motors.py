from machine import Pin, PWM

class DCMotor:
    def __init__(self, forwardPin = 2, backwardPin = 1):
        self.fwd_pwm = PWM(Pin(forwardPin), freq=50)    
        self.bwd_pwm = PWM(Pin(backwardPin), freq=50)
        
        
    def speed(self, spd): # -1 to +1
        if spd == 0:
            self.stop()
            return
        if spd < -1:
            spd = -1
        if spd > 1:
            spd = 1
        duty_cycle = int(0xFFFF * abs(spd))
        if spd > 0:
            self.fwd_pwm.duty_u16(duty_cycle) 
            self.bwd_pwm.duty_u16(0)
        else:
            self.fwd_pwm.duty_u16(0) 
            self.bwd_pwm.duty_u16(duty_cycle)
        
    def stop(self):
        self.fwd_pwm.duty_u16(0) 
        self.bwd_pwm.duty_u16(0) 
