# 🔀 Capítulo 7 - Operador Lógico `or`

En este capítulo aprenderás a utilizar el operador lógico `or`.

Este operador permite comprobar varias condiciones y ejecutar un bloque de código cuando **al menos una de ellas es verdadera**.

Es muy utilizado cuando existen diferentes formas de cumplir un requisito.

---

# 📚 Objetivos

Al finalizar este capítulo podrás:

- ✅ Comprender cómo funciona el operador `or`.
- ✅ Combinar dos condiciones.
- ✅ Crear programas que acepten diferentes opciones.
- ✅ Utilizar `or` dentro de una estructura `if`.

---

# 📂 Archivos del capítulo

| Archivo | Descripción |
|---------|-------------|
| `operador.py` | Introducción al operador `or`. |
| `Ejercicios.py` | Actividades para practicar. |
| `Soluciones.py` | Solución de los ejercicios. |
| `DesafioFinal.py` | Reto para reforzar lo aprendido. |

---

# 🤔 ¿Qué hace el operador `or`?

El operador `or` une dos o más condiciones.

Para que una condición sea verdadera, **solo una de ellas debe cumplirse**.

---

# 💻 Ejemplo

```python
experiencia = int(input("¿Cuántos años de experiencia tienes? "))
titulo = input("¿Tienes título? (Sí o No): ")

if experiencia >= 5 or titulo == "Si":
    print("Puedes aplicar.")
else:
    print("No puedes aplicar.")
```

En este ejemplo una persona puede aplicar si:

- Tiene **5 años o más de experiencia**, **o**
- Tiene un **título profesional**.

No necesita cumplir ambas condiciones.

---

# 📌 ¿Cuándo utilizar `or`?

Utiliza `or` cuando una persona pueda cumplir un requisito de diferentes maneras.

Ejemplos:

- Tener experiencia o un título.
- Ser menor de edad o adulto mayor.
- Ser cliente VIP o tener un cupón de descuento.

---

# 💻 Ejercicios

Resuelve primero los ejercicios por tu cuenta y luego consulta el archivo `Soluciones.py`.

---

# 🎯 Lo aprendido

En este capítulo aprendiste:

- ✔ Cómo funciona el operador `or`.
- ✔ Cómo unir dos condiciones.
- ✔ Cómo crear programas con varias alternativas.

---

# 🚀 Siguiente capítulo

En el siguiente capítulo aprenderás a utilizar el operador lógico `not`.

---

⭐ Si este proyecto te está ayudando, considera darle una estrella al repositorio.
