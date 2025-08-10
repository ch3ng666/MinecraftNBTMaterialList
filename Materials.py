import nbtlib
from collections import Counter
import os


def listar_materiales_y_entidades(ruta_nbt):
    estructura = nbtlib.load(ruta_nbt)

    palette = estructura["palette"]
    indice_a_bloque = {i: bloque["Name"] for i, bloque in enumerate(palette)}

    contador_bloques = Counter()
    for bloque in estructura["blocks"]:
        state = bloque["state"]
        nombre = indice_a_bloque[state]
        if nombre != "minecraft:air":
            contador_bloques[nombre] += 1

    contador_entidades = Counter()
    if "entities" in estructura:
        for entidad in estructura["entities"]:
            nombre_entidad = entidad["nbt"]["id"]
            contador_entidades[nombre_entidad] += 1

    # Crear archivo txt con el mismo nombre que el nbt
    nombre_txt = os.path.splitext(ruta_nbt)[0] + ".txt"
    with open(nombre_txt, "w", encoding="utf-8") as f:
        f.write("=== Materials ===\n")
        for bloque, cantidad in contador_bloques.most_common():
            f.write(f"{bloque}: {cantidad}\n")

        if contador_entidades:
            f.write("\n=== Entities ===\n")
            for entidad, cantidad in contador_entidades.most_common():
                f.write(f"{entidad}: {cantidad}\n")

    print(f"File Created: {nombre_txt}")


if __name__ == "__main__":
    archivo = input("NBT File Name (e.g. structure.nbt): ").strip()
    if not archivo.endswith(".nbt"):
        archivo = archivo + ".nbt"
    listar_materiales_y_entidades(archivo)
    input("\nPress Enter to exit...")
