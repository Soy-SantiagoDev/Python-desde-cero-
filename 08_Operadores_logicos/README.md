# 🚫 Capítulo 8 - Operador Lógico `not`

En este capítulo aprenderás a utilizar el operador lógico `not`.

Este operador permite invertir el resultado de una condición. Si una condición es verdadera, `not` la convierte en falsa. Si una condición es falsa, `not` la convierte en verdadera.

---

# 📚 Objetivos

Al finalizar este capítulo podrás:

- ✅ Comprender cómo funciona el operador `not`.
- ✅ Invertir el resultado de una condición.
- ✅ Utilizar `not` junto con `if`.
- ✅ Crear programas con validaciones simples.

---

# 📂 Archivos del capítulo

| Archivo | Descripción |
|---------|-------------|
| `operador.py` | Introducción al operador `not`. |
| `Ejercicios.py` | Ejercicios para practicar. |
| `Soluciones.py` | Solución de los ejercicios. |
| `DesafioFinal.py` | Reto para reforzar lo aprendido. |

---

# 🤔 ¿Qué hace el operador `not`?

El operador `not` invierte el resultado de una condición.

Si una condición es verdadera, `not` la convierte en falsa.

Si una condición es falsa, `not` la convierte en verdadera.

---

# 💻 Ejemplo

```python
bloqueo = input("¿El usuario está bloqueado? (si/no): ")

if not bloqueo.lower() == "si":
    print("Tienes acceso.")
else:
    print("No tienes acceso.")
```

En este ejemplo:

- Si el usuario responde **"si"**, significa que está bloqueado y no podrá acceder.
- Si responde **"no"**, podrá ingresar al sistema.

---

# 📌 ¿Cuándo utilizar `not`?

Utiliza `not` cuando necesites comprobar que una condición **no** se cumpla.

Ejemplos:

- El usuario no está bloqueado.
- El producto no está agotado.
- El archivo no existe.

---

# 💻 Ejercicios

Resuelve primero los ejercicios por tu cuenta y luego revisa las soluciones.

---

# 🎯 Lo aprendido

En este capítulo aprendiste:

- ✔ Cómo funciona el operador `not`.
- ✔ Cómo invertir una condición.
- ✔ Cómo utilizar `not` en estructuras `if`.

---

# 🚀 Siguiente capítulo

En el siguiente capítulo aprenderás a utilizar condicionales con múltiples opciones mediante `elif`.

---

⭐ Si este proyecto te está ayudando, considera darle una estrella al repositorio.
