DROP TABLE IF EXISTS usuarios;
DROP TABLE IF EXISTS facturas;
DROP TABLE IF EXISTS menu;
DROP TABLE IF EXISTS inventario;
DROP TABLE IF EXISTS preparacion;

CREATE DATABASE IF NOT EXISTS proyecto;
USE proyecto;

CREATE TABLE usuarios (
  nombreCompleto VARCHAR(90),
  correo VARCHAR(80),
  usuario VARCHAR(15) PRIMARY KEY,
  clave VARCHAR(50)
);

CREATE TABLE facturas (
    id INT(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombreCliente VARCHAR(50),
    email VARCHAR(50),
    totalCuenta DECIMAL(10,2),
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE inventario (
    id_inventario INT AUTO_INCREMENT PRIMARY KEY,
    ingrediente VARCHAR(100),
    cantidad_disponible INT
);

CREATE TABLE menu (
    id_menu INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    precio DECIMAL(10,2),
    cantidad INT(11)
);

CREATE TABLE preparacion (
    id_preparacion INT AUTO_INCREMENT PRIMARY KEY,
    menu_id INT,
    inventario_id INT,
    FOREIGN KEY (menu_id) REFERENCES menu(id_menu),
    FOREIGN KEY (inventario_id) REFERENCES inventario(id_inventario)
);

INSERT INTO usuarios (nombreCompleto, correo, usuario, clave) VALUES ('Admin', 'admin@admin.com', 'admin', 'admin');
INSERT INTO usuarios (nombreCompleto, correo, usuario, clave) VALUES ('Usuario 1', 'user1@user.com', 'user1', '1234');