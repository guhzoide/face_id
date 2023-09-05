CREATE TABLE acessos (
    id int NOT NULL AUTO_INCREMENT,
    colaborador_nome VARCHAR(50) NOT NULL,
    chapa VARCHAR(50) NOT NULL,
    cpf VARCHAR(50) NOT NULL,
    data VARCHAR(50) NOT NULL,
    acesso_autorizado BOOLEAN NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE cadastros (
    nome VARCHAR(50) NOT NULL,
    chapa VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    cpf VARCHAR(50) NOT NULL,
    nivel VARCHAR(50) NOT NULL
);