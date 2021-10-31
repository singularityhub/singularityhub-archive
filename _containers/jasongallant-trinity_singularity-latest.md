---
id: 3036
name: "jasongallant/trinity_singularity"
branch: "master"
tag: "latest"
commit: "bfb8638109096f6f006def73c7b8d1a007528d62"
version: "2cb388c81dc87eabb748fa148ff8809e"
build_date: "2021-03-23T13:56:59.960Z"
size_mb: 4724
size: 1867632671
sif: "https://datasets.datalad.org/shub/jasongallant/trinity_singularity/latest/2021-03-23-bfb86381-2cb388c8/2cb388c81dc87eabb748fa148ff8809e.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jasongallant/trinity_singularity/latest/2021-03-23-bfb86381-2cb388c8/
recipe: https://datasets.datalad.org/shub/jasongallant/trinity_singularity/latest/2021-03-23-bfb86381-2cb388c8/Singularity
collection: jasongallant/trinity_singularity
---

# jasongallant/trinity_singularity:latest

```bash
$ singularity pull shub://jasongallant/trinity_singularity:latest
```

## Singularity Recipe

```singularity
################################################################################
# Basic bootstrap definition to build CentOS 7 container from Docker container
################################################################################

BootStrap: docker
From: trinityrnaseq/trinityrnaseq

################################################################################
# Copy any necessary files into the container
################################################################################
#%files
#~/my_file /path/in/container

%post
################################################################################
# Install additional login shells for users that need them
################################################################################
#yum -y install tcsh ksh zsh

################################################################################
# Install additional packages
################################################################################
#yum -y install vim

################################################################################
# Create directories to enable access to common HPCC mount points
################################################################################
mkdir -p /mnt/home
mkdir -p /mnt/research
mkdir -p /mnt/dfs17
mkdir -p /mnt/ffs17
mkdir -p /mnt/local
mkdir -p /mnt/gs18
mkdir -p /mnt/ls15
mkdir -p /opt/software

################################################################################
# Run the user's login shell, or a user specified command
################################################################################
%runscript
SHELL="$(getent passwd $USER | awk -F: '{print $NF}')"
SHELL=${SHELL:-/bin/bash}
if [[ "$@" == "" ]]; then
  exec env -i TERM="$TERM" HOME="$HOME" $SHELL -l
else
  exec env -i TERM="$TERM" HOME="$HOME" $@
fi
```

## Collection

 - Name: [jasongallant/trinity_singularity](https://github.com/jasongallant/trinity_singularity)
 - License: None

