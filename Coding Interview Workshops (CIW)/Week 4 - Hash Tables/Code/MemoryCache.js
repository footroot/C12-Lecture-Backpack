// Implementation of a hash table in JS which will be used to implement a memory cache
// Collision handling will be done using linear probing

// Each element in our array needs to hold a key-value pair
// We create a node class to hold the pair 
// We also implement a mechanism to keep track of whether the node was accessed recently
class Node {
    constructor (key, value, accessed){
        this.key = key;
        this.value = value;
        this.accessed = accessed;
    }
}

class HashTable {
    // Initialise the Hash Table of arbitary size
    // Use numpy empty array for the associative array
    constructor (capacity = 20) {
        this.capacity = capacity;
        this.size = 0;
        this.buckets = new Array(this.capacity).fill(null);
    }
    
    // We will be using the built in hash function
    // Since this returns integers of arbitray sizes, we 
    // use the mod function to ensure they fit in the array
    hash(key) {
        return String(key).length % this.capacity;
    }
    
    // Return the key of the value that was accessed last 
    // i.e. the item with the lowest access value
    find_last_accessed() {
        let min_accessed = Infinity;
        let min_key = null;

        this.buckets.forEach((node) => {
            if (node.accessed < min_accessed) {
                min_accessed = node.accessed;
                min_key = node.key;
            }
        })
            
        return min_key
    }
    
    // Set a key-value pair in the hash table
    set(key, value, accessed) {
        // Check whether the table is full, if so remove last accessed item
        if (this.size == this.capacity) {
            let remove_key = this.find_last_accessed();
            this.remove(remove_key);
        }

        // Hash the key of the pair
        let index = this.hash(key);

        // Check if there is a collision
        if (this.buckets[index] == null) {
            this.buckets[index] = new Node(key, value, accessed);
            this.size += 1;
        } else {
            // If there is a collision find the next empty spot to insert
            index += 1;
            if (index == this.capacity)
                index = 0;

            while (this.buckets[index] != null){
                index += 1;
                if (index == this.capacity)
                    index = 0;
            }

            this.buckets[index] = new Node(key, value, accessed);
            this.size += 1;
        }
    }

    // Get the value associated with a given key
    get(key, accessed) {
        // Find the index where the pair is stored
        let index = this.hash(key);

        // Check the bucket and retrieve the correct value
        // Return null if the key is not in the hash table
        let node = this.buckets[index];
        if (node == null) {
            return null;
        } else {
            let counter = 1;
            while (node.key != key) {
                // Check whether the whole hash table has been iterated through
                if (counter == this.capacity) 
                    return null;
                counter += 1
                
                // Check whether the end of the table has been reached
                index += 1
                if (index == this.capacity) 
                    index = 0;

                node = this.buckets[index];
                if (node == null) {
                    return null
                }
            }
        }
            node.accessed = accessed
            return node.value
    }

    // Remove a pair from the hashtable given the key
    // Return the removed value and null if key isnt found  
    remove(key) {
        // Find the index where the pair is stored
        let index = this.hash(key);

        // Check the bucket and remove the correct node
        // Return null if the key is not in the hash table
        let node = this.buckets[index];
        if (node == null) {
            return null
        } else {
            let counter = 1;
            while (node.key != key) {
                // Check whether the whole hash table has been iterated through
                if (counter == this.capacity)
                    return null;
                counter += 1
                
                // Check whether the end of the table has been reached
                index += 1
                if (index == this.capacity)
                    index = 0;

                node = this.buckets[index];
                if (node == null)
                    return null;
            }
            // Remove the item from the list by setting the element to null
            this.size -= 1;
            this.buckets[index] = null;
            return node.value;
        }
    }
}

class MemoryCache {
    constructor (max_cache_size = 100) {
        this.max_cache_size = max_cache_size;
        this.cache = new HashTable(this.max_cache_size);
        this.accessCount = 0;
    }

    // Method to read file from disk if not found in cache
    // This is a dummy method for demonstration purposes
    read_from_disk(filename) {
        console.log(`Reading ${filename} data from disk`);
        return `Example data from ${filename}`;
    }
    
    // Method to get data from file given a file name
    // If the file is not in the cache, fetch from disk
    get_file(filename) {
        let data = this.cache.get(filename, this.accessCount);
        
        if (data != null) {
            console.log(`Data fetched from cache: ${data}`);
            this.accessCount += 1;
            return data;
        }

        // Fetch data from disk and add to cache
        data = this.read_from_disk(filename);
        this.cache.set(filename, data, this.accessCount);
        this.accessCount += 1;
        return data;
    }

}

// Example cache to test code
cache = new MemoryCache(2);

// First access - data is read from disk and stored in the cache
console.log(cache.get_file("file1.txt"));

// Second access - data is retrieved from the cache
console.log(cache.get_file("file1.txt"));

// Access a different file - data is read from disk and stored in the cache
console.log(cache.get_file("file2.txt"));

// Access a different file, causing eviction from the cache
console.log(cache.get_file("file3.txt"));

// Access the evicted file - data is read from disk and stored in the cache
console.log(cache.get_file("file1.txt"));

