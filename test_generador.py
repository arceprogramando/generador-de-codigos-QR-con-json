#!/usr/bin/env python3
"""
Script de prueba para el generador de códigos QR
"""

from generador_qr import generar_qr_desde_json
import os

def test_basico():
    """Prueba básica del generador"""
    print("=== Ejecutando pruebas del generador de QR ===\n")
    
    # Test 1: Con un diccionario Python
    print("Test 1: Generando QR desde diccionario Python...")
    datos_dict = {
        "usuario": "test_user",
        "id": 12345,
        "activo": True
    }
    output1 = "/tmp/test_dict.png"
    generar_qr_desde_json(datos_dict, output1)
    assert os.path.exists(output1), "Error: El archivo no fue creado"
    print(f"✓ Archivo creado: {output1}\n")
    
    # Test 2: Con una cadena JSON
    print("Test 2: Generando QR desde cadena JSON...")
    json_string = '{"mensaje": "Hola Mundo", "código": "ABC123"}'
    output2 = "/tmp/test_string.png"
    generar_qr_desde_json(json_string, output2)
    assert os.path.exists(output2), "Error: El archivo no fue creado"
    print(f"✓ Archivo creado: {output2}\n")
    
    # Test 3: Con un archivo JSON
    print("Test 3: Generando QR desde archivo JSON...")
    output3 = "/tmp/test_file.png"
    generar_qr_desde_json("ejemplo.json", output3)
    assert os.path.exists(output3), "Error: El archivo no fue creado"
    print(f"✓ Archivo creado: {output3}\n")
    
    print("=== Todas las pruebas pasaron exitosamente ===")

if __name__ == "__main__":
    test_basico()
