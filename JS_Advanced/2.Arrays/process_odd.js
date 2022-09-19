function solve(input) {
    return input
        .filter((n, i) => i % 2 === 1)
        .map(n => n * 2)
        .reverse()
        .join(' ');
}

let result = solve(3, 0, 10, 4, 7, 3)
console.log(result)