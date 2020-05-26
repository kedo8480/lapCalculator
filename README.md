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
python lapCalculator/Main.py {input_file_name} {export_file_name} {number_of_top_results}
```

As an example:
```
python lapCalculator/Main.py driverTimes.csv results.csv 3
```
Will extract data using the driverTimes.csv file, calculate the average driving times, and export the top 3 times to the results.csv file.

## Running the tests

Inside of the main project directory run the following command to run tests.

```
coverage run -m unittest test.LapCalculatorTest
```

Run the following command to see the coverage report.

```
coverage report -m
```