from colorama import Fore
import subprocess
import textwrap
import json
import os
import re

class Wayback:
    def __init__(self):
        self.script_path = os.path.abspath(__file__)
        self.script_dir = os.path.dirname(self.script_path)
        self.script_path = re.sub(r"\\", "/", self.script_dir)

    def launch_scan(self, api):
        p = subprocess.Popen(
            ["curl", api],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )
        self.urls = []
        url_count = 0

        for line in p.stdout:
            line = line.strip()
            if "http" in line.lower():
                url_count += 1
                self.urls.append(line)
                print(textwrap.dedent(
                    f"{Fore.RED}[{url_count}] {Fore.WHITE}{line}"
                ))

    def find_scan_type(self, scan)
        with open(f"{self.script_path}/datas/wayback_api.json", "r") as file:
            data = json.load(file)
        try:
            return data[scan]
        except KeyError:
            raise Exception("Scan type could not be determined.")

    def save_output(self, filename):
        cwd = os.getcwd()
        with open(f"{cwd}/{filename}", "w", encoding="utf-8") as file:
            try:
                for i in self.urls:
                    file.write(f"{i}\n")
                print(textwrap.dedent(
                    f"{Fore.GREEN}[+] {Fore.WHITE}Output file created: {filename}"
                ))
            except Exception as e:
                raise Exception(f"Failed to save output: {e}")

api = Wayback()
