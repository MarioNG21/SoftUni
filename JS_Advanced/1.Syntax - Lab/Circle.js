function circleArea(number){
    if (typeof(number) !== 'number'){
        console.log(`We can not calculate the circle area, because we receive a ${typeof number}.`)
    }
    else{
        let result = Math.PI * Math.pow(number, 2);
        console.log(result.toFixed(2));
    }
}