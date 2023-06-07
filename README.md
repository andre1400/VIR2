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
