/**
    APC

    1. Assumptions
    - int in stack
    - 100 calls to push, pop, top and empty
    - use deque (doubly linked list)


    2. Plan 

    [9,0,7,8]
    - push (1) -> [1,9,0,7,8]
    - pop () -> [9,0,7,8]

    [] [9,0,7,8] -> 1 -> [1] [9,0,7,8] -> [1,9,0,7,8] []
                    -> [9,0,7,8,1] -> [0,7,8,1,9], [7,8,1,9,0], [8,1,9,0,7], [1,9,0,7,8]

    - enqueue (1) -> [9,0,7,8,1]
    - dequeue () -> [0,7,8,1]


    3. Code
    REMEMBER: enqueue is push, dequeue is shift because we're using a list to   implement the queue

 */

    var MyStack = function() {
        this.q1 = [];
        this.q2 = [];
        this.inQ1 = true;
    };
    
    /** 
     * @param {number} x
     * @return {void}
     */
    MyStack.prototype.push = function(x) {
        if (this.inQ1) {
            this.q2.push(x);
            while (this.q1.length > 0) {
                this.q2.push(this.q1.shift());
            }
            this.inQ1 = false;
        } else {
            this.q1.push(x);
            while (this.q2.length > 0) {
                this.q1.push(this.q2.shift());
            }
            this.inQ1 = true;
        }
    };
    
    /**
     * @return {number}
     */
    MyStack.prototype.pop = function() {
        if (this.inQ1) 
            return this.q1.shift();
        else 
            return this.q2.shift();
        
    };
    
    /**
     * @return {number}
     */
    MyStack.prototype.top = function() {
        if (this.inQ1) 
            return this.q1[0];
        else 
            return this.q2[0];
        
    };
    
    /**
     * @return {boolean}
     */
    MyStack.prototype.empty = function() {
        if (this.inQ1) 
            if (this.q1.length == 0)
                return true;
            else
                return false;
        else 
            if (this.q2.length == 0)
                return true;
            else
                return false;
    };
    
    /** 
     * Your MyStack object will be instantiated and called as such:
     * var obj = new MyStack()
     * obj.push(x)
     * var param_2 = obj.pop()
     * var param_3 = obj.top()
     * var param_4 = obj.empty()
     */