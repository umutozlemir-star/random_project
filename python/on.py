import os
import subprocess

def onc():
    yol = os.path.join(".", "python", "code")
    try:
        subprocess.run(["python", "main.py"], cwd=yol, shell=True)
    except:
        pass
