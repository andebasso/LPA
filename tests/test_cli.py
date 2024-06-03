import unittest
import subprocess

class TestCLI(unittest.TestCase):
    def test_list_profiles(self):
        result = subprocess.run(['python', 'src/lui/cli.py', '--list'], capture_output=True, text=True)
        self.assertIn('Listando perfis eSIM', result.stdout)

    def test_activate_profile(self):
        result = subprocess.run(['python', 'src/lui/cli.py', '--activate', 'profile1'], capture_output=True, text=True)
        self.assertIn('Ativando perfil eSIM: profile1', result.stdout)

    def test_deactivate_profile(self):
        result = subprocess.run(['python', 'src/lui/cli.py', '--deactivate', 'profile2'], capture_output=True, text=True)
        self.assertIn('Desativando perfil eSIM: profile2', result.stdout)

    def test_delete_profile(self):
        result = subprocess.run(['python', 'src/lui/cli.py', '--delete', 'profile3'], capture_output=True, text=True)
        self.assertIn('Excluindo perfil eSIM: profile3', result.stdout)

if __name__ == '__main__':
    unittest.main()

