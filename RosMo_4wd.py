from RosMo_Motors import DCMotor

class RosMo4WD:
    def __init__(self, RLfwdpin=40,RLbwdpin=8,RRfwdpin=1,RRbwdpin=2,FLfwdpin=21,FLbwdpin=39,FRfwdpin=15,FRbwdpin=16):
        self.motorRL = DCMotor(RLfwdpin,RLbwdpin)
        self.motorRR = DCMotor(RRfwdpin,RRbwdpin)
        self.motorFL = DCMotor(FLfwdpin,FLbwdpin)
        self.motorFR = DCMotor(FRfwdpin,FRbwdpin)

    def setThrottles(self,rl,rr,fl,fr):    
        self.motorRL.speed(rl)
        self.motorRR.speed(rr)
        self.motorFL.speed(fl)
        self.motorFR.speed(fr)   
    
    def stop(self):
        self.motorRL.stop()  
        self.motorRR.stop()  
        self.motorFL.stop()  
        self.motorFR.stop()    

    def forward(self,speed):
        self.setThrottles(speed, speed, speed, speed)

    def backward(self,speed):
        self.setThrottles(-speed, -speed, -speed, -speed)

    def turn_left(self,speed):
        self.setThrottles(-speed, speed, -speed, speed)

    def turn_right(self,speed):
        self.setThrottles(speed, -speed, speed, -speed)

    def curve_left(self,speed, biasPcent=20):
        self.setThrottles(speed * (100 - biasPcent) / 100, speed * (100 + biasPcent) / 100, speed * (100 - biasPcent) / 100, speed * (100 + biasPcent) / 100)

    def curve_right(self,speed, biasPcent=20):
        self.setThrottles(speed * (100 + biasPcent) / 100, speed * (100 - biasPcent) / 100, speed * (100 + biasPcent) / 100, speed * (100 - biasPcent) / 100)


class RosMoMecanum(RosMo4WD):
    def __init__(self, RLfwdpin=16,RLbwdpin=15,RRfwdpin=39,RRbwdpin=21,FLfwdpin=8,FLbwdpin=40,FRfwdpin=2,FRbwdpin=1):
        super().__init__(RLfwdpin,RLbwdpin,RRfwdpin,RRbwdpin,FLfwdpin,FLbwdpin,FRfwdpin,FRbwdpin)
        
    def crab_left(self,speed):
        self.setThrottles(speed, -speed, -speed, speed)

    def crab_right(self,speed):
        self.setThrottles(-speed, speed, speed, -speed)

    def diag_left(self,speed):
        self.setThrottles(speed, 0, 0, speed)

    def diag_right(self,speed):
        self.setThrottles(0, speed, speed, 0)
