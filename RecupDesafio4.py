class Aplicacion:
    def __init__(self, nombre, version):
        """
        El nombre es una cadena,
        La versión es una cadena con el formato x.y.z en donde x, y, z valen 1-9 únicamente
        La versión mínima es 1.0.0, y la máxima 9.9.9
        """
        self.nombre = nombre
        self.version = version

class Contacto:
    def __init__(self, nombre, numero):
        self.nombre = nombre
        self.numero = numero

class Celular:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.aplicaciones = []
        self.contactos = []

    def instalar_aplicacion(self, aplicacion):
        """
        Agrega una aplicación a la lista de aplicaciones del celular.
        """
        self.aplicaciones.append(aplicacion)

    def agregar_contacto(self, contacto):
        """
        Agrega un contacto a la lista de contactos del celular.
        """
        self.contactos.append(contacto)

    def mostrar_aplicaciones(self):
        """
        Muestra todas las aplicaciones instaladas en el celular con el formato Nombre vVersion.
        Ejemplo Instagram v1.2.3
        """
        for aplicacion in self.aplicaciones:
            print(f"{aplicacion.nombre} v{aplicacion.version}")

    def mostrar_contactos(self):
        """
        Muestra todos los contactos guardados en el celular con el formato Nombre - Numero
        """
        for contacto in self.contactos:
            print(f"{contacto.nombre} - {contacto.numero}")

    def actualizar_aplicacion(self, aplicacion, nueva_version):
        """
        Actualiza la versión de una aplicación específica.
        Si la aplicación no está instalada en el celular, se debe manejar ese caso de manera adecuada.
        """
        if aplicacion in self.aplicaciones:
            numero=self.aplicaciones.index(aplicacion)
            aplicacion.version=nueva_version
            self.aplicaciones[numero]=aplicacion
            print(f"La aplicación se actualizó con éxito! v{aplicacion.version}")
        else:
             print(f"La aplicación {aplicacion.nombre} no se encuentra instalada")

    def limpiar_aplicaciones(self, version_minima):
        """
        Elimina las aplicaciones que tengan una versión inferior a la especificada.
        Las versiones serán siempre del tipo x.y.z, en donde x, y, z pueden valer un solo dígito 1-9.
        La mínima versión posible será la 1.0.0, y la máxima 9.9.9
        """
        for aplicacion in self.aplicaciones:
           
            if (int(aplicacion.version[0])<int(version_minima[0])):
                print(int(version_minima[0]))
                self.aplicaciones.remove(aplicacion)
                print(f"La aplicación {aplicacion.nombre} se eliminó correctamente")
            else:
                print(f"La aplicación no tiene verisón inferior a v{version_minima}")

    def eliminar_contacto(self, contacto):
        """
        Elimina un contacto de la lista de contactos del celular.
        Si el contacto no existe en la lista de contactos del celular, se debe manejar ese caso de manera adecuada.
        """
        if contacto in self.contactos:
            self.contactos.remove(contacto)
            print(f"El contacto {contacto.nombre} se eliminó correctamente")
        else:
             print(f"El contacto {contacto.nombre} no existe en la lista del celular")


# Tarea 1: Instanciar un objeto Celular, dos Aplicaciones y dos Contactos.

aplicacion1=Aplicacion("Instegram","2.3.4")
aplicacion2=Aplicacion("Facebook","0.4.5")

contacto1=Contacto("Carlos","15309032")
contacto2=Contacto("Oscar","15255595")

celular1=Celular("Samsung","xtz")


# Tarea 2: Instalar las dos aplicaciones en el celular.

celular1.instalar_aplicacion(aplicacion1)
celular1.instalar_aplicacion(aplicacion2)

# # Tarea 3: Agregar los dos contactos al celular.

celular1.agregar_contacto(contacto1)
celular1.agregar_contacto(contacto2)

# # Tarea 4: Mostrar todas las aplicaciones instaladas en el celular.

celular1.mostrar_aplicaciones()

# # Tarea 5: Mostrar todos los contactos guardados en el celular.

celular1.mostrar_contactos()

# # Tarea 6: Actualizar la versión de una de las aplicaciones instaladas en el celular.

celular1.actualizar_aplicacion(aplicacion1,"5.6.7")

# # Tarea 7: Eliminar uno de los contactos del celular.

celular1.eliminar_contacto(contacto1)

# # Tarea 8: Eliminar aplicaciones con versiones anteriores a la 1.5.0

celular1.limpiar_aplicaciones("1.5.0")