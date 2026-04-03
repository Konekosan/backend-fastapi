CREATE TABLE usager_role (
    usager_id INTEGER NOT NULL REFERENCES usager(id) ON DELETE CASCADE,
    role_id INTEGER NOT NULL REFERENCES role(id) ON DELETE CASCADE,
    PRIMARY KEY (usager_id, role_id)
);