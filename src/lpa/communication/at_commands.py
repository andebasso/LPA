# at_commands.py for Sierra Wireless AirPrime MC7455
# doc ref 4117727 AirPrime EM-MC74xx AT Command Reference r4

# AT password commands
ENTERCND = '!ENTERCND' #Enable access to password-protected commands
SETCND = '!SETCND' #Set AT command password

# Basic Commands
RESET = 'ATZ'
ECHO_OFF = 'ATE0'
ECHO_ON = 'ATE1'

# SIM and eSIM Management Commands
CHECK_SIM_STATUS = 'AT+CPIN?'
CHANGE_PIN = 'AT+CPIN="oldPIN","newPIN"'  # Replace oldPIN and newPIN with actual values

# Network Management Commands
GET_SIGNAL_QUALITY = 'AT+CSQ'
GET_NETWORK_REGISTRATION_STATUS = 'AT+CREG?'
SET_NETWORK_MODE = 'AT+CFUN='  # Add mode number

# Device Information Commands
GET_IMEI = 'AT+CGSN'
GET_FIRMWARE_INFO = 'AT+CGMR'
GET_MODEL_INFO = 'AT+CGMM'

# eSIM Specific Commands
LIST_PROFILES = 'AT+CRSM='  # Add specific parameters
ACTIVATE_PROFILE = 'AT+CPOL='  # Add specific parameters
DELETE_PROFILE = 'AT+CPOL='  # Add specific parameters, etc.

# GPS Commands
GPS_CONTROL = 'AT+CGPS='  # Turn GPS on/off
GET_GPS_STATUS = 'AT+CGPSINFO'

# LTE and Network Commands
SET_BAND = 'AT!BAND='  # Add specific parameters for band configuration
GET_BAND = 'AT!BAND?'

# Data Call and Connectivity Commands
SET_APN = 'AT+CGDCONT='  # Define PDP context (APN settings)
ACTIVATE_DATA_CALL = 'ATD*99***1#'

# Error Handling and Diagnostics
GET_ERROR_REPORT = 'AT+CEER'
GET_DIAGNOSTIC_INFO = 'AT!GSTATUS?'

# Modem status commands
ANTSEL = '!ANTSEL'  # Set/query external antenna select configuration
BAND = '!BAND'  # Select/return frequency band set
BOOTHOLD = '!BOOTHOLD'  # Reset modem and wait in bootloader for firmware download
CUSTOM = '!CUSTOM'  # Set/return customization settings
DATALOOPBACK = '!DATALOOPBACK'  # Enable/disable and configure loopback mode
GCFEN = '!GCFEN'  # Enable/disable GCF test mode
GETBAND = '!GETBAND'  # Return the current active band
GOBIIMPREF = '!GOBIIMPREF'  # Query Gobi Image Management preferences
GSTATUS = '!GSTATUS'  # Return operational status
HWID = '!HWID'  # Display hardware version
IMPREF = '!IMPREF'  # Query/set Image Management preferences
LTEINFO = '!LTEINFO'  # Display LTE network information
NVENCRYPTIMEI = '!NVENCRYPTIMEI'  # Write unencrypted IMEI to modem
NVPLMN = '!NVPLMN'  # Provision/display PLMN list for Network Personalization locking
PCINFO = '!PCINFO'  # Return power control status information
PCOFFEN = '!PCOFFEN'  # Set/return Power Off Enable state
PCTEMP = '!PCTEMP'  # Return current temperature information
PCTEMPLIMITS = '!PCTEMPLIMITS'  # Set/report temperature state limit values
PCVOLT = '!PCVOLT'  # Return current power supply voltage information
PCVOLTLIMITS = '!PCVOLTLIMITS'  # Set/report power supply voltage state limit values
PRIID = '!PRIID'  # Set/report module PRI part number and revision
RESET = '!RESET'  # Reset modem
SCACT = '!SCACT'  # Activate/deactivate data connection
SELMODE = '!SELMODE'  # Set/return current service domain
TMSTATUS = '!TMSTATUS'  # Report Thermal Mitigation Status
USBCOMP = '!USBCOMP'  # Set/report USB interface configuration
USBINFO = '!USBINFO'  # Return information from active USB descriptor
USBPID = '!USBPID'  # Set/report product ID in USB descriptor
V = '&V'  # Return operating mode AT configuration parameters

# Diagnostic commands
BCFWUPDATESTATUS = '!BCFWUPDATESTATUS'  # Report status of most recent firmware update attempt
ERR = '!ERR'  # Display diagnostic information
GCCLR = '!GCCLR'  # Clear crash dump data
GCDUMP = '!GCDUMP'  # Display crash dump data
RXDEN = '!RXDEN'  # Enable/disable WCDMA/LTE/TD-SCDMA receive diversity

# Test commands
DACGPSCTON = '!DACGPSCTON'  # Return GPS CtoN and frequency measurement
DACGPSMASKON = '!DACGPSMASKON'  # Set CGPS IQ log mask
DACGPSSTANDALONE = '!DACGPSSTANDALONE'  # Enter/exit StandAlone (SA) RF mode
DACGPSTESTMODE = '!DACGPSTESTMODE'  # Start/stop CGPS diagnostic task
DAFTMACT = '!DAFTMACT'  # Put modem into Factory Test Mode
DAFTMDEACT = '!DAFTMDEACT'  # Put modem into online mode from Factory Test Mode
DALGAVGAGC = '!DALGAVGAGC'  # Return averaged Rx AGC value (LTE only)
DALGRXAGC = '!DALGRXAGC'  # Return Rx AGC value (LTE only)
DALGTXAGC = '!DALGTXAGC'  # Return Tx AGC value and transmitter parameters (LTE only)
DALSNSVAL = '!DALSNSVAL'  # Set LTE NS value (LTE only)
DALSRXBW = '!DALSRXBW'  # Set LTE Rx bandwidth (LTE only)
DALSTXBW = '!DALSTXBW'  # Set LTE Tx bandwidth (LTE only)
DALSTXMOD = '!DALSTXMOD'  # Set LTE Tx modulation type (LTE only)
DALSWAVEFORM = '!DALSWAVEFORM'  # Set LTE TX waveform (LTE only)
DAOFFLINE = '!DAOFFLINE'  # Place modem offline
DASBAND = '!DASBAND'  # Set frequency band
DASCHAN = '!DASCHAN'  # Set modem channel (frequency)
DASLNAGAIN = '!DASLNAGAIN'  # Set LNA gain state
DASPDM = '!DASPDM'  # Set PDM value
DASTXOFF = '!DASTXOFF'  # Turn Tx PA off (WCDMA or LTE mode)
DASTXON = '!DASTXON'  # Turn Tx PA on (WCDMA or LTE mode)
DAWGAVGAGC = '!DAWGAVGAGC'  # Return averaged Rx AGC value (WCDMA only)
DAWGRXAGC = '!DAWGRXAGC'  # Return Rx AGC value (WCDMA only)
DAWINFO = '!DAWINFO'  # Return WCDMA mode RF information (WCDMA only)
DAWSCONFIGRX = '!DAWSCONFIGRX'  # Set WCDMA receiver to factory calibration settings (WCDMA only)
DAWSPARANGE = '!DAWSPARANGE'  # Set PA range state machine (WCDMA only)
DAWSSCHAIN = '!DAWSSCHAIN'  # Enable secondary receive chain (WCDMA only)
DAWSCHAINTCM = '!DAWSCHAINTCM'  # Place receive chain in test call mode (WCDMA only)
DAWSTXCW = '!DAWSTXCW'  # Set waveform used by the transmitter (WCDMA only)
DAWSTXPWR = '!DAWSTXPWR'  # Set desired Tx power level (WCDMA mode only)

# Memory management commands
NVBACKUP = '!NVBACKUP'  # Back up device configuration
RMARESET = '!RMARESET'  # Back up device configuration

# GNSS commands
GPSAUTOSTART = '!GPSAUTOSTART'  # Configure GPS auto-start features
GPSCLRASSIST = '!GPSCLRASSIST'  # Clear specific GPS assistance data
GPSCOLDSTART = '!GPSCOLDSTART'  # Clear all GNSS assistance data
GPSEND = '!GPSEND'  # End an active session
GPSFIX = '!GPSFIX'  # Initiate GPS position fix
GPSLBSAPN = '!GPSLBSAPN'  # Set GPS LBS APNs
GPSLOC = '!GPSLOC'  # Return last known location of the modem
GPSMOMETHOD = '!GPSMOMETHOD'  # Set/report GPS MO method
GPSNIQOSTIME = '!GPSNIQOSTIME'  # Set/report GPS QoS timeout period for network-initialized fixes
GPSNMEACONFIG = '!GPSNMEACONFIG'  # Enable and set NMEA data output rate
GPSNMEASENTENCE = '!GPSNMEASENTENCE'  # Set/report NMEA sentence type
GPSPORTID = '!GPSPORTID'  # Set/report port ID to use over TCP/IP
GPSPOSMODE = '!GPSPOSMODE'  # Configure support for GPS positioning modes
GPSSATINFO = '!GPSSATINFO'  # Request satellite information
GPSSTATUS = '!GPSSTATUS'  # Request current status of a position fix session
GPSSUPLURL = '!GPSSUPLURL'  # Set/report SUPL server URL
GPSSUPLVER = '!GPSSUPLVER'  # Set/report SUPL server version
GPSTRACK = '!GPSTRACK'  # Initiate local tracking (multiple fix) session
GPSTRANSSEC = '!GPSTRANSSEC'  # Control GPS transport security
WANT = '+WANT'  # Enable/disable GNSS antenna power

# SIM commands
# SIM Command: Display remaining number of SIM unlock retries
CPINR = '+CPINR'  # Display the number of remaining SIM unlock retries. Use this command to query the remaining retries for a specified PIN/PUK type. It supports various PIN/PUK types including SIM PIN, SIM PUK, SIM PIN2, SIM PUK2, and different personalization PIN/PUKs (e.g., PH-NET PIN, PH-NET PUK).

# SIM Command: Select active SIM interface
UIMS = '!UIMS'  # Select the active SIM interface on a module supporting multiple SIM interfaces. Use this command to switch between internal and external SIM card slots, or between different UICC interfaces. The command allows selecting the active SIM interface and querying the currently selected interface.

# OMA-DM commands
HOSTDEVINFO = '!HOSTDEVINFO'  # Configure host device details
IDSCONFIGACC = '!IDSCONFIGACC'  # Configure DM account authentication mode and XML format
IDSCREATEACC = '!IDSCREATEACC'  # Enter DM account credentials
IDSSUPPORT = '!IDSSUPPORT'  # Configure DM sessions
IMSTESTMODE = '!IMSTESTMODE'  # Enable/disable IMS test mode
OSINFO = '!OSINFO'  # Configure host device operating system information

# SAR backoff and thermal control commands
MAXPWR = '!MAXPWR'  # Set/report maximum Tx power
SARBACKOFF = '!SARBACKOFF'  # Set/report offset from maximum Tx power
SARINTGPIOMODE = '!SARINTGPIOMODE'  # Set/report default pull mode for SAR interrupt GPIOs
SARSTATE = '!SARSTATE'  # Set/report SAR backoff state
SARSTATEDFLT = '!SARSTATEDFLT'  # Set/report default SAR backoff state

# AirVantage commands
# Configure AirVantage Management Services
WDSC = "+WDSC"  # Enable or disable selected Mode. For Mode = 4, use <Timer_1> to <Timer_n> for interval timers

# Display most recent AirVantage Management Services error
WDSE = "+WDSE"  # Display the most recent HTTP(S) response for the package download

# Display AirVantage Management Services status information
WDSG = "+WDSG"  # Display general AirVantage Management Services status details

# Activate/deactivate AirVantage Management Services unsolicited notifications
WDSI = "+WDSI"  # Activate/deactivate notifications as specified by Level

# Activate/deactivate AirVantage Management Services unsolicited notifications
WDSI_notification = "+WDSI (notification)"  # AirVantage Management Services events—Unsolicited notification

# Reply to AirVantage server request
WDSR = "+WDSR"  # Send Reply to a user agreement request from the module. For specific Reply types, include a Timer for the module to send a new request after the specified delay

# Configure/connect AirVantage Management Services session
WDSS = "+WDSS"  # Configure or clear a dedicated APN and initiate a connection to the AirVantage server. Also used to activate automatic registration to the AirVantage server
