class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._edelliset = []

    def miinus(self, operandi):
        self.aseta_arvo(self._arvo - operandi)

    def plus(self, operandi):
        self.aseta_arvo(self._arvo + operandi)

    def nollaa(self):
        self.aseta_arvo(0)

    def kumoa(self):
        if not self._edelliset:
            return
        self._arvo = self._edelliset.pop()

    def aseta_arvo(self, arvo):
        self._edelliset.append(self._arvo)
        self._arvo = arvo

    def arvo(self):
        return self._arvo
