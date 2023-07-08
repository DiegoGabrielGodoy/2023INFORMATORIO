-- Obtener la lista de las ventas, pero con el nombre de la persona que lo vende en lugar de su identificador:
SELECT vendedores.NombreVendedor, ventas.Producto, ventas.Kilos
FROM ventas
INNER JOIN vendedores ON ventas.Vendedor = vendedores.IdVendedor;

-- Obtener la lista de las ventas pero con el nombre del producto en lugar del código:
SELECT productos.NomProducto, ventas.Vendedor, ventas.Kilos
FROM ventas
INNER JOIN productos ON ventas.Producto = productos.IdProducto;

-- Obtener la lista de las ventas pero con el nombre del producto y quién lo vendió:
SELECT productos.NomProducto, vendedores.NombreVendedor, ventas.Kilos
FROM ventas
INNER JOIN productos ON ventas.Producto = productos.IdProducto
INNER JOIN vendedores ON ventas.Vendedor = vendedores.IdVendedor;

-- Obtener el nombre de quien más kilos vendió:
SELECT vendedores.NombreVendedor, SUM(ventas.Kilos) AS TotalKilos
FROM ventas
INNER JOIN vendedores ON ventas.Vendedor = vendedores.IdVendedor
GROUP BY ventas.Vendedor
ORDER BY TotalKilos DESC
LIMIT 1;

-- uántos Kilos de Tomates se han vendido:
SELECT SUM(ventas.Kilos) AS TotalKilosTomates
FROM ventas
INNER JOIN productos ON ventas.Producto = productos.IdProducto
WHERE productos.NomProducto = 'Tomates';

-- Obtener todos los datos de cada venta que haya superado el promedio de kilos vendidos en total:
SELECT ventas.Vendedor, ventas.Producto, ventas.Kilos
FROM ventas
WHERE ventas.Kilos > (SELECT AVG(Kilos) FROM ventas);

-- Obtener cuál fue el producto más vendido del grupo de "Hortalizas":
SELECT productos.NomProducto, SUM(ventas.Kilos) AS TotalKilos
FROM ventas
INNER JOIN productos ON ventas.Producto = productos.IdProducto
INNER JOIN grupos ON productos.IdGrupo = grupos.IdGrupo
WHERE grupos.NombreGrupo = 'Hortalizas'
GROUP BY ventas.Producto
ORDER BY TotalKilos DESC
LIMIT 1;

-- Obtener los datos de la persona que menos kilos vendió e informar el nombre del producto y del grupo al que corresponde esa venta:
SELECT vendedores.NombreVendedor, productos.NomProducto, grupos.NombreGrupo, ventas.Kilos
FROM ventas
INNER JOIN vendedores ON ventas.Vendedor = vendedores.IdVendedor
INNER JOIN productos ON ventas.Producto = productos.IdProducto
INNER JOIN grupos ON productos.IdGrupo = grupos.IdGrupo
WHERE ventas.Kilos = (SELECT MIN(Kilos) FROM ventas)
LIMIT 1;

-- Obtener los totales de ventas por producto:
SELECT productos.NomProducto, SUM(ventas.Kilos) AS TotalKilos
FROM ventas
INNER JOIN productos ON ventas.Producto = productos.IdProducto
GROUP BY ventas.Producto;

-- Consulta interesante para informar a quien administra la Verdulería online:
SELECT grupos.NombreGrupo, productos.NomProducto, SUM(ventas.Kilos) AS TotalKilos
FROM ventas
INNER JOIN productos ON ventas.Producto = productos.IdProducto
INNER JOIN grupos ON productos.IdGrupo = grupos.IdGrupo
GROUP BY ventas.Producto
ORDER BY TotalKilos DESC
LIMIT 5;