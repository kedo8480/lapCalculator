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

## Usage Notes
### Input File
- The file driverTimes.csv is provided as a potential data set. You can also use your own data set, just ensure it's in the main project directory.
- The input file cannot be empty or an Exception will be thrown.
- The input file must exist in the project directory or an exception will be thrown.
- There cannot be any negative driving times in your data set.
- If there are less than 3 drivers in the data set, an Exception will be thrown for insufficient data.

### Export File
- Upon completing, the results will be exported to the file specified in the arguments. If that file already exists, it will be overwritten.
- If there are multiple drivers with the same average lap time, the top 3 times will be chosen first by fastest time and then by alphabetical name. This means if "Anderson" and "Azalea" were tied for 3rd, Anderson would be included in the top three results and not Azalea.

## Running the tests

Inside of the main project directory run the following command to run tests.

```
coverage run -m unittest test.LapCalculatorTest
```

Then, run the following command to see the coverage report.

```
coverage report -m
```

Running the following will create an html "pretty print" test result file.
```
coverage html
```