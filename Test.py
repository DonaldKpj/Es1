import Insertion_Sort
import Quick_Sort

import numpy as np
from timeit import default_timer as timer
import matplotlib.pyplot as plt


# creazione di array random
def array(A, n):
    for i in range(0, n):
        A.insert(i, int(np.random.rand() * 100))

# creazione di array ordinato
def ordered_array(A, n, k):
    for i in range(0, n):
        A.insert(i, i * k)

# creazione di array inversamente ordinato
def inverted_order_array(A, n, k):
    k = k * k
    ordered_array(A, n, k)
    A.reverse()

# tempo di insertion sort
def time_insertion_sort(A):
    start = timer()
    Insertion_Sort.insertion_sort(A)
    end = timer()
    return end - start

# tempo di insertion sort
def time_quick_sort(B, p, r):
    start = timer()
    Quick_Sort.quick_sort(B, p, r)
    end = timer()
    return end - start


def main():

    # file tempi di ordinamento is vs qs con sequenza input random
    f = open('random.txt', 'w')
    f.write('Random\n')
    f.write('Dim ')
    f.write(' insertion_sort ')
    f.write(' quick_sort\n')

    # file tempi di ordinamento is vs qs con sequenza input ordinata
    g = open('ordered.txt', 'w')
    g.write('Ordinato\n')
    g.write('Dim ')
    g.write(' insertion_sort ')
    g.write(' quick_sort\n')

    # file tempi di ordinamento is vs qs con sequenza input ordinata al contrario
    h = open('reverse.txt', 'w')
    h.write('Reverse\n')
    h.write('Dim ')
    h.write(' insertion_sort ')
    h.write(' quick_sort\n')

    A = []

    # matrici di appoggio utilizzate per salvare (insert) i valori da plottare nei grafici
    time_is_random = []
    time_qs_random = []
    time_is_ordered = []
    time_qs_ordered = []
    time_is_reverse = []
    time_qs_reverse = []

    # dimensioni matrici, con passo 100
    for j in range(1, 4000, 100):
        timeISrandom = 0
        timeQSrandom = 0
        timeISordered = 0
        timeQSordered = 0
        timeISreverse = 0
        timeQSreverse = 0

        # 25 prove per ogni passo della dim degli array in input
        # i ha anche la funzione di seed per gli input degli array da ordianare
        # essendo gli input crescenti o decrescenti il seed non è necessaria sia complesso
        for i in range(1, 25):

            # test su array random
            array(A, j)
            B = A[:]
            timeISrandom += time_insertion_sort(A)
            timeQSrandom += time_quick_sort(B, 0, j-1)
            A.clear()
            B.clear()

            # test su array ordinato
            ordered_array(A, j, i)
            B = A[:]
            timeISordered += time_insertion_sort(A)
            timeQSordered += time_quick_sort(B, 0, j-1)
            A.clear()
            B.clear()

            # test su array inversamente ordinato
            inverted_order_array(A, j, i)
            B = A[:]
            timeISreverse += time_insertion_sort(A)
            timeQSreverse += time_quick_sort(B, 0, j-1)
            A.clear()
            B.clear()

        # scrittura su file con ordinamento input random
        time_is_random.insert(j, timeISrandom / i)
        time_qs_random.insert(j, timeQSrandom / i)
        f.write(str(j))
        f.write(' & ')
        f.write(str(round(timeISrandom / i, 4)))
        f.write(' & ')
        f.write(str(round(timeQSrandom / i, 4)))
        f.write(' \\\ \hline\n')

        # scrittura su file con ordinamento input ordinato
        time_is_ordered.insert(j, timeISordered / i)
        time_qs_ordered.insert(j, timeQSordered / i)
        g.write(str(j))
        g.write(' & ')
        g.write(str(round(timeISordered / i, 4)))
        g.write(' & ')
        g.write(str(round(timeQSordered / i, 4)))
        g.write(' \\\ \hline\n')

        # scrittura su file con ordinamento input inversamente ordinato
        time_is_reverse.insert(j, timeISreverse / i)
        time_qs_reverse.insert(j, timeQSreverse / i)
        h.write(str(j))
        h.write(' & ')
        h.write(str(round(timeISreverse / i, 4)))
        h.write(' & ')
        h.write(str(round(timeQSreverse / i, 4)))
        h.write(' \\\ \hline\n')


    # plot dei vari grafici
    x = np.arange(1, 4000, 100)
    plt.plot(x, time_is_random, label="Insertion-sort")
    plt.plot(x, time_qs_random, label="Quick-sort")
    plt.legend()
    plt.savefig('random.png', bbox_inches='tight')
    plt.close()

    plt.plot(x, time_is_ordered, label="Insertion-sort")
    plt.plot(x, time_qs_ordered, label="Quick-sort")
    plt.legend()
    plt.savefig('ordered.png', bbox_inches='tight')
    plt.close()

    plt.plot(x, time_is_reverse, label="Insertion-sort")
    plt.plot(x, time_qs_reverse, label="Quick-sort")
    plt.legend()
    plt.savefig('reverse.png', bbox_inches='tight')
    plt.close()
    f.close()
    g.close()
    h.close()

if __name__ == '__main__':
    main()

