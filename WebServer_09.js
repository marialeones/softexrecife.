const express = require('express');
const app = express();

app.listen(3000, () => {
  console.log('Servidor rodando na porta 3000!');
});

app.get('/users', (req, res) => {
  });
  
  app.get('/users/:id', (req, res) => {
  });
  
  app.post('/users', (req, res) => {
  });
  
  app.put('/users/:id', (req, res) => {
  });
  
  app.delete('/users/:id', (req, res) => {

  });
  