from RosMo_4wd import RosMo4WD
import utime

class RosMo:
    def __init__(self):
        self.car = RosMo4WD()
        self.ultrasonic = False
        self.trg_pin = -1
        self.ech_pin = -1

    def addUltrasonic(self,echoPin,trigPin):
        if trigPin >= 0 and echoPin >= 0:
            self.trg_pin = Pin(trigPin, Pin.OUT)
            self.ech_pin = Pin(echoPin, Pin.IN)
            self.ultrasonic = True

    def getDistanceCm(self):
        if not self.ultrasonic:
            return -1
        distance = -1
        self.trg_pin.off()
        utime.sleep_us(2)
        self.trg_pin.on()
        utime.sleep_us(20)
        self.trg_pin.off()
        pulse_duration = time_pulse_us(self.ech_pin, 1)
        if ((pulse_duration < 60000) and (pulse_duration > 1)):
            distance = pulse_duration / 58.00
        return(distance)    
