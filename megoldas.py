from fuvar import Fuvar
from typing import Dict, List
from operator import itemgetter, attrgetter #sorted-hez kell lista rendezés objektumokból

#@property csak egy tulajdonság nem kap beviteli paramétert csak a self-et
class Megoldas(object):
    _fuvarok: List[Fuvar] = list()
    _fuvaroknew: List[Fuvar] = list()

    # Ez a contructor. itt csak beolvassa a sorok majd átajda az Epizod osztálynak az példányosít és beleteszi az _epizodok lisátba
    def __init__(self, forras_file: str) -> None:
        with open(forras_file, "r", encoding='UTF8') as sr:
            sorok: List[str] = sr.read().splitlines()
            for i in range(0, len(sorok), 1):
                self._fuvarok.append(Fuvar(sorok[i]))
        self._fuvarok = sorted(self._fuvarok, key = attrgetter("nap", "fuvar")) #sorted(listaneve, mialapján = lekéri_az_egyed_tulajdonságait("nap","fuvar"))
    @property
    def elso(self) -> int():
        return self._fuvarok[0]
    @property
    def utolso(self) -> int():
        return self._fuvarok[len(self._fuvarok)-1]
    @property
    def szabadnap(self) -> list():
        darab = 0
        pihenok = list()
        for i in range(1,8):
            for w in self._fuvarok:
                if int(i) == int(w.nap):
                    darab = darab + 1
            if darab == 0:
                pihenok.append(i)
            darab = 0
        return pihenok
    @property
    def legtobbfuvar(self) -> list():
        napiFuvar = 0
        fuvarSzamok = list()
        for i in range(1,8):
            for w in self._fuvarok:
                if i == w.nap:
                    napiFuvar += 1
            fuvarSzamok.append(napiFuvar)
            napiFuvar = 0
        #legnagyobb = max(fuvarSzamok)
        #return  "A(z) "+str(fuvarSzamok.index(legnagyobb))+" napon volt a legtöbb fuvar. "+str(legnagyobb)+"db fuvar"
        return fuvarSzamok
    @property
    def km(self) -> list():
        km = 0
        napikm  = list()
        for i in range(1,8):
            for w in self._fuvarok:
                if i == w.nap:
                    km += w.hossz
            napikm.append(km)
            km = 0
        return napikm
    
    def ar(self, a) -> int():
        ft = 0
        if a >= 1 and a <=2:
            ft = int(500)
        elif a >= 3 and a <= 5:
            ft = int(700)
        elif a >= 6 and a <= 10:
            ft = int (900)
        elif a >= 11 and a <= 20:
            ft = int(1400)
        elif a >= 21 and a <= 30:
            ft = int(2000)
        return ft
    @property
    def osszertek(self)->int():
        return sum(map(lambda x: int(x.ar), self._fuvarok))
    def write(self)-> None:
        with open('tavok.txt', 'w', encoding='UTF8') as sw:
            for sor in self._fuvarok:
                sw.write(f'{sor.nap} {sor.fuvar} {sor.hossz} {sor.ar}\n')