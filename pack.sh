
#!/bin/bash

# A script to prepare python task files for submission.
# It copies task*.py files, removes comments, zips them, and cleans up.

# Exit immediately if a command exits with a non-zero status.
set -e

# --- Configuration ---
SOLUTION_DIR="merged/"
GLOB_PATTERN="task*.py"
OUTPUT_ZIP="submission.zip"

# --- Pre-flight Checks ---

# Check if any files match the glob pattern.
# 'shopt -s nullglob' makes the glob expand to nothing if no files match.
shopt -s nullglob
files=($SOLUTION_DIR/$GLOB_PATTERN)
if [ ${#files[@]} -eq 0 ]; then
    echo "Warning: No files found matching '$GLOB_PATTERN'. Exiting."
    exit 0
fi
shopt -u nullglob # Revert to default glob behavior

# --- Main Logic ---

# 1. Create a secure, temporary directory
# mktemp -d creates a unique directory in /tmp/ and prints its name.
TEMP_DIR=$(mktemp -d)
echo "✅ Created temporary folder: $TEMP_DIR"

# 2. Set up a trap to ensure the temporary folder is removed on script exit
# This runs whether the script succeeds, fails, or is interrupted (Ctrl+C).
trap 'echo "🧹 Cleaning up temporary folder..."; rm -r "$TEMP_DIR"' EXIT

# 2.5 merge
python merge.py

# 3. Copy all matching files to the temporary folder
echo "📂 Copying files..."
cp $SOLUTION_DIR/$GLOB_PATTERN "$TEMP_DIR/"

# 4. Remove all lines that start with '#' and empty lines from each file in the temp folder
echo "✏️  Removing commented lines from copies..."
for file in "$TEMP_DIR"/$GLOB_PATTERN; do
    tmpfile=$(mktemp)
    python code_golf_utils/compile.py < "$file" > "$tmpfile"
    mv "$tmpfile" "$file"
    echo "   - Processed $(basename "$file")"
done

# 5. Zip the modified files into submissions.zip
echo "📦 Zipping files into $OUTPUT_ZIP..."
# We use a subshell ( ... ) to change directories temporarily.
# This way, the zip file contains clean filenames (e.g., "task1.py")
# instead of full paths (e.g., "tmp/tmp.XyZaBc/task1.py").
cd "$TEMP_DIR"
wc -c *.py | grep -v total | python "$OLDPWD/format_scores.py" > "$OLDPWD/scores.txt"
rm -f "$OLDPWD/$OUTPUT_ZIP"
zip "$OLDPWD/$OUTPUT_ZIP" *.py

# The trap will automatically run now to remove the temporary folder.
echo "🎉 Done! Your submission file is ready: $OUTPUT_ZIP"
