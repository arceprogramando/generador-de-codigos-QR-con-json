#!/usr/bin/env python3
"""
Generador de códigos QR a partir de datos JSON
Este script toma datos en formato JSON y genera una imagen QR con esa información.
"""

import json
import sys
import qrcode
from pathlib import Path


def generar_qr_desde_json(json_input, output_path="qr_code.png"):
    """
    Genera un código QR a partir de datos JSON.
    
    Args:
        json_input: Puede ser una cadena JSON, un diccionario Python, o una ruta a un archivo JSON
        output_path: Ruta donde se guardará la imagen QR generada
    
    Returns:
        str: Ruta del archivo de imagen generado
    """
    try:
        # Si es una ruta de archivo, leer el contenido
        if isinstance(json_input, str) and Path(json_input).is_file():
            with open(json_input, 'r', encoding='utf-8') as f:
                data = json.load(f)
                json_string = json.dumps(data, ensure_ascii=False)
        # Si es una cadena JSON, validarla
        elif isinstance(json_input, str):
            data = json.loads(json_input)
            json_string = json.dumps(data, ensure_ascii=False)
        # Si es un diccionario, convertirlo a JSON
        elif isinstance(json_input, dict):
            json_string = json.dumps(json_input, ensure_ascii=False)
        else:
            raise ValueError("El input debe ser una cadena JSON, un diccionario o una ruta a un archivo JSON")
        
        # Crear el código QR
        qr = qrcode.QRCode(
            version=1,  # Controla el tamaño del código QR
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        
        qr.add_data(json_string)
        qr.make(fit=True)
        
        # Crear la imagen
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(output_path)
        
        print(f"✓ Código QR generado exitosamente: {output_path}")
        print(f"  Datos codificados: {json_string[:100]}{'...' if len(json_string) > 100 else ''}")
        
        return output_path
    
    except json.JSONDecodeError as e:
        print(f"✗ Error al decodificar JSON: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"✗ Error al generar código QR: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    """Función principal para uso desde línea de comandos"""
    if len(sys.argv) < 2:
        print("Uso: python generador_qr.py <archivo_json|cadena_json> [output_path]")
        print("\nEjemplos:")
        print("  python generador_qr.py datos.json")
        print('  python generador_qr.py \'{"nombre": "Juan", "edad": 30}\' mi_qr.png')
        print("  python generador_qr.py datos.json codigo_salida.png")
        sys.exit(1)
    
    json_input = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else "qr_code.png"
    
    generar_qr_desde_json(json_input, output_path)


if __name__ == "__main__":
    main()
