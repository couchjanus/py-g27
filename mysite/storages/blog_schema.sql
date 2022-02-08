-- Schema for application.
DROP TABLE IF EXISTS blogs;

CREATE TABLE blogs (
   id INTEGER PRIMARY KEY,
   title VARCHAR(250)  NOT NULL,
   category VARCHAR(250)   NOT NULL,
   cover VARCHAR(250),
   content TEXT
);
