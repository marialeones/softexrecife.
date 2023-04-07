const express = require('express');
const router = express.Router();
router.post('/', (req, res) => {
    const livro = req.body;
    res.status(201).json(livro);
  });
  const express = require('express');
const router = express.Router();
const livros = [];

function obterLivroPorId(id) {
  return livros.find(l => l.id === id);
}

router.post('/', (req, res) => {
  const livro = req.body;
  
  livro.id = livros.length + 1;

  livros.push(livro);
  res.status(201).json(livro);
});

router.get('/:id', (req, res) => {
  const id = parseInt(req.params.id);

  const livro = obterLivroPorId(id);

  if (livro) {

    res.status(200).json(livro);
  } else {
 
    res.status(404).send('Livro não encontrado');
  }
});

router.put('/:id', (req, res) => {

  const id = parseInt(req.params.id);

  const livro = obterLivroPorId(id);

  if (livro) {
  
    livro.titulo = req.body.titulo;
    livro.autor = req.body.autor;
    livro.isbn = req.body.isbn;

    res.status(200).json(livro);
  } else {
    res.status(


  