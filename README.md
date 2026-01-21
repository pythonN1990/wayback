<h1 align="center">Wayback</h1>

<p align="center">
  <b>Historical URL discovery tool powered by the Wayback Machine</b>
</p>

<p align="center">
  <a href="https://github.com/pythonN1990/wayback/actions">
    <img src="https://img.shields.io/badge/build-demo-lightgrey">
  </a>
  <a href="https://github.com/pythonN1990/wayback">
    <img src="https://img.shields.io/github/stars/pythonN1990/wayback?style=flat">
  </a>
  <a href="https://github.com/pythonN1990/wayback/blob/main/LICENSE">
  <img src="https://img.shields.io/badge/license-MIT-blue">
</a>
  <img src="https://img.shields.io/badge/python-3.x-blue">
</p>

---

## Overview

**Wayback** is a CLI-based OSINT and reconnaissance tool that collects historical URLs from the Wayback Machine and prepares them for security testing workflows.

It is designed to be fast, simple, and automation-friendly.  
This repository currently provides a **demo release**, with core functionality implemented and v1 under active development.

---

## Features

- Fetch archived URLs from the Wayback Machine
- Multiple scan modes via predefined API templates
- Clean, CLI-friendly output
- Output export to file
- Designed for chaining with other security tools

---

## Installation

Clone the repository:

```bash
git clone https://github.com/pythonN1990/wayback.git
```
```bash
cd wayback
```
Install requirements:

```bash
pip install -r requirements.txt
```
Usage
Basic scan:

```bash
python main.py -u example.com
```
Specify scan type:

```bash
python main.py -u example.com -s {scan_type}
```
Save output to file:

```bash
python main.py -u example.com -o urls.txt
```
Silent mode:

```bash
python main.py -u example.com --silent
```
Example Output
<p align="center"> <img src="assets/output-preview.png" width="700" alt="Wayback Output Preview"> </p>

Use Cases
Reconnaissance during penetration testing

Bug bounty endpoint discovery

Historical attack surface analysis

