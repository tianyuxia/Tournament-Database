#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")

def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    c = db.cursor()
    c.execute("DELETE FROM matches;")
    db.commit()
    db.close()

def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    c = db.cursor()
    c.execute("DELETE FROM players;")
    db.commit()
    db.close()

def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    c = db.cursor()
    c.execute("SELECT count(*) FROM players;")
    player_count = c.fetchall()[0][0]
    db.commit()
    db.close()
    return player_count

def countMatches():
    db = connect()
    c = db.cursor()
    c.execute("SELECT count(*) FROM matches;")
    match_count = c.fetchall()[0][0]
    db.commit()
    db.close()
    return match_count

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    db = connect()
    c = db.cursor()
    c.execute("INSERT INTO players (name) VALUES (%s);", (name, ))
    db.commit()
    db.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """

    db = connect()
    c = db.cursor()
    # Selecting from created view
    c.execute("SELECT * FROM report_match_table;") 
    player_standing = c.fetchall()
    db.close()
    return player_standing


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """

    db = connect()
    c = db.cursor()
    c.execute("INSERT INTO matches (winner, loser) VALUES (%s, %s);", (winner, loser))
    db.commit()
    db.close()
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    id1 = 0
    name1 = ""
    id2 = 0
    name2 = ""
    alternate = True
    swiss_pair = []
    player_standing = playerStandings()
    for player_tuple in player_standing:
        if alternate:
            id1 = player_tuple[0]
            name1 = player_tuple[1]
            alternate = False;
        else:
            id2 = player_tuple[0]
            name2 = player_tuple[1]
            temp_tuple = (id1, name1, id2, name2)
            swiss_pair.append(temp_tuple)
            alternate = True
    return swiss_pair



