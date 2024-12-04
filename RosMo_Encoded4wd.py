from RosMo_N20enc import EncodedMotor, PID

class RosMoEnc4WD:
    def __init__(self, RLfwdpin=40,RLbwdpin=8,RLrev=False,RLencA=38,RLencB=45,
                 RRfwdpin=1,RRbwdpin=2,RRrev=True,RRencA=44,RRencB=43,
                 FLfwdpin=21,FLbwdpin=39,FLrev=False,FLencA=14,FLencB=9,
                 FRfwdpin=15,FRbwdpin=16,FRrev=True,FRencA=7,FRencB=4):
        
        motorRL = EncodedMotor(RLfwdpin,RLbwdpin,RLrev,RLencA,RLencB)
        motorRR = EncodedMotor(RRfwdpin,RRbwdpin,RRrev,RRencA,RRencB)
        motorFL = EncodedMotor(FLfwdpin,FLbwdpin,FLrev,FLencA,FLencB)
        motorFR = EncodedMotor(FRfwdpin,FRbwdpin,FRrev,FRencA,FRencB)
        self.pidRL = PID(motorRL, 3, 0, 10, 800)
        self.pidRR = PID(motorRR, 3, 0, 10, 800)
        self.pidFL = PID(motorFL, 3, 0, 10, 800)
        self.pidFR = PID(motorFR, 3, 0, 10, 800)

    def setThrottles(self,rl,rr,fl,fr):    
        self.pidRL.setRPM(rl)
        self.pidRR.setRPM(rr)
        self.pidFL.setRPM(fl)
        self.pidFR.setRPM(fr)
    
    def stop(self):
        self.pidRL.speed(0)  
        self.pidRR.speed(0)  
        self.pidFL.speed(0)  
        self.pidFR.speed(0)    

    def forward(self,rpm):
        self.setThrottles(rpm, rpm, rpm, rpm)

    def backward(self,rpm):
        self.setThrottles(-rpm, -rpm, -rpm, -rpm)

    def turn_left(self,rpm):
        self.setThrottles(-rpm, rpm, -rpm, rpm)

    def turn_right(self,rpm):
        self.setThrottles(rpm, -rpm, rpm, -rpm)

    def curve_left(self,rpm, biasPcent=20):
        self.setThrottles(rpm * (100 - biasPcent) / 100, rpm * (100 + biasPcent) / 100, rpm * (100 - biasPcent) / 100, rpm * (100 + biasPcent) / 100)

    def curve_right(self,rpm, biasPcent=20):
        self.setThrottles(rpm * (100 + biasPcent) / 100, rpm * (100 - biasPcent) / 100, rpm * (100 + biasPcent) / 100, rpm * (100 - biasPcent) / 100)


class RosMoEncMecanum(RosMoEnc4WD):
    def __init__(self, RLfwdpin=40,RLbwdpin=8,RLrev=False,RLencA=38,RLencB=45,
                 RRfwdpin=1,RRbwdpin=2,RRrev=True,RRencA=44,RRencB=43,
                 FLfwdpin=21,FLbwdpin=39,FLrev=False,FLencA=14,FLencB=9,
                 FRfwdpin=15,FRbwdpin=16,FRrev=True,FRencA=7,FRencB=4):
        super().__init__(RLfwdpin,RLbwdpin,RLrev,RLencA,RLencB,RRfwdpin,RRbwdpin,RRrev,RRencA,RRencB,
                 FLfwdpin,FLbwdpin,FLrev,FLencA,FLencB,FRfwdpin,FRbwdpin,FRrev,FRencA,FRencB)
        
    def crab_left(self,rpm):
        self.setThrottles(rpm, -rpm, -rpm, rpm)

    def crab_right(self,rpm):
        self.setThrottles(-rpm, rpm, rpm, -rpm)

    def diag_left(self,rpm):
        self.setThrottles(rpm, 0, 0, rpm)

    def diag_right(self,rpm):
        self.setThrottles(0, rpm, rpm, 0)
