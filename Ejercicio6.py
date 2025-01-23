def mostrar_menu():
    opciones = [
        "1. Añadir alumno/a", "2. Eliminar alumno/a", "3. Mostrar alumno/a",
        "4. Listar todo el alumnado", "5. Listar alumnado aprobado", "6. Terminar"
    ]
    print("\nMenú de opciones:")
    print("\n".join(opciones))

def gestionar_alumnos():
    base_datos = {}
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            nif = input("Ingrese el NIF: ")
            if nif in base_datos:
                print("Este NIF ya está registrado.")
                continue
            base_datos[nif] = {
                "nombre": input("Nombre: "), "apellidos": input("Apellidos: "),
                "telefono": input("Teléfono: "), "correo": input("Correo: "),
                "aprobado": input("¿Aprobado? (s/n): ").strip().lower() == 's'
            }
        elif opcion == "2":
            base_datos.pop(input("Ingrese el NIF: "), print("No encontrado."))
        elif opcion == "3":
            nif = input("Ingrese el NIF: ")
            print(base_datos.get(nif, "No encontrado."))
        elif opcion == "4":
            for nif, datos in base_datos.items():
                print(f"NIF: {nif} - Nombre: {datos['nombre']} {datos['apellidos']}")
        elif opcion == "5":
            for nif, datos in base_datos.items():
                if datos["aprobado"]:
                    print(f"NIF: {nif} - Nombre: {datos['nombre']} {datos['apellidos']}")
        elif opcion == "6":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

gestionar_alumnos()