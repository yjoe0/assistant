from components import load_components

class Core(object):
    def __init__(self):
        self.debug = False
        self.SAMPLING_RATE = False

    def setDebug(self, debug):
        self.debug = debug

    def wakeUp(self):
        raise NotImplementedError()

    def listen(self, times):
        raise NotImplementedError()

    def startAccord(self, times):
        raise NotImplementedError()

    def setAudio(self,NUM_SAMPLES,SAMPLING_RATE,LEVEL,COUNT_NUM,SAVE_LENGTH):
        raise NotImplementedError()
    def txt2audio(self, txt):
        raise NotImplementedError()

    def audio2txt(self, data):
        raise NotImplementedError()

    def play(self, path):
        raise NotImplementedError()

    def getResTuLing(self, txt):
        raise NotImplementedError()
load_components(Core)
