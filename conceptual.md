### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
  PostgreSQL is an object-relational database management system.

- What is the difference between SQL and PostgreSQL?

- In `psql`, how do you connect to a database?
In command line type:
 $psql name_of_database

- What is the difference between `HAVING` and `WHERE`?
 `WHERE`: + Used to filter the records from the table based on the   
            specified condition.
          + Can be used without GROUP BY Clause.
          + Cannot contain aggregate function
          + Can be used with SELECT, UPDATE, DELETE statement.
          + Used before GROUP BY Clause
          + used with single row function like UPPER, LOWER etc.

`HAVING`: + Used to filter record from the groups based on the specified condition.
          + Cannot be used without GROUP BY Clause.
          + Implements in column operation.
          + Can contain aggregate function.
          + Can only be used with SELECT statement.
          + Used after GROUP BY Clause.
          + Used with multiple row function like SUM, COUNT etc.



- What is the difference between an `INNER` and `OUTER` join?
+`INNER` join: returns records that have matching values in both tables
+`OUTER` join : will also keep information that is not related to the other table    
         in the resulting table 

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
+`LEFT OUTER`: all of the row from first table(left) combined with matching rows from the second table(right).
+`RIGHT OUTER`: the matching row from the first table(left) combined with all the rows from the second table(right)

- What is an ORM? What do they do?
  An object-relational mapper provides an object-oriented layer between relational databases and object-oriented programming languages without having to write SQL queries

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
  Client-side requests (via AJAX): You can do easily using AJAX libraries Don’t have to involve Flask in the API Can be faster: browser could talk directly to, say, Google Maps

  Server-side requests: Same-Origin Policy may prevent browser requests Easier for server to store/process the data Need password to access API

- What is CSRF? What is the purpose of the CSRF token? 
  Cross-Site Request Forgery, which a form on any site can submit to any other site

- What is the purpose of `form.hidden_tag()`?
  It generates a hidden field that includes a token that is used to protect the form against CSRF attacks
