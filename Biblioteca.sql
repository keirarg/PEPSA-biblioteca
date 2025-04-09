CREATE DATABASE IF NOT EXISTS PEPSA; 
CREATE USER 'user'@'%' IDENTIFIED BY 'userpw';
GRANT ALL PRIVILEGES ON PEPSA.* TO 'user'@'%';
FLUSH PRIVILEGES;
USE PEPSA;
CREATE TABLE IF NOT EXISTS libros(
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    autor VARCHAR(255) NOT NULL,
    anio INT(4) NOT NULL,
    precio DECIMAL(9, 2) NOT NULL,
    precioIVA DECIMAL(9, 2) NOT NULL,
    foto LONGTEXT
); CREATE TABLE IF NOT EXISTS usuarios(
    correo VARCHAR(255),
    usuario VARCHAR(100) NOT NULL PRIMARY KEY,
    clave VARCHAR(255) NOT NULL,
    perfil VARCHAR(100) NOT NULL,
    fechaUltimoAcceso DATE,
    numeroAccesosErroneos INTEGER,
    estado VARCHAR(20),
    fechaBloqueo DATE,
    debeResetearContraseña BOOLEAN
); 
INSERT INTO `usuarios`(`correo`, `usuario`, `clave`, `perfil`, `fechaUltimoAcceso`, `numeroAccesosErroneos`, `estado`, `fechaBloqueo`, `debeResetearContraseña`)
VALUES('root@root.com', 'root', '$2b$10$PBeZdw2k4yRGWBHsBHuPluHwdr37uKbAIkhtx9dWDGt2EMTJ5B1q2', 'admin', '2022-03-01', 0, 'activo', NULL, FALSE);
INSERT INTO `libros`(`id`, `titulo`, `autor`, `anio`, `precio`, `precioIVA`, `foto`)
VALUES( 1, 'Drácula', 'Bram Stoker', 1897, 19.95, 24.14, NULL);
