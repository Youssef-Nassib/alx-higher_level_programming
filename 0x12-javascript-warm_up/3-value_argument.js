#!/usr/bin/node
const args = process.argv;
if (process.argv.length === 2) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log(args[2]);
}
