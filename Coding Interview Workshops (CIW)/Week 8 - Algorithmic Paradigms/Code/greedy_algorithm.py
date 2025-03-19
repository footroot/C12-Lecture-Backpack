'''
Greedy Algorithm: Activity Selection Problem
Given n activities with start and end times, select the maximum number of non-overlapping activities.

'''

def activity_selection(activities):
    # Sort list of activities by end time
    activities.sort(key=lambda x: x[1])  

    selected = [activities[0]]  # List of activities that will be done
    last_end = activities[0][1]  # End time of current activity

    # Loop through each activity and check whether the start time is 
    # after the current activities end time
    for i in range(1, len(activities)):  
        if activities[i][0] >= last_end:  
            selected.append(activities[i])  
            last_end = activities[i][1]  

    return selected

activities = [[1, 3], [2, 5], [4, 6], [6, 8], [5, 7]]
print(activity_selection(activities=activities))