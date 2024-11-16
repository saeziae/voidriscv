#!/usr/bin/env python3

import yaml

data = {}
with open("data.yaml", "r", encoding="utf-8") as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

# Prepare Markdown table
md_table = "| Name | Status | Notes |\n"
md_table += "| :- | :- | :- |\n"

for name, details in data.items():
    status = details.get("status", "") if isinstance(details, dict) else ""
    notes = details.get("notes", "") if isinstance(details, dict) else ""
    md_table += f"| {name} | {status} | {notes} |\n"

header = ""
with open("template.md", "r", encoding="utf-8") as file:
    header = file.read()

# Write to file
with open("README.md", "w", encoding="utf-8") as file:
    file.write(header)
    file.write(md_table)
