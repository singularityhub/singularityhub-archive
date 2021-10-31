#!/bin/bash

# Incremental script to build
mkdir -p __containers
mkdir -p __collection
mv _containers/*.md __containers/
mv _collection/*.md __collection/
mkdir -p _containers
mkdir -p _collection
for letter in {a..z}; do
    printf "Copying over $letter\n"
    mv __containers/$letter* _containers/
    bundle exec jekyll build --incremental
done
for letter in {a..z}; do
    printf "Copying over collection $letter\n"
    mv __collection/$letter* _collection/
    bundle exec jekyll build --incremental
done

# Move everything else
mv __collection/*.md _collection/
bundle exec jekyll build --incremental
mv __containers/*.md _containers/
bundle exec jekyll build --incremental
rmdir __containers
rmdir __collection

# Final build is needed for main page
bundle exec jekyll build
