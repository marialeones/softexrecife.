const express = require('express');
const app = express();
const PORT = 3000;

app.get('/usuario', (req, res) => {
  const usuario = {
    nome: "José",
    email: "jose.silva@gmail.com",
    idade: 27,
    cidade: "Pernambuco"
  };

  res.json(usuario);
});

app.listen(PORT, () => {
  console.log(`Servidor rodando na porta ${PORT}`);
});
