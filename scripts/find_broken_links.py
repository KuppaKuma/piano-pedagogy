import os
import re

# Resolve the repository path (one level above this script)
repo_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Collect all existing markdown file basenames (case-insensitive)
existing_notes = set()
for root, dirs, files in os.walk(repo_path):
    # Skip .git, .obsidian, and .archive_original
    if any(p in root for p in [".git", ".obsidian", ".archive_original"]):
        continue
    for f in files:
        if f.endswith(".md"):
            existing_notes.add(os.path.splitext(f)[0].lower())

print(f"Total existing notes found in repository: {len(existing_notes)}")

# Patterns to find wiki-links: [[Link]] or [[Link|Display]] or [[Link#Header]]
link_pattern = re.compile(r'\[\[(.*?)\]\]')

broken_links = []

for root, dirs, files in os.walk(repo_path):
    if any(p in root for p in [".git", ".obsidian", ".archive_original"]):
        continue
    for f in files:
        if f.endswith(".md"):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8', errors='ignore') as fh:
                content = fh.read()
            
            matches = link_pattern.findall(content)
            for m in matches:
                # Remove display name or heading anchor if any
                target = m.split("|")[0].split("#")[0].strip()
                if not target:
                    continue
                
                target_lower = target.lower()
                target_base = os.path.splitext(os.path.basename(target))[0].lower()
                
                if target_lower not in existing_notes and target_base not in existing_notes:
                    # Check if it is a common attachment extension
                    if any(target_lower.endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.gif', '.webp', '.pdf', '.svg']):
                        continue
                    broken_links.append((path, m))

if broken_links:
    print(f"\nFound {len(broken_links)} potential broken links:")
    for path, link in broken_links:
        rel_path = os.path.relpath(path, repo_path)
        print(f"- {rel_path}: [[{link}]]")
else:
    print("\nNo broken links found!")
