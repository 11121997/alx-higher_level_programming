#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  const v = parseInt(process.argv[2]);
  for (let w = 0; w < v; w++) {
    console.log('X'.repeat(v));
  }
}
