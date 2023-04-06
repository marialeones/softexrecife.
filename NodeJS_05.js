const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Você está acessando uma rota GET');
});

app.post('/', (req, res) => {
  res.send('Você está acessando uma rota POST');
});

app.put('/', (req, res) => {
  res.send('Você está acessando uma rota PUT');
});

app.delete('/', (req, res) => {
  res.send('Você está acessando uma rota DELETE');
});

app.listen(3000, () => {
  console.log('Servidor rodando na porta 3000');
});

// para rodar use: node index.js
// Requisição GET: curl http://localhost:3000/
// Requisição POST: curl -X POST http://localhost:3000/
