# import resources
import os
import csv

# Path to collect data from resources folder
election_data = os.path.join("Resources", "election_data.csv")

# Read in the CSV file
with open(election_data, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # remove headers
    csv_header = next(csvreader)
    
    votes = 0
    candidates = {}
    candidates_percent = {}
    winner = ""
    winner_count = 0
    
    
    for row in csvreader:
        
        votes += 1
        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1
            
    for key,value in candidates.items():
        candidates_percent[key] = round((value/votes) * 100, 2)
    
    
    
    for key in candidates.keys():
        if candidates[key] > winner_count:
            winner = key
            winner_count = candidates[key]
                   
    
    
    print("Election Results")
    print("------------------")
    print("Total Votes: " + str(votes))
    print("------------------")
    for key, value in candidates.items():
        print(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ")")
    print("-------------------")
    print("Winner: " + winner)
    print("-------------------")
        

    output = open("Output/results.txt", "w")

    output.write("Election Results \n")
    output.write("------------------ \n")
    output.write("Total Votes: " + str(votes) + "\n")
    output.write("------------------ \n")
    for key, value in candidates.items():
        output.write(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ") \n")
    output.write("------------------- \n")
    output.write("Winner: " + winner + "\n")
    output.write("------------------- \n")    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        