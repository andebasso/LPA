from .at_commands import RESET, ECHO_OFF  # Importa comandos AT necessários
from .utilities import send_at_command  # Supondo que esta é uma função de utilidade que você tem

def reset_modem():
    send_at_command(RESET)

def disable_echo():
    send_at_command(ECHO_OFF)