function solve(array) {
    let first_element = Number(array.shift());
    let last_element = Number(array.pop());

    let sum_of_both = first_element + last_element;
    console.log(sum_of_both)
}