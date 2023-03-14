from pathlib import Path

directories = [p for p in Path("/run/media/bing/Seagate Portable Drive/series").iterdir() if p.is_dir()]

# Get the number of files in each directory
directory_counts = [(d, len(list(d.glob("*")))) for d in directories]

# Sort the directories based on the number of files
sorted_directories = sorted(directory_counts, key=lambda x: x[1])

# Print the directories in order from the least files to the most files
for directory in sorted_directories:
    print(f"{directory[0].name}: {directory[1]} files")