import requests

def get_esim_profile(smdp_address, activation_code):
    """Solicita um perfil eSIM do servidor SM-DP+."""
    headers = {'Content-Type': 'application/json'}
    payload = {'activationCode': activation_code}
    
    response = requests.post(f'{smdp_address}/profiles', headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()  # Retorna o perfil eSIM
    else:
        response.raise_for_status()  # Lança uma exceção se ocorreu um erro

