import re

print("Iniciando escaneo del binario de Blood Strike...")

# Buscar strings legibles dentro del binario pesado
with open(" BloodStrikeBinary", "rb") as f:
    data = f.read()

# Buscar palabras clave típicas de apuntado y renderizado
keywords = [b"Aim", b"Lock", b"Glow", b"Renderer", b"Striker", b"Recoil"]
found = []

for kw in keywords:
    matches = re.finditer(kw, data)
    for m in matches:
        offset = m.start()
        # Intentar extraer la cadena de texto completa
        start = max(0, offset - 10)
        end = min(len(data), offset + 30)
        chunk = data[start:end]
        # Limpiar caracteres no legibles
        clean_text = "".join([chr(b) if 32 <= b < 127 else "." for b in chunk])
        found.append(f"Offset aproximado: {hex(offset)} | Contexto: {clean_text}")

# Guardar los resultados en un archivo de texto
with open("resultados_bloodstrike.txt", "w") as out:
    out.write("\n".join(found))

print("¡Escaneo finalizado con éxito! Resultados guardados en resultados_bloodstrike.txt")
