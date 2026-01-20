import subprocess
import platform
import sys
from datetime import datetime
import logging
import os

logging.basicConfig(
    filename=os.path.join(os.getcwd(), "applog.log"),
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)

logging.info(platform.system())

if platform.system() != "Linux":
    logging.info("Your current platform is " + platform.system() + ". Only Linux is supported" )
    logging.error(f"Program errorred")
    sys.exit(1)  

def get_os_family():
    try:
        info = platform.freedesktop_os_release()
        # ID is the specific distro (e.g., 'ubuntu'), ID_LIKE is the family
        ids = [info.get("ID")]
        if "ID_LIKE" in info:
            ids.extend(info["ID_LIKE"].split())
        
        if any(x in ids for x in ["debian", "ubuntu"]):
            return "Debian-based"
        elif any(x in ids for x in ["rhel", "fedora", "centos", "amzn"]):
            return "RedHat-based"
    except (AttributeError, FileNotFoundError):
        return "Unknown"

result = get_os_family()

if os.geteuid() != 0:
    logging.error(f"Root priviledges required. Program errorred")
    sys.exit(1)  

if result == "Debian-based":
    try:
        logging.info(f"Installation started ")
        cmd = subprocess.run(["apt", "update","&&", "apt", "upgrade", "-y"], shell=True, capture_output=True, text=True, timeout=600)
    except subprocess.TimeoutExpired:
        logging.error("Command timed out after 600 seconds")
elif result == "RedHat-based":
    try:
        logging.info(f"Installation started")
        cmd = subprocess.run(["yum", "update", "-y"], capture_output=True, text=True, timeout=600)
    except subprocess.TimeoutExpired:
        logging.error("Command timed out after 600 seconds")
else: 
    logging.info("Unable to identify the OS. Only RedHat and Debian based OS are supported")
    logging.error(f"Program errorred")
    sys.exit(1)  

logging.debug(cmd)


if cmd.returncode != 0:
    logging.error(f"Program errorred with {cmd.stderr} ")
    sys.exit(1)  

elif cmd.returncode == 0:
    logging.info(f"Upgrade successful")
