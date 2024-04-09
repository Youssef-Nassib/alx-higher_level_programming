#!/usr/bin/node
const args = process.argv
args = parseInt(args);
if(isNaN(args)){
	console.log('Not a number');}
console.log('My number: ' + args);
