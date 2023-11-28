#!/usr/bin/node
/* Script that writes a string to a file.
The first argument is the file path
The second argument is the string to write
The content of the file must be written in utf-8
If an error occurred during while writing, print the error object
*/

const fs = require('fs');
const filename = process.argv[2];
const contents = process.argv[3];
fs.writeFile(filename, contents, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
