import os
import subprocess
import shlex
import sys
from typing import Tuple

def execute_system_command(cmd_str: str) -> Tuple[int, str]:
    """
    Executes a shell command across Windows (powershell/cmd) or POSIX systems.
    Returns (returncode, combined_output).
    """
    if not cmd_str.strip():
        return 0, ""

    try:
        if sys.platform == "win32":
            # Run in PowerShell or cmd
            process = subprocess.Popen(
                ["powershell", "-NoProfile", "-Command", cmd_str],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                shell=False
            )
        else:
            process = subprocess.Popen(
                cmd_str,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                shell=True
            )

        stdout, stderr = process.communicate()
        output = stdout + ("\n" + stderr if stderr else "")
        return process.returncode, output.strip()
    except Exception as e:
        return 1, f"Failed to execute command: {str(e)}"
