--- DATABASE 생성
CREATE DATABASE side_project_database;

--- User 생성
CREATE USER side_project_user WITH PASSWORD '1r2r3r4r';
ALTER ROLE side_project_user SET client_encoding TO 'utf8';
ALTER ROLE side_project_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE side_project_user WITH SUPERUSER;

--- DB에 대한 User 권한 부여
GRANT ALL PRIVILEGES ON DATABASE side_project_database TO side_project_user;
