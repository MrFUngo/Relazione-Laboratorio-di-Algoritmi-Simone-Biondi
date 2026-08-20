import time
import matplotlib.pyplot as plt
import random
import gc # GARBAGE COLLECTOR DI PYTHON
from strutture_dati import *



#INIZIALIZZAZIONE DELLE STRUTTURE DATI
abr = AlberoABR()
avl = AlberoAVL()
rb = AlberoRB()
nodi_AVL = []
nodi_RB = []
nodi_ABR = []
tempi_RB = []
tempi_AVL = []
tempi_ABR = []

global_timer = time.perf_counter() #Timer per esecuzione dell'intero programma, a partire da qui

#COSTANTE DA SCEGLIERE PER NUMERO DI NODI DA INSERIRE + LIMITE IN SECONDI 
MAX_NODI = 50000
LIMITE = 30


#CASO RANDOMIZZATO
SEED = 42
random.seed(SEED)
valori = random.sample(range(1, MAX_NODI + 1), MAX_NODI)
ultimo_aggiornamento = 0

print("INIZIO CASO RANDOMIZZATO")

#RANDOMIZED-ABR
print("INIZIO DI RANDOMIZED-ABR")
inizio = time.perf_counter() # Per tenere traccia del tempo di Randomized-ABR
for i in range(1, MAX_NODI + 1): #+1 Poichè l'indicizzazione parte da 0
    abr.ABR_Tree_Insert(Nodo_ABR(valori[i-1]))
    tempo = time.perf_counter() - inizio
    nodi_ABR.append(i)
    fine = time.perf_counter()
    tempi_ABR.append((fine - inizio))  
    if tempo - ultimo_aggiornamento >= 1:
        print(
            f"\rTempo trascorso: {tempo:.0f}s",
            end="",
            flush=True
        )
        ultimo_aggiornamento = tempo
    if tempo >= LIMITE:
        print(f"\nLimite di {LIMITE}s raggiunto. Termina RANDOMIZED-ABR.")
        break
print("\nFINE RANDOMIZED-ABR. Tempo utilizzato per inserimento: ", f"{time.perf_counter() - inizio:.5f}s")
del abr
gc.collect()
#FINE RANDOMIZED-ABR

#RANDOMIZED-RB
print("INIZIO DI RANDOMIZED-RB")
inizio = time.perf_counter()
for i in range(1, MAX_NODI + 1): #+1 Poichè l'indicizzazione parte da 0
    rb.RB_Tree_Insert(Nodo_RB(valori[i-1]))
    tempo = time.perf_counter() - inizio
    nodi_RB.append(i)
    fine = time.perf_counter()
    tempi_RB.append((fine - inizio))
    if tempo - ultimo_aggiornamento >= 1:
        print(
            f"\rTempo trascorso: {tempo:.0f}s",
            end="",
            flush=True
        )
        ultimo_aggiornamento = tempo
    if tempo >= LIMITE:
        print(f"\nLimite di {LIMITE}s raggiunto. Termina RANDOMIZED-RB.")
        break
time.sleep(1)
print("\nFINE RANDOMIZED-RB. Tempo utilizzato per inserimento: ", f"{time.perf_counter() - inizio:.5f}s")
del rb
gc.collect()


#RANDOMIZED-AVL
print("INIZIO DI RANDOMIZED-AVL")
ultimo_aggiornamento = 0
inizio = time.perf_counter()
for i in range(1, MAX_NODI +1):
    avl.AVL_Tree_Insert(Nodo_AVL(valori[i-1]))
    tempo = time.perf_counter() - inizio
    nodi_AVL.append(i)
    fine = time.perf_counter()
    tempi_AVL.append((fine - inizio))
    if tempo - ultimo_aggiornamento >= 1:
        print(
            f"\rTempo trascorso: {tempo:.0f}s",
            end="",
            flush=True
        )
        ultimo_aggiornamento = tempo
    if tempo >= LIMITE:
        print(f"\nLimite di {LIMITE}s raggiunto. Termina RANDOMIZED-AVL.")
        break
print("\nFINE RANDOMIZED-AVL. Tempo utilizzato per inserimento: ", f"{time.perf_counter() - inizio:.5f}s")
del avl
gc.collect()
#FINE RANDOMIZED-AVL

print("FINE CASO RANDOMIZZATO. Tempo globale trascorso da esecuzione programma: ", f"{time.perf_counter() - global_timer:.0f}s")


#Grafico numero 1 per le differenze tra AVL,ABR e RB nel caso randomizzato
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()
ax1.plot(nodi_ABR, tempi_ABR, label="ABR")
ax1.plot(nodi_AVL, tempi_AVL, label="AVL")
ax1.plot(nodi_RB, tempi_RB, label = "RB")

