#!/usr/bin/env bash
set -e

pkill -f "jekyll serve" 2>/dev/null || true

bundle exec jekyll serve \
  --host 0.0.0.0 \
  --port 4000 \
  --baseurl ""
