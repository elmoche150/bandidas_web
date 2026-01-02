CREATE DATABASE IF NOT EXISTS bandidas_db;
USE bandida_db;


CREATE TABLE menu (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    precio INT,
    estado ENUM('bebida','comida') DEFAULT 'comida'
);


CREATE TABLE comandas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    fecha_finalizacion DATETIME NULL,
    estado ENUM('pendiente','terminada') DEFAULT 'pendiente'
);

CREATE TABLE comanda_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    comanda_id INT,
    producto_id INT,
    detalles TEXT,
    cantidad INT DEFAULT 1,
    FOREIGN KEY (comanda_id) REFERENCES comandas(id),
    FOREIGN KEY (producto_id) REFERENCES menu(id)
);