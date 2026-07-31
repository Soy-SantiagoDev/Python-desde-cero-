# ⏭️ Capítulo 14 - La instrucción `continue`

En este capítulo aprenderás a utilizar la instrucción `continue`.

Mientras que `break` finaliza completamente un ciclo, `continue` hace que el programa omita la iteración actual y continúe con la siguiente.

Es una herramienta muy útil cuando queremos ignorar ciertos casos sin detener el ciclo.

---

# 📚 Objetivos

Al finalizar este capítulo podrás:

- ✅ Comprender cómo funciona `continue`.
- ✅ Saltar una iteración de un ciclo.
- ✅ Utilizar `continue` junto con `while`.
- ✅ Crear programas con condiciones más específicas.

---

# 📂 Archivos del capítulo

| Archivo | Descripción |
|---------|-------------|
| `continue.py` | Introducción a la instrucción `continue`. |
| `Ejercicios.py` | Ejercicios para practicar. |
| `Soluciones.py` | Solución de los ejercicios. |
| `DesafioFinal.py` | Reto para reforzar lo aprendido. |

---

# 🤔 ¿Qué hace `continue`?

La instrucción `continue` hace que Python omita el resto del código de la iteración actual y pase inmediatamente a la siguiente.

El ciclo no termina; simplemente continúa con la siguiente repetición.

---

# 💻 Ejemplo

```python
contador = 0

while contador < 5:
    contador += 1

    if contador == 3:
        continue

    print(f"Repetición número {contador}")
```

Resultado:

```
Repetición número 1
Repetición número 2
Repetición número 4
Repetición número 5
```

Observa que el número **3** no se imprime porque esa iteración fue omitida.

---

# 💻 Ejercicios

Resuelve los ejercicios antes de consultar las soluciones.

---

# 🎯 Lo aprendido

En este capítulo aprendiste:

- ✔ Qué hace `continue`.
- ✔ Cómo omitir una iteración.
- ✔ Cómo utilizar `continue` dentro de un ciclo.

---

# 🚀 Siguiente capítulo

En el siguiente capítulo aprenderás a utilizar el ciclo `for`.

---

⭐ Si este proyecto te está ayudando, considera darle una estrella al repositorio.
