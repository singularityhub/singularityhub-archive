---
id: 6024
name: "whit2333/container_stuff"
branch: "master"
tag: "latest"
commit: "f0f3b77df01dcb44c549fe10f4fd015313368a4a"
version: "a03bc89c955f551dfffdb1f620c22cb6"
build_date: "2018-12-19T23:56:55.604Z"
size_mb: 3086
size: 1081843743
sif: "https://datasets.datalad.org/shub/whit2333/container_stuff/latest/2018-12-19-f0f3b77d-a03bc89c/a03bc89c955f551dfffdb1f620c22cb6.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/whit2333/container_stuff/latest/2018-12-19-f0f3b77d-a03bc89c/
recipe: https://datasets.datalad.org/shub/whit2333/container_stuff/latest/2018-12-19-f0f3b77d-a03bc89c/Singularity
collection: whit2333/container_stuff
---

# whit2333/container_stuff:latest

```bash
$ singularity pull shub://whit2333/container_stuff:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: whit2333/root_base:latest

# =======================
# global
# =======================
%runscript
  source /usr/local/bin/thisroot.sh
  /bin/bash "$@"

%post
  echo "Hello from inside the container"
  echo "Install additional software here"

%help
  Help me. I'm in the container.

%labels
  Maintainer "Whitney Armstrong"
  Version v0.1

%environment
  export PYTHONPATH=/usr/local/lib:${PYTHONPATH}

# =======================
# root-config
# =======================
%apprun root
  source /usr/local/bin/thisroot.sh
  root "$@"

%appenv lolcat
  export PYTHONPATH=/usr/local/lib:$PYTHONPATH
  export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
  BEST_APP=lolcat
  export BEST_APP

# =======================
# root-config
# =======================
%apprun root-config
  source /usr/local/bin/thisroot.sh
  root-config "$@"

# =======================
# cowsay
# =======================
%apprun rootbrowse
  source /usr/local/bin/thisroot.sh
  rootbrowse "$@"

# =======================
# lolcat
# =======================
#%appinstall rootls
#    apt-get -y install lolcat
#
#%appenv lolcat
#    BEST_APP=lolcat
#    export BEST_APP
#
#%apphelp lolcat
#    lolcat is the best app

%apprun rootls
  source /usr/local/bin/thisroot.sh
  rootls "$@"
```

## Collection

 - Name: [whit2333/container_stuff](https://github.com/whit2333/container_stuff)
 - License: None

