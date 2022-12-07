#Import Dependencies
import csv

#Open CSV pathway
#csv_path = ('.\PyPoll\Resources\election_data.csv') Relative path does not work, tutor has advised to leave comment instead.
csv_path = (r'C:\Users\domin\OneDrive\Documents\Desktop\DV_Bootcamp\Modules\Week 3 - Python\Starter_Code\PyPoll\Resources\election_data.csv')

#Set Initial Variables
total_votes = 0
cand_opt = []
cand_votes = {}
win_cand = ""
win_count= 0

#Open csv file, use DictReader for easier naming of specific columns
with open(csv_path) as csv_file:
    csv_reader= csv.DictReader(csv_file)

    #Loop through each row
    for row in csv_reader:

        #Add to the total vote count
        total_votes = total_votes + 1

        #Checking candidates 
        candidate_name = row["Candidate"]

        if candidate_name not in cand_opt:
            cand_opt.append(candidate_name)

            cand_votes[candidate_name] = 0
       
        cand_votes[candidate_name] = cand_votes[candidate_name] + 1

#Create text file and input endpoint data
file_to_output = (r"C:\Users\domin\OneDrive\Documents\Desktop\DV_Bootcamp\Modules\Week 3 - Python\Python-Challenge\PyPoll\Analysis\election_analysis.txt")
#file_to_output = "PyPoll\Analysis\election_analysis.txt" #Relative path, does not work. Tutor has advised to leave it as comment.

with open (file_to_output, 'w') as txt_file:
    output_1 = (
    f' Election Results \n'
    f'-----------------------\n'
    f'Total Votes: {total_votes}\n'
    f'-------------------------\n'

    )
    print(output_1)

    txt_file.write(output_1)
    
    #Loop again through the collated data above and print end result in the assigned text file.
    for candidate in cand_votes:
            votes = cand_votes.get(candidate)
            vote_percentage = float(votes) / float(total_votes) * 100
    
            if (votes > win_count):
                win_count = votes
                win_cand = candidate
            
            output_2 = f'{candidate}: {vote_percentage: .3f}% ({votes})\n'
            print(output_2)

            txt_file.write(output_2)
    
    win_summary = (
         f'-------------------------\n'
         f'Winner: {win_cand}\n'
         f'--------------------------\n'
    )

    print(win_summary)
    txt_file.write(win_summary)