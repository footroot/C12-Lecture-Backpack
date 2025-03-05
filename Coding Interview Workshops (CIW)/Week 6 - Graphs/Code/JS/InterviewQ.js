/**

1. Assumptions
 - it doesnt have to be very (time or space) efficient -> must be clean, not overly complex
 - All input will be correct
 - There can be no town judge or 1 town judge
 - a person can't trust themselves

2. Plan
 - Think of this with a graph -> nodes are the people, trust is the edges
 - Directed graph
 - Town Judge in a graph: edges going to the node, from every other node, no edges away from the node
 - Maybe count how many edges going towards a node?
 - Count all edges going TO a node for ALL nodes
 -> we want the element with count = n - 1
 -> we can have another count for edges going FROM the node
 -> instead, subtract 1 from count when edge goes from node
 O(n) space
 To improve time: we could use a tree instead to store our values -> may not work because of the storage and access situation


3. Code!

*/
/**
 * @param {number} n
 * @param {number[][]} trust
 * @return {number}
 */
var findJudge = function(n, trust) {
    // Variables
    let counts = new Array(n).fill(0);;
    let a, b;

    // Loop
    for (var t = 0; t < trust.length; t++) {
        a = trust[t][0];
        b = trust[t][1];

        counts[b-1]++;
        counts[a-1]--;
    }   
    
    let count;

    // Find our judge
    for (let i = 0; i < n; i++) {
        count = counts[i];
        console.log(count)
        if (count == (n-1))
            return i + 1;
    }
        
    return -1;
};
        