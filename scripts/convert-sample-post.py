#!/usr/bin/env python3
"""
Test script to convert a sample post from TOML to YAML front matter
with PaperMod-specific cover image format.
"""

import os
import re
import sys

def convert_post_frontmatter(input_file, output_file):
    """Convert a single post from TOML to YAML front matter."""
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract TOML frontmatter
    toml_pattern = r'^\+\+\+(.*?)\+\+\+(.*)'
    match = re.match(toml_pattern, content, re.DOTALL)
    
    if not match:
        print(f"No TOML frontmatter found in {input_file}")
        return False
        
    toml_content = match.group(1).strip()
    post_content = match.group(2)
    
    # Extract fields using regex
    yaml_lines = ['---']
    
    # Title
    title_match = re.search(r'title\s*=\s*"([^"]*)"', toml_content)
    if title_match:
        yaml_lines.append(f'title: "{title_match.group(1)}"')
    
    # Author
    author_match = re.search(r'author\s*=\s*"([^"]*)"', toml_content)
    if author_match:
        yaml_lines.append(f'author: "{author_match.group(1)}"')
    
    # Date
    date_match = re.search(r'date\s*=\s*([^\n]+)', toml_content)
    if date_match:
        yaml_lines.append(f'date: {date_match.group(1).strip()}')
    
    # Draft
    draft_match = re.search(r'draft\s*=\s*(true|false)', toml_content)
    if draft_match:
        yaml_lines.append(f'draft: {draft_match.group(1)}')
    
    # Slug
    slug_match = re.search(r'slug\s*=\s*"([^"]*)"', toml_content)
    if slug_match:
        yaml_lines.append(f'slug: "{slug_match.group(1)}"')
    
    # Image -> Cover conversion
    image_match = re.search(r'image\s*=\s*"([^"]*)"', toml_content)
    if image_match:
        yaml_lines.append('cover:')
        yaml_lines.append(f'  image: "{image_match.group(1)}"')
        yaml_lines.append(f'  alt: "{title_match.group(1) if title_match else "Cover image"}"')
        yaml_lines.append('  relative: false')
    
    # Tags
    tags_match = re.search(r'tags\s*=\s*\[(.*?)\]', toml_content, re.DOTALL)
    if tags_match:
        tags_content = tags_match.group(1).strip()
        tags = [tag.strip().strip('"') for tag in tags_content.split(',')]
        yaml_lines.append(f'tags: {tags}')
    
    # Categories
    categories_match = re.search(r'categories\s*=\s*\[(.*?)\]', toml_content, re.DOTALL)
    if categories_match:
        categories_content = categories_match.group(1).strip()
        categories = [cat.strip().strip('"') for cat in categories_content.split(',')]
        yaml_lines.append(f'categories: {categories}')
    
    yaml_lines.append('---')
    
    # Combine YAML frontmatter with post content
    yaml_frontmatter = '\n'.join(yaml_lines)
    new_content = yaml_frontmatter + post_content
    
    # Write converted file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Converted {input_file} -> {output_file}")
    return True

if __name__ == "__main__":
    input_file = "content/posts/blogging-with-hugo.md"
    output_file = "content/posts/blogging-with-hugo-converted.md"
    
    if convert_post_frontmatter(input_file, output_file):
        print("Conversion successful!")
    else:
        print("Conversion failed!")
        sys.exit(1)