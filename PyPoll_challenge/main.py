import os  # import modules
import csv
csvpath = os.path.join('..','Resources', 'election_data.csv')  #set path election_data1 file is reduced test file
with open(csvpath) as csvfile:    # open file reader
    csvreader = csv.reader(csvfile, delimiter = ',')
    print(csvreader)
    csv_header = next(csvreader) # since file has header 
    print(f"CSV Header:{csv_header}")
    total_votes = 0 # initialize counter to count numb of rows to get total votes except header
    candidate_list = [] # initialise empty list
    for row in csvreader:  # lopp through all rows as line by line
        total_votes = total_votes + 1   
        candidate_list.append(row[2])   # populating list by appenging row at time
    #print(candidate_list) 
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
def get_count_duplicates(candidate_list):  # counting duplicate creating get_counter function
    dict_of_elems=dict()    # initialize empty dict/tuple to count duplicates key, value pair
    for candidate in candidate_list:    
        if candidate in dict_of_elems:
            dict_of_elems[candidate] += 1 
        else:
            dict_of_elems[candidate] = 1
    dict_of_elems = { key: value for key,value in dict_of_elems.items() if value >=1} # dict_comprehention
    return dict_of_elems
dict_of_elems = get_count_duplicates(candidate_list)
percent=0
total=len(candidate_list) # to use for percentage calc
for key, value in dict_of_elems.items():
    percent = value/total*100
    print(f"{key}: {(round(percent,3))}%  ({value})") 
    winner = max(dict_of_elems, key=dict_of_elems.get)
print("-------------------------")
print(f"Winner:   {winner}")
print("-------------------------")

#output file
output_file = os.path.join('Election_result.txt')

with open(output_file,"w") as datafile:
    datafile.write("Election Results ")
    datafile.write("\n")
    datafile.write("-----------------------------")
    datafile.write("\n")
    datafile.write(f"Total Votes: {total_votes}")
    datafile.write("\n")
    datafile.write("------------------------------")
    datafile.write("\n")
    for key, value in dict_of_elems.items():
        datafile.write("\n")
        datafile.write(f"{key}: {(round(percent,3))}%  ({value})") 
    datafile.write("\n")
    datafile.write("----------------------------")
    datafile.write("\n")
    datafile.write(f"Winner:   {winner}")
    datafile.write("\n")
    datafile.write("----------------------------")
    datafile.write("\n")

