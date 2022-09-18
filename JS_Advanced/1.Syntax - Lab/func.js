function sayMyName(name, age = 15) {
    console.log(`My name is ${name} and I am ${age} years old`)

}

sayMyName('mario', age = 40)


// Return Result from function
function sum(x, y) {
    return x + y;

    // Can be used only in the function block and not outside of it 

    function anotherFunc() {
        console.log('Something !')

    }
}

result = sum(2, 2)
console.log(result)

// 'let' function 
sumFunc(5, 3) // Ne moje predi function da se dostupi kato e zapazena kato promenliva ako beshe bez 'let' shteshe da stane
let sumFunc = function (y, z) {
    return y + z;
}

// Fast Function
let sumFunction = (a, b) => {
    return a + b;
}
// Another way
let func = x => x + 100;
func(10) 
//Result = 110
