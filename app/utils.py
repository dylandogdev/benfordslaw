import csv
from flask import render_template

def get_list_from_flat_file(path, column):
    # get data from flat file
    myfile = open(path, 'r')
    file = csv.DictReader(myfile, delimiter='\t', quoting=csv.QUOTE_NONE)

    # capture values in list
    values = []
    for col in file:
        values.append(col[column])
    return values

def get_expected_values_numeric(total):
    expected_percent = [.301, .176, .125, .097, .079, .067, .058, .051, .046]
    expected_values = []
    for x in expected_percent:
        expected_values.append(total * x)
    return expected_values

def get_occurences_by_first_digit(values):
    observed = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0, len(values)):
        num = int(str(values[i][0]))
        if num == 1:
            observed[0] += 1
        elif num == 2:
            observed[1] += 1
        elif num == 3:
            observed[2] += 1
        elif num == 4:
            observed[3] += 1
        elif num == 5:
            observed[4] += 1
        elif num == 6:
            observed[5] += 1
        elif num == 7:
            observed[6] += 1
        elif num == 8:
            observed[7] += 1
        elif num == 9:
            observed[8] += 1
        elif num == 0:
             continue
    return observed


def get_observed_percentages(observed, total):
    observedPercent = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for x in range(0, len(observed)):
        observedPercent[x] = observed[x] / total * 100
    return observedPercent

def get_does_data_pass_benfords_law(benfordValues, observedPercent):
    for x in range(9):
        if abs(benfordValues[x] - observedPercent[x]) > 4:
            return False
        else:
            return True
