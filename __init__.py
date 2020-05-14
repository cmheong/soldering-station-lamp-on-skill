from mycroft import MycroftSkill, intent_file_handler


class SolderingStationLampOn(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('on.lamp.station.soldering.intent')
    def handle_on_lamp_station_soldering(self, message):
        self.speak_dialog('on.lamp.station.soldering')


def create_skill():
    return SolderingStationLampOn()

