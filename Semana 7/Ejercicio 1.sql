Crear la BD con el siguiente esquema, respetando las claves requeridas:
EMPLEADO( NOMBRE-EMPLEADO, DIRECCION, CIUDAD)
TRABAJA (NOMBRE-EMPLEADO, NOMBRE-EMPRESA, SUELDO)
EMPRESA (NOMBRE-EMPRESA, CIUDAD)
SUPERVISA (NOMBRE-EMPLEADO, NOMBRE-SUPERVISOR)

CREATE TABLE empleado (
  nombre_empleado VARCHAR(100) NOT NULL,
  direccion VARCHAR(200),
  ciudad VARCHAR(100),
  PRIMARY KEY (nombre_empleado)
);

CREATE TABLE trabaja (
    nombre_empleado VARCHAR (100) NOT NULL,
    nombre_empresa VARCHAR (100) NOT NULL,
    sueldo INT NOT NULL,
    FOREIGN KEY (nombre_empleado) REFERENCES empleado(nombre_empleado),
    FOREIGN KEY (nombre_empresa) REFERENCES empresa(nombre_empresa)
);

CREATE TABLE empresa (
    nombre_empresa VARCHAR(100) NOT NULL,
    ciudad VARCHAR (50) NOT NULL,
    PRIMARY KEY (nombre_empresa)
);

CREATE TABLE supervisa (
    nombre_empleado VARCHAR (100) NOT NULL,
    nombre_supervisor VARCHAR (100) NOT NULL,
    FOREIGN KEY (nombre_empleado) REFERENCES empleado(nombre_empleado),
    FOREIGN KEY (nombre_supervisor) REFERENCES empleado(nombre_empleado)
);
