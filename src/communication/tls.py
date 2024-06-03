import ssl
import socket

def create_tls_connection(hostname, port):
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1
    context.set_ciphers('HIGH:!aNULL:!eNULL:!MD5:!RC4')
    context.verify_mode = ssl.CERT_REQUIRED
    context.check_hostname = True
    context.load_default_certs()

    sock = socket.create_connection((hostname, port))
    tls_connection = context.wrap_socket(sock, server_hostname=hostname)
    return tls_connection

