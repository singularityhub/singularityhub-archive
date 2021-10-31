---
id: 710
name: "okuisatoshi/singularity-ijavascript"
branch: "master"
tag: "latest"
commit: "44af6b617f3776113af254bbeecc4bc19dc4cb5d"
version: "ab338864559db9f301b85831c702e49daf44c6ef67ef48f563f8a916fab3fd1b"
build_date: "2020-09-01T02:37:38.224Z"
size_mb: 155.0078125
size: 162537472
sif: "https://datasets.datalad.org/shub/okuisatoshi/singularity-ijavascript/latest/2020-09-01-44af6b61-ab338864/ab338864559db9f301b85831c702e49daf44c6ef67ef48f563f8a916fab3fd1b.sif"
url: https://datasets.datalad.org/shub/okuisatoshi/singularity-ijavascript/latest/2020-09-01-44af6b61-ab338864/
recipe: https://datasets.datalad.org/shub/okuisatoshi/singularity-ijavascript/latest/2020-09-01-44af6b61-ab338864/Singularity
collection: okuisatoshi/singularity-ijavascript
---

# okuisatoshi/singularity-ijavascript:latest

```bash
$ singularity pull shub://okuisatoshi/singularity-ijavascript:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:python:3.7-alpine

%post

apk --update --no-cache add bash alpine-sdk zeromq-dev nodejs npm libffi-dev
pip install jupyter
npm install -g ijavascript

%environment

# export IJS_PORT=8888

# Otherwise, you will encounter the error "Permisson denied /run/user ..."
# See: https://github.com/jupyter/notebook/issues/1318
export XDG_RUNTIME_DIR=""

%runscript

echo "Opening IJavascript (Jupyter) notebook ..."
test -z "$IJS_PORT" && IJS_PORT=8888
/usr/bin/ijs --notebook-dir=. --ip='*' --port=$IJS_PORT --no-browser
```

## Collection

 - Name: [okuisatoshi/singularity-ijavascript](https://github.com/okuisatoshi/singularity-ijavascript)
 - License: None

