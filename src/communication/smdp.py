import json
from .tls import create_tls_connection

def get_esim_profile(smdp_hostname, port, token_autenticacao, codigo_ativacao):
    tls_connection = create_tls_connection(smdp_hostname, port)

    request_payload = json.dumps({'activationCode': codigo_ativacao}).encode('utf-8')
    request_headers = (
        f"POST /profiles HTTP/1.1\r\n"
        f"Host: {smdp_hostname}\r\n"
        f"Authorization: Bearer {token_autenticacao}\r\n"
        f"Content-Type: application/json\r\n"
        f"Content-Length: {len(request_payload)}\r\n"
        f"\r\n"
    ).encode('utf-8')

    tls_connection.sendall(request_headers + request_payload)
    response = tls_connection.recv(4096)
    print(response)
    tls_connection.close()

    return response


