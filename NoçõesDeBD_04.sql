SELECT * FROM Aluno WHERE Nota > 7.0;

SELECT * FROM Aluno WHERE Ano = 1 AND Nota >= 8.0;

SELECT PNome, UNome, Nota FROM Aluno;

CREATE TABLE Professor AS SELECT PNome, UNome FROM Disciplina;

CREATE TABLE Aluno2 AS SELECT PNome, UNome FROM Aluno;

SELECT PNome, UNome FROM Aluno UNION SELECT PNome, UNome FROM Professor;

SELECT PNome, UNome FROM Aluno INTERSECT SELECT PNome, UNome FROM Professor;

SELECT PNome, UNome FROM Aluno EXCEPT SELECT PNome, UNome FROM Professor;
