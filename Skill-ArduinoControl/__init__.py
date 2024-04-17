from mycroft import MycroftSkill, intent_handler
import serial

class ArduinoControlSkill(MycroftSkill):
    def __init__(self):
        super(ArduinoControlSkill, self).__init__(name="ArduinoControlSkill")
        self.arduino = serial.Serial('/dev/ttyUSB0', 115200)  # Adjust as necessary

    @intent_handler('walk.intent')
    def handle_walk(self, message):
        self.arduino.write(b'W')
        self.speak("Walking")

    @intent_handler('stop.intent')
    def handle_stop(self, message):
        self.arduino.write(b'S')
        self.speak("all motor function stopped")

    def shutdown(self):
        if self.arduino.is_open:
            self.arduino.close()

def create_skill():
    return ArduinoControlSkill()
