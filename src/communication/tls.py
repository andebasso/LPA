import ssl
import socket

def create_tls_context():
    # Cria um contexto SSL que especifica a utilização do TLS 1.2 ou superior
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)  # Cria um contexto específico para o cliente
    context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1  # Desativa TLS 1.0 e 1.1
    context.set_ciphers('HIGH:!aNULL:!eNULL:!MD5:!RC4')  # Exemplo de configuração de cifras seguras
    context.verify_mode = ssl.CERT_REQUIRED
    context.check_hostname = True
    context.load_default_certs()  # Carrega os certificados padrão do sistema
    
    return context

# Exemplo de uso
if __name__ == "__main__":
    hostname = 'example.com'
    port = 443
    tls_connection = create_tls_context(hostname, port)
    # Agora você pode usar tls_connection para enviar e receber dados seguros
