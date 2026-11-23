
CREATE TABLE IF NOT EXISTS notes (
    id SERIAL PRIMARY KEY,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO notes (content)
VALUES
    ('My first DevOps note'),
    ('Docker and PostgreSQL are working!');
