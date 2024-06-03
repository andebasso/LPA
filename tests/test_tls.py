import unittest
from src.communication.tls import create_tls_connection

class TestTLS(unittest.TestCase):
    def test_create_tls_connection(self):
        hostname = 'example.com'
        port = 443
        connection = create_tls_connection(hostname, port)
        self.assertIsNotNone(connection)
        connection.close()

if __name__ == '__main__':
    unittest.main()
