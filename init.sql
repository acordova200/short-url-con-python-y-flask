DROP DATABASE IF EXISTS db_enlaces_cortos;

CREATE DATABASE db_enlaces_cortos CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE TABLE db_enlaces_cortos.ENLACES (
    id INT AUTO_INCREMENT PRIMARY KEY,
    url VARCHAR(255) NOT NULL,
    enlace_corto VARCHAR(20) NOT NULL UNIQUE
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

