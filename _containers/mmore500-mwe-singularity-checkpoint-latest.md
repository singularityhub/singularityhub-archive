---
id: 6047
name: "mmore500/mwe-singularity-checkpoint"
branch: "master"
tag: "latest"
commit: "a0fd72d343616754d20ec64a7d03fe105dc199fc"
version: "ef5222109d966a597873ce04ca2b3a7c"
build_date: "2021-01-02T05:24:22.408Z"
size_mb: 521
size: 196026399
sif: "https://datasets.datalad.org/shub/mmore500/mwe-singularity-checkpoint/latest/2021-01-02-a0fd72d3-ef522210/ef5222109d966a597873ce04ca2b3a7c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mmore500/mwe-singularity-checkpoint/latest/2021-01-02-a0fd72d3-ef522210/
recipe: https://datasets.datalad.org/shub/mmore500/mwe-singularity-checkpoint/latest/2021-01-02-a0fd72d3-ef522210/Singularity
collection: mmore500/mwe-singularity-checkpoint
---

# mmore500/mwe-singularity-checkpoint:latest

```bash
$ singularity pull shub://mmore500/mwe-singularity-checkpoint:latest
```

## Singularity Recipe

```singularity
################################################################################
# Basic bootstrap definition to build Ubuntu container from Docker container
################################################################################

Bootstrap:docker
From:ubuntu:latest

%labels
Maintainer Matthew Andres Moreno
Version 0.1.0

################################################################################
# Copy any necessary files into the container
################################################################################
%files
. /opt/mwe-singularity-checkpoint

%post
################################################################################
# Install additional packages
################################################################################
apt-get update

apt-get install -y git
apt-get install -y build-essential
apt-get install -y make
apt-get install -y figlet
git clone https://github.com/mmore500/dmtcp
cd dmtcp
git checkout b8be8be2874258d2f45324a42d609c0c63da0079 .
./configure && make && make install
cd ..

chmod 777 -R /opt

################################################################################
# Run the user's login shell, or a user specified command
################################################################################
%runscript
/opt/mwe-singularity-checkpoint/demonstrate.sh
```

## Collection

 - Name: [mmore500/mwe-singularity-checkpoint](https://github.com/mmore500/mwe-singularity-checkpoint)
 - License: None

