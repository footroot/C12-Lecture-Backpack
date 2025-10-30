// const values = "abcdef".split("")
// let rightPointer = values.length - 1;
// let temp = undefined;

// for (let i = 0; i < values.length - 1; i++) {             
//     if (i == 1)
//         temp = values[i]    

//     if (i == values.length - 2){
//         values[1] = values[i]
//         values[i] = temp
//     }

// }

// console.log(values)


// const values = "abc".split("")
// const reverse = values[2].concat(
//     values[1],
//     values[0]
// )

// console.log(reverse)

const { fiction: {author} } = { author:'bill', fiction:{ author:'jane'}}
console.log(author)