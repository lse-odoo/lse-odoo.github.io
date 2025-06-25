
# Convert all pictures files in _static folder to avif using mogrify
# This script will skip existing avif files
if [ -d _static ]; then
    find _static -name '*.png' | while read -r file; do
        echo "Converting $file to avif"
        avif_file="${file%.*}.avif"
        if [ ! -e "$avif_file" ]; then
            mogrify -monitor -format avif "$file"
        fi
    done
else
    echo "Error: _static folder not found in current directory. Please run this script from _static parent directory."
fi
