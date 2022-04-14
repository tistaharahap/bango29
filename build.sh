#!/bin/sh
export BASE_URL="${HUGO_URL:-https://bango29.com}"
echo "URL: ${BASE_URL}"

hugo -D -c content --minify -b $BASE_URL
