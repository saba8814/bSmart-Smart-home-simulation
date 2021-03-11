class Audio:
    def __init__(self):
        self.state = False
        self.audioVolume = 0 #indicates volume level 0.01 to 1.0 (1.0 maps to loudest, and 0.01 maps to 1% of volume )
        self.audioInput = '' #attribute that holds current audio stream be it personal assitant or youtube video
    def turnOn(self):
        self.state = True
    def turnOff(self):
        self.state = False
