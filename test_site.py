#!/usr/bin/env python3
"""
Test script to verify the Jekyll site structure and content.
This ensures the GitHub Pages site will build correctly.
"""

import os
import yaml
import re
from pathlib import Path

def test_config_file():
    """Test that _config.yml exists and is valid YAML."""
    config_path = Path("_config.yml")
    assert config_path.exists(), "_config.yml file not found"
    
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    
    # Check required fields
    required_fields = ['title', 'description', 'baseurl', 'url']
    for field in required_fields:
        assert field in config, f"Required field '{field}' not found in _config.yml"
    
    print("✓ _config.yml is valid and contains required fields")

def test_index_page():
    """Test that index.md exists and has proper front matter."""
    index_path = Path("index.md")
    assert index_path.exists(), "index.md file not found"
    
    with open(index_path, 'r') as f:
        content = f.read()
    
    # Check for front matter
    assert content.startswith('---'), "index.md missing front matter"
    
    # Extract front matter
    front_matter_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    assert front_matter_match, "Invalid front matter format in index.md"
    
    front_matter = yaml.safe_load(front_matter_match.group(1))
    assert 'layout' in front_matter, "index.md missing layout in front matter"
    
    print("✓ index.md is valid with proper front matter")

def test_methods_collection():
    """Test that methods collection exists and contains valid entries."""
    methods_dir = Path("_methods")
    assert methods_dir.exists(), "_methods directory not found"
    
    method_files = list(methods_dir.glob("*.md"))
    assert len(method_files) > 0, "No method files found in _methods directory"
    
    for method_file in method_files:
        with open(method_file, 'r') as f:
            content = f.read()
        
        # Check for front matter
        assert content.startswith('---'), f"{method_file.name} missing front matter"
        
        # Extract and validate front matter
        front_matter_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        assert front_matter_match, f"Invalid front matter format in {method_file.name}"
        
        front_matter = yaml.safe_load(front_matter_match.group(1))
        
        # Check required fields
        required_fields = ['title', 'description', 'category']
        for field in required_fields:
            assert field in front_matter, f"{method_file.name} missing '{field}' in front matter"
    
    print(f"✓ Found {len(method_files)} valid method files in _methods collection")

def test_navigation_pages():
    """Test that main navigation pages exist."""
    nav_pages = ['about.md', 'methods/index.md']
    
    for page in nav_pages:
        page_path = Path(page)
        assert page_path.exists(), f"Navigation page {page} not found"
        
        with open(page_path, 'r') as f:
            content = f.read()
        
        assert content.startswith('---'), f"{page} missing front matter"
    
    print("✓ All navigation pages exist and have front matter")

def test_gemfile():
    """Test that Gemfile exists for Jekyll dependencies."""
    gemfile_path = Path("Gemfile")
    assert gemfile_path.exists(), "Gemfile not found"
    
    with open(gemfile_path, 'r') as f:
        content = f.read()
    
    # Check for essential gems
    assert 'jekyll' in content, "Gemfile missing Jekyll dependency"
    assert 'github-pages' in content, "Gemfile missing github-pages dependency"
    
    print("✓ Gemfile exists with required dependencies")

def test_content_quality():
    """Test that content meets quality standards."""
    # Check that methods reference ACM Digital Library or IEEE
    methods_dir = Path("_methods")
    
    for method_file in methods_dir.glob("*.md"):
        with open(method_file, 'r') as f:
            content = f.read().lower()
        
        # Should reference academic sources
        has_academic_source = any(source in content for source in [
            'acm digital library', 'ieee', 'chi conference', 'ubicomp'
        ])
        
        assert has_academic_source, f"{method_file.name} should reference academic sources"
    
    print("✓ All method files reference appropriate academic sources")

def main():
    """Run all tests."""
    print("Testing HCI Methods Superbook site structure...")
    
    # Change to the correct directory
    os.chdir(Path(__file__).parent)
    
    try:
        test_config_file()
        test_index_page()
        test_methods_collection()
        test_navigation_pages()
        test_gemfile()
        test_content_quality()
        
        print("\n🎉 All tests passed! The site structure is valid.")
        return True
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        return False
    except Exception as e:
        print(f"\n💥 Unexpected error: {e}")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)