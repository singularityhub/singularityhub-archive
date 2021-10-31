---
id: 1169
name: "singularityhub/sregistry-cli"
branch: "master"
tag: "latest"
commit: "feb34d1a1d68278148263a3e5c2a43db636c1368"
version: "37710369b0653ec5120e2f880693e24a"
build_date: "2019-09-17T07:34:21.910Z"
size_mb: 861
size: 366690335
sif: "https://datasets.datalad.org/shub/singularityhub/sregistry-cli/latest/2019-09-17-feb34d1a-37710369/37710369b0653ec5120e2f880693e24a.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/singularityhub/sregistry-cli/latest/2019-09-17-feb34d1a-37710369/
recipe: https://datasets.datalad.org/shub/singularityhub/sregistry-cli/latest/2019-09-17-feb34d1a-37710369/Singularity
collection: singularityhub/sregistry-cli
---

# singularityhub/sregistry-cli:latest

```bash
$ singularity pull shub://singularityhub/sregistry-cli:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3

# sudo singularity build sregistry.simg Singularity


#######################################
# Global
#######################################

%runscript
    exec /opt/conda/bin/sregistry "$@"


#######################################
# Google Cloud Storage
#######################################

%appenv google-storage
    SREGISTRY_CLIENT=google-storage
    export SREGISTRY_CLIENT
%apprun google-storage
    exec /opt/conda/bin/sregistry "$@"



#######################################
# Google Cloud Drive
#######################################

%appenv google-drive
    SREGISTRY_CLIENT=google-drive
    export SREGISTRY_CLIENT
%apprun google-drive
    exec /opt/conda/bin/sregistry "$@"



#######################################
# Singularity Hub
#######################################

%appenv hub
    SREGISTRY_CLIENT=hub
    export SREGISTRY_CLIENT
%apprun hub
    exec /opt/conda/bin/sregistry "$@"


#######################################
# Singularity Registry
#######################################

%appenv registry
    SREGISTRY_CLIENT=registry
    export SREGISTRY_CLIENT
%apprun registry
    exec /opt/conda/bin/sregistry "$@"


%labels
    maintainer vsochat@stanford.edu

%post
    apt-get update && apt-get install -y git build-essential \
                   libtool \
                   squashfs-tools \
                   autotools-dev \
                   automake \
                   autoconf \
                   uuid-dev \
                   libssl-dev

    /opt/conda/bin/pip install dateutils

    # Install Singularity
    cd /opt && git clone https://www.github.com/singularityware/singularity.git && cd singularity
    ./autogen.sh && ./configure --prefix=/usr/local && make && make install

    # Install SRegistry Global
    cd /opt && git clone https://www.github.com/singularityhub/sregistry-cli
    cd sregistry-cli
    /opt/conda/bin/pip install setuptools

    # This installs all "install extras"
    /opt/conda/bin/pip install -e .
    /opt/conda/bin/pip install -e .[google-drive]
    /opt/conda/bin/pip install -e .[google-storage]
```

## Collection

 - Name: [singularityhub/sregistry-cli](https://github.com/singularityhub/sregistry-cli)
 - License: [GNU Affero General Public License v3.0](https://api.github.com/licenses/agpl-3.0)

