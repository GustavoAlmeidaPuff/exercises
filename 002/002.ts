const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('qual é seu nome?', (nome: string) => {
    console.log('Prazer em te conhecer ' + nome);
})