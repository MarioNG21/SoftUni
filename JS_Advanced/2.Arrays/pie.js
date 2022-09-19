function solve(pies, first_pie, second_pie) {
    let start_index = pies.indexOf(first_pie);
    let last_index = pies.indexOf(second_pie);
    let result = pies.slice(start_index, last_index + 1);
    return result;
}