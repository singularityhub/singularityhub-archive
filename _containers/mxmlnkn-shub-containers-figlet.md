---
id: 7548
name: "mxmlnkn/shub-containers"
branch: "master"
tag: "figlet"
commit: "1e68e0b9333632983c8e6ca181d8345125ed855b"
version: "f4507f1bd939e55b6af8074d8cb0cabd"
build_date: "2019-03-01T19:49:14.152Z"
size_mb: 79
size: 34361375
sif: "https://datasets.datalad.org/shub/mxmlnkn/shub-containers/figlet/2019-03-01-1e68e0b9-f4507f1b/f4507f1bd939e55b6af8074d8cb0cabd.simg"
url: https://datasets.datalad.org/shub/mxmlnkn/shub-containers/figlet/2019-03-01-1e68e0b9-f4507f1b/
recipe: https://datasets.datalad.org/shub/mxmlnkn/shub-containers/figlet/2019-03-01-1e68e0b9-f4507f1b/Singularity
collection: mxmlnkn/shub-containers
---

# mxmlnkn/shub-containers:figlet

```bash
$ singularity pull shub://mxmlnkn/shub-containers:figlet
```

## Singularity Recipe

```singularity
BootStrap: docker
From: debian:9-slim

%setup
    echo 'Hello World!' > default-message.txt

%files
    default-message.txt /etc/default-message.txt

%environment
    export DEFAULT_MESSAGE="$( cat /etc/default-message.txt )"

%post
    apt-get update && apt-get -y install figlet

%runscript
    if test $# -eq 0; then
        figlet "$DEFAULT_MESSAGE"
    else
        figlet "$@"
    fi

%test
    if command -v figlet 1>/dev/null 2>&1; then
        echo 'Everything is ok.'
        exit 0
    else
        echo 'Figlet command is missing!'
        exit 1
    fi

%labels
    Author mk@tu-dresden.de
    Version v0.0.1

%help
Microservice for running figlet, a tool for creating ASCII text banners
```

## Collection

 - Name: [mxmlnkn/shub-containers](https://github.com/mxmlnkn/shub-containers)
 - License: None

