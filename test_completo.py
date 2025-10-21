#!/usr/bin/env python3
"""
Script de prueba completo para el generador de códigos QR
Incluye pruebas para JSON y texto plano
"""

from generador_qr import generar_qr_desde_json
import os
import tempfile

def test_completo():
    """Prueba completa del generador con todas las funcionalidades"""
    print("=== Ejecutando pruebas completas del generador de QR ===\n")
    
    # Test 1: Con un diccionario Python
    print("Test 1: Generando QR desde diccionario Python...")
    datos_dict = {
        "usuario": "test_user",
        "id": 12345,
        "activo": True
    }
    output1 = "test_dict.png"
    generar_qr_desde_json(datos_dict, output1)
    assert os.path.exists(output1), "Error: El archivo no fue creado"
    print(f"✓ Archivo creado: {output1}\n")
    
    # Test 2: Con una cadena JSON
    print("Test 2: Generando QR desde cadena JSON...")
    json_string = '{"mensaje": "Hola Mundo", "código": "ABC123"}'
    output2 = "test_string.png"
    generar_qr_desde_json(json_string, output2)
    assert os.path.exists(output2), "Error: El archivo no fue creado"
    print(f"✓ Archivo creado: {output2}\n")
    
    # Test 3: Con texto plano (número)
    print("Test 3: Generando QR desde número...")
    numero = "31656839"
    output3 = "test_numero.png"
    generar_qr_desde_json(numero, output3)
    assert os.path.exists(output3), "Error: El archivo no fue creado"
    print(f"✓ Archivo creado: {output3}\n")
    
    # Test 4: Con texto plano (string)
    print("Test 4: Generando QR desde texto plano...")
    texto = "Este es un texto de prueba con acentos: María, José, Ñoño"
    output4 = "test_texto.png"
    generar_qr_desde_json(texto, output4)
    assert os.path.exists(output4), "Error: El archivo no fue creado"
    print(f"✓ Archivo creado: {output4}\n")
    
    # Test 5: Con archivo JSON existente
    print("Test 5: Generando QR desde archivo JSON...")
    output5 = "test_archivo_json.png"
    generar_qr_desde_json("ejemplo.json", output5)
    assert os.path.exists(output5), "Error: El archivo no fue creado"
    print(f"✓ Archivo creado: {output5}\n")
    
    # Test 6: Con archivo de texto plano
    print("Test 6: Generando QR desde archivo de texto...")
    output6 = "test_archivo_texto.png"
    generar_qr_desde_json("texto_prueba.txt", output6)
    assert os.path.exists(output6), "Error: El archivo no fue creado"
    print(f"✓ Archivo creado: {output6}\n")
    
    print("🎉 Todas las pruebas pasaron exitosamente!")
    print("\nArchivos generados:")
    archivos = [output1, output2, output3, output4, output5, output6]
    for archivo in archivos:
        if os.path.exists(archivo):
            size = os.path.getsize(archivo)
            print(f"  - {archivo} ({size} bytes)")

if __name__ == "__main__":
    test_completo()