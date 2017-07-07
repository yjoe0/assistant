from components import load_components

class Core(object):
    def __init__(self):
        pass


    def wakeUp(self):
        raise NotImplementedError()

    def listen(self, times):
        raise NotImplementedError()

    def startAccord(self, times):
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
