import unittest
from src.profiles.profile_manager import list_profiles, activate_profile, deactivate_profile, delete_profile

class TestProfileManager(unittest.TestCase):
    def test_list_profiles(self):
        list_profiles()  # Verifique a saída manualmente

    def test_activate_profile(self):
        activate_profile('profile1')  # Verifique a saída manualmente

    def test_deactivate_profile(self):
        deactivate_profile('profile2')  # Verifique a saída manualmente

    def test_delete_profile(self):
        delete_profile('profile3')  # Verifique a saída manualmente

if __name__ == '__main__':
    unittest.main()
