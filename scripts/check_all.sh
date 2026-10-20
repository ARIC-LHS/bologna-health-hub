#!/usr/bin/env bash

set -e

echo "== Validate data =="
python scripts/validate_data.py

echo "== Generate pages =="
python scripts/generate_pages.py

echo "== Verify generated wrappers =="
git diff --exit-code -- topics researchers

echo "== Build Jekyll =="
bundle exec jekyll build --trace

echo "== Done =="