# ⚖️ Capítulo 5 - Comparadores y Condiciones

En este capítulo aprenderás a comparar valores utilizando los operadores de comparación de Python.

Estos operadores son la base de las estructuras condicionales (`if`, `elif` y `else`), ya que permiten tomar decisiones según el resultado de una comparación.

---

# 📚 Objetivos

Al finalizar este capítulo podrás:

- ✅ Comparar números.
- ✅ Utilizar los operadores de comparación.
- ✅ Comprender cuándo una condición es verdadera o falsa.
- ✅ Crear programas que respondan según la información ingresada por el usuario.

---

# 📂 Archivos del capítulo

| Archivo | Descripción |
|---------|-------------|
| `comparadores.py` | Ejemplos de operadores de comparación. |
| `Ejercicios.py` | Actividades para practicar. |
| `Soluciones.py` | Solución de los ejercicios. |
| `DesafioFinal.py` | Reto para reforzar lo aprendido. |

---

# 🤔 ¿Qué son los operadores de comparación?

Los operadores de comparación permiten comparar dos valores.

El resultado de una comparación siempre será:

- `True` (Verdadero)
- `False` (Falso)

Estas comparaciones son las que utilizan las estructuras `if`.

---

# 📚 Operadores de comparación

| Operador | Significado | Ejemplo |
|----------|-------------|---------|
| `==` | Igual que | `5 == 5` |
| `!=` | Diferente de | `5 != 3` |
| `>` | Mayor que | `10 > 4` |
| `<` | Menor que | `8 < 15` |
| `>=` | Mayor o igual que | `18 >= 18` |
| `<=` | Menor o igual que | `12 <= 20` |

---

# 💻 Ejemplo

```python
edad = int(input("¿Cuántos años tienes? "))

if edad == 18:
    print("Tienes exactamente 18 años.")
elif edad > 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
```

---

# 📌 ¿Qué devuelve una comparación?

```python
print(10 > 5)
```

Resultado

```
True
```

```python
print(10 < 5)
```

Resultado

```
False
```

---

# 💻 Ejercicios

Resuelve primero los ejercicios y después compara tus respuestas con el archivo `Soluciones.py`.

---

# 🎯 Lo aprendido

En este capítulo aprendiste:

- ✔ Los operadores de comparación.
- ✔ Cómo comparar números.
- ✔ Qué significa `True` y `False`.
- ✔ Cómo utilizar comparaciones dentro de un `if`.

---

# 🚀 Siguiente capítulo

En el siguiente capítulo aprenderás a combinar varias condiciones utilizando los operadores lógicos (`and`, `or` y `not`).

---

⭐ Si este proyecto te está ayudando, considera darle una estrella al repositorio.
