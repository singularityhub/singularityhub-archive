---
id: 2289
name: "jekriske/vscode"
branch: "master"
tag: "latest"
commit: "385d887fc38c95d114d39d22c2cceeb405a8fc9d"
version: "222a9a73c5e7222e8a69a9b02d91be37"
build_date: "2020-06-30T18:54:02.867Z"
size_mb: 887
size: 279441439
sif: "https://datasets.datalad.org/shub/jekriske/vscode/latest/2020-06-30-385d887f-222a9a73/222a9a73c5e7222e8a69a9b02d91be37.simg"
url: https://datasets.datalad.org/shub/jekriske/vscode/latest/2020-06-30-385d887f-222a9a73/
recipe: https://datasets.datalad.org/shub/jekriske/vscode/latest/2020-06-30-385d887f-222a9a73/Singularity
collection: jekriske/vscode
---

# jekriske/vscode:latest

```bash
$ singularity pull shub://jekriske/vscode:latest
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: bionic
MirrorURL:  http://us.archive.ubuntu.com/ubuntu/
Include: ca-certificates curl git

%post
  mkdir -p /run/user /run/dbus
  chmod 1777 /run/user /run/dbus
  echo "deb http://us.archive.ubuntu.com/ubuntu bionic universe" >> /etc/apt/sources.list
  echo "deb http://us.archive.ubuntu.com/ubuntu bionic-security main" >> /etc/apt/sources.list
  apt update && apt install -y apt-transport-https gnupg2
  curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
  mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg
  echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list
  apt update
  apt install -y overlay-scrollbar-gtk2 \
                 libatk-bridge2.0 \
                 libcanberra-gtk-module \
                 unity-gtk2-module \
                 gtk2-engines-murrine \
                 language-pack-en-base \
                 libgail-3-0 \
                 libatk-adaptor \
                 libgail-common \
                 libgl1-mesa-glx \
                 libxss1 \
                 libgtk2.0-0 \
                 libasound2 \
                 code
  apt upgrade -y
  apt clean
  rm -rf /var/lib/apt/lists/*

%runscript
  exec code "$@"
```

## Collection

 - Name: [jekriske/vscode](https://github.com/jekriske/vscode)
 - License: None

