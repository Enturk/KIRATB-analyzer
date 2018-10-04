import os
import sys
from subprocess import call
from os import listdir
from os.path import isfile, join
import collections

# Read csv file of usernames and return a list of usernames
def read_file(file_name):
    username_list = []
    username_file = open(file_name, "r")
    for username in username_file:
        username_list.append(username)
    username_file.close()
    return username_list 

def get_user_tweets(user):
    # Time is year-month-day
    #call(["python", "Exporter.py","--querysearch",KIRATB,"--maxtweets", "3"])
    call(["python", "Exporter_interacter.py","--since", "2016-01-01", "--until", "2017-11-04","--username", user])
    # Note: Tweets for THIS PROGRAM ONLY are stored at "/home/ubuntu/workspace/Retrieved data/Interacter_data/"
    return

####################################################################################################################
# Code starts here

# Loop through files with the usernames of people who responded to a KIRATB
os.chdir("/home/ubuntu/workspace/data/responses_data")

#Command to get all the Files in our directory
onlyfiles = [f for f in listdir(os.getcwd()) if isfile(join(os.getcwd(), f))]
# Make sure we only have .csv files and no python files or anything like that
only_csv = []
for file in onlyfiles:
    # Checks if the last 4 characters in the string are ".csv"
    if (file[-4:] == ".csv"):
        only_csv.append(file)

#ISSUE POSSIBLY IN USERNAME LIST CODE BELOW
#print(len(onlyfiles))
print(only_csv[1:10])
username_list = []
for file in only_csv:
    # Get a list of all of the usernames (with duplicates)
    username_list = username_list + read_file(file)
    
    #os.remove(file) # THIS WILL DELETE THE FILE!!! ONLY UNCOMMENT WHEN WE KNOW THIS WORKS PERFECTLY!
    
# You can use sets to obtain a merged list of unique values
#username_list = list(set(username_list))

#USERNAME LIST IS EMPTY
print(len(username_list))
print("Before eliminating duplicates: " + str(len(username_list)))

# Or we can use collections.Counter to get unique values and number of them
username_counter = collections.Counter(username_list)
# username_counter.values() will print list of number of repeats
# username_counter.keys() will print list of actual list quantities (aka the usernames)
# username_counter.most_common(Number) will print list of lists with key and value of length Number
# ^^^ good for finding the top X results

print("After eliminating duplicates: " + str(len(username_counter.values())))    

# Return to directory with correct exporter file (we want Exporter_interacter.py)
os.chdir("/home/ubuntu/workspace/Python_Scripts/")
# Note: Tweets for THIS PROGRAM ONLY are stored at "/home/ubuntu/workspace/data/Interacter_data/"

# Add back in in a second
#for user in username_list:
#    get_user_tweets(user)





























