#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const l = process.argv.sort();
  console.log(l.reverse()[1]);
}
