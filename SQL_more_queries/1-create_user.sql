-- create a new user 
CREATE USER IF NOT EXISTS "user_0d_1"@"local_host" IDENTIFIED BY "user_0d_1_pwd";
GRANTS ALL PRIVILEGES ON "." to "user_0d_1"@"local_host";