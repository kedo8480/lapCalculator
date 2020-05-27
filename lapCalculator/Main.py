from LapCalculator import *
import sys


def main():
    if len(sys.argv) == 3:
        import_file = sys.argv[1]
        export_file = sys.argv[2]
        export_complete = getTopDrivers(import_file, export_file, 3)

        if export_complete:
            print ("The results of the top 3 average driver times has been exported to " + export_file)
    else:
        print("Incorrect parameters. Please follow this usage:")
        print("python app/Main.py {input_file_name} {export_file_name} {number_of_top_results}")

if __name__ == "__main__":
    main()
