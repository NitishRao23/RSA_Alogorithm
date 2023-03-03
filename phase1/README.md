# Overview:  
	VANET is a network of the vehicles, which are connected by the wireless links. 
	The main objective of the communication in this network is to give a reliable and exact knowledge about the neighbouring vehicle on the road. 
	The wormhole attack can perform the unauthorised access, disrupting routing process, performing DOS attack, breaking of the security of the data packets transmission. 
	So here we need to provide the security in the network by preventing the wormhole attack.

### RSA Algorithm:  
	RSA algorithm is used to provide both confidentiality and authentication to the transmitted packets. 
	We use this algorithm for the encryption and decryption on both the sender and receiver side. 
	We also generate the public and private keys.

### Packet Leash:
	We use this technique to prevent from the wormhole attack. 
	Here, we use temporal leash which uses the packet expiration time as base.

For this implementation we use an approach is to distribute the shared key with both the confidentiality and authenticity in the VANET network by using the RSA algorithm.

## Setup  
### Git Bash Installation:  
	1. Download from the link: "https://git-scm.com/"
	2. Download installer.
	3. Run the ".exe" file and follow the installing instructions.
	4. Launch Git Bash.
	5. If there are any issues in the installation process check the path in the environment variables.

### VS Code:  
	1. Download the VS code installer from the link: "https://code.visualstudio.com/docs?dv=win"
	2. Run the installer i.e., ".exe" file.
	3. It is installed defaultly under the mentioned path: "C:\Users\user_name\AppData\Local\Programs\Microsoft VS Code"
	4. Check the path in the environment variables for any issues in the installation.

### WSL:  
	1. Run the "Command Prompt or Powershell" as administrator.
	2. Run the "wsl --install" command (This command will enable all the necessary features to run)
	3. Restart the machine.

### Python:  
	1. Download the installer from: "https://www.python.org/downloads/"
	2. Run the executable installer ".exe" file.
	3. Once it is installed check the version using "python --version" command.
	4. Check the path in the environment variables for any issues in the installation process.

