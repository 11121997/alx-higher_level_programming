#SQL - More queries project
===========================
#How to create a new MySQL user?
-- CREATE USER `name`@`localhost`;
------------------------------------
#How to manage privileges for a user to a database or table?
-- GRANT PRIVILEGE ON (`database` or `table`) TO `table`@`localhost`;
-- FLUSH PRIVILEGE "reload" -> should implement after create user or grant
-- REVOKE
-- SHOW GRANTS
-- DROP USER
