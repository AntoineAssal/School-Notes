# Database Management System

**DB** : Database \
**DBS** : Database system = DB + DBMS \
User &rarr; UI &rarr; API(database application) &rarr; DBMS &rarr; DB (I think?)

## What is DBMS?
- A form of persistent storage that supports convenient, efficient, and secure access and manipulation of data.

<p align="center">
<a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\dpi{150}&space;\bg_white&space;\fn_cm&space;\small&space;ACID=&space;\mathbf{A}tomicity,&space;\mathbf{C}onsistency,&space;\boldsymbol{I}solation,&space;\mathbf{D}urability" target="_blank"><img src="https://latex.codecogs.com/png.latex?\inline&space;\dpi{150}&space;\bg_white&space;\fn_cm&space;\small&space;ACID=&space;\mathbf{A}tomicity,&space;\mathbf{C}onsistency,&space;\boldsymbol{I}solation,&space;\mathbf{D}urability" title="\small ACID= \mathbf{A}tomicity, \mathbf{C}onsistency, \boldsymbol{I}solation, \mathbf{D}urability" /></a>
</p>

- **Atomicity**: All or nothing. Either all the operations are done or none of them are done.
- **Consistency**: All databases need to have consistency constraints. These are often shown with relationships among data elements (example: account balances cannot be negative). Operations are expected to preserve consistency of the database.
- **Atomicity**: Every operation must appear to be executed as if no other operation is executing at the same time.  
- **Atomicity**: The condition that the effect on the database of an operation must never be lost even if system fails. 

## Queries and other DML actions are grouped into transactions. 
The transaction processor is split into two parts:
1.  A **concurrency-control** manager/scheduler, responsible for assuring atomicity and isolation of transactions/operations. 
2. A l**ogging and recovery** manager, responsible for the durability of transactions.

## Advantages of Databases:
- Minimizes (not eliminate) redundancy and avoids inconsistency.
- Provides concurrent access to shared data. (Multi-user).
- Provides centralized control over data management.
- Security and authorization.
- Persistent because the data will outlive the program that operates on it.
- Data abstraction and independence.
## Disadvantages of File Processing Systems (FPS):
- Redundancy by having same data repeated over multiple files.
- Inconsistency because every file needs to be updated on change.
- High cost and maintenance because it require knowledge of multiple programming languages.

## DBMS Architecture
<p align="center">
	<img src="https://i.imgur.com/5R1TmvN.png" alt="DBMS Architecture">
</p>

### Input:
1. Queries.
2. Transactions.
3. Schema creation and modifications. 
### Query Processor and optimizer: 
Handles queries, transactions, and schema modifications, then finds the best plan to process the given query and issues commands to storage manager.
### Storage manager:  
Obtains the information requested from data storage. Modifies data in storage when requested.
### Transaction manager: 
Responsible for the consistency of the data. The database has several queries running simultaneously and should not interfere with each other. Ensures data integrity even if there’s a power failure.

## DBMS Languages
### Data Definition Language (DDL): 
The language/notation used for defining schemas and syntax for tables, indexes view constraints
```sql
Create Table:
        CREATE TABLE <name> (list, elements)
        CREATE TABLE employees(id INTEGER , first_name VARCHAR(50), last_name VARCHAR(75), fname VARCHAR(50), dateofbirth DATE);   
Drop Table:
        DROP TABLE employees;    
ALTER TABLE:
        ALTER TABLE <name> parameters
        ALTER TABLE employees ADD phone INTEGER;
TRUNCATE Table:
        TRUNCATE TABLE <name>;
        TRUNCATE TABLE employees;
```
### Data Manipulation Language (DML):
Language/Notation for accessing and manipulating data. Statements can change the state (content of the database).
```sql
Add Column:
        ALTER TABLE R ADD <column declaration>
Remove Column:
        ALTER TABLE R DROP COLUMN <column_name>
Modify Column:
        ALTER TABLE R ALTER COLUMN SET DEFAULT <property>
Insert values into table:
        INSERT INTO R(A1, …, An) VALUES (v1,…, vn) 
        INSERT INTO <table>(column1, column2) VALUES (value1, value2)
Delete Attributes:    
        DELETE FROM <relation> WHERE <condition> 
Update Attributes:
        UPDATE R SET <new-value assignments> WHERE <condition>
```