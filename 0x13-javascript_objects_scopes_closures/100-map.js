#!/usr/bin/node

const list = require('100-data').list;
const array = list.map((e, i) => e * i);
console.log(list);
console.log(array);
