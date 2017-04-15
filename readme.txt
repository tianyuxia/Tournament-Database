The following repository contains Python works which utilize PSQL to create a database used to monitor a swiss pairing tournament results. Files in the repository and their functions are explained below

tournament.py - Python file with implemented function to manage database and provide tournament results
tournament.sql - SQL schemas for the databased used
tournament_test.py - Test files used for debugging

1. To start program, navigate to the repository directory
2. Create database named tournament using CREATE DATABASE tournament in PSQL
3. Populate the database with schemas found in tournament.sql by running psql -c '\i tournament.sql'in the command window
4. Run tournament_test.py to confirm if all tests have been passed