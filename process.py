#!/usr/bin/env python3
import cgi
import random
import math

# Obtener los datos del formulario
form = cgi.FieldStorage()
number = int(form.getvalue("number", 0))
text = form.getvalue("text", "")

# Número par o impar y cálculo respectivo
if number % 2 == 0:
    num_result = f"The number {number} is even. Its square root is {math.sqrt(number):.2f}."
else:
    num_result = f"The number {number} is odd. Its cube is {number ** 3}."

# Convertir texto a binario y contar vocales
binary_text = ' '.join(format(ord(char), '08b') for char in text)
vowel_count = sum(1 for char in text.lower() if char in "aeiou")

# Juego de la caza del tesoro
secret_number = random.randint(1, 100)
attempts = []
found = False

for i in range(1, 6):  # 5 intentos
    guess = random.randint(1, 100)
    if guess == secret_number:
        found = True
        attempts.append(f"Attempt {i}: {guess} (Correct!)")
        break
    elif guess > secret_number:
        attempts.append(f"Attempt {i}: {guess} (Too high!)")
    else:
        attempts.append(f"Attempt {i}: {guess} (Too low!)")

treasure_result = "You found the treasure in {} attempts!".format(i) if found else "You did not find the treasure."

# Mostrar los resultados en la página PHP
print("Content-type: text/html\n")
print("<html><body>")
print("<h2>Treasure Hunt Results</h2>")
print(f"<p><b>Number Puzzle:</b> {num_result}</p>")
print(f"<p><b>Text Puzzle:</b> Binary: {binary_text} | Vowel Count: {vowel_count}</p>")
print("<p><b>Treasure Hunt:</b></p>")
print("<ul>")
for attempt in attempts:
    print(f"<li>{attempt}</li>")
print("</ul>")
print(f"<p>{treasure_result}</p>")
print("</body></html>")
