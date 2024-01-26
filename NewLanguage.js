const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question("Enter three space-separated integers (L, M, N): ", (input) => {
  // Process the input
  let [L, M, N] = input.split(' ').map(Number);

  // Initialize the minimum number of operations to infinity
  let ops = 0;

  while (L <= N && M <= N) {
    if (L < M) {
      L += M;
    } else {
      M += L;
    }
    ops += 1;
  }

  // Print the minimum number of operations
  console.log(ops);

  // Close the readline interface
  rl.close();
});
