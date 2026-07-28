# 🔀 Capítulo 4 - Condicionales `if` y `else`

Hasta ahora nuestros programas ejecutaban todas las instrucciones en el mismo orden.

En este capítulo aprenderás a tomar decisiones utilizando las estructuras condicionales `if` y `else`.

Gracias a ellas, un programa puede realizar diferentes acciones dependiendo de la información ingresada por el usuario.

---

# 📚 Objetivos

Al finalizar este capítulo podrás:

- ✅ Comprender qué es una condición.
- ✅ Utilizar la estructura `if`.
- ✅ Utilizar la estructura `else`.
- ✅ Comparar valores.
- ✅ Convertir datos con `int()`.
- ✅ Crear programas que tomen decisiones.

---

# 📂 Archivos del capítulo

| Archivo | Descripción |
|---------|-------------|
| `if_else.py` | Introducción a los condicionales. |
| `Ejercicios.py` | Actividades para practicar. |
| `Soluciones.py` | Solución de los ejercicios. |
| `DesafioFinal.py` | Reto para aplicar lo aprendido. |

---

# 🤔 ¿Qué es un condicional?

Un condicional permite que un programa tome decisiones.

Dependiendo de si una condición es verdadera o falsa, Python ejecutará un bloque de código diferente.

---

# 📌 La estructura `if`

```python
edad = 20

if edad >= 18:
    print("Eres mayor de edad.")
```

Si la condición es verdadera, Python ejecutará el código que está indentado debajo del `if`.

---

# 📌 La estructura `else`

El bloque `else` se ejecuta cuando la condición del `if` es falsa.

```python
edad = 15

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
```

Resultado

```
Eres menor de edad.
```

---

# 📌 ¿Por qué usamos `int()`?

La función `input()` devuelve un texto (`str`).

Para comparar edades o realizar operaciones matemáticas, debemos convertir ese texto a un número entero.

```python
edad = int(input("¿Cuál es tu edad? "))
```

De esta forma podremos hacer comparaciones como:

```python
if edad >= 18:
```

---

# 📚 Operadores de comparación utilizados

| Operador | Significado |
|----------|-------------|
| `>` | Mayor que |
| `<` | Menor que |
| `>=` | Mayor o igual que |
| `<=` | Menor o igual que |
| `==` | Igual que |
| `!=` | Diferente de |

---

# 💻 Ejercicios

Resuelve los ejercicios antes de consultar las soluciones.

Aprender a programar requiere mucha práctica.

---

# 🎯 Lo aprendido

En este capítulo aprendiste:

- ✔ Qué es un condicional.
- ✔ Cómo utilizar `if`.
- ✔ Cómo utilizar `else`.
- ✔ Cómo comparar números.
- ✔ Cómo convertir texto a enteros con `int()`.

---

# 🚀 Siguiente capítulo

En el siguiente capítulo conocerás los operadores de comparación con más detalle y aprenderás cómo utilizarlos en diferentes situaciones.

---

⭐ Si este proyecto te está ayudando, considera darle una estrella al repositorio.
