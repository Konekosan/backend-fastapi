CREATE TABLE permission (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nom TEXT UNIQUE NOT NULL
);

INSERT INTO permission (nom) VALUES
('read_usager'),
('create_usager'),
('update_usager'),
('delete_usager');