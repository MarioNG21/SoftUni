function printLargest(first, second, third){
    
    // let array = [first, second, third];
    // let max = Math.max(array);
    
    let result = 0;
    if (first >= second && first >= third){
        result = first;
    }
    else if (second >= first && second >= third){
        result = second;
    }
    else {
        result = third;
    }

    console.log(`The largest number is ${result}`)
}