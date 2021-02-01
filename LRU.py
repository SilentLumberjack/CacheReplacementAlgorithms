import csv, random

#implementation of LRU (Least Recently Used) Page Replacement algorithm in Python
#for more information watch these https://www.youtube.com/watch?v=4wVp97-uqr0

def createRandomlyProcessesList(size:int, numberOfProcesses:int):
    """ Returns a list with set length (size argument) of randomly generated processes from 1 to numberOfProcesses argument """
    return [random.randint(1, numberOfProcesses) for i in range(size)]

def createManuallyProcessesList():
    """ Returns a list of processes entered manually by user""" 
    numberOfProcesses = int(input("How many processes you want to create: "))
    processesList = []
    for _ in range(numberOfProcesses):
        process = int(input("Enter a process: "))
        processesList.append(process)
    return processesList

def getNumberOfPageFaultsOfProcesses(processesList:list, emptyPageSlots:int):
    """ Returns number of Page faults for given list of processes and number of empty page slots """ 

    #logic of this function is to append incoming processes to pageSlots list by the time it will be full (emptyPageSlots variable)
    #when pageSlots will be full, in case if we will get element that is not in this list, we will delete first element from it, becouse this element will be automatically least recently used
    #and then append the new one 
    #in case if element will be it list we will delete it, and immediately append it to list, thus we will update out list pf cache

    pageFault = 0
    pageSlots = []
    for process in processesList:
        if process not in pageSlots:
            if len(pageSlots) < emptyPageSlots:
                pageSlots.append(process)
            else:
                del pageSlots[0]
                pageSlots.append(process)

            pageFault += 1
        else:
            pageSlots.remove(process)
            pageSlots.append(process)

    return pageFault

def writeProcessesDataToCSVfile(processesList:list, fileName:str="processesDataLRU.csv"):
    """ Writes down all the information about single process to a CSV file given as argument, if file wasn't given as argument - 
    creates new CSV file named 'processesDataLRU.scv' and writes down information to it """

    CSVcolumns = ["Process ID"]
    processesList = [{CSVcolumns[0]: i} for i in processesList]

    try:
        with open(fileName, "w+") as f:
            writer = csv.DictWriter(f, fieldnames=CSVcolumns)
            writer.writeheader()
            for process in processesList:
                writer.writerow(process)
                
        print("Successfully written to", fileName)
    except IOError:
        print("Input/Output error!") 

def readProcessesDataFromCSVfile(fileName:str):
    """ Reads information about processes from CSV file. Returns a list where every single process is a dictionary. """ 

    try:
        with open(fileName, "r") as f:
            processesList = [{key: value for key, value in row.items()}
            for row in csv.DictReader(f, skipinitialspace=True)]
            print("Successfully read from", fileName)

            return [process["Process ID"] for process in processesList]
    except IOError:
        print("Input/Output error!")


if __name__ == "__main__":

    for cacheMemory in (3, 5, 7):
        allTestedProcessesList = []
        everagePageFault = 0
        for i in range(100):
            processesList = createRandomlyProcessesList(100, 20)
            allTestedProcessesList += processesList
            everagePageFault += getNumberOfPageFaultsOfProcesses(processesList, cacheMemory)

        print("For", cacheMemory, "free cache pages average number of page faults is", everagePageFault / 100)
        writeProcessesDataToCSVfile(allTestedProcessesList, "processesDataLRU_" + str(cacheMemory) + ".csv")

    


    