ax1.set_xlabel("Numero di nodi inseriti")
ax1.set_ylabel("Tempo totale trascorso secondi")
ax1.set_title("Confronto ABR, RB e AVL nel caso Randomizzato")
ax1.grid(True)
ax1.legend()
time.sleep(2)

#SET UP per il caso peggiore di ABR.
abr = AlberoABR()
avl = AlberoAVL()
rb = AlberoRB()
nodi_AVL = []
nodi_RB = []
nodi_ABR = []
tempi_RB = []
tempi_AVL = []
tempi_ABR = []

#CASO PEGGIORE -> Inserisco Limit in modo da interrompere su ABR nel caso superi 30 sec.
ultimo_aggiornamento = 0
flag = False

#CASO PEGGIORE ABR
print("INIZIO CASO PEGGIORE: Timer di ABR impostato a " + str(LIMITE) + " secondi.")
inizio = time.perf_counter()

for i in range(1, MAX_NODI + 1):
    abr.ABR_Tree_Insert(Nodo_ABR(i))
    tempo = time.perf_counter() - inizio
    nodi_ABR.append(i)
    tempi_ABR.append(tempo)

    if tempo - ultimo_aggiornamento >= 1:
        print(
            f"\rTempo trascorso: {tempo:.0f}s",
            end="",
            flush=True
        )
        ultimo_aggiornamento = tempo

    if tempo >= LIMITE:
        print(f"\nLimite di {LIMITE}s raggiunto. Termina ABR.")
        flag = True
        break
if not flag:
    print("\nFINE ABR. Tempo utilizzato per inserimento: ", f"{time.perf_counter() - inizio:.5f}s")

del abr
gc.collect()
#FINE CASO PEGGIORE ABR

#CASO PEGGIORE ABR - USO DI RB
print("INIZIO RB")
ultimo_aggiornamento = 0
inizio = time.perf_counter()
for i in range(1, MAX_NODI +1):
    rb.RB_Tree_Insert(Nodo_RB(i))
    tempo = time.perf_counter() - inizio
    nodi_RB.append(i)
    fine = time.perf_counter()
    tempi_RB.append(fine - inizio)
    if tempo - ultimo_aggiornamento >= 1:
        print(
            f"\rTempo trascorso: {tempo:.0f}s",
            end="",
            flush=True
        )
        ultimo_aggiornamento = tempo
    if tempo >= LIMITE:
        print(f"\nLimite di {LIMITE}s raggiunto. Termina RB.")
        break
print("\nFINE RB. Tempo utilizzato per inserimento: ", f"{time.perf_counter() - inizio:.5f}s")
del rb
gc.collect()
#FINE CASO PEGGIORE ABR - USO RB


#CASO PEGGIORE ABR - USO DI AVL
print("INIZIO AVL")
ultimo_aggiornamento = 0
inizio = time.perf_counter()
for i in range(1, MAX_NODI +1):
    avl.AVL_Tree_Insert(Nodo_AVL(i))
    tempo = time.perf_counter() - inizio
    nodi_AVL.append(i)
    fine = time.perf_counter()
    tempi_AVL.append(fine - inizio)
    if tempo - ultimo_aggiornamento >= 1:
        print(
            f"\rTempo trascorso: {tempo:.0f}s",
            end="",
            flush=True
        )
        ultimo_aggiornamento = tempo
    if tempo >= LIMITE:
        print(f"\nLimite di {LIMITE}s raggiunto. Termina AVL.")
        break
print("\nFINE AVL. Tempo utilizzato per inserimento: ", f"{time.perf_counter() - inizio:.5f}s")
del avl
gc.collect()
#FINE CASO PEGGIORE ABR - USO AVL



print("FINE CASO PEGGIORE. Tempo globale trascorso da esecuzione programma: ", f"{time.perf_counter() - global_timer:.0f}s")


#CREAZIONE DEL GRAFICO 2 DEL CASO PEGGIORE DI ABR, CONFRONTO CON AVL E RB
print("Generazione dei Grafici in corso...")
ax2.plot(nodi_ABR, tempi_ABR, label="ABR")
ax2.plot(nodi_AVL, tempi_AVL, label="AVL")
ax2.plot(nodi_RB, tempi_RB, label = "RB")

ax2.set_xlabel("Numero di nodi inseriti")
ax2.set_ylabel("Tempo totale trascorso (secondi)")
ax2.set_title("Confronto ABR, RB e AVL nel caso Peggiore di ABR")
ax2.grid(True)
ax2.legend()
print("Grafici generati con successo.")
plt.show()


