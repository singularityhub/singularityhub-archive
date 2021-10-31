---
id: 2557
name: "monaghaa/singularity_git_tutorial"
branch: "master"
tag: "latest"
commit: "b886c6e47665aac28e40605bf0b3a4649046dc31"
version: "fc94c3b44a2353ad3c9cc38d8fc09016"
build_date: "2020-05-15T20:27:29.022Z"
size_mb: 50.0
size: 14241823
sif: "https://datasets.datalad.org/shub/monaghaa/singularity_git_tutorial/latest/2020-05-15-b886c6e4-fc94c3b4/fc94c3b44a2353ad3c9cc38d8fc09016.sif"
url: https://datasets.datalad.org/shub/monaghaa/singularity_git_tutorial/latest/2020-05-15-b886c6e4-fc94c3b4/
recipe: https://datasets.datalad.org/shub/monaghaa/singularity_git_tutorial/latest/2020-05-15-b886c6e4-fc94c3b4/Singularity
collection: monaghaa/singularity_git_tutorial
---

# monaghaa/singularity_git_tutorial:latest

```bash
$ singularity pull shub://monaghaa/singularity_git_tutorial:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:alpine:latest

%labels
MAINTAINER Andy M

%environment
HELLO_BASE=/code
export HELLO_BASE

%runscript
echo "This script is executed when you 'singularity run' the image!" 
exec /bin/sh /code/hello.sh "$@"  

%post  
echo "This section is performed after you bootstrap to build the image."  
apk update
mkdir -p /code  
apk add vim nano bash 
echo "echo Hello World" >> /code/hello.sh
chmod u+x /code/hello.sh
```

## Collection

 - Name: [monaghaa/singularity_git_tutorial](https://github.com/monaghaa/singularity_git_tutorial)
 - License: None

