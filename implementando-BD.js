const mysql = require("mysql2");

const conexao = mysql.createConnection({
  host: "localhost",
  user: "root",
  senha: "senha123",
  nome: "banco-dados"
});

conexao.connect(function(err) {
  if (err) {
    console.error("Erro ao conectar ao banco de dados: " + err.stack);
    return;
  }

  console.log("Conexão com o banco de dados estabelecida com sucesso!");
});


conexao.end(function(err) {
  if (err) {
    console.error("Erro ao finalizar conexão com o banco de dados: " + err.stack);
    return;
  }

  console.log("Conexão com o banco de dados finalizada com sucesso!");
});
