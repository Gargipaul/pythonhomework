# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 12:00:04 2019

@author: gargi
"""

import os
import csv

votes_per_candidate = {}
total_votes_cast = 0 

election_data = os.path.join("election_data.csv")


def store_values(input_csv):

	with open(input_csv, "r", newline="") as current_csv:

		csv_reader = csv.reader(current_csv, delimiter=",")
		next(csv_reader)

		for row in csv_reader:
			candidate = row[2]
			if candidate in votes_per_candidate:
				votes_per_candidate[candidate].append([1])
			else:
				votes_per_candidate[candidate] = [1]


store_values(election_data)

vpc_combined = {key : len(values) for key, values in votes_per_candidate.items()}
total_votes = sum(vpc_combined.values())

print("Election Results")
print("--------------------")
print("Total votes: " + str(total_votes))
print("--------------------")
for key, value in vpc_combined.items():
	print(key + ": " + str("{:.2%}".format(value / total_votes)) + " (" + str(value) + " votes)")
	winner = max(vpc_combined, key=lambda key: vpc_combined[key])
print("--------------------")
print("Winner: " + str(winner))


with open('election_data.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(total_votes) + "\n")
    text.write("---------------------------------------\n")
    for key, value in vpc_combined.items():
        text.write(key + ": " + str("{:.2%}".format(value / total_votes)) + " (" + str(value) + " votes)" + ")\n")
    winner = max(vpc_combined, key=lambda key: "vpc_combined[key] + \n")
    text.write("---------------------------------------\n")
    text.write("Winner:" + str(winner) + "\n........")