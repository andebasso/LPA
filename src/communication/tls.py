import ssl
import socket

def create_tls_connection(server_hostname, port):
    # Crie um contexto SSL padrão
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    # Retorna um socket que representa a conexão TLS com o servidor
    conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=server_hostname)
    conn.connect((server_hostname, port))
    return conn

# Exemplo de uso
if __name__ == "__main__":
    hostname = 'example.com'
    port = 443
    tls_connection = create_tls_connection(hostname, port)
    # Agora você pode usar tls_connection para enviar e receber dados seguros
