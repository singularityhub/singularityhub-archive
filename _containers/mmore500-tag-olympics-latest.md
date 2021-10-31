---
id: 10290
name: "mmore500/tag-olympics"
branch: "master"
tag: "latest"
commit: "5453f5a2484d5281e7e2944685c2814c74df9365"
version: "7efd125ae7dc80edafae8528ed855278"
build_date: "2019-07-21T23:27:09.681Z"
size_mb: 877.0
size: 392753183
sif: "https://datasets.datalad.org/shub/mmore500/tag-olympics/latest/2019-07-21-5453f5a2-7efd125a/7efd125ae7dc80edafae8528ed855278.sif"
url: https://datasets.datalad.org/shub/mmore500/tag-olympics/latest/2019-07-21-5453f5a2-7efd125a/
recipe: https://datasets.datalad.org/shub/mmore500/tag-olympics/latest/2019-07-21-5453f5a2-7efd125a/Singularity
collection: mmore500/tag-olympics
---

# mmore500/tag-olympics:latest

```bash
$ singularity pull shub://mmore500/tag-olympics:latest
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
. /opt/tag-olympics

%post
################################################################################
# Install additional packages
################################################################################
apt-get update

# apt-get install -y software-properties-common
# add-apt-repository ppa:ubuntu-toolchain-r/test
# apt-get update
# apt-get install -y gcc-8 g++-8

apt-get install -y git
apt-get install -y build-essential
apt-get install -y make
apt-get install -y python3
apt-get install -y python3-pip

pip3 install numpy
pip3 install matplotlib
pip3 install pandas
pip3 install seaborn

git clone https://github.com/devosoft/Empirical /opt/Empirical -b match-bin

chmod 777 -R /opt

################################################################################
# Run the user's login shell, or a user specified command
################################################################################
%runscript
echo "Nothing here but us birds!"
```

## Collection

 - Name: [mmore500/tag-olympics](https://github.com/mmore500/tag-olympics)
 - License: [MIT License](https://api.github.com/licenses/mit)

