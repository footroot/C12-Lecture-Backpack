// Swapping values using a for loop.
// const numbers = [1,2,3,4,5,6,7,8,9,10]

for (let left = 0; left < numbers.length; left++) {
    const right = (numbers.length - 1) - left;    
    
    if (left >= right)
        break

    const temp = numbers[left]
    numbers[left] = numbers[right] 
    numbers[right] = temp
}

// Look for matching Pairs 
const numbers = [1,2,1,3,4,3,5,6,7,8,7]
let matches = 0;

for (let left = 0; left < numbers.length - 1; left++){    
    const right = left + 2;

    if (numbers[left] == numbers[right]){
        matches++
        console.log("There is a match:", numbers[left], numbers[right])
    }
}