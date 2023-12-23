'''
Question 49.  Interval scheduling
Suppose you are given a list of lectures with their start time and end times. How can you choose
the maximum number of non-overlapping lectures?
This problem is also sometimes articulated as the party planning problem:
You are asked to be the organizer for n parties and are provided with their
start and end times. (For example: P1: 7 AM – 9 AM; P2: 8 AM to 3 PM;
P3: 4 AM to 8 AM.)You can only be organizing one party at a time, so you
need to choose. For every party that you organize, you are given a fixed
reward (1000$) irrespective of the length of the party. How do you select the
parties to maximize your reward ? What is the time complexity of your
algorithm in terms of n?
'''

import random

# Say 1 PM = 13 O'clock and 1 Am = 1 O'clock
party_list = [
    [1,4],
    [2,3],
    [2,8],
    [6,7]
]

should_generate_party_list = True
party_list_length = 30

def generate_party_list(list_length):
    party_list = []
    for _ in range(0, list_length):
        former = random.randint(0, 46)
        latter = random.randint(former + 1, 48)
            
        party_list.append([former/2,latter/2])
        
    return party_list

def recursive_choose(array, choose_list):
    # find the earlist ending one, and append to choose list
    temp_low = array[0][1]
    temp_low_number = 0
    for i in range(1,len(array)):
        if(array[i][1] < temp_low):
            temp_low = array[i][1]
            temp_low_number = i
    choose_list.append([temp_low_number,array[temp_low_number]])
    print("add: ", temp_low_number, array[temp_low_number])
    # find the array afterwards, if no, then just return
    new_list = []
    threhold = array[temp_low_number][1]
    for i in range(0,len(array)):
        if(array[i][0] > threhold):
            new_list.append(array[i])
    if(len(new_list) == 0):
        print(choose_list)
        return choose_list
    else:
        recursive_choose(new_list, choose_list)
    # recursive call
    
if __name__ == "__main__":
    if(should_generate_party_list):
        party_list = generate_party_list(party_list_length)

    first_list = []
    last_list = []
    
    for i,j in party_list:
        first_list.append(i)
        last_list.append(j)
    
    print(party_list)    
    print(first_list,"\n",last_list)
    
    schedule_list = []
    schedule_list = recursive_choose(party_list, schedule_list)
    print('\n', schedule_list)
    
    