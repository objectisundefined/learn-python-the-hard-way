// // @ts-check

/*
const stdin = process.openStdin();

stdin.on("data", function(d) {
  // note:  d is an object, and when converted to a string it will
  // end with a linefeed.  so we (rather crudely) account for that  
  // with toString() and then trim() 
  console.log("you entered: [" +  d.toString().trim() + "]");
});
*/

const { promisify } = require('util')

const input = promisify((prompt, callback) => {
  process.stdin.resume()

  process.stdout.write(prompt)

  process.stdin.once('data', data => {
    callback(null, data.toString())
  })
})

const game = async () => {
  process.stdout.write("read user input\n")

  const val = await input("> ")

  return val
}

game().then(val => process.stdout.write('your input: ' + val))
  // pause stdin, otherwise process will not exit
  .then(() => process.stdin.pause())

// https://stackoverflow.com/questions/5006821/nodejs-how-to-read-keystrokes-from-stdin
// https://stackoverflow.com/questions/18193953/waiting-for-user-to-enter-input-in-node-js

// read user input with Node.js is disgusting