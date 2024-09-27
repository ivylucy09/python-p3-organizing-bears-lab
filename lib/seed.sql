-- lib/seed.sql

CREATE TABLE bears (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    sex TEXT,
    color TEXT,
    temperament TEXT,
    alive BOOLEAN
);

-- Insert some seed data
INSERT INTO bears (name, age, sex, color, temperament, alive)
VALUES 
    ('Mr. Chocolate', 10, 'M', 'brown', 'grumpy', 1),
    ('Rowdy', 7, 'M', 'black', 'calm', 1),
    ('Tabitha', 6, 'F', 'black', 'aggressive', 1),
    ('Sergeant Brown', 9, 'M', 'brown', 'calm', 1),
    ('Melissa', 5, 'F', 'brown', 'calm', 1),
    ('Grinch', 8, 'M', 'brown', 'grumpy', 0),
    ('Wendy', 3, 'F', 'black', 'friendly', 1),
    (NULL, 4, 'M', 'brown', 'aggressive', 0);
