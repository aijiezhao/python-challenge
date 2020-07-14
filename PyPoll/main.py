import os
import csv
from pathlib import Path 

election = os.path.join('PyPoll', 'Resources', 'election_data.csv')

total = 0 
khan = 0
correy = 0
li = 0
OTooley = 0

with open(election,newline="", encoding="utf-8") as elections:
    csvreader = csv.reader(elections,delimiter=",") 
    header = next(csvreader)     

    for row in csvreader: 
        total +=1

        if row[2] == "Khan": 
            khan +=1
        elif row[2] == "Correy":
            correy +=1
        elif row[2] == "Li": 
            li +=1
        elif row[2] == "O'Tooley":
            OTooley +=1

candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [khan, correy ,li ,OTooley]

dict_votes = dict(zip(candidates,votes))
winner = max(dict_votes, key=dict_votes.get)

khan_percent = (khan/total) *100
correy_percent = (correy/total) * 100
li_percent = (li/total)* 100
OTooley_percent = (OTooley/total) * 100

print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total}")
print(f"----------------------------")
print(f"Khan: {khan_percent:.3f}% ({khan})")
print(f"Correy: {correy_percent:.3f}% ({correy})")
print(f"Li: {li_percent:.3f}% ({li})")
print(f"O'Tooley: {OTooley_percent:.3f}% ({OTooley})")
print(f"----------------------------")
print(f"Winner: {winner}")
print(f"----------------------------")

analysis = Path("PyPoll","analysis", "Analysis.txt")

with open(analysis,"w") as file:

    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Khan: {khan_percent:.3f}% ({khan})")
    file.write("\n")
    file.write(f"Correy: {correy_percent:.3f}% ({correy})")
    file.write("\n")
    file.write(f"Li: {li_percent:.3f}% ({li})")
    file.write("\n")
    file.write(f"O'Tooley: {OTooley_percent:.3f}% ({OTooley})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {winner}")
    file.write("\n")
    file.write(f"----------------------------")