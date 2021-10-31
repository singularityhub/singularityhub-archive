---
id: 2479
name: "mmore500/automap-soro"
branch: "master"
tag: "latest"
commit: "0542395c758610a05de152a8f4d366287383b785"
version: "85bf24ec0cc43b541eacbd358f858ee1"
build_date: "2019-07-27T17:56:20.222Z"
size_mb: 1106
size: 433889311
sif: "https://datasets.datalad.org/shub/mmore500/automap-soro/latest/2019-07-27-0542395c-85bf24ec/85bf24ec0cc43b541eacbd358f858ee1.simg"
url: https://datasets.datalad.org/shub/mmore500/automap-soro/latest/2019-07-27-0542395c-85bf24ec/
recipe: https://datasets.datalad.org/shub/mmore500/automap-soro/latest/2019-07-27-0542395c-85bf24ec/Singularity
collection: mmore500/automap-soro
---

# mmore500/automap-soro:latest

```bash
$ singularity pull shub://mmore500/automap-soro:latest
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
Version 0.0.0

################################################################################
# Copy any necessary files into the container
################################################################################
%files
. /opt/automap-soro

%post
################################################################################
# Install additional packages
################################################################################
apt-get update

apt-get install -y libqt4-dev qt4-qmake libqwt-dev freeglut3-dev zlib1g-dev

apt-get install -y python
apt-get install -y python-setuptools python-dev build-essential python-pip
export LC_ALL=C
pip install scipy networkx==1.11

apt-get install -y git
git clone https://github.com/skriegman/evosoro.git /opt/evosoro
cd /opt/evosoro/evosoro/_voxcad/
./rebuild_everything.sh

cd Voxelyze
make
make installusr
cd ../voxelyzeMain/
make

chmod 777 -R /opt

################################################################################
# Create directories to enable access to common HPCC mount points
################################################################################
mkdir -p /mnt/home
mkdir -p /mnt/research
mkdir -p /mnt/dfs17
mkdir -p /mnt/ffs17
mkdir -p /mnt/local
mkdir -p /mnt/ls15
mkdir -p /opt/software
mkdir -p /mnt/scratch

################################################################################
# Run the user's login shell, or a user specified command
################################################################################
%runscript
exec "$@"
```

## Collection

 - Name: [mmore500/automap-soro](https://github.com/mmore500/automap-soro)
 - License: [MIT License](https://api.github.com/licenses/mit)

