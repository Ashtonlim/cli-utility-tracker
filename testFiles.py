import csv
import os

fname = 'username_db.csv'


def intInput(prompt = 'Enter an integer number: '):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please input integer only...") 

def csvHasHeader(filename):
    try:
        with open(filename, 'r') as f:
            return csv.Sniffer().has_header(f.read(2048))
    except:
        print('file empty or error')


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


def readCsv(csvReader):
    return [row for row in csvReader]

def readCsvByCol(csvReader, col):
    return [row[col] for row in csvReader]

def readCsvByCols(csvReader, cols):
    firstRow = next(csvReader)
    
    data = [[v] for i, v in enumerate(firstRow) if i in cols]
    for row in csvReader:
        for j, v in enumerate(row):
            if j in cols:
                data[j].append(v)

    return data

def getHeadersByName(filename):
    try:
        with open(filename, 'r') as f:
            if csvHasHeader(filename):
                return next(csv.reader(f), None)
            return None

    except IOError:
        print("Initialising CSV database...")

def getHeadersByNum(filename):
    try:
        with open(filename, 'r') as f:
            headers = next(csv.reader(f), None)
            return list(range(0, len(headers)))

    except IOError:
        print("Initialising CSV database...")

def readFileU(filename, cols = []):
    try:
        with open(filename, 'r') as f:
            csvReader = csv.reader(f)

            if csvHasHeader(filename):
                headers = next(csvReader, None)  # skip the headers
                print(f'Headers: {headers}')
                
            if len(cols) > 1:
                return readCsvByCols(csvReader, cols)
            elif len(cols) == 1:
                return readCsvByCol(csvReader, cols[0])

            return readCsv(csvReader)

    except IOError:
        print("Initialising CSV database...")


def readFileIntoDict(filename, cols = []):
    try:
        with open(filename, 'r') as f:
            csvReader = csv.DictReader(f, delimiter=',')

            if csvHasHeader(filename):
                headers = next(csvReader, None)  # skip the headers
                print(f'Headers: {headers}')
                
                if len(cols) > 1:
                    return readCsvByCols(csvReader, cols)
                elif len(cols) == 1:
                    return readCsvByCol(csvReader, cols[0])

                # returns list of dicts
                return readCsv(csvReader)
                
            else:
                print('cannot turn into a dict without headers')

    except IOError:

        print("Initialising CSV database...")

print(readFileU(fname))
print(readFileU(fname, [0]))
print(readFileU(fname, getHeadersByNum(fname)))

print()

print(readFileIntoDict(fname))
print(readFileIntoDict(fname, ['username']))
# print(readFileIntoDict(fname, getHeadersByNum(fname)))
