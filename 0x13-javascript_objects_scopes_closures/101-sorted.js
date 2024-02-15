#!/usr/bin/node

const dict = require('./101-data').dict;
const dict2 = {};

for (const [key, val] of Object.entries(dict)) {
  dict2[val] ? dict2[val].push(key) : dict2[val] = [key];
}
console.log(dict2);
