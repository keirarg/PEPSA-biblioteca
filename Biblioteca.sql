CREATE DATABASE IF NOT EXISTS PEPSA;
USE PEPSA;
CREATE TABLE libros(
    id BIGINT PRIMARY KEY,
    titulo BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    autor VARCHAR(255) NOT NULL,
    anio VARCHAR(255) NOT NULL,
    precio DECIMAL(9,2) NOT NULL,
	foto VARCHAR(255)
);
CREATE TABLE usuarios(
	usuario VARCHAR(100) NOT NULL PRIMARY KEY,
    clave VARCHAR(255) NOT NULL,
    perfil VARCHAR(100) NOT NULL,
    fechaUltimoAcceso DATE
);
INSERT INTO `usuarios` (`usuario`, `clave`, `perfil`, `fechaUltimoAcceso`) VALUES ('root', '1234', 'admin', '2022-03-01');