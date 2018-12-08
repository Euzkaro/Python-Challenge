import os
import csv


csvpath = os.path.join('/Users/gallasteguicrino/Desktop/NUCHI201811DATA2/Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    list_candidates = []
    list_votes_per_candidate = []
    count_votes = 0
    first_row = True

    for row in csvreader:
        count_votes = count_votes + 1

        if(first_row == True):
            list_candidates.append(row[2])
            list_votes_per_candidate.append(1)
            first_row = False
    
        else:
            candidate_found = False
            for candidate in list_candidates:
                if(row[2] == candidate):
                    candidate_found = True
                    list_votes_per_candidate[list_candidates.index(candidate)] = list_votes_per_candidate[list_candidates.index(candidate)] + 1
            if(candidate_found == False):
                list_candidates.append(row[2])
                list_votes_per_candidate.append(1)


count_winner = 0
for candidate in list_candidates:
    if(list_votes_per_candidate[list_candidates.index(candidate)] > count_winner):
        count_winner = list_votes_per_candidate[list_candidates.index(candidate)]
        winner = candidate

#  Terminal Summary 
print("____________________________________")
print("     Election  Results Summary      ")
print("____________________________________")
print("Total Votes: " + str(count_votes))
print("____________________________________")
for candidate in list_candidates:
    print(candidate + ": " + "{:.3%}".format(list_votes_per_candidate[list_candidates.index(candidate)]/count_votes) + " (" + str(list_votes_per_candidate[list_candidates.index(candidate)]) + ")")
print("____________________________________")
print("Winner: " + winner)
print("____________________________________")

# Text Summary 
f = open("PyPoll_output.txt","w")
f.write("     Election  Results Summary      " + "\n")
f.write("____________________________________" + "\n")
f.write("Total Votes: " + str(count_votes) + "\n")
f.write("____________________________________" + "\n")
for candidate in list_candidates:
    f.write(candidate + ": " + "{:.3%}".format(list_votes_per_candidate[list_candidates.index(candidate)]/count_votes) + " (" + str(list_votes_per_candidate[list_candidates.index(candidate)]) + ")" + "\n")
f.write("____________________________________" + "\n")
f.write("Winner: " + winner + "\n")
f.write("____________________________________")
f.close()