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
python app/Main.py
```

## Running the tests

Inside of the `/test` directory run the following command to run tests.

```
coverage run -m unittest LapCalculatorTest
```

Run the following command to see the coverage report.

```
coverage report -m
```