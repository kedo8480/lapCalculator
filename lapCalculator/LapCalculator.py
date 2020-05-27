import csv
import os

# Create the top driver list
# Params: import filename, export filename, n for top n times
# Returns: boolean value if exported results into file
def getTopDrivers(import_file, export_file, n):
    raw_data = ingestCSVData(import_file)
    averages = calculateAvgs(raw_data)
    top = topN(averages, n)
    return exportCSVData(top, export_file)


# Ingest data from CSV file
# Params: csv filename
# Returns: Dictionary of lap times {lastName: [lapTimesArray]}
def ingestCSVData(filename):
    data = {}

    if not os.path.exists(filename):
        raise Exception("Input File does not exist.")

    if os.path.getsize(filename) == 0:
        raise Exception("Input File was empty.")

    with open(filename) as csv_read_file:
        csv_reader = csv.reader(csv_read_file, delimiter=',')
        for row in csv_reader:
            data.setdefault(row[0], []).append(float(row[1]))

    csv_read_file.close()
    return data


# Calculate average of each driver and update dictionary values
# Params: Dictionary of lap times {lastName: [lapTimesArray]}
# Returns: Dictionary of average lap times {lastname: avgTime}
def calculateAvgs(data):
    for driver in data:

        time_array = data[driver]
        time_sum = 0
        for i in range(0, len(time_array)):
            if time_array[i] < 0:
                raise Exception("This data cannot contain negative values.")
            time_sum = time_sum + time_array[i]

        data[driver] = round(time_sum / len(time_array), 2)

    return data


# Sort and return top n lap times
# Params: Dictionary of average lap times {lastname: avgTime} and n for top n times
# Returns: List of top n lap times [[lastname, time]...]
def topN(data, n):
    if len(data) < n:
        raise Exception("This data has less than " + str(n) + " drivers. Insufficient data set.")

    sorted_averages = sorted(data.items(), key=lambda x: (x[1], x[0]))

    top_lap_times = []
    for i in range(0, n):
        top_lap_times.append([sorted_averages[i][0], sorted_averages[i][1]])

    return top_lap_times


# Export top N drivers to CSV file
# Params: List of top n lap times
# Returns: True when complete
def exportCSVData(data, filename):
    with open(filename, 'w') as csv_write_file:
        writer = csv.writer(csv_write_file)
        for item in data:
            writer.writerow([item[0], item[1]])

    csv_write_file.close()
    return True
