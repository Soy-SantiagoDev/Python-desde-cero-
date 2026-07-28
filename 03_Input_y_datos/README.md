# ⌨️ Capítulo 3 - Input y Datos

En este capítulo aprenderás a interactuar con el usuario utilizando la función `input()`.

Hasta ahora nuestros programas mostraban información en pantalla, pero no podían recibir datos. Gracias a `input()`, el usuario puede escribir información desde el teclado y el programa podrá utilizarla.

---

# 📚 Objetivos

Al finalizar este capítulo podrás:

- ✅ Utilizar la función `input()`.
- ✅ Guardar datos ingresados por el usuario.
- ✅ Mostrar esos datos en la consola.
- ✅ Comprender que `input()` siempre devuelve un texto (`str`).

---

# 📂 Archivos del capítulo

| Archivo | Descripción |
|---------|-------------|
| `input.py` | Aprende a utilizar la función `input()`. |
| `Ejercicios.py` | Actividades para practicar. |
| `Soluciones.py` | Solución de los ejercicios. |
| `DesafioFinal.py` | Un reto para aplicar todo lo aprendido. |

---

# 🤔 ¿Qué es input()?

La función `input()` permite que un programa espere a que el usuario escriba información desde el teclado.

Su sintaxis es muy sencilla.

```python
nombre = input("¿Cuál es tu nombre? ")
```

Cuando el usuario escriba su nombre y presione **Enter**, ese dato quedará almacenado en la variable `nombre`.

---

# 📝 Mostrar la información

Una vez almacenado el dato, podemos utilizar `print()` para mostrarlo.

```python
print("Hola", nombre)
```

Ejemplo de ejecución:

```
¿Cuál es tu nombre? Carlos
Hola Carlos
```

---

# 📌 Importante

Todo lo que el usuario escribe mediante `input()` se guarda como un **texto** (`str`).

Por ejemplo:

```python
edad = input("¿Cuál es tu edad? ")
```

Si el usuario escribe:

```
20
```

Python almacenará:

```python
edad = "20"
```

Observa que el número está entre comillas, por lo que realmente es un texto.

Más adelante aprenderás cómo convertir ese texto en un número utilizando funciones como `int()` y `float()`.

---

# 💻 Ejercicios

Resuelve primero los ejercicios por tu cuenta.

Si tienes dificultades, consulta el archivo `Soluciones.py`.

---

# 🎯 Lo aprendido

En este capítulo aprendiste:

- ✔ Cómo recibir información del usuario.
- ✔ Cómo almacenar esos datos en variables.
- ✔ Cómo mostrar la información en pantalla.
- ✔ Que `input()` devuelve un dato de tipo texto.

---

# 🚀 Siguiente capítulo

En el siguiente capítulo aprenderás a realizar operaciones matemáticas utilizando los datos ingresados por el usuario.

---

⭐ Si este proyecto te está ayudando, considera darle una estrella al repositorio.
