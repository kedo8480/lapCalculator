from LapCalculator import *
import sys

def main():
    importFile = sys.argv[1]
    exportFile = sys.argv[2]
    n = int(sys.argv[3])
    exportComplete = getTopDrivers(importFile, exportFile, n)

    if (exportComplete):
        print ("The results of the top " + sys.argv[3] + " average driver times has been exported to " + exportFile)


if __name__ == "__main__":
    main()