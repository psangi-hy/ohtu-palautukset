def kopioi(a, b, lkm):
    for i in range(0, lkm):
        b[i] = a[i]

def tarkista_epanegatiivinen_kokonaisluku(luku, minka):
    if not isinstance(luku, int):
        raise TypeError(f"{minka} on oltava kokonaisluku.")
    if luku < 0:
        raise ValueError(f"{minka} on oltava epänegatiivinen.")

class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        tarkista_epanegatiivinen_kokonaisluku(kapasiteetti, "Kapasiteetin")
        tarkista_epanegatiivinen_kokonaisluku(kasvatuskoko, "Kasvatuskoon")

        self.kasvatuskoko = kasvatuskoko
        self.kapasiteetti = kapasiteetti
        self.alkiot = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        for i in range(0, self.alkioiden_lkm):
            if n == self.alkiot[i]:
                return True

        return False

    def _kasvata_listaa(self):
        uusi = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
        self.kopioi_lista(self.alkiot, uusi)
        self.alkiot = uusi

    def lisaa(self, n):
        if self.kuuluu(n):
            return False

        if self.alkioiden_lkm >= len(self.alkiot):
            self._kasvata_listaa()

        self.alkiot[self.alkioiden_lkm] = n
        self.alkioiden_lkm = self.alkioiden_lkm + 1

        return True

    def _poista_kohdasta(self, indeksi):
        if indeksi < 0 or indeksi >= self.alkioiden_lkm:
            raise ValueException("Indeksi on virheellinen.")

        self.alkioiden_lkm -= 1

        for i in range(indeksi, self.alkioiden_lkm):
            self.alkiot[i] = self.alkiot[i + 1]

    def poista(self, n):
        for i in range(0, self.alkioiden_lkm):
            if n == self.alkiot[i]:
                self._poista_kohdasta(i)
                return True

        return False

    def kopioi_lista(self, a, b):
        kopioi(a, b, len(a))

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)
        kopioi(self.alkiot, taulu, self.alkioiden_lkm)
        return taulu

    @staticmethod
    def yhdiste(a, b):
        tulos = IntJoukko(kapasiteetti=max(a.mahtavuus(), b.mahtavuus()))
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            tulos.lisaa(a_taulu[i])
            tulos.lisaa(b_taulu[i])

        return tulos

    @staticmethod
    def leikkaus(a, b):
        tulos = IntJoukko()
        a_taulu = a.to_int_list()

        for i in range(0, len(a_taulu)):
            if b.kuuluu(a_taulu[i]):
                tulos.lisaa(a_taulu[i])

        return tulos

    @staticmethod
    def erotus(a, b):
        tulos = IntJoukko()
        a_taulu = a.to_int_list()

        for i in range(0, len(a_taulu)):
            if not b.kuuluu(a_taulu[i]):
                tulos.lisaa(a_taulu[i])

        return tulos

    def __str__(self):
        tulos = "{"
        if self.alkioiden_lkm:
            tulos += str(self.alkiot[0])
        for i in range(1, self.alkioiden_lkm):
            tulos += ", " + str(self.alkiot[i])
        tulos += "}"
        return tulos
