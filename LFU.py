import csv, random

#implementation of LRU (Least Frequently Used) Page Replacement algorithm in Python
#for more information watch these https://www.youtube.com/watch?v=uL0xP57negc

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

    #logic of this function is to store processes as a dictionaries with two keys: process ID and counter of requests
    #we will store all the processes in pageSlots list, that will represents our cache memory, and will have length = emptyPageSlots
    #while our list of processes in cache memory will not we full, we will aappend incoming processes to it
    #when pageSlots will be full, in case if we will get element that is not in this list, we will delete first element from it, 
    #because this element will be automatically least frequently used one (we will sort list by request counter of processes before deleting) and then append the new one 
    #in case if element will be it list we will increment it's request counter

    pageFault = 0
    pageSlots = []
    for process in processesList:
        if not any(dct["Process ID"] == process for dct in pageSlots):
            if len(pageSlots) < emptyPageSlots:
                pageSlots.append({"Process ID": process,
                                  "Request Counter": 0})
            else: 
                pageSlots = sorted(pageSlots, key = lambda i: i["Request Counter"])
                del pageSlots[0]
                pageSlots.append({"Process ID": process,
                                  "Request Counter": 0})

            pageFault += 1
        else:
            for cacheProcess in range(len(pageSlots)):
                if pageSlots[cacheProcess]["Process ID"] == process:
                    pageSlots[cacheProcess]["Request Counter"] += 1


    return pageFault

def writeProcessesDataToCSVfile(processesList:list, fileName:str="processesDataLFU.csv"):
    """ Writes down all the information about single process to a CSV file given as argument, if file wasn't given as argument - 
    creates new CSV file named 'processesDataLFU.scv' and writes down information to it """

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
        writeProcessesDataToCSVfile(allTestedProcessesList, "processesDataLFU_" + str(cacheMemory) + ".csv")
        

    

    

    