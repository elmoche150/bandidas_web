CREATE DATABASE IF NOT EXISTS bandidas_db;
USE bandidas_db;


CREATE TABLE menu (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    precio INT NOT NULL,
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
    comanda_id INT NOT NULL,
    producto_id INT NOT NULL,
    detalles TEXT,
    cantidad INT DEFAULT 1,
    FOREIGN KEY (comanda_id) REFERENCES comandas(id) ON DELETE CASCADE,
    FOREIGN KEY (producto_id) REFERENCES menu(id)
);
