// Problem Statement:

// Write a JavaScript program to find the area of a circle using:
// radius
// pi

// Solve the following:
// Declare radius using let and assign a value to it. Then, redeclare the same variable again using 'let' and observe the output. Also, try to re-assign a value to the radius.
// Repeat the above step with the 'var' keyword.
// Declare pi using 'const' keyword and initialize it with the appropriate value and then try re-assigning a value to it.



// Solving 1st problem
let radius = 5;
const pi = 3.14;

// let radius = 5;  ---> it will throw the error because we can't re-declare the "let" keyword
console.log("Area of Circle is with radius 5 = " + radius * pi);
radius = 10;       // re-assigning the "let" keyword
console.log("Area of Circle is with radius 10 = " + radius * pi);

// Solving 2nd problem
var varRadius = 4;
var varPi = 3.14

var varRadius = 8;  // re-decleartion of "var" keyword is possible
console.log("Area of Circle is with radius 8 = " + varRadius * varPi);
varRadius = 18;     // re-assigning of "var" is also possible
console.log("Area of Circle is with radius 18 = " + varRadius * varPi);


// Solving 3rd problem
// const pi = 3.14;  ----> re-decleration of "const" keyword is not possible
// pi = 3.1432; ----> re-assigning of "const" keyword is not possible