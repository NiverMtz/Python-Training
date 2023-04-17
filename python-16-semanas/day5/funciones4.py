def describir_persona(nombre, *args, **kwargs):
    print(f"Características de {nombre}:")
    for k, w in kwargs.items():
        print(f"{k}: {w}")


describir_persona("María", color_ojos="azules", color_pelo="rubio")
