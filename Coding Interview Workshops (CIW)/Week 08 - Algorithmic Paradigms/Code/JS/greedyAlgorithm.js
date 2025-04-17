/**
 * Greedy Algorithm: Activity Selection Problem
 * Given n activities with start and end times, 
 * select the maximum number of non-overlapping activities.
 * 
 */

function activitySelection(activities) {
    activities.sort((a, b) => a[1] - b[1]); // Sort by finish time

    let selected = [activities[0]]; // List of activities that will be done
    let lastEnd = activities[0][1]; // End time of current activity

    // Loop through each activity and check whether the start time is 
    // after the current activities end time
    for (let i = 1; i < activities.length; i++) {
        if (activities[i][0] >= lastEnd) {
            selected.push(activities[i]);
            lastEnd = activities[i][1];
        }
    }
    return selected;
}

// Example Usage
let activities = [[1, 3], [2, 5], [4, 6], [6, 8], [5, 7]];
console.log(activitySelection(activities));