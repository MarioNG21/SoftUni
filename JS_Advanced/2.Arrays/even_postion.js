function solve(arr) {
    let result_arr = []
    for (let i = 0; i < arr.length; i++) {
        if (i % 2 === 0) {
            result_arr.push(arr[i])
        }
    }
    console.log(result_arr.join(' '))
}

solve(['20', '30', '40', '50', '60'])