# Generador de Códigos QR con JSON y Texto Plano

Herramienta para generar códigos QR a partir de datos en formato JSON o texto plano.

## Descripción

Esta herramienta permite convertir datos JSON o texto plano en imágenes de códigos QR de forma sencilla. Puede recibir los datos de múltiples formas:
- Archivo JSON
- Cadena JSON directamente
- Diccionario Python (cuando se usa como módulo)
- **NUEVO:** Texto plano (números, frases, etc.)
- **NUEVO:** Archivos de texto plano

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

#### Opción 3: Usando texto plano (NUEVO)

```bash
# Con un número
python generador_qr.py 31656839

# Con texto
python generador_qr.py "Hola Mundo"

# Con un archivo de texto
python generador_qr.py mi_archivo.txt
```

#### Opción 4: Especificar el nombre del archivo de salida

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

# Con texto plano (NUEVO)
generar_qr_desde_json("31656839", "numero.png")
generar_qr_desde_json("Hola Mundo", "texto.png")
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
- ✓ **NUEVO:** Soporte para texto plano (números, frases, etc.)
- ✓ **NUEVO:** Soporte para archivos de texto plano
- ✓ **NUEVO:** Detección automática del tipo de contenido
- ✓ Codificación UTF-8 para caracteres especiales
- ✓ Manejo de errores robusto
- ✓ Personalización del nombre del archivo de salida

## Licencia

Este proyecto está bajo la licencia MIT.