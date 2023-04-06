const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Bem-vindo à minha página inicial!');
});

app.get('/pessoa/:nome', (req, res) => {
  const nome = req.params.nome;
  res.send(`Bem-vindo(a), ${nome}!`);
});

app.get('/produtos', (req, res) => {
  const categoria = req.query.categoria;
  const preco = req.query.preco;
  if (categoria && preco) {
    res.send(`Listando produtos da categoria ${categoria} com preço até ${preco}.`);
  } else {
    res.send('Listando todos os produtos.');
  }
});

app.listen(8080, () => {
  console.log('Servidor rodando na porta 8080');
});
