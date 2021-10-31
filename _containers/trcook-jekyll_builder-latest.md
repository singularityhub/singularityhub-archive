---
id: 996
name: "trcook/jekyll_builder"
branch: "master"
tag: "latest"
commit: "fdb3f53ce55d80c146e27fe8b54bf5de2ba4e3b0"
version: "0f2ff0d46e09f4e34198b99c67b1daef"
build_date: "2017-11-30T18:44:51.672Z"
size_mb: 328
size: 106074143
sif: "https://datasets.datalad.org/shub/trcook/jekyll_builder/latest/2017-11-30-fdb3f53c-0f2ff0d4/0f2ff0d46e09f4e34198b99c67b1daef.simg"
url: https://datasets.datalad.org/shub/trcook/jekyll_builder/latest/2017-11-30-fdb3f53c-0f2ff0d4/
recipe: https://datasets.datalad.org/shub/trcook/jekyll_builder/latest/2017-11-30-fdb3f53c-0f2ff0d4/Singularity
collection: trcook/jekyll_builder
---

# trcook/jekyll_builder:latest

```bash
$ singularity pull shub://trcook/jekyll_builder:latest
```

## Singularity Recipe

```singularity
bootstrap:docker
From:ruby:2.4-alpine


%setup 
mkdir -p ${SINGULARITY_ROOTFS}/work
cp Gemfile ${SINGULARITY_ROOTFS}/work/Gemfile

%files

landing/Gemfile /work
landing/Rakefile /work
landing/_layouts /work
landing/_includes /work
landing/robots.txt /work
landing/assets /work
landing/_base_config.yml /work

%post
export GEM_HOME=/usr/local/bundle
export GEM_HOME=/usr/local/bundle
export BUNDLE_APP_CONFIG=/usr/local/bundle
export BUNDLE_BIN=/usr/local/bundle/bin
export BUNDLE_PATH=/usr/local/bundle
export BUNDLE_SILENCE_ROOT_WARNING=1

apk add --update alpine-sdk
cd /work
adduser -D alpine

# these lines ensures that ruby runs properly for user
chmod -R ugo+rwx /work
chmod -R ugo+rwx /usr/local
chown -R alpine /work
chgrp -R alpine /work

bundle install


%runscript
BACK=$PWD
export BACK
echo $BACK
cp landing/*.md /work
cp -r landing/pages/ /work/pages/
cp -r landing/assets/ /work/assets/
cp landing/_base_config.yml /work
cd /work
echo $(ls)
rake setup local
jekyll build
echo 'deployed'
cp -r _site $BACK/_site
jekyll serve -H 0.0.0.0

%apprun remote
BACK=$PWD
export BACK
echo $BACK
cp landing/*.md /work
cp -r landing/pages/ /work/pages/
cp -r landing/assets/ /work/assets/
cp landing/_base_config.yml /work
cd /work
echo $(ls)
rake setup remote
jekyll build
echo 'deployed'
cp -r _site $BACK/_site
```

## Collection

 - Name: [trcook/jekyll_builder](https://github.com/trcook/jekyll_builder)
 - License: None

