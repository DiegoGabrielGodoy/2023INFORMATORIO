-- Lista el nombre de todos los productos que hay en la tabla producto.
SELECT nombre FROM producto;

-- Lista todas las columnas de la tabla producto.
SHOW COLUMNS FROM producto;

--Lista el nombre de los productos y el precio en USD.
SELECT nombre, CONCAT('$', precio) AS precio_usd FROM producto;

-- Lista los nombres y los precios de todos los productos de la tabla producto, convirtiendo los nombres a mayúscula.
SELECT UPPER(nombre) AS nombre_mayuscula, precio FROM producto;

--Lista los nombres y los precios de todos los productos de la tabla producto, redondeando el valor del precio.
SELECT nombre, ROUND(precio) AS precio_redondeado FROM producto;

-- Lista el código de los fabricantes que tienen productos en la tabla producto.
SELECT DISTINCT codigo_fabricante FROM producto;

--Lista el código de los fabricantes que tienen productos en la tabla producto, eliminando los códigos que aparecen repetidos.
SELECT DISTINCT codigo_fabricante FROM producto;

-- Lista los nombres de los fabricantes ordenados de forma ascendente.
SELECT nombre FROM fabricante ORDER BY nombre ASC;

--Lista los nombres de los productos ordenados en primer lugar por el nombre de forma ascendente y en segundo lugar por el precio de forma descendente.
SELECT nombre, precio FROM producto ORDER BY nombre ASC, precio DESC;

--Devuelve una lista con las 5 primeras filas de la tabla fabricante.
SELECT * FROM fabricante LIMIT 5;

--Lista el nombre de todos los productos del fabricante cuyo código de fabricante es igual a 2.
SELECT nombre FROM producto WHERE codigo_fabricante = 2;

-- Lista el nombre de los productos que tienen un precio menor o igual a 120 USD.
SELECT nombre FROM producto WHERE precio <= 120;

-- Devuelve todos los productos del fabricante Lenovo (sin utilizar INNER JOIN).
SELECT producto.* 
FROM producto, fabricante 
WHERE producto.codigo_fabricante = fabricante.codigo_fabricante 
  AND fabricante.nombre = 'Lenovo';

--Devuelve todos los datos de los productos que tienen el mismo precio que el producto más caro del fabricante Lenovo (sin utilizar INNER JOIN).
SELECT producto.* 
FROM producto, fabricante 
WHERE producto.codigo_fabricante = fabricante.codigo_fabricante 
  AND producto.precio = (SELECT MAX(precio) FROM producto WHERE codigo_fabricante = (SELECT codigo_fabricante FROM fabricante WHERE nombre = 'Lenovo'));

--Lista el nombre del producto más caro del fabricante Lenovo.
SELECT nombre 
FROM producto 
WHERE precio = (SELECT MAX(precio) FROM producto WHERE codigo_fabricante = (SELECT codigo_fabricante FROM fabricante WHERE nombre = 'Lenovo'));

-- Devuelve los nombres de los fabricantes que tienen productos asociados (utilizando ALL).
SELECT nombre 
FROM fabricante 
WHERE codigo_fabricante = ALL (SELECT DISTINCT codigo_fabricante FROM producto);
