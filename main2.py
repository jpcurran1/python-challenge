import os
import pandas as pd 
print("Election Results")
print("-------------------------")
election_df = pd.read_csv('./PyPoll/Resources/election_data.csv')
total_votes = len(election_df["Voter ID"])
print("Total Votes: " + str(total_votes))
print("-------------------------")
results_df = election_df[['Candidate','County']].groupby('Candidate').count().sort_values(by=['County'], ascending=False)
results_df = results_df.rename(columns={'County':'Total Votes'})
results_df['Percent'] = results_df['Total Votes'].apply(lambda x: round((x/total_votes)*100))
for index, row in results_df.head().iterrows():
    print("{0}: {1}.000% ({2})".format(index, row['Percent'], row['Total Votes']))
print("-------------------------")
print("Winner: " + str(results_df.first_valid_index()))
print("-------------------------")

    






