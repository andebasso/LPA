import serial
import time

class Modem:
    def __init__(self, port='/dev/ttyUSB2', baudrate=115200):
        self.port = port
        self.baudrate = baudrate
        self.connection = None

    def open_connection(self):
        self.connection = serial.Serial(self.port, self.baudrate, timeout=1)
        # Pode adicionar mais configurações de inicialização aqui

    def close_connection(self):
        if self.connection:
            self.connection.close()
            self.connection = None

    def send_at_command(self, command):
        if not self.connection:
            raise Exception('Modem not connected')
        self.connection.write((command + '\r\n').encode())
        time.sleep(1)  # Aguardar resposta
        response = self.connection.read_all().decode()
        return response

    # Aqui você pode adicionar mais métodos específicos para seu modem
