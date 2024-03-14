# Local Profile Assistant (LPA) Project

## Overview

This project aims to develop a Local Profile Assistant (LPA) for managing eSIM profiles within devices. The LPA allows devices to store multiple eSIM profiles and switch between them without needing to replace physical SIM cards. This software is intended to facilitate seamless communication with modem devices, handle eSIM profile management, and interact with Subscription Manager Data Preparation (SM-DP+) servers for profile provisioning and management.

## LPA Services
This role provides the necessary access to the services and data required by LPAd functions. These services include:
- Provide the address(es) of the Root SM-DS(s) and the Default SM-DP+, if configured
- Transfer Bound Profile Package from the LPAd to the ISD-P
- Provide list of installed Profiles and their Profile Metadata
- Retrieve EID
- Provide Local Profile Management Operations
- Provide Remote Profile Management
- Provide authentication and integrity verification for Event Retrieval from an SM-DS
- Provide pending Notifications

## Features

- Communicate with modem devices using AT commands.
- Download, activate, deactivate, and delete eSIM profiles.
- Interface with SM-DP+ servers for eSIM management.
- User-friendly interface for managing eSIM profiles.
- Secure handling of credentials and personal information.

## Installation

(Provide detailed step-by-step installation instructions here. Include any prerequisites, libraries to install, and environmental setup.)

## Usage

(Provide instructions on how to use the software, including command-line instructions, configuration settings, and examples.)

## Contributing

We welcome contributions to the Local Profile Assistant project! Please read our contributing guidelines before submitting pull requests or issues.

## License

(Include information about the project's license here. If you have not decided on a license yet, you might consider options like MIT, GPL, or Apache.)

## Acknowledgments

(Here you can give acknowledgment to any resource, library, or individuals that helped you in the development of this project.)

Thank you for your interest in our Local Profile Assistant (LPA) project. We look forward to seeing how it evolves with your input and support!

## MAP

Project_lpa/
│
├── src/
│   ├── lpa/                     # Local Profile Assistant
│   │   ├── lds/                 # Local Discovery Service
│   │   │   ├── __init__.py
│   │   │   └── lds_services.py
│   │   │
│   │   ├── lpd/                 # Local Profile Download
│   │   │   ├── __init__.py
│   │   │   ├── lpd_services.py
│   │   │   └── profile_handling.py
│   │   │
│   │   ├── lpr/                 # Local Profile Assistant (services)
│   │   │   ├── __init__.py
│   │   │   ├── lpr_services.py
│   │   │   └── content_management.py
│   │   │
│   │   └── lui/                 # Local User Interface
│   │       ├── __init__.py
│   │       ├── cli.py
│   │       └── gui.py
│   │
│   ├── communication/           # Comunicação com o modem e redes
│   │   ├── __init__.py
│   │   ├── modem.py             # Interações específicas com o modem
│   │   └── at_commands.py       # Definição e execução de comandos AT
│   │
│   ├── interfaces/              # Comunicação externa
│   │   ├── __init__.py
│   │   ├── es9plus.py
│   │   ├── es21.py
│   │   ├── es11.py
│   │   ├── eshri.py
│   │   ├── es20.py
│   │   └── es22.py
│   │
│   └── utils/
│       ├── __init__.py
│       └── utilities.py
│
├── tests/
│   └──  # Arquivos de teste
│
├── venv/
│
├── requirements.txt
└── README.md
