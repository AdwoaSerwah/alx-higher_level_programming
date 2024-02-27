-- Convert the database to UTF8
USE hbtn_0c_0;
ALTER DATABASE hbtn_0c_0 CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

ALTER TABLE first_table COLLATE=utf8mb4_unicode_ci;

-- Convert the name field in the first_table table to UTF8
ALTER TABLE first_table
MODIFY COLUMN name VARCHAR(256);
-- DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
