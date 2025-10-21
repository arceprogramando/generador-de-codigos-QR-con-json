# Generador de Códigos QR con JSON

Herramienta para generar códigos QR a partir de datos en formato JSON.

## Descripción

Esta herramienta permite convertir datos JSON en imágenes de códigos QR de forma sencilla. Puede recibir los datos de tres formas diferentes:
- Archivo JSON
- Cadena JSON directamente
- Diccionario Python (cuando se usa como módulo)

## Requisitos

- Python 3.6 o superior
- Dependencias listadas en `requirements.txt`

## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/arceprogramando/generador-de-codigos-QR-con-json.git
cd generador-de-codigos-QR-con-json

# Instalar dependencias
pip install -r requirements.txt
```

## Uso

### Desde línea de comandos

#### Opción 1: Usando un archivo JSON

```bash
python generador_qr.py ejemplo.json
```

Esto generará un archivo `qr_code.png` con los datos del JSON.

#### Opción 2: Usando una cadena JSON directamente

```bash
python generador_qr.py '{"nombre": "Juan", "edad": 30}'
```

#### Opción 3: Especificar el nombre del archivo de salida

```bash
python generador_qr.py ejemplo.json mi_codigo_qr.png
```

### Como módulo Python

```python
from generador_qr import generar_qr_desde_json

# Con un archivo JSON
generar_qr_desde_json("datos.json", "output.png")

# Con una cadena JSON
generar_qr_desde_json('{"clave": "valor"}', "output.png")

# Con un diccionario Python
datos = {"nombre": "María", "ciudad": "Buenos Aires"}
generar_qr_desde_json(datos, "output.png")
```

## Ejemplo

El repositorio incluye un archivo `ejemplo.json` con datos de ejemplo:

```json
{
  "nombre": "Juan Pérez",
  "email": "juan.perez@ejemplo.com",
  "telefono": "+54 11 1234-5678",
  "empresa": "Tech Solutions",
  "sitio_web": "https://ejemplo.com"
}
```

Para generar un código QR con estos datos:

```bash
python generador_qr.py ejemplo.json
```

## Características

- ✓ Soporte para archivos JSON
- ✓ Soporte para cadenas JSON directas
- ✓ Soporte para diccionarios Python
- ✓ Codificación UTF-8 para caracteres especiales
- ✓ Manejo de errores robusto
- ✓ Personalización del nombre del archivo de salida

## Licencia

Este proyecto está bajo la licencia MIT.