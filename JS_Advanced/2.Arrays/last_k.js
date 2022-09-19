function solve(n, k) {
    let array = [1, ]

    for (let i = 1; i < n; i++) {
        let num = 0;
        for (let new_i = i; i - k < i; i) {
            num += array[new_i]

        }
        array.push(num);

    }
    console.log(array)
}

solve(6, 3)