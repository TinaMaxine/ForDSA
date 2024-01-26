// Given a string, print all possible substrings of the given string.
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Give a string to print all of its substrings: ', (str) => {
    const n = str.length;

    console.log('The Given String is:', str);

    for (let num = 0; num < (1 << n); num++) {
        let sub = '';
        for (let i = 0; i < n; i++) {
            if (num & (1 << i)) {
                sub += str[i];
            }
        }
        console.log(sub);
    }

    rl.close();
});





// const str = prompt("Give a string to print all of its substrings:");
// const n = str.length;

// console.log("The Given String is:", str);

// for (let num = 0; num < (1 << n); num++) {
//     let sub = "";
//     for (let i = 0; i < n; i++) {
//         if (num & (1 << i)) {
//             sub += str[i];
//         }
//     }
//     console.log(sub);
// }
