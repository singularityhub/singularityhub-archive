---
id: 3557
name: "federatedcloud/NixTemplates"
branch: "master"
tag: "base_alpine"
commit: "986d6260809ad5d7cd02fcac1a3a55f0efa88928"
version: "c3d67c7d2f88b37236f721e52e083472"
build_date: "2018-07-16T20:47:11.179Z"
size_mb: 300
size: 53358623
sif: "https://datasets.datalad.org/shub/federatedcloud/NixTemplates/base_alpine/2018-07-16-986d6260-c3d67c7d/c3d67c7d2f88b37236f721e52e083472.simg"
url: https://datasets.datalad.org/shub/federatedcloud/NixTemplates/base_alpine/2018-07-16-986d6260-c3d67c7d/
recipe: https://datasets.datalad.org/shub/federatedcloud/NixTemplates/base_alpine/2018-07-16-986d6260-c3d67c7d/Singularity
collection: federatedcloud/NixTemplates
---

# federatedcloud/NixTemplates:base_alpine

```bash
$ singularity pull shub://federatedcloud/NixTemplates:base_alpine
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: alpine:3.7

%environment
export BASEIMG=alpine:3.7
export ENVSDIR=/nixenv/nixuser
export PATH=/nixenv/nixuser/.nix-profile/bin:/nixenv/nixuser/.nix-profile/sbin:/bin:/sbin:/usr/bin:/usr/sbin
export GIT_SSL_CAINFO=/etc/ssl/certs/ca-certificates.crt
export NIX_SSL_CERT_FILE=$GIT_SSL_CAINFO
export NIX_PATH=/nix/var/nix/profiles/per-user/$USER/channels/
export nixenv=". /nixenv/nixuser/.nix-profile/etc/profile.d/nix.sh"

%setup
mkdir -p $SINGULARITY_ROOTFS/template/hometmp/.config/nixpkgs
mkdir -p $SINGULARITY_ROOTFS//nixenv/nixuser

%files
./alpine_install_cmds.sh /template/
./config.nix /template/hometmp/.config/nixpkgs/

%labels
MAINTAINER Brandon Barker <brandon.barker@cornell.edu>

%post

ENVSDIR=/nixenv/nixuser

mkdir -p /run/user
mkdir -m 0755 /nix

cd /nixenv/nixuser

/template/alpine_install_cmds.sh

#
# This only matters if nix is run as root:
#
echo "nixbld:x:30000:nixbld1,nixbld2,nixbld3,nixbld4,nixbld5,nixbld6,nixbld7,nixbld8,nixbld9,nixbld10,nixbld11,nixbld12,nixbld13,nixbld14,nixbld15,nixbld16,nixbld17,nixbld18,nixbld19,nixbld20,nixbld21,nixbld22,nixbld23,nixbld24,nixbld25,nixbld26,nixbld27,nixbld28,nixbld29,nixbld30" >> /etc/group \
&& for i in $(seq 1 30); do echo "nixbld$i:x:$((30000 + $i)):30000:::" >> /etc/passwd; done

wget -O- http://nixos.org/releases/nix/nix-2.0.4/nix-2.0.4-x86_64-linux.tar.bz2 | bzcat - | tar xf - \
&& USER=nobody HOME=/nixenv/nixuser sh nix-*-x86_64-linux/install 

chmod -R a+rw /nixenv/nixuser

#
# This broke at some point, so trying system certs for now:
# GIT_SSL_CAINFO=/nixenv/nixuser/.nix-profile/etc/ssl/certs/ca-bundle.crt \
# 
PATH=/nixenv/nixuser/.nix-profile/bin:/nixenv/nixuser/.nix-profile/sbin:/bin:/sbin:/usr/bin:/usr/sbin
GIT_SSL_CAINFO=/etc/ssl/certs/ca-certificates.crt
NIX_SSL_CERT_FILE=$GIT_SSL_CAINFO
  
nixenv=". /nixenv/nixuser/.nix-profile/etc/profile.d/nix.sh"

chmod -R a+rw /nix
chmod a+rwx /run/user

%runscript

USER=$(whoami)
echo "runscript user is $USER"

if [ ! -f ${HOME}/.config/nixpkgs ]; then
  mkdir -p $HOME/.config/nixpkgs
  cp -R /template/hometmp/.config/nixpkgs/* $HOME/.config/nixpkgs/
fi


if [ ! -f /run/user/$(id -u $USER) ]; then
  #  chown $USER:$USER /run/user/$(id -u $USER) &&
  mkdir -p /run/user/$(id -u $USER) && \
  ln -s /nix/var/nix/profiles/per-user/$USER/profile $HOME/.nix-profile
fi

if [ ! -f "/nix/var/nix/profiles/per-user/$USER/channels" ]; then
  $nixenv && nix-channel --add https://nixos.org/channels/nixpkgs-unstable nixpkgs && \
  nix-channel --add https://nixos.org/channels/nixos-unstable nixos
  $nixenv && nix-channel --update
fi

export NIX_PATH="/nix/var/nix/profiles/per-user/$USER/channels/"

exec /bin/sh "$@"
```

## Collection

 - Name: [federatedcloud/NixTemplates](https://github.com/federatedcloud/NixTemplates)
 - License: [BSD 3-Clause "New" or "Revised" License](https://api.github.com/licenses/bsd-3-clause)

