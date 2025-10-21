#!/bin/bash
# Script de demostración del generador de códigos QR

echo "==================================="
echo "DEMOSTRACIÓN DEL GENERADOR DE QR"
echo "==================================="
echo ""

echo "1. Generando QR desde archivo JSON (ejemplo.json)..."
python generador_qr.py ejemplo.json demo_archivo.png
echo ""

echo "2. Generando QR desde cadena JSON con información de contacto..."
python generador_qr.py '{"tipo":"contacto","nombre":"María García","tel":"+54 9 11 5555-1234"}' demo_contacto.png
echo ""

echo "3. Generando QR desde cadena JSON con URL..."
python generador_qr.py '{"tipo":"url","sitio":"https://github.com/arceprogramando","descripcion":"Perfil de GitHub"}' demo_url.png
echo ""

echo "4. Generando QR desde cadena JSON con datos de producto..."
python generador_qr.py '{"producto":"Notebook Dell XPS 15","precio":2500,"moneda":"USD","stock":5}' demo_producto.png
echo ""

echo "==================================="
echo "Demostración completada!"
echo "Archivos generados:"
ls -lh demo_*.png 2>/dev/null | awk '{print "  -", $9, "(" $5 ")"}'
echo "==================================="
