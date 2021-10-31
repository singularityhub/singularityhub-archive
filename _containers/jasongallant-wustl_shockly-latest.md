---
id: 4106
name: "jasongallant/wustl_shockly"
branch: "master"
tag: "latest"
commit: "4c0eaac093688192cd8f50fc4c4418fbb37a23d9"
version: "738938dd6d0857891b001275fe3a0627"
build_date: "2018-08-21T21:25:53.560Z"
size_mb: 4768
size: 1887445023
sif: "https://datasets.datalad.org/shub/jasongallant/wustl_shockly/latest/2018-08-21-4c0eaac0-738938dd/738938dd6d0857891b001275fe3a0627.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jasongallant/wustl_shockly/latest/2018-08-21-4c0eaac0-738938dd/
recipe: https://datasets.datalad.org/shub/jasongallant/wustl_shockly/latest/2018-08-21-4c0eaac0-738938dd/Singularity
collection: jasongallant/wustl_shockly
---

# jasongallant/wustl_shockly:latest

```bash
$ singularity pull shub://jasongallant/wustl_shockly:latest
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
mkdir -p /home
mkdir -p /scratch

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

 - Name: [jasongallant/wustl_shockly](https://github.com/jasongallant/wustl_shockly)
 - License: None

