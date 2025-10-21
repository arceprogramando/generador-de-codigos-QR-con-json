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
    Genera un código QR a partir de datos JSON o texto plano.
    
    Args:
        json_input: Puede ser una cadena JSON, un diccionario Python, una ruta a un archivo JSON, o texto plano
        output_path: Ruta donde se guardará la imagen QR generada
    
    Returns:
        str: Ruta del archivo de imagen generado
    """
    try:
        # Si es una ruta de archivo, leer el contenido
        if isinstance(json_input, str) and Path(json_input).is_file():
            with open(json_input, 'r', encoding='utf-8') as f:
                content = f.read()
                try:
                    data = json.loads(content)
                    json_string = json.dumps(data, ensure_ascii=False)
                    data_type = "JSON desde archivo"
                except json.JSONDecodeError:
                    # Si no es JSON válido, usar el contenido como texto plano
                    json_string = content
                    data_type = "Texto plano desde archivo"
        # Si es una cadena, intentar validarla como JSON primero
        elif isinstance(json_input, str):
            try:
                data = json.loads(json_input)
                json_string = json.dumps(data, ensure_ascii=False)
                data_type = "JSON"
            except json.JSONDecodeError:
                # Si no es JSON válido, usar como texto plano
                json_string = json_input
                data_type = "Texto plano"
        # Si es un diccionario, convertirlo a JSON
        elif isinstance(json_input, dict):
            json_string = json.dumps(json_input, ensure_ascii=False)
            data_type = "Diccionario Python"
        else:
            raise ValueError("El input debe ser una cadena JSON, un diccionario, una ruta a un archivo, o texto plano")
        
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
        print(f"  Tipo de datos: {data_type}")
        print(f"  Datos codificados: {json_string[:100]}{'...' if len(json_string) > 100 else ''}")
        
        return output_path
    
    except Exception as e:
        print(f"✗ Error al generar código QR: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    """Función principal para uso desde línea de comandos"""
    if len(sys.argv) < 2:
        print("Uso: python generador_qr.py <archivo_json|cadena_json|texto_plano> [output_path]")
        print("\nEjemplos:")
        print("  python generador_qr.py datos.json")
        print('  python generador_qr.py \'{"nombre": "Juan", "edad": 30}\' mi_qr.png')
        print("  python generador_qr.py 31656839")
        print("  python generador_qr.py 'Hola Mundo' mi_texto.png")
        print("  python generador_qr.py datos.json codigo_salida.png")
        sys.exit(1)
    
    json_input = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else "qr_code.png"
    
    generar_qr_desde_json(json_input, output_path)


if __name__ == "__main__":
    main()
