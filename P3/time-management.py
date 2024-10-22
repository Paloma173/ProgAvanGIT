import re

class Time:
    """
    Clase que representa una hora en formato AM/PM o de 24 horas.

    Atributos de clase:
    TIME_FORMATS (tuple): Formatos de hora válidos ("AM", "PM", "24 HOURS").
    time_count (int): Contador de objetos Time creados.

    Atributos de instancia:
    hours (int): Almacena las horas.
    minutes (int): Almacena los minutos.
    seconds (int): Almacena los segundos.
    format (str): Almacena el formato de la hora ("AM", "PM" o "24 HOURS").
    """

    TIME_FORMATS = ("AM", "PM", "24 HOURS")
    time_count = 0  # Contador de objetos Time creados

    def __init__(self):
        """
        Inicializa los atributos de la clase Time a valores predeterminados.
        Horas, minutos y segundos se inicializan a 0, y el formato se inicializa a "24 HOURS".
        """
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.format = "24 HOURS"
        Time.time_count += 1  # Incrementa el contador al crear un objeto

    def __assign_format(self, psz_format):
        """
        Asigna y valida el formato de hora.

        Args:
        psz_format (str): El formato de hora a asignar (AM, PM o 24 HOURS).

        Returns:
        bool: True si el formato es válido y ha sido asignado correctamente, False en caso contrario.
        """
        psz_format = psz_format.upper()
        if psz_format in Time.TIME_FORMATS:
            self.format = psz_format
            return True
        return False

    def __is_24hour_format(self):
        """
        Verifica si el formato de hora es "24 HOURS".

        Returns:
        bool: True si el formato es "24 HOURS", False en caso contrario.
        """
        return self.format == "24 HOURS"

    def _is_valid_time(self):
        """
        Verifica si los valores de horas, minutos y segundos son válidos según el formato de la hora.

        Returns:
        bool: True si la hora es válida, False en caso contrario.
        """
        if self.__is_24hour_format():
            return 0 <= self.hours <= 23
        else:
            return 1 <= self.hours <= 12 and 0 <= self.minutes < 60 and 0 <= self.seconds < 60

    def set_time(self, hours, minutes, seconds, psz_format):
        """
        Asigna la hora validando los valores ingresados.

        Args:
        hours (int): Horas a asignar.
        minutes (int): Minutos a asignar.
        seconds (int): Segundos a asignar.
        psz_format (str): Formato de hora (AM, PM o 24 HOURS).

        Returns:
        bool: True si la hora fue asignada correctamente, False en caso contrario.
        """
        if not self.__assign_format(psz_format):
            print("Formato de hora inválido.")
            return False
        
        if not (0 <= minutes < 60 and 0 <= seconds < 60):
            print("Minutos o segundos fuera del rango.")
            return False

        if self.__is_24hour_format():
            if not (0 <= hours <= 23):
                print("Horas fuera de rango para formato 24 HORAS.")
                return False
        else:
            if not (1 <= hours <= 12):
                print("Horas fuera de rango para formato AM/PM.")
                return False

        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        return True

    def get_time(self):
        """
        Retorna la hora actual formateada como una cadena.

        Returns:
        str: La hora en formato HH:MM:SS con el formato (AM/PM/24 HOURS).
        """
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02} {self.format}"

    @classmethod
    def from_string(cls, time_string):
        """
        Crea un objeto Time a partir de una cadena de tiempo.

        Args:
        time_string (str): Una cadena en el formato "HH:MM:SS FORMAT" donde FORMAT puede ser AM, PM o 24 HOURS.

        Returns:
        Time: Un nuevo objeto Time creado con los valores extraídos de la cadena.
        None: Si el formato de la cadena es inválido.
        """
        pattern = r"(\d{1,2}):(\d{2}):(\d{2})\s*(AM|PM|24 HOURS)"
        match = re.match(pattern, time_string, re.IGNORECASE)
        if match:
            hours, minutes, seconds, time_format = match.groups()
            hours = int(hours)
            minutes = int(minutes)
            seconds = int(seconds)
            new_time = cls()
            if not new_time.set_time(hours, minutes, seconds, time_format.upper()):
                print("Error al crear el objeto Time.")
                return None
            return new_time
        else:
            print("Formato de hora inválido. Debe ser HH:MM:SS AM/PM o HH:MM:SS 24 HOURS.")
            return None

    @staticmethod
    def is_valid_format(time_format):
        """
        Verifica si el formato de hora es válido.

        Args:
        time_format (str): El formato de hora a verificar.

        Returns:
        bool: True si el formato es válido (AM, PM o 24 HOURS), False en caso contrario.
        """
        return time_format.upper() in Time.TIME_FORMATS

    @classmethod
    def get_time_count(cls):
        """
        Retorna el número total de objetos Time creados.

        Returns:
        int: El número de objetos Time creados.
        """
        return cls.time_count


# Función para mostrar la hora en una cadena formateada
def show_time_string(time_obj):
    """
    Retorna la hora de un objeto Time como una cadena.

    Args:
    time_obj (Time): El objeto Time del cual se quiere obtener la hora.

    Returns:
    str: La hora formateada como HH:MM:SS FORMAT.
    """
    return time_obj.get_time()


# Función principal para el menú
def main():
    """
    Función principal que ejecuta un menú para interactuar con el usuario.
    Permite introducir una nueva hora, visualizar la hora actual o crear una hora desde una cadena.
    """
    current_time = Time()
    while True:
        print("\nMenú:")
        print("1. Introducir una nueva hora")
        print("2. Visualizar hora")
        print("3. Crear una hora a partir de una cadena (formato HH:MM:SS)")
        print("4. Terminar")
        
        choice = input("Seleccione una opción: ")
        
        if choice == "1":
            try:
                hours = int(input("Ingrese las horas: "))
                minutes = int(input("Ingrese los minutos: "))
                seconds = int(input("Ingrese los segundos: "))
                time_format = input("Ingrese el formato (AM, PM, 24 HOURS): ")
                if current_time.set_time(hours, minutes, seconds, time_format):
                    print("Hora asignada correctamente.")
                else:
                    print("Error al asignar la hora.")
            except ValueError:
                print("Entrada no válida. Intente nuevamente.")
                
        elif choice == "2":
            print(f"La hora actual es: {show_time_string(current_time)}")
        
        elif choice == "3":
            time_string = input("Ingrese una cadena de tiempo (HH:MM:SS FORMATO): ")
            new_time = Time.from_string(time_string)
            if new_time:
                current_time = new_time
                print(f"La nueva hora es: {show_time_string(current_time)}")
        
        elif choice == "4":
            print("Terminando el programa.")
            break
        
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
