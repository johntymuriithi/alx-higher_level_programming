#!/usr/bin/node
const argv = process.argv;
let big = 0;
let sec = 0;

if (argv[2] === undefined) {
  console.log(0);
} else if (argv[3] === undefined) {
  console.log(0);
} else {
  for (const x of argv) {
    if (big < parseInt(x)) {
      big = parseInt(x);
    }
  }
  for (const x of argv) {
    if (parseInt(x) === big) {
      continue;
    }
    if (sec < parseInt(x)) {
      sec = parseInt(x);
    }
  }
  console.log(sec);
}
