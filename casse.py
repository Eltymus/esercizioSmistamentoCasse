from random import *

class Casse :

    Cassa1_totali = 0
    Cassa2_totali = 0
    Cassa3_totali = 0
    max_clienti_per_cassa = 5

    def __init__(self):
            self.cassa1 = 0
            self.cassa2 = 0
            self.cassa3 = 0

    # mettere una classe per aggiungere alle casse e tiene il conto mettendo le persone sempre nella cassa con meno persone (nomeclasse sort)

    def sortCasse(self, coda_generale):
            i = 0
            while i < len(coda_generale):
                cliente = coda_generale[i]
                if self.cassa1 < Casse.max_clienti_per_cassa and (self.cassa1 <= self.cassa2 and self.cassa1 <= self.cassa3):
                    print(cliente, "va alla cassa 1")
                    Casse.Cassa1_totali += 1
                    self.cassa1 += 1
                    coda_generale.pop(i)
                elif self.cassa2 < Casse.max_clienti_per_cassa and self.cassa2 <= self.cassa3:
                    print(cliente, "va alla cassa 2")
                    Casse.Cassa2_totali += 1
                    self.cassa2 += 1
                    coda_generale.pop(i)
                elif self.cassa3 < Casse.max_clienti_per_cassa:
                    print(cliente, "va alla cassa 3")
                    Casse.Cassa3_totali += 1
                    self.cassa3 += 1
                    coda_generale.pop(i)
                else:
                    self.cassa1 -= randint(1,3)
                    self.cassa2 -= randint(1,3)
                    self.cassa3 -= randint(1,3)  
        
    # mettere una classe che conta i clienti totali del giorno e li mette su un foglòio di testo esterno . assieme a un conteggio totale dei clineti di ogni cassa (nomeclass countot)

    def contTot(self,arr):
        return int(len(arr))

    def contCasseTot():
        return "Cassa 1 : " + str(Casse.Cassa1_totali) + "\nCassa 2 : " + str(Casse.Cassa2_totali) +"\nCassa 3 : "+ str(Casse.Cassa3_totali)








