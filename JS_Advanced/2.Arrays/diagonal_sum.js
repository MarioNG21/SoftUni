function solve(matrix) {
    let main_diagonal = 0;
    let column_length = matrix[0].length - 1;
    let second_diagonal = 0;
    for (let i = 0; i < matrix.length; i++) {
        main_diagonal += matrix[i][i];
        second_diagonal += matrix[i][column_length]
        column_length--;

    }
    console.log(main_diagonal + ' ' + second_diagonal);
}