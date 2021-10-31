---
id: 5191
name: "whit2333/container12"
branch: "master"
tag: "latest"
commit: "d2a166aac509bad63af32bbfcb77946e80845241"
version: "041f838f21f3cc5f3872437000218d82"
build_date: "2018-10-12T03:09:53.246Z"
size_mb: 3085
size: 1090375711
sif: "https://datasets.datalad.org/shub/whit2333/container12/latest/2018-10-12-d2a166aa-041f838f/041f838f21f3cc5f3872437000218d82.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/whit2333/container12/latest/2018-10-12-d2a166aa-041f838f/
recipe: https://datasets.datalad.org/shub/whit2333/container12/latest/2018-10-12-d2a166aa-041f838f/Singularity
collection: whit2333/container12
---

# whit2333/container12:latest

```bash
$ singularity pull shub://whit2333/container12:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: whit2333/container12:latest

# =======================
# global
# =======================

%help
  container12: a clas12 software container for analysis
  Includes root, hipo_tools, ...

%labels
  Maintainer "Whitney Armstrong"
  Version v0.1


%setup -c /bin/bash
  export SINGULARITY_SHELL=/bin/bash

%post -c /bin/bash
  source /usr/local/bin/thisroot.sh
  echo "Hello from inside the container"
  echo "Install additional software here"

%runscript
  #source /usr/local/bin/thisroot.sh
  /bin/bash "$@"

%environment
  export ROOTSYS=/usr/local
  export PYTHONPATH=/usr/local/lib:${PYTHONPATH}
  export PATH=/usr/local/bin:${PATH}
  export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
  export ROOT_INCLUDE_PATH=/usr/local/include:/usr/local/include/podd:/usr/local/include/hcana


# =======================
# root
# =======================
%apprun root
  #source /usr/local/bin/thisroot.sh
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
  #source /usr/local/bin/thisroot.sh
  root-config "$@"

# =======================
# rootbrowse
# =======================
%apprun rootbrowse
  #source /usr/local/bin/thisroot.sh
  rootbrowse "$@"

# =======================
# rootls
# =======================
%apprun rootls
  #source /usr/local/bin/thisroot.sh
  rootls "$@"

# =======================
# toohip4root
# =======================
%apprun toohip4root
  #source /usr/local/bin/thisroot.sh
  toohip4root "$@"

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
  #source /usr/local/bin/thisroot.sh
  rootls "$@"
```

## Collection

 - Name: [whit2333/container12](https://github.com/whit2333/container12)
 - License: None

