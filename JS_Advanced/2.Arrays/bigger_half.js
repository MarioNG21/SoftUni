function solve(input) {
    input.sort((a, b) => a - b);
    return input.slice(input.length / 2);

}