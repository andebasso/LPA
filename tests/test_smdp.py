import unittest
from unittest.mock import patch
from src.communication.smdp import get_esim_profile

class TestSMDP(unittest.TestCase):
    @patch('src.communication.tls.create_tls_connection')
    def test_get_esim_profile(self, mock_create_tls_connection):
        mock_conn = mock_create_tls_connection.return_value
        mock_conn.recv.return_value = b'HTTP/1.1 200 OK\r\n\r\n{"status": "success"}'

        smdp_hostname = 'smdp.example.com'
        port = 443
        token_autenticacao = 'seu_token_aqui'
        codigo_ativacao = 'codigo_de_ativacao'
        response = get_esim_profile(smdp_hostname, port, token_autenticacao, codigo_ativacao)
        self.assertIn(b'HTTP/1.1', response)

if __name__ == '__main__':
    unittest.main()

