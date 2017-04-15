-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
DROP VIEW report_match_table;
DROP TABLE players;
DROP TABLE matches;

CREATE TABLE players (
    id      SERIAL PRIMARY KEY,
    name    TEXT
);

CREATE TABLE matches (
    id      SERIAL PRIMARY KEY,
    winner  INTEGER,
    loser   INTEGER
);

CREATE VIEW report_match_table AS
    SELECT players.id, players.name, 
    count(CASE WHEN players.id = matches.winner THEN 1 END) AS wins, 
    count(CASE WHEN players.id = matches.loser OR players.id = matches.winner THEN 1 END) AS total
    FROM players LEFT JOIN matches
    ON players.id = matches.winner OR players.id = matches.loser
    GROUP BY players.id
    ORDER BY wins desc;
