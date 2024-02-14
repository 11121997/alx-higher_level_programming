#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occurences = 0;
  for (const e of list) {
    if (e === searchElement) {
      occurences++;
    }
  }
  return occurences;
};
