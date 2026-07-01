# Explicación del Backend TITAN

## Introducción

Para el desarrollo del backend del proyecto TITAN se utilizó FastAPI como framework principal, junto con SQLAlchemy para la conexión a la base de datos y Pydantic para la validación de la información.

El objetivo de este backend es administrar la programación de cursos, la inscripción de participantes y la consulta de información relacionada con las capacitaciones realizadas por la empresa.

---

# Estructura General del Proyecto

El proyecto está organizado en diferentes módulos para mantener el código ordenado y facilitar su mantenimiento.

```text
App
└── Modulo_Cursos
    ├── config
    ├── controllers
    ├── middleware
    ├── models
    ├── routes
    ├── schemas
    └── utils
```

Cada carpeta tiene una responsabilidad específica dentro de la aplicación.

---

# Archivo main.py

Este archivo es el punto de inicio de la aplicación.

Aquí se realizan las configuraciones principales del sistema, como:

- Inicializar FastAPI.
- Configurar la conexión con la base de datos.
- Registrar las rutas del módulo de cursos.
- Configurar el middleware.
- Configurar el manejo de errores.
- Permitir la comunicación con el frontend mediante CORS.

También contiene una ruta principal que permite verificar que la API se encuentra funcionando correctamente.

---

# Carpeta Config

Esta carpeta contiene la configuración de la base de datos.

En ella se define:

- La conexión a MySQL.
- La creación de sesiones.
- La clase base para los modelos.
- La función que permite abrir y cerrar conexiones de manera segura.

Su función principal es servir de puente entre la aplicación y la base de datos.

---

# Carpeta Models

En esta carpeta se encuentran los modelos de SQLAlchemy.

Cada modelo representa una tabla de la base de datos.

Por ejemplo:

### Usuario

Representa las personas registradas en el sistema.

Contiene información como:

- Nombre
- Apellido
- Correo
- Documento
- Rol

### Curso

Representa los cursos disponibles para capacitación.

### ProgramacionCurso

Permite registrar una fecha específica para la realización de un curso.

### Inscripcion

Permite relacionar participantes con cursos programados.

### Certificado

Guarda los certificados obtenidos por los participantes.

Estos modelos permiten trabajar con la base de datos utilizando objetos de Python en lugar de escribir consultas SQL manualmente.

---

# Carpeta Schemas

Los schemas fueron desarrollados utilizando Pydantic.

Su función es validar la información que recibe y devuelve la API.

Por ejemplo, cuando se crea una programación de curso, el schema verifica que:

- Todos los campos obligatorios estén presentes.
- Los tipos de datos sean correctos.
- Los valores cumplan las restricciones establecidas.

Esto ayuda a prevenir errores antes de que la información llegue a la base de datos.

---

# Carpeta Routes

Esta carpeta contiene todos los endpoints de la API.

Los endpoints permiten que el frontend se comunique con el backend.

Entre las rutas implementadas se encuentran:

### Crear programación de curso

Permite registrar una nueva programación.

### Inscribir participante

Permite registrar participantes en una programación existente.

### Consultar calendario

Permite visualizar todas las programaciones registradas.

### Consultar instructores

Permite obtener la lista de instructores disponibles.

### Consultar cursos

Permite obtener la lista de cursos registrados.

### Buscar participante

Permite buscar participantes mediante parámetros enviados en la URL.

---

# Carpeta Controllers

Los controladores contienen la lógica de negocio de la aplicación.

Aquí se encuentran las validaciones necesarias antes de guardar información en la base de datos.

Por ejemplo:

### Validación de cupos

Verifica que existan cupos disponibles antes de realizar una inscripción.

### Validación médica

Verifica que el participante tenga un examen médico vigente.

### Validación de inscripción duplicada

Evita que un participante sea inscrito varias veces en la misma programación.

### Validación de reentrenamiento

Comprueba que el participante cumpla con los requisitos para cursos de reentrenamiento.

Estas validaciones garantizan que la información almacenada sea consistente.

---

# Carpeta Middleware

El middleware permite interceptar las peticiones antes de que lleguen a las rutas o antes de enviar una respuesta al cliente.

En este proyecto se utiliza para controlar errores inesperados y devolver mensajes adecuados cuando ocurre una falla del sistema.

Esto mejora la experiencia del usuario y facilita la identificación de problemas.

---

# Carpeta Utils

Contiene funciones auxiliares reutilizables dentro del proyecto.

Su objetivo es evitar la repetición de código y mantener una estructura más organizada.

También permite generar respuestas con un formato uniforme para toda la API.

---

# Manejo de Base de Datos

La aplicación utiliza SQLAlchemy como ORM.

Gracias a esto, las operaciones sobre la base de datos pueden realizarse mediante objetos de Python.

Algunas operaciones implementadas son:

- Consultar registros.
- Insertar información.
- Actualizar datos.
- Eliminar registros.

Todo esto se realiza manteniendo la integridad de la información almacenada.

---

# Validaciones Implementadas

Durante el desarrollo del backend se implementaron diferentes validaciones para garantizar la calidad de los datos.

Entre ellas se encuentran:

- Validación de tipos de datos.
- Validación de campos obligatorios.
- Validación de cupos disponibles.
- Validación de participantes existentes.
- Validación de certificados.
- Validación de exámenes médicos.

Estas validaciones permiten evitar inconsistencias dentro del sistema.

---

# Conclusión

El backend del proyecto TITAN fue desarrollado siguiendo una arquitectura modular que facilita la organización y el mantenimiento del código.

La utilización de FastAPI, SQLAlchemy y Pydantic permitió construir una API robusta, escalable y segura, capaz de gestionar correctamente la programación de cursos, la inscripción de participantes y la validación de los diferentes requisitos establecidos por la organización.
