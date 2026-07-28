# 🤝 Capítulo 6 - Operador Lógico `and`

En este capítulo aprenderás a utilizar el operador lógico `and`.

Este operador permite comprobar que **dos o más condiciones sean verdaderas al mismo tiempo**.

Es muy utilizado cuando un programa necesita verificar varios requisitos antes de tomar una decisión.

---

# 📚 Objetivos

Al finalizar este capítulo podrás:

- ✅ Comprender cómo funciona el operador `and`.
- ✅ Combinar dos condiciones.
- ✅ Crear programas que validen varios requisitos.
- ✅ Utilizar `and` junto con `if`.

---

# 📂 Archivos del capítulo

| Archivo | Descripción |
|---------|-------------|
| `operador.py` | Introducción al operador `and`. |
| `Ejercicios.py` | Ejercicios para practicar. |
| `Soluciones.py` | Solución de los ejercicios. |
| `DesafioFinal.py` | Reto para aplicar lo aprendido. |

---

# 🤔 ¿Qué hace el operador `and`?

El operador `and` une dos condiciones.

Para que el resultado sea **verdadero**, ambas condiciones deben cumplirse.

Por ejemplo:

```python
edad = 25

if edad >= 18 and edad <= 60:
    print("Puedes participar.")
```

En este ejemplo:

- La edad debe ser mayor o igual a 18.
- La edad debe ser menor o igual a 60.

Si alguna condición no se cumple, el programa ejecutará el bloque `else`.

---

# 💻 Ejemplo

```python
edad = int(input("¿Cuántos años tienes? "))

if edad >= 18 and edad <= 60:
    print("Puedes participar.")
else:
    print("No puedes participar.")
```

---

# 📌 ¿Cuándo utilizar `and`?

Utiliza `and` cuando todas las condiciones deban cumplirse.

Ejemplos:

- Tener entre 18 y 60 años.
- Obtener una nota entre 70 y 100.
- Tener una temperatura entre 20 y 30 grados.

---

# 💻 Ejercicios

Antes de consultar las soluciones, intenta resolver todos los ejercicios por tu cuenta.

La práctica es la mejor forma de aprender programación.

---

# 🎯 Lo aprendido

En este capítulo aprendiste:

- ✔ Qué es el operador lógico `and`.
- ✔ Cómo combinar dos condiciones.
- ✔ Cómo utilizar `and` junto con `if`.
- ✔ Cómo validar rangos de valores.

---

# 🚀 Siguiente capítulo

En el siguiente capítulo aprenderás el operador lógico `or`.

---

⭐ Si este proyecto te está ayudando, considera darle una estrella al repositorio.
