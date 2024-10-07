from random import *
from casse import Casse
from datetime import datetime

obj = datetime.now()
data_corrente = obj.strftime("%d-%m-%Y")

cassa = Casse() # questa me la ha consigliata ChatGPT perchè non funzionava mettendo solo Casse.sortCasse?

n_random = (randint(10,80))

coda_generale=[] 

for n in range(n_random) :
    coda_generale.append("cliente" + " " + str(n) )

totGiornaliero = "oggi abbiamo avuto : " + str(cassa.contTot(coda_generale)) + " clienti in totale."

# Classe funzionante e alla fine report in altro file di testo
# ha più senso nel main , simula fine giornata

# Verifica che la lista non sia vuota

cassa.sortCasse(coda_generale)

report = open(data_corrente + "_" + "report_giornaliero.txt","w")
report.write(str(datetime.now()) + "\n" +  totGiornaliero + "\n" + str(Casse.contCasseTot()))
report.close()
