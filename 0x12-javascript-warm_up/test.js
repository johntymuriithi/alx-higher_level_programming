function factorial (n) {
  // Base case: factorial of 0 is 1
  if (isNaN(n) === true) {
    return 1;
  }
  // Recursive case: factorial of n is n times factorial of (n - 1)
  return n * factorial(n - 1);
}

// Example usage:
console.log(factorial(4)); // Outputs: 120
