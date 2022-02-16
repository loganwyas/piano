from lights_controller import LightsController

class SimpleController:
    DOWN = 144

    def __init__(self, num_lights, color_on, color_off):
        # state of the lights
        self.num_lights = num_lights
        self.color_on = color_on
        self.color_off = color_off
        self.next_light = 0
        self.prev_light = 0

        # initialize the lights API
        self.lights_api = LightsController()


    def process_event(self, event):
        message, deltatime = event
        state = message[0]
        print(message, deltatime)
        if state == SimpleController.DOWN:
            self.lights_api.setLightColor(self.next_light % self.num_lights, self.color_on)
            self.next_light+=1
        else:
            self.lights_api.setLightColor(self.prev_light % self.num_lights, self.color_off)
            self.prev_light+=1
