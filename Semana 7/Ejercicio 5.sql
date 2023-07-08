-- Lista las asignaturas del tipo "optativa":
SELECT nombre
FROM asignatura
WHERE tipo = 'optativa';

-- Lista los nombres de Departamento de la Universidad:
SELECT nombre
FROM departamento;

-- Listar apellidos y nombre de las Personas, convirtiendo ambos elementos a mayúsculas:
SELECT UPPER(apellido1) AS apellido1_mayusculas, UPPER(apellido2) AS apellido2_mayusculas, UPPER(nombre) AS nombre_mayusculas
FROM persona;
-- Listar apellidos y nombres de Profesores mayores a 40 años en la Universidad:
SELECT apellido1, apellido2, nombre
FROM persona
WHERE id IN (SELECT id_profesor FROM profesor)
    AND fecha_nacimiento <= DATE_ADD(CURDATE(), INTERVAL -40 YEAR);
