import argparse
from profiles.profile_manager import list_profiles, activate_profile, deactivate_profile, delete_profile

def main():
    parser = argparse.ArgumentParser(description='Gerenciador LPA para eSIM')
    parser.add_argument('--list', help='Lista todos os perfis eSIM', action='store_true')
    parser.add_argument('--activate', help='Ativa um perfil eSIM', type=str)
    parser.add_argument('--deactivate', help='Desativa um perfil eSIM', type=str)
    parser.add_argument('--delete', help='Exclui um perfil eSIM', type=str)
    args = parser.parse_args()

    if args.list:
        list_profiles()
    elif args.activate:
        activate_profile(args.activate)
    elif args.deactivate:
        deactivate_profile(args.deactivate)
    elif args.delete:
        delete_profile(args.delete)

if __name__ == "__main__":
    main()
