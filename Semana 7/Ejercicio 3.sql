CREATE DATABASE productos;

USE productos;

CREATE TABLE fabricante (
    codigo_fabricante INT(10) NOT NULL PRIMARY KEY,
    nombre VARCHAR(100)
);

CREATE TABLE producto (
    codigo_fabricante INT(10) NOT NULL PRIMARY KEY,
    codigo_producto INT(10) NOT NULL,
    nombre VARCHAR(100),
    FOREIGN KEY (codigo_fabricante) REFERENCES fabricante(codigo_fabricante)
);

INSERT INTO fabricante VALUES (1, 'Asus');
INSERT INTO fabricante VALUES (2, 'Lenovo');
INSERT INTO fabricante VALUES (3, 'Hewlett-Packard');
INSERT INTO fabricante VALUES (4, 'Samsung');
INSERT INTO fabricante VALUES (5, 'Seagate');
INSERT INTO fabricante VALUES (6, 'Crucial');
INSERT INTO fabricante VALUES (7, 'Gigabyte');
INSERT INTO fabricante VALUES (8, 'Huawei');
INSERT INTO fabricante VALUES (9, 'Xiaomi');

INSERT INTO producto VALUES (1, 5, 'Disco duro SATA3 1TB');
INSERT INTO producto VALUES (2, 6, 'Memoria RAM DDR4 8GB');
INSERT INTO producto VALUES (3, 4, 'Disco SSD 1 TB');
INSERT INTO producto VALUES (4, 7, 'GeForce GTX 1050Ti');
INSERT INTO producto VALUES (5, 6, 'GeForce GTX 1080 Xtreme');
INSERT INTO producto VALUES (6, 1, 'Monitor 24 LED Full HD');
INSERT INTO producto VALUES (7, 1, 'Monitor 27 LED Full HD');
INSERT INTO producto VALUES (8, 2, 'Portátil Yoga 520');
INSERT INTO producto VALUES (9, 2, 'Portátil Ideapd 320');
INSERT INTO producto VALUES (10, 3, 'Impresora HP Deskjet 3720');
INSERT INTO producto VALUES (11, 3, 'Impresora HP Laserjet Pro M26nw');
