# LapCalculator

LapCalculator is a simple ETL that extracts data from a csv, calculates average lap times, and exports the top 3 times in ascending order to a csv. It is written in Python and uses the Python unittest library for unit tests and Coverage.py for coverage.

## Dependencies

Ensure Coverage.py is installed.

```
pip install coverage
```

## Running the code

Inside of the main project directory run the following command.

```
python lapCalculator/Main.py {input_file_name} {export_file_name}
```

As an example:
```
python lapCalculator/Main.py driverTimes.csv results.csv
```
Will extract data using the driverTimes.csv file, calculate the average driving times, and export the top 3 times to the results.csv file.

### Input File
The file driverTimes.csv is provided as a potential data set. You can also use your own data set, just ensure it's in the main project directory.
### Export File
Upon completing, the results will be exported to the file specified in the arguments. If that file already exists, it will be overwritten.

## Running the tests

Inside of the main project directory run the following command to run tests.

```
coverage run -m unittest test.LapCalculatorTest
```

Then, run the following command to see the coverage report.

```
coverage report -m
```