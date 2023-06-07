# VIR2
Installation de git

```python
sudp apt install git
```

Clonage du repo

```python
git glone https://github.com/andre1400/VIR2.git
```

Installation du module python qu’on aura besoin pour notre script plus tard

```python
pip install absl-py
```

Installation d’Ansbile

```bash
apt update
apt upgrade
apt install python3-pip
python3 -m pip install --user ansible
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source .bashrc
ansible-galaxy collection install community.mysql
```
# Utilisation des contenaires
## Creation
/// INPUT
```
root@pve:~# python3 ./ScriptPython.py --task create --number 5
```
/// OUTPUT
```
Creation des pentesterlabs
ID : 200 Created
ID : 201 Created
ID : 202 Created
ID : 203 Created
ID : 204 Created
Creation des machines attaquantes
ID : 300 Created
ID : 301 Created
ID : 302 Created
ID : 303 Created
ID : 304 Created
```
## Start
/// INPUT
```
root@pve:~# python3 ./ScriptPython.py --task start --number 5
```
///OUTPUT
```
root@pve-01:/vir2/VIR2# python3 ./ScriptPython.py --task start --number 3

==Start des machines pentesterlabs==
ID : 200 IP : 10.10.111.150/24
Username: root Password: Pa$$w0rd
ID : 201 IP : 10.10.111.151/24
Username: root Password: Pa$$w0rd
ID : 202 IP : 10.10.111.152/24
Username: root Password: Pa$$w0rd

==Start des machines attaquantes Let's GO !!!...==
ID : 400 IP : 10.10.111.143/24
Username: root Password: Pa$$w0rd
ID : 401 IP : 10.10.111.153/24
Username: root Password: Pa$$w0rd
ID : 402 IP : 10.10.111.154/24
Username: root Password: Pa$$w0rd
root@pve-01:/vir2/VIR2#
```
## STOP
/// INPUT
```
root@pve:~# python3 ./ScriptPython.py --task stop --number 5
```
/// OUTPUT
```
Stop des pentesterlabs
ID : 200 Stopped
ID : 201 Stopped
ID : 202 Stopped
ID : 203 Stopped
ID : 204 Stopped
Stop des machines attaquantes
ID : 300 Stopped
ID : 301 Stopped
ID : 302 Stopped
ID : 303 Stopped
ID : 304 Stopped
```
## SUPPRESSION
/// INPUT
```
root@pve:~# python3 ./ScriptPython.py --task remove --number 5
```
///OUTPUT
```
Remove some pentesterlabs
ID : 200 Removed
ID : 201 Removed
ID : 202 Removed
ID : 203 Removed
ID : 204 Removed
Remove some attacking machines
ID : 300 Removed
ID : 301 Removed
ID : 302 Removed
ID : 303 Removed
ID : 304 Removed
```
## Lister
*Ca va lister uniquement l'environnement lab de l'étudiant, pour tous lister : pct list*

/// INPUT
```
root@pve:~# python3 ./ScriptPython.py --task list --number 2
```
///OUTPUT
```
Listing all containers :
200 stopped penterlabT
201 stopped penterlabT
300 stopped attackerT
301 stopped attackerT
```
