---
id: 1885
name: "jekriske/atom"
branch: "master"
tag: "1.24.0"
commit: "cb287fadb78bc796e6c0a9410013c6f4082d52fd"
version: "a19e82f5313d33ef4643c0c5003ccae7"
build_date: "2018-02-28T17:00:44.642Z"
size_mb: 780
size: 249991199
sif: "https://datasets.datalad.org/shub/jekriske/atom/1.24.0/2018-02-28-cb287fad-a19e82f5/a19e82f5313d33ef4643c0c5003ccae7.simg"
url: https://datasets.datalad.org/shub/jekriske/atom/1.24.0/2018-02-28-cb287fad-a19e82f5/
recipe: https://datasets.datalad.org/shub/jekriske/atom/1.24.0/2018-02-28-cb287fad-a19e82f5/Singularity
collection: jekriske/atom
---

# jekriske/atom:1.24.0

```bash
$ singularity pull shub://jekriske/atom:1.24.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: debian:stretch-slim

%labels
  Maintainer Jeff Kriske

%runscript
  atom "$@"

%post
  apt update && apt upgrade -y
  apt install -y --no-install-recommends \
                 apt-transport-https \
                 ca-certificates \
                 curl \
                 gconf2 \
                 gconf-service \
                 git \
                 gnupg2 \
                 gvfs-bin \
                 libasound2 \
                 libcap2 \
                 libgconf-2-4 \
                 libgtk2.0-0 \
                 libnotify4 \
                 libnss3 \
                 libxkbfile1 \
                 libxss1 \
                 libxtst6 \
                 libgl1-mesa-glx \
                 libgl1-mesa-dri \
                 python \
                 xdg-utils
  curl -L https://packagecloud.io/AtomEditor/atom/gpgkey | apt-key add -
  sh -c 'echo "deb [arch=amd64] https://packagecloud.io/AtomEditor/atom/any/ any main" > /etc/apt/sources.list.d/atom.list'
  apt-get update
  apt-get install -y --no-install-recommends atom
  apt-get clean
  sed -i 's/BIG-REQUESTS/_IG-REQUESTS/' /usr/lib/x86_64-linux-gnu/libxcb.so.1.1.0
  rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [jekriske/atom](https://github.com/jekriske/atom)
 - License: None

