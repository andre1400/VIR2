import os
import time
from absl import app
from absl import flags

FLAGS = flags.FLAGS
flags.DEFINE_enum('task', None, ['start', 'stop', 'create', 'remove', 'list'], 'Task to do')
flags.DEFINE_integer('number', None, 'Number of instances')

def getIP(id):
    cmd = f"pct exec {id}" + " -- ip addr | grep eth0 | grep inet | awk '{print $2}'"
    ip = os.popen(cmd).read()
    return ip

def startLxc(id):
    cmd = f"pct start {id}"
    out = os.system(cmd)
    return out

def stopLxc(id):
    cmd = f"pct stop {id}"
    out = os.system(cmd)
    return out

def clone(id, newId):
    cmd = f"pct clone {id} {newId} --full --storage local-lvm"
    out = os.popen(cmd).read()
    return out

def list():
    cmd = 'pct list | grep "[2-9][0-9]"'
    out = os.popen(cmd).read()
    return out

def remove(id):
    cmd = f"pct destroy {id}"
    out = os.system(cmd)
    return out

def main(ARGV):
    pentesterlab = 103  # To edit with the correct ids
    attacking = 100  # To edit with the correct ids

    if FLAGS.task is None:
        print("Invalid argument")
        return

    if FLAGS.task == "list":
        print("Listing all containers :")
        out = list()
        print(out)
        return

    if FLAGS.number is None:
        print("Invalid argument")
        return
    
    if FLAGS.task == "start":
        print("\n==Start des machines pentesterlabs==")
        for x in range(200, 200 + FLAGS.number):
            out = startLxc(x)
            # Wait for dhcp
            time.sleep(7)
            ip = getIP(x)
            if out == 0:
                print(f"ID : {x} IP : {ip}".rstrip())
                print("Username: root Password: Pa$$w0rd")
            else:
                print(f'Error starting container {x}')

        print("\n==Start des machines attaquantes==")
        for x in range(400, 400 + FLAGS.number):
            out = startLxc(x)
            # Wait for lxc to boot, to get all ips
            time.sleep(7)
            ip = getIP(x)
            if out == 0:
                print(f"ID : {x} IP : {ip}".rstrip())
                print("Username: root Password: Pa$$w0rd")
            else:
                print(f'Error starting container {x}')

        return

    if FLAGS.task == "stop":
        print("\n==Stop des machines pentesterlabs==")
        for x in range(200, 200 + FLAGS.number):
            out = stopLxc(x)
            if out == 0:
                print(f"ID : {x} Stopped")
            else:
                print(f'Error stopping container {x}')

        print("\n==Stop des machines attaquantes==")
        for x in range(400, 400 + FLAGS.number):
            out = stopLxc(x)
            if out == 0:
                print(f"ID : {x} Stopped")
            else:
                print(f'Error stopping container {x}')

        return

    if FLAGS.task == "create":
        print("\n==Creation des machines pentesterlabs==")
        for x in range(200, 200 + FLAGS.number):
            out = clone(pentesterlab, x)
            print(f"ID : {x} Created")

        print("\n==Creation des machines attaquantes==")
        for x in range(400, 400 + FLAGS.number):
            out = clone(attacking, x)
            print(f"ID : {x} Created")

        return

    if FLAGS.task == "remove":
        print("\n==Remove des machines pentesterlabs==")
        for x in range(200, 200 + FLAGS.number):
            out = remove(x)
            print(f"ID : {x} Removed")

        print("\n==Remove des machines attaquantes==")
        for x in range(400, 400 + FLAGS.number):
            out = remove(x)
            print(f"ID : {x} Removed")

        return

if __name__ == "__main__":
    app.run(main)
