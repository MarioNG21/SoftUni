function solve(numbers) {
    function Sum(x) {
        return x;
    }
    function Inverse(x) {
        return 1 / x;
    }
    function String(x) {
        return x.toString();
    }

    console.log(aggregate(numbers, Sum));
    console.log(aggregate(numbers, Inverse));
    console.log(aggregate(numbers, String));

    function aggregate(numbers, func) {
        let start_number = 0;
        let full_length = numbers.length
        let result = 0;
        for (let i = start_number; i < full_length; i++) {
            if (func.toString() === 'String' && i === 0){
                result = numbers[i] ;
            }
            result += func(numbers[i]);
        }
        return result;
    }
}