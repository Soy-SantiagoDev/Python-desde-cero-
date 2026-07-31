# 🔀 Capítulo 7 - Operador Lógico `or`

En este capítulo aprenderás a utilizar el operador lógico `or`.

A diferencia de `and`, el operador `or` solo necesita que **una de las condiciones sea verdadera** para ejecutar un bloque de código.

---

# 📚 Objetivos

Al finalizar este capítulo podrás:

- ✅ Comprender cómo funciona el operador `or`.
- ✅ Combinar varias condiciones.
- ✅ Crear programas con diferentes alternativas.
- ✅ Utilizar `or` junto con `if`.

---

# 📂 Archivos del capítulo

| Archivo | Descripción |
|---------|-------------|
| `operador.py` | Introducción al operador `or`. |
| `Ejercicios.py` | Ejercicios para practicar. |
| `Soluciones.py` | Solución de los ejercicios. |
| `DesafioFinal.py` | Reto para aplicar lo aprendido. |

---

# 🤔 ¿Qué hace el operador `or`?

El operador `or` une dos o más condiciones.

Basta con que **una de ellas sea verdadera** para que el resultado sea verdadero.

---

# 💻 Ejemplo

```python
experiencia = int(input("¿Cuántos años de experiencia tienes? "))
titulo = input("¿Tienes título? (sí o no): ").lower()

if experiencia >= 5 or titulo == "sí":
    print("Puedes aplicar.")
else:
    print("No puedes aplicar.")
```

En este ejemplo, una persona puede aplicar si:

- Tiene **5 años o más de experiencia**, **o**
- Tiene un **título profesional**.

No es necesario cumplir ambas condiciones.

---

# 📌 ¿Cuándo utilizar `or`?

Utiliza `or` cuando exista más de una forma de cumplir un requisito.

Ejemplos:

- Tener experiencia o un título.
- Ser menor de 18 o mayor de 60.
- Tener descuento o ser cliente VIP.

---

# 💻 Ejercicios

Resuelve primero los ejercicios y luego revisa las soluciones.

---

# 🎯 Lo aprendido

En este capítulo aprendiste:

- ✔ Qué es el operador lógico `or`.
- ✔ Cómo combinar condiciones.
- ✔ Cómo utilizar `or` en estructuras `if`.

---

# 🚀 Siguiente capítulo

En el siguiente capítulo aprenderás el operador lógico `not`.

---

⭐ Si este proyecto te está ayudando, considera darle una estrella al repositorio.
