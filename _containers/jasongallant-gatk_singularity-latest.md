---
id: 1864
name: "jasongallant/gatk_singularity"
branch: "master"
tag: "latest"
commit: "1682987ef17596fa00a9253b253a891b96c07f23"
version: "d82649e7f6322ecc7bf2a942fc9029a2"
build_date: "2021-04-08T07:44:39.139Z"
size_mb: 5090
size: 2543775775
sif: "https://datasets.datalad.org/shub/jasongallant/gatk_singularity/latest/2021-04-08-1682987e-d82649e7/d82649e7f6322ecc7bf2a942fc9029a2.simg"
url: https://datasets.datalad.org/shub/jasongallant/gatk_singularity/latest/2021-04-08-1682987e-d82649e7/
recipe: https://datasets.datalad.org/shub/jasongallant/gatk_singularity/latest/2021-04-08-1682987e-d82649e7/Singularity
collection: jasongallant/gatk_singularity
---

# jasongallant/gatk_singularity:latest

```bash
$ singularity pull shub://jasongallant/gatk_singularity:latest
```

## Singularity Recipe

```singularity
################################################################################
# Basic bootstrap definition to build CentOS 7 container from Docker container
################################################################################

BootStrap: docker
From: broadinstitute/gatk

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

 - Name: [jasongallant/gatk_singularity](https://github.com/jasongallant/gatk_singularity)
 - License: None

