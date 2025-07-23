-- User Table
CREATE TABLE user (
    id SERIAL PRIMARY KEY,
    email VARCHAR(120) UNIQUE NOT NULL,
    password VARCHAR(60) NOT NULL,
    score INTEGER DEFAULT 0
);

-- Question Table
CREATE TABLE question (
    id SERIAL PRIMARY KEY,
    topic VARCHAR(50) NOT NULL,
    question TEXT NOT NULL,
    options TEXT NOT NULL, -- Stored as JSON string or Pickle
    correct VARCHAR(100) NOT NULL
);
