CREATE TABLE usager (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nom TEXT,
    email TEXT,
    sexe TEXT,
    adresse TEXT,
    date_naissance DATE,
    identifiant TEXT,
    hashed_password TEXT,
    is_active BOOLEAN DEFAULT TRUE
);


INSERT INTO usager (nom, email, sexe, adresse, date_naissance) VALUES
('Jean Dupont', 'jean.dupont@email.com', 'M', '12 rue de Paris, Bordeaux', '1990-05-12'),
('Marie Martin', 'marie.martin@email.com', 'F', '8 avenue Victor Hugo, Lyon', '1985-11-23'),
('Lucas Bernard', 'lucas.bernard@email.com', 'M', '25 boulevard Saint-Michel, Paris', '1993-07-04'),
('Sophie Petit', 'sophie.petit@email.com', 'F', '3 place Bellecour, Lyon', '1988-02-17'),
('Thomas Moreau', 'thomas.moreau@email.com', 'M', '45 rue Nationale, Lille', '1995-09-30');