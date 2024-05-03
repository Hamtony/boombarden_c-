Integrantes:
Tomas Alonso Pastor Salazar
Diego Armando Flores Carrizales
Antonio Francisco Datto Aponte

Projecto:
Una calculadora implementada con antlr4 y python que reciba de input formato de texto y se transforme a un arbol de antlr y recorrerlo para resolver la operacion compuesta.
El input agrega en un archivo como el input.txt y se especifica como argumento corriendo el archivo Driver.py.

El programa puede realizar las siguientes operaciones:
- suma
- resta
- multiplicacion
- division
- modulo (resto)
- potencia
- raiz cuadrada
- factorial
- valor absoluto

Ejemplos de uso:

input:
+ | - (+ 5 (* 4.7 3)) (- (^ 3 2) !4) | 100
output:
143.1

input:
% (+ * + >81 1 0.5 | -9 |) 5
output:
4.0