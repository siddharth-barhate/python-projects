# Linux OS Patching Automation 

This repository contains a Python script that automates basic operating system package updates on Linux systems.
It is designed as a **learning exercise** to understand OS automation, subprocess execution, logging, and failure handling from an SRE/DevOps perspective.

---

## What this script does

* Verifies the system is running Linux
* Detects the OS family (Debian-based or RedHat-based)
* Ensures the script is executed with root privileges
* Runs the appropriate package update command:

  * Debian-based: `apt update && apt upgrade -y`
  * RedHat-based: `yum update -y`
* Applies a timeout to prevent hanging executions
* Logs execution details, success, and failure states
* Exits with proper status codes for automation compatibility

---

## Important note ⚠️

**The package update commands used in this script are for learning purposes only.**

In real production environments:

* OS patching is usually handled via configuration management tools (Ansible, Chef, Puppet)
* Or through immutable infrastructure pipelines (AMI baking, image builds)
* Additional safeguards such as reboots, rollbacks, and staged deployments are required

This script is intentionally simple to focus on **automation fundamentals**, not full production patch management.

---

## Requirements

* Linux OS
* Python 3.12+
* Root privileges

---

## How to run

```bash
sudo python3 linux_os_patching.py
```

Logs will be written to `applog.log` in the current working directory.

---

## What this script demonstrates

* Running system commands from Python using `subprocess`
* Handling exit codes and timeouts
* Defensive OS detection
* Explicit privilege enforcement
* Structured logging with configurable verbosity
* Writing automation that fails fast and predictably


---

## Disclaimer

Use at your own risk.
Do not run on production systems without proper validation and safeguards.
