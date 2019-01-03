# import resources
import os
import csv

# Path to collect data from resources folder
budget_data = os.path.join("Resources", "budget_data.csv")

# Read in the CSV file
with open(budget_data, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # remove headers
    csv_header = next(csvreader)
    
    # Calculate total number of months
    date = []   
    revenue = []
    rev_change = []
    
    for row in csvreader:
        
        revenue.append(float(row[1]))
        date.append(row[0])
    
    print("Financial Analysis")
    print("----------------------")
    print("Total Months:", len(date))
    print("Total Revenue: $", sum(revenue))
    
    for i in range(1,len(revenue)):
        
        rev_change.append(revenue[i] - revenue[i - 1])
        avg_rev_change = sum(rev_change)/len(rev_change)
        
        max_rev_change = max(rev_change)
        max_rev_change_date = str(date[rev_change.index(max(rev_change))])
        
        min_rev_change = min(rev_change)
        min_rev_change_date = str(date[rev_change.index(min(rev_change))])
        
    del rev_change[0]
    del date[0]
        
    print("Average Revenue Change: $", round(avg_rev_change))
    print("Greatest Increase in Revenue:", max_rev_change_date,"($", max_rev_change,")")
    print("Greatest Decrease in Revenue:", min_rev_change_date,"($", min_rev_change,")")
    
    output = open("Output/results.txt", "w")

    output.write("Financial Analysis \n")
    output.write("------------------ \n")
    output.write("Total Months: " + str(len(date)) + "\n")
    output.write("Total Revenue: $" + str(sum(revenue)) + "\n")
    output.write("------------------ \n")
    output.write("Average Revenue Change: $" + str(round(avg_rev_change)) + "\n")
    output.write("Greatest Increase in Revenue:" + str(max_rev_change_date) + "($" + str(max_rev_change) + ") \n")
    output.write("Greatest Decrease in Revenue:" + str(min_rev_change_date) + "($" + str(min_rev_change) + ") \n")  
        
        
        
    
    
    
    

        



