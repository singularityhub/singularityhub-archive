---
id: 4098
name: "jasongallant/singular_shockly"
branch: "master"
tag: "latest"
commit: "a390c0ab3a8656791fbd2036c883e18c6eb02fc5"
version: "efe572ec8019e1721d6c30729216c9d1"
build_date: "2018-08-21T21:25:53.529Z"
size_mb: 4768
size: 1887445023
sif: "https://datasets.datalad.org/shub/jasongallant/singular_shockly/latest/2018-08-21-a390c0ab-efe572ec/efe572ec8019e1721d6c30729216c9d1.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jasongallant/singular_shockly/latest/2018-08-21-a390c0ab-efe572ec/
recipe: https://datasets.datalad.org/shub/jasongallant/singular_shockly/latest/2018-08-21-a390c0ab-efe572ec/Singularity
collection: jasongallant/singular_shockly
---

# jasongallant/singular_shockly:latest

```bash
$ singularity pull shub://jasongallant/singular_shockly:latest
```

## Singularity Recipe

```singularity
################################################################################
# Basic bootstrap definition to build CentOS 7 container from Docker container
################################################################################

BootStrap: docker
From: jasongallant/singular_shockly

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

 - Name: [jasongallant/singular_shockly](https://github.com/jasongallant/singular_shockly)
 - License: None

