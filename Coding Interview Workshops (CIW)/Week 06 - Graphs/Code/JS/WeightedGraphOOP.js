// JavaScript Implementation of Weighted, Undirected/Directed Graph

class Node {
    // Constructor of a node with edges defined
    // Edges are a dictionary with a key of the destination node (can be empty)
    // And a value of the weight of the edge
    constructor (label, edges) {
        this.label = label;
        this.edges = edges;
    }

    // Add an edge to a node
    add_edge (dest_node, weight) {
        this.edges.set(dest_node, weight);
    }
}

class Graph {
    // Constructor for a graph with no nodes
    constructor () {
        this.nodes = [];
    }

    // Add disconnected node to the graph
    add_node(node) {
        this.nodes.push(new Node(node, new Map()));
    }
    
    // Add an edge to the graph from a source node to a destination
    add_edge(source, dest, weight) {
        let sourceIndex = "not found";
        let destIndex = "not found";

        for (let i = 0; i < this.nodes.length; i++) {
            let node = this.nodes[i];

            if (node.label == source)
                sourceIndex = i;
            if (node.label == dest)
                destIndex = i;

            if ((sourceIndex != "not found") && (destIndex != "not found"))
                break;
        }
        
        if ((sourceIndex == "not found") || (destIndex == "not found"))
            return 0;
        else
            this.nodes[sourceIndex].add_edge(this.nodes[destIndex], weight);
    }

    print_graph() {
        this.nodes.forEach(printFunction);

        function printFunction(node) {
            console.log(`(${node.label})`);

            let edgesString = [];
            let str;

            function edgeStringFunction (weight, node, map) {
                str = `-------  ${weight}  -------  (${node.label})`;
                edgesString.push(str);
            }
            node.edges.forEach(edgeStringFunction);

            console.log(edgesString.join(", "));
        }  
    }
}

let egGraph = new Graph();
nodes = ["a", "b", "c", "d"];
nodes.forEach((node) => egGraph.add_node(node));

edges = [["a", "b"], ["a", "c"], ["b", "d"], ["d", "c"]]
weights = [10, 4, 3, 7]
for (let i = 0; i < edges.length; i++) {
    egGraph.add_edge(edges[i][0], edges[i][1], weights[i]);
}

egGraph.print_graph();
            



        


                


    