import subprocess
import requests

dei_server = ""
def line_notify(dei_server):
    print(f'サーバーが死んでいます\n{dei_server}')


hosts = ["192.168.0.201", "192.168.0.202"]
for host in hosts:
    res = subprocess.run(["ping", host, "-c","2", "-W", "300"], stdout=subprocess.PIPE)
    print(res.stdout.decode("cp932"))

    if res.returncode == 0:
        print("生存")
    else:
        print("死亡")
        dei_server += host+"\n"

if dei_server == "": pass 
else: line_notify(dei_server)

print()