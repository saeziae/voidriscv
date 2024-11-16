#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <directory> <output_file>"
    exit 1
fi

# Output file
output_file="$2"
# Clear the output file
>"$output_file"

# Walk through all directories that are not symbolic links
find "$1" -mindepth 1 -maxdepth 1 -type d ! -xtype l | while read -r dir; do
    echo "`basename "$dir"`:" >> "$output_file"
    template_file="$dir/template"
    if grep -q "aarch" "$template_file" && ! grep -q "riscv" "$template_file"; then
        echo "  status: MISSING" >>"$output_file"
    fi

done

echo "Results saved to $output_file"
