from LapCalculator import *
import sys


def main():
    try:
        import_file = sys.argv[1]
        export_file = sys.argv[2]
        n = int(sys.argv[3])
        export_complete = getTopDrivers(import_file, export_file, n)

        if export_complete:
            print ("The results of the top " + sys.argv[3] + " average driver times has been exported to " + export_file)
    except:
        print("Incorrect parameters. Please follow this usage:")
        print("python app/Main.py {input_file_name} {export_file_name} {number_of_top_results}")


if __name__ == "__main__":
    main()
