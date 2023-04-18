# esercizio del foglio 12 numero 2 corso di laser e ottica quantistica


# rapp con istogrammi emisssione fotoni per sorgenti di luce devole: n = 0.1, 1, 100
# calcolare n3 n4 nc nei moduli di uscita di beam splitter 50/50
# ripeti un esperimento 10**5 volte con distribuzione di poisson


import matplotlib.pyplot as plt
import numpy as np

ripetizione: int = 10 ** 4
n: np.array = np.array([0.1, 1, 100])
sensitivity = 1
E0 = 100


def smistatore(numero_fotoni):
    # abbiamo 2**n possibilità di uscita
    # la funzione deve scegliere una di queste
    # e restituire il numero di fotoni in uscita
    # per ogni possibile uscita
    if numero_fotoni == 0:
        return (0, 0)
    random = np.random.randint(0, numero_fotoni)
    lista = []
    for i in range(numero_fotoni):
        tupla = (i, numero_fotoni - i)
        lista.append(tupla)
    # print(lista)
    return lista[random]


# grafico con 3 istogrammi
fig, ax = plt.subplots(1, 3, figsize=(15, 5))

for j in range(len(n)):
    # preparo i detector
    D3 = np.zeros(ripetizione)
    D4 = np.zeros(ripetizione)
    # genero con distribuzione di poisson
    generatore = np.random.poisson(n[j], ripetizione)

    coincidenti = np.zeros(ripetizione)

    for i in range(ripetizione):
        tupla_scelta = smistatore(generatore[i])
        # print('tupla scelta: ', tupla_scelta[0])

        if tupla_scelta[0] == 0:  # controlla che tutti i fotoni vadano in un solo detector
            if np.random.random() < 0.5:  # al 50% va in D3 altrimenti in D4 (50/50)
                D3[i] = 1
            else:
                D4[i] = 1
        else:
            coincidenti[i] = 1

    somma = [np.sum(D3), np.sum(D4), np.sum(coincidenti)]

    # istogramma per ogni detector e coincidenti
    ax[j].set_title('n = ' + str(n[j]))
    ax[j].bar(['D3', 'D4', 'coincid'], somma, width=0.5,
              color='green',
              align='center',
              label='numero di fotoni')  # etichetta della legenda)
    ax[j].legend()
    ax[j].grid(True, linestyle='-.',
               linewidth=0.5,
               color='grey',
               alpha=0.5,
               axis='y')
    # inserisci nome asse x
    ax[j].set_xlabel('N3 * N4 / Nc = ' + str(round(somma[0] * somma[1] / somma[2], 3)))
    ax[j].set_ylabel('numero di fotoni')
    ax[j].set_ylim(0, 10000)

plt.suptitle('istogrammi per emissione fotoni per \n sorgenti di luce debole: n = 0.1, 1, 100')
plt.tight_layout()
plt.show()
