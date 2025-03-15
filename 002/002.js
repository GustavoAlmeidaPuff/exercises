var readline = require('readline');
var rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.question('qual é seu nome?', function (nome) {
    console.log('Prazer em te conhecer ' + nome);
});
