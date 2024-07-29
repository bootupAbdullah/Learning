"user strict";

console.log("hello");
console.log("I am writing in Javascript");


//testing some scripts:
//<script> alert("Hey, this is Javascript! Look you\'re already doing it! :"))</script>
// TIL: you don't need the 'script' tag ie <script> on a seperate file that has been attached to the html through 'src='
alert("I'm JavaScript!")


// variables
// let admin, user;

// user = "John"

// admin = user;

// alert(admin);

// let earth, currentUser;

// const BIRTHDAY = '16.12.1987';
// const age = someCode(BIRTHDAY);

// types

let user = "Ilya";

alert( `hello ${1}` );

alert( `hello ${"user"}`);

alert( `hello ${user}` );

// 2.6 Iteraction: alert, prompt, confirm 

let answer = prompt('Are you a bunny rabbit?', 'Yes');
alert (`It looks like your answered \'${answer}\' to the question: \'Are you a bunny rabbit?\'`);

let age = prompt('How old are you?', 100);

alert(`You are ${age} years old!`); // You are 100 years old!