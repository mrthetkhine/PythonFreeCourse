let my_list = [1,2,3,4,5,6,7,8,9,10]
let isEven = (x)=> x %2 ==0
let isGreaterThan5 = (x) => x > 5
let incOne = (x) => x+1
console.log("Is even 4=> ",isEven(4))
console.log("Even list ", my_list.filter(isEven)
                                 .map(incOne)
                                 .reduce((a,b)=>a+b)
                                 )   
                                 //.filter(isGreaterThan5));