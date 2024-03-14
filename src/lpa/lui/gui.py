import tkinter as tk
from profiles.profile_manager import list_profiles, activate_profile, deactivate_profile

def update_profiles():
    # Função para atualizar a lista de perfis na GUI
    pass

def create_gui():
    window = tk.Tk()
    window.title('Gerenciador LPA para eSIM')

    # Adicione elementos à janela, como botões, listas de perfis, etc.

    window.mainloop()

if __name__ == "__main__":
    create_gui()
