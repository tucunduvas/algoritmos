"""
GUIA COMPLETO DE COMANDOS SQL COM EXEMPLOS

1. COMANDOS DML (Data Manipulation Language)
-------------------------------------------

SELECT - Recupera dados
EXEMPLO:
SELECT nome, idade FROM clientes WHERE idade > 30;

INSERT - Insere dados
EXEMPLO:
INSERT INTO clientes (nome, idade) VALUES ('Ana', 28);

UPDATE - Atualiza dados
EXEMPLO:
UPDATE clientes SET idade = 29 WHERE nome = 'Ana';

DELETE - Remove dados
EXEMPLO:
DELETE FROM clientes WHERE nome = 'Ana';

2. COMANDOS DDL (Data Definition Language)
-------------------------------------------

CREATE TABLE - Cria uma tabela
EXEMPLO:
CREATE TABLE clientes (
    id INT PRIMARY KEY,
    nome VARCHAR(100),
    idade INT
);

ALTER TABLE - Altera estrutura da tabela
EXEMPLO:
ALTER TABLE clientes ADD email VARCHAR(100);

DROP TABLE - Remove uma tabela
EXEMPLO:
DROP TABLE clientes;

3. COMANDOS TCL (Transaction Control Language)
----------------------------------------------

BEGIN / COMMIT / ROLLBACK - Controle de transações
EXEMPLO:
BEGIN;
UPDATE contas SET saldo = saldo - 100 WHERE id = 1;
UPDATE contas SET saldo = saldo + 100 WHERE id = 2;
COMMIT;

4. COMANDOS DCL (Data Control Language)
----------------------------------------

GRANT - Concede permissões
EXEMPLO:
GRANT SELECT, INSERT ON clientes TO usuarioX;

REVOKE - Revoga permissões
EXEMPLO:
REVOKE INSERT ON clientes FROM usuarioX;

5. CONSULTAS AVANÇADAS
------------------------

JOIN - Junção de tabelas
EXEMPLO:
SELECT c.nome, p.pedido
FROM clientes c
JOIN pedidos p ON c.id = p.cliente_id;

GROUP BY / HAVING - Agrupamento
EXEMPLO:
SELECT cliente_id, COUNT(*) FROM pedidos
GROUP BY cliente_id
HAVING COUNT(*) > 5;

SUBQUERY - Subconsulta
EXEMPLO:
SELECT nome FROM clientes
WHERE id IN (SELECT cliente_id FROM pedidos WHERE valor > 100);

Funções de agregação:
EXEMPLO:
SELECT AVG(idade), MAX(idade), MIN(idade), COUNT(*) FROM clientes;

6. OUTROS COMANDOS ÚTEIS
--------------------------

ORDER BY - Ordena resultados
EXEMPLO:
SELECT nome FROM clientes ORDER BY idade DESC;

DISTINCT - Remove duplicados
EXEMPLO:
SELECT DISTINCT cidade FROM clientes;

LIMIT - Limita resultados
EXEMPLO:
SELECT * FROM clientes LIMIT 10;

IN / NOT IN - Conjunto de valores
EXEMPLO:
SELECT nome FROM clientes WHERE cidade IN ('São Paulo', 'Rio de Janeiro');

LIKE - Busca por padrão
EXEMPLO:
SELECT nome FROM clientes WHERE nome LIKE 'A%';

BETWEEN - Intervalo
EXEMPLO:
SELECT * FROM clientes WHERE idade BETWEEN 20 AND 30;

IS NULL - Verifica valores nulos
EXEMPLO:
SELECT * FROM clientes WHERE email IS NULL;
"""

# Gerando o PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
for linha in conteudo.split('\n'):
    pdf.cell(200, 10, txt=linha, ln=True)

# Salvando o PDF
pdf.output("guia_completo_sql.pdf")
