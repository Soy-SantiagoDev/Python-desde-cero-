# ⛔ Capítulo 13 - La instrucción `break`

En este capítulo aprenderás a utilizar la instrucción `break`.

Hasta ahora, los ciclos `while` terminaban cuando su condición dejaba de cumplirse. Con `break`, podemos finalizar un ciclo inmediatamente cuando ocurre una condición específica.

---

# 📚 Objetivos

Al finalizar este capítulo podrás:

- ✅ Comprender cómo funciona `break`.
- ✅ Finalizar un ciclo antes de tiempo.
- ✅ Utilizar `break` junto con `while`.
- ✅ Crear programas interactivos.

---

# 📂 Archivos del capítulo

| Archivo | Descripción |
|---------|-------------|
| `break.py` | Introducción a la instrucción `break`. |
| `Ejercicios.py` | Ejercicios para practicar. |
| `Soluciones.py` | Solución de los ejercicios. |
| `DesafioFinal.py` | Reto para reforzar lo aprendido. |

---

# 🤔 ¿Qué hace `break`?

La instrucción `break` detiene un ciclo inmediatamente.

Cuando Python encuentra un `break`, sale del ciclo y continúa ejecutando el resto del programa.

---

# 💻 Ejemplo

```python
while True:

    palabra = input("Escribe la palabra salir para terminar: ")

    if palabra == "salir":
        print("Programa finalizado.")
        break

    print("Escribiste la palabra:", palabra)
```

---

# 📌 ¿Cómo funciona?

1. El ciclo comienza con `while True`.
2. El usuario escribe una palabra.
3. Si escribe `salir`, el programa ejecuta `break`.
4. El ciclo termina inmediatamente.

---

# 💻 Ejercicios

Resuelve los ejercicios antes de consultar las soluciones.

---

# 🎯 Lo aprendido

En este capítulo aprendiste:

- ✔ Qué hace `break`.
- ✔ Cómo detener un ciclo.
- ✔ Cómo utilizar `break` dentro de un `while`.

---

# 🚀 Siguiente capítulo

En el siguiente capítulo aprenderás a utilizar `continue` para saltar una iteración de un ciclo sin finalizarlo.

---

⭐ Si este proyecto te está ayudando, considera darle una estrella al repositorio.
