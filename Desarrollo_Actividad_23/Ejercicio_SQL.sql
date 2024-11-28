-- Creación de Tabla
CREATE TABLE `Datos_Estudiantes`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Nombres` VARCHAR(255) NOT NULL,
    `Apellidos` VARCHAR(255) NOT NULL,
    `Dirección` VARCHAR(255) NOT NULL,
    `Edad` INT NOT NULL,
    `Estatura` FLOAT(53) NOT NULL,
    `Genero` VARCHAR(255) NOT NULL
);
-- Insertar datos
INSERT INTO Datos_Estudiantes VALUES (1, 'Katerin', 'Gamez', 'Mirador', 37, 1.62, 'Femenino');
INSERT INTO Datos_Estudiantes VALUES (2, 'Ismael', 'Madrid', 'Mirador', 8, 1.2, 'Masculino');
INSERT INTO Datos_Estudiantes VALUES (3, 'Esteban', 'Madrid', 'Mirador', 3, 0.8, 'Masculino');

-- Mostrar dastos de la tabla
SELECT * FROM Datos_Estudiantes;

-- Seleccionar una columna de una tabla
SELECT Edad FROM Datos_Estudiantes;

-- Seleccionar dos columnas de una tabla
SELECT Nombres, Apellidos FROM Datos_Estudiantes;

-- Seleccionar una columna de la tabla filtrada
SELECT Nombres FROM Datos_Estudiantes WHERE Genero = 'Masculino';

-- Actualizar campo en una tabla con busqueda
UPDATE Datos_Estudiantes SET Edad = 4 WHERE Nombres = 'Esteban';
UPDATE Datos_Estudiantes SET Estatura = 2 WHERE Apellidos = 'Madrid';
SELECT * FROM Datos_Estudiantes;

-- Eliminar registro en una tabla
DELETE FROM Datos_Estudiantes WHERE id = 2;
SELECT * FROM Datos_Estudiantes;
