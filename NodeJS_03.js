const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Requisição GET recebida');
});

app.post('/', (req, res) => {
  res.send('Requisição POST recebida');
});

app.listen(8080, () => {
  console.log('Servidor rodando na porta 8080');
});
