import time
from numpy.random import seed
from numpy.random import randint
import matplotlib.pyplot as plt

class timecomplexity():
    def __init__(self):
        self.listo = []

    def driverCode(self):
        elementsForInsertion = list()
        timesForInsertion = list()
        elementsForMerge = list()
        timesForMerge = list()
        for i in range(1,20):
            a = randint(0,50*i,50*i*i)

            startForInsertion = time.clock()
            BigO.insertionSort(a)
            endForInsertion = time.clock()
            startForMerge = time.clock()
            BigO.mergeSort(a)
            endForMerge = time.clock()

            print(len(a), "Elements sorted by Insertion Sort in", str(endForInsertion-startForInsertion) + "secs")
            elementsForInsertion.append(len(a))
            timesForInsertion.append(endForInsertion-startForInsertion)


            print(len(a), "Elements sorted by Merge Sort in", str(endForMerge-startForMerge) +"secs")
            elementsForMerge.append(len(a))
            timesForMerge.append(endForMerge-startForMerge)

        plt.xlabel('List Length')
        plt.ylabel('Time Complexity')
        plt.plot(elementsForInsertion,timesForInsertion,label ='Insertion')
        plt.plot(elementsForMerge,timesForMerge,label = 'Merge')
        plt.grid()
        plt.legend()
        plt.show()

    def insertionSort(self,lists):
        for i in range(1, len(lists)):

            key = lists[i]


            j = i-1
            while j >= 0 and key < lists[j] :
                    lists[j + 1] = lists[j]
                    j -= 1
            lists[j + 1] = key

    def mergeSort(self,nlist):
        if len(nlist)>1:
            mid = len(nlist)//2
            lefthalf = nlist[:mid]
            righthalf = nlist[mid:]

            BigO.mergeSort(lefthalf)
            BigO.mergeSort(righthalf)
            i=j=k=0
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    nlist[k]=lefthalf[i]
                    i=i+1
                else:
                    nlist[k]=righthalf[j]
                    j=j+1
                k=k+1

            while i < len(lefthalf):
                nlist[k]=lefthalf[i]
                i=i+1
                k=k+1

            while j < len(righthalf):
                nlist[k]=righthalf[j]
                j=j+1
                k=k+1

BigO = timecomplexity()
BigO.driverCode()
