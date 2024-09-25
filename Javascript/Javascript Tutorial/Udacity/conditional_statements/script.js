var shirtWidth = 22;
var shirtLength = 30;
var shirtSleeve = 8.63;



if ((shirtWidth === 18 || shirtWidth === 19.99) && (shirtLength === 28 || shirtLength === 28.99) && (shirtSleeve === 8.13 || shirtSleeve === 8.379)) {
    console.log('S');
} else if ((shirtWidth === 20 || shirtWidth === 21.999) && (shirtLength === 29 || shirtLength === 29.999 ) && (shirtSleeve === 8.38 || shirtSleeve === 8.629 )) {
    console.log('M')
} else if ((shirtWidth === 22 || shirtWidth === 23.999 ) && (shirtLength === 30 || shirtLength === 30.999) && (shirtSleeve === 8.63 || shirtSleeve === 8.889 )) {
    console.log('L')
// } else if ((shirtWidth === 24) && (shirtLength === 31) && (shirtSleeve === 8.88 )) {
//     console.log('XL')
// } else if ((shirtWidth === 26) && (shirtLength === 33) && (shirtSleeve === 9.63 )) {
//     console.log('2XL')
// } else if ((shirtWidth === 28) && (shirtLength === 34) && (shirtSleeve === 10.13 )) {
//     console.log('3XL')
} else {
    console.log('NA')
}


// let thisNumber = 20.1

// if ((thisNumber >= 19 || thisNumber < 20)) {
//     console.log('first condiiton met and printed')
// } else if (thisNumber >= 20) {
//     console.log('second condition met')
// }