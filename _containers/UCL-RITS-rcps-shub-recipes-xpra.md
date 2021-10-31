---
id: 4245
name: "UCL-RITS/rcps-shub-recipes"
branch: "master"
tag: "xpra"
commit: "3bc31a6230e1c4f961770f20a0a118082e250678"
version: "4b875ab0c0a52fc710de0be77372cb59"
build_date: "2018-11-07T13:35:06.730Z"
size_mb: 871
size: 372523039
sif: "https://datasets.datalad.org/shub/UCL-RITS/rcps-shub-recipes/xpra/2018-11-07-3bc31a62-4b875ab0/4b875ab0c0a52fc710de0be77372cb59.simg"
url: https://datasets.datalad.org/shub/UCL-RITS/rcps-shub-recipes/xpra/2018-11-07-3bc31a62-4b875ab0/
recipe: https://datasets.datalad.org/shub/UCL-RITS/rcps-shub-recipes/xpra/2018-11-07-3bc31a62-4b875ab0/Singularity
collection: UCL-RITS/rcps-shub-recipes
---

# UCL-RITS/rcps-shub-recipes:xpra

```bash
$ singularity pull shub://UCL-RITS/rcps-shub-recipes:xpra
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: bionic
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%environment
# Sets up environment for module use
#  --> requires /shared to be bound
MODULE_VERSION=3.2.6
MODULEPATH=/shared/ucl/apps/modulefiles/core:/shared/ucl/apps/modulefiles/applications:/shared/ucl/apps/modulefiles/libraries:/shared/ucl/apps/modulefiles/compilers:/shared/ucl/apps/modulefiles/development:/shared/ucl/apps/modulefiles/bundles
MODULE_VERSION_STACK=3.2.6
MODULESHOME=/shared/ucl/apps/modules/3.2.6/Modules/3.2.6
export MODULE_VERSION MODULEPATH MODULE_VERSION_STACK MODULESHOME
module () 
{ 
    eval `/shared/ucl/apps/modules/3.2.6/Modules/$MODULE_VERSION/bin/modulecmd bash $*`
}

%post
  cat >>/etc/apt/sources.list <<EOF
deb http://us.archive.ubuntu.com/ubuntu/ bionic main restricted
deb http://us.archive.ubuntu.com/ubuntu/ bionic-updates main restricted
deb http://us.archive.ubuntu.com/ubuntu/ bionic universe
deb http://us.archive.ubuntu.com/ubuntu/ bionic-updates universe
deb http://us.archive.ubuntu.com/ubuntu/ bionic multiverse
deb http://us.archive.ubuntu.com/ubuntu/ bionic-updates multiverse
deb http://us.archive.ubuntu.com/ubuntu/ bionic-backports main restricted universe multiverse
deb http://security.ubuntu.com/ubuntu bionic-security main restricted
deb http://security.ubuntu.com/ubuntu bionic-security universe
deb http://security.ubuntu.com/ubuntu bionic-security multiverse
EOF
        apt-get -y update
	# Numpy is apparently required for certain parts of Xpra to work properly
        apt-get -y install xpra xterm less python-numpy python3-numpy 
        printf "#!/bin/sh\nxpra start --systemd-run=no --user=\$USER --start-via-proxy=no --start-on-connect=xterm --notifications=no \"\$@\"\n"  >> /usr/bin/custom-xpra-server-start
        printf "#!/bin/sh\nxpra attach --opengl=no --no-printing --notifications=no --webcam=no\n \"\$@\"" >> /usr/bin/custom-xpra-attach
        chmod +x /usr/bin/custom-xpra-server-start /usr/bin/custom-xpra-attach

%help
This is a Singularity container intended to run Xpra on UCL central HPC clusters.

It is Ubuntu-based, and contains an installation of Xpra and two scripts to abbreviate some awkward commands:

    custom-xpra-server-start
    custom-xpra-attach
```

## Collection

 - Name: [UCL-RITS/rcps-shub-recipes](https://github.com/UCL-RITS/rcps-shub-recipes)
 - License: [MIT License](https://api.github.com/licenses/mit)

