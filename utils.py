import csv
import os

def intInput(prompt = 'Enter an integer number: '):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Please input integer only...") 

# refer here for details on this - https://stackoverflow.com/questions/40193388/how-to-check-if-a-csv-has-a-header-using-python/40193509
# checks if csv file has a header row
# passes filename instead of the actual file as f.read moves the cursor (demarcation of where the reader is currently at) to later in the file
# asking for the next chunks of data will only return data after the cursor
def csvHasHeader(filename):
    try:
        with open(filename, 'r') as f:
            sniffer = csv.Sniffer()
            return sniffer.has_header(f.read(2048))
    except:
        print('file empty or error')

# This function might be dangerous if not used properly. Perhaps delete.
# def csvHasHeaderByFile(f):
#     try:
#         sniffer = csv.Sniffer()
#         hh = sniffer.has_header(f.read(2048))
#         # returns cursor back to start of file
#         f.seek(0)
#         return hh
#     except:
#         print('file empty or error')

# https://stackoverflow.com/questions/2507808/how-to-check-whether-a-file-is-empty-or-not
def fileIsEmpty(filename):
    return os.stat(filename).st_size == 0

def userSelect(options):
    print("Are you a new or existing user?")
    optLen = len(options)

    for n, txt in enumerate(options):
        print(f"{n}) {txt}")
    
    print() 

    i = intInput()

    try:
        while i < 0 and i >= optLen:
            i = intInput()
        return i
    except:
        pass
    return None

# rows = []
# # checks if username already
# for row in csvReader:
#     rows.append(row)
# return rows
# fn below is equivalent to the above 
def readCsv(csvReader):
    return [row for row in csvReader]

def readCsvByCol(csvReader, col):
    return [row[col] for row in csvReader]

# cols specifies the cols to retrive from CSV (0 indexed)
# e.g. cols = [0,1,3], get cols 0, 1 and 3 from csv and ignore the rest
def readCsvByCols(csvReader, cols):
    firstRow = next(csvReader)
    
    # initialise list of empty lists
    data = [[] for _ in firstRow]

    # fill each empty list with the corresponding element in first row
    # e.g. [[gab], [1], [1]]
    for i, v in enumerate(firstRow):
        if i in cols:
            data[i].append(v)

    # same as above but with the rest of the elements if any
    # e.g. [[gab, jack], [1, 2], [1, 2]]
    for row in csvReader:
        for j, v in enumerate(row):
            if j in cols:
                data[j].append(v)

    # remove all empty lists
    return [item for item in data if item]



def readFile(filename, cols = []):
    try:
        with open(filename, 'r') as f:
            csvReader = csv.reader(f)

            if csvHasHeader(filename):
                headers = next(csvReader, None)  # skip the headers
                print(f'csv file has headers: {headers}')
                
            if len(cols) > 1:
                return readCsvByCols(csvReader, cols)
            elif len(cols) == 1:
                return readCsvByCol(csvReader, cols[0])

            return readCsv(csvReader)

    except IOError:
        print("Initialising CSV database...")


def getByID(filename, ID):
    try:
        with open(filename, 'r') as f:
            csvReader = csv.reader(f)

            if csvHasHeader(filename):
                headers = next(csvReader, None)  # skip the headers
                print(f'csv file has headers: {headers}')

            for row in csvReader:
                if ID in row:
                    return row

            return None
            
    except IOError:
        print("Initialising CSV database...")


# reads as a dict
def readFileIntoDict(filename, cols = []):
    try:
        with open(filename, 'r') as f:
            csvReader = csv.DictReader(f, delimiter=',')

            if not csvHasHeader(filename):
                print('cannot turn into a dict without headers')
                return None
                
            if len(cols) > 1:
                firstRow = next(csvReader)

                # initialise list of empty lists
                data = [[] for _ in firstRow]

                # fill each empty list with the corresponding element in first row
                # e.g. [[gab], [1], [1]]
                for i, v in enumerate(firstRow.values()):
                    if i in cols:
                        data[i].append(v)

                # same as above but with the rest of the elements if any
                # e.g. [[gab, jack], [1, 2], [1, 2]]
                for row in csvReader:
                    for j, v in enumerate(row.values()):
                        if j in cols:
                            data[j].append(v)

                return [item for item in data if item]
                # return readCsvByCols(csvReader, cols)
            elif len(cols) == 1:
                return readCsvByCol(csvReader, cols[0])

            # returns list of dicts
            return readCsv(csvReader)
                

    except IOError:
        print("Initialising CSV database...")
        print('No such file or other error')
    

def appendFileDict(filename, input):
    try:
        with open(filename, 'a', newline='') as f:
            csvWriter = csv.DictWriter(f, input[0].keys())

            if fileIsEmpty(filename):
                csvWriter.writeheader()

            csvWriter.writerows(input)

    except IOError:
        print("File not accessible")

def appendFile(filename, input):
    try:
        with open(filename, 'a', newline='') as f:
            csvWriter = csv.writer(f, delimiter=',')
            csvWriter.writerow(input)

    except IOError:
        print("File not accessible")

def writeFile(filename, input):
    try:
        # why you need newline arg - https://stackoverflow.com/questions/3348460/csv-file-written-with-python-has-blank-lines-between-each-row
        with open(filename, 'w', newline='') as f:
            csvWriter = csv.writer(f, delimiter=',')
            csvWriter.writerows(input)

    except IOError:
        print("File not accessible")

