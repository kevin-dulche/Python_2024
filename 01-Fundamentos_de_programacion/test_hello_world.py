import unittest
import subprocess

class TestMiPrograma(unittest.TestCase):
    def test_salida_programa(self):

        ruta_programa = "04-practica.py" # Ruta al programa a probar

        # Ejecuta el programa y captura su salida
        resultado = subprocess.run(
            ["python", ruta_programa], capture_output=True, text=True
        )
        # Salida esperada
        salida_esperada = (
            "Te doy la bienvenida al Coding Playground\n"
            "Mi primer print\n"
            "30\n"
        )
        # Compara la salida del programa con la esperada
        self.assertEqual(resultado.stdout, salida_esperada)

def test_main():
    unittest.main()


if __name__ == "__main__":
    test_main()