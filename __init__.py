from mycroft import MycroftSkill, intent_file_handler
import subprocess

class SolderingStationLampOff(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('off.lamp.station.soldering.intent')
    def handle_off_lamp_station_soldering(self, message):
        cmd = "curl -k http://ww.xx.yy.zz:8080/1/on"
        answer = ""
        try:
            answer = subprocess.check_output(cmd, shell=True)
        except:
            print(str(answer))
        print(str(answer))

        self.speak_dialog('off.lamp.station.soldering')


def create_skill():
    return SolderingStationLampOff()

