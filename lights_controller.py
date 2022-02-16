import board
import neopixel

class LightsController():
    def __init__(self, num_lights):
        self.pixels = neopixel.NeoPixel(board.D18,
                                        num_lights,
                                        brightness=1,
                                        pixel_order=neopixel.RGB)
        self.pixels.fill((0,0,0))
    
    def setLightColor(self, index, color):
        self.pixels[index] = color
