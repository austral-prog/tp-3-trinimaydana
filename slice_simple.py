def slice_simple():
    texto = "Awesome"
    medio = int(len(texto)/2)
    # Código a implementar, se debe utilizar la variable 'texto' para resolver el ejercicio.
    # No se debe modificar la definición de la función, ni ingresar otro valor mediante input

    print(texto.lower()[0:3])
    print(texto.lower()[medio-1:medio+2])
    print(texto.lower()[0:5]+texto.lower()[-2:])

    # Código a implementar, se debe utilizar la variable 'texto' para resolver el ejercicio.
    # No se debe modificar la definición de la función, ni ingresar otro valor mediante input.




# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_simple_test.py` o `python tp3_slice_simple_test.py`
