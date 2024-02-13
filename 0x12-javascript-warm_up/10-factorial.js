#!/usr/bin/node
const argv = process.argv;
const arg1 = parseInt(argv[2]); // Convert the argument to a number

function factorial (n) {
  if (isNaN(n) === true) { // Check for NaN and negative numbers
    return 'Invalid input';
  }
  if (n === 0) { // Base case: factorial of 0 is 1
    return 1;
  }
  return n * factorial(n - 1); // Recursive case
}
console.log(factorial(arg1));
