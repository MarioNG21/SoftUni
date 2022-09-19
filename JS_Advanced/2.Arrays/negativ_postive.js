function solve(array) {
    let new_arr = []
    for (let number of array) {
        if (number < 0) {
            new_arr.unshift(number)
        } else {
            new_arr.push(number)
        }
    }
    for (let result_num of new_arr) {
        console.log(result_num)
    }
}
solve([7, -2, 8, 9])