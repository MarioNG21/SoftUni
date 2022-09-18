let a = 15;
let b = 5;

console.log(a % b);

// Celochistleno
console.log(Math.floor(a / b));

function ProcessText(first, second, third){
    let lengthFirst = first.length;
    let LengthSecond = second.length;
    let LengthThird = third.length;

    let sum = lengthFirst + LengthSecond + LengthThird;

    let averageLength = Math.floor(sum / 3);
    console.log(sum)
    console.log(averageLength)
}

// Ternar operator

let sum = result > 100 ? 200 : 300;
  