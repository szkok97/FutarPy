from typing import List #beimportáljuk a Listákat 
#launch json externalterminal
class Fuvar(object):
    
    def __init__(self, adatok: List[str]) -> None: # A self a this, az adazok pedig egy sor a txt-ből. Ez a constructor
        adat: list() = adatok.split(' ')
        self.nap: int = int(adat[0])
        self.fuvar: int = int(adat[1])
        self.hossz: int = int(adat[2])
        self.ar = self.arak(int(adat[2]))
        #if int(adat[2]) >= 1 and int(adat[2]) <=2:
        #    self.ar = int(500)
        #elif int(adat[2]) >= 3 and int(adat[2]) <= 5:
        #    self.ar = int(700)
        #elif int(adat[2]) >= 6 and int(adat[2]) <= 10:
        #    self.ar = int (900)
        #elif int(adat[2]) >= 11 and int(adat[2]) <= 20:
        #    self.ar = int(1400)
        #elif int(adat[2]) >= 21 and int(adat[2]) <= 30:
        #    self.ar = int(2000)
    @staticmethod
    def arak(ho:int):
        ft = 0
        if ho >= 1 and ho <= 2:
            ft = int(500)
        elif ho >= 3 and ho <= 5:
            ft = int(700)
        elif ho >= 6 and ho <= 10:
            ft = int (900)
        elif ho >= 11 and ho <= 20:
            ft = int(1400)
        elif ho >= 21 and ho <= 30:
            ft = int(2000)
        return ft