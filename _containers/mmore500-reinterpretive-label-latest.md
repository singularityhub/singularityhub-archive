---
id: 3324
name: "mmore500/reinterpretive-label"
branch: "master"
tag: "latest"
commit: "a140e233282ac3eb6407f90fe41df5e481621b8e"
version: "41671c730a764d835c0c9246c42758fe"
build_date: "2019-12-12T20:44:56.637Z"
size_mb: 2304
size: 1707794463
sif: "https://datasets.datalad.org/shub/mmore500/reinterpretive-label/latest/2019-12-12-a140e233-41671c73/41671c730a764d835c0c9246c42758fe.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mmore500/reinterpretive-label/latest/2019-12-12-a140e233-41671c73/
recipe: https://datasets.datalad.org/shub/mmore500/reinterpretive-label/latest/2019-12-12-a140e233-41671c73/Singularity
collection: mmore500/reinterpretive-label
---

# mmore500/reinterpretive-label:latest

```bash
$ singularity pull shub://mmore500/reinterpretive-label:latest
```

## Singularity Recipe

```singularity
################################################################################
# Basic bootstrap definition to build Ubuntu container
################################################################################

Bootstrap: shub
From: singularityhub/ubuntu

%labels
Maintainer Matthew Andres Moreno
Version 0.0.0

################################################################################
# Copy any necessary files into the container
################################################################################
%files
. /opt/reinterpretive-label

%post
################################################################################
# Install additional packages
################################################################################
apt-get clean && apt-get update && apt-get install -y \
    locales \
    language-pack-fi  \
    language-pack-en && \
    export LANGUAGE=en_US.UTF-8 && \
    export LANG=en_US.UTF-8 && \
    export LC_ALL=en_US.UTF-8 && \
    locale-gen en_US.UTF-8 && \
    dpkg-reconfigure locales

apt-get install -y dialog
apt-get install -y apt-utils
apt-get install -y texlive
apt-get install -y texlive-latex-extra
apt-get install -y texlive-xetex
apt-get install -y curl
apt-get install -y fontconfig
apt-get install -y unzip

curl -L https://www.fontsquirrel.com/fonts/download/poppins > poppins.zip
unzip poppins.zip

mkdir /usr/share/fonts/opentype
mv *.otf /usr/share/fonts/opentype

fc-cache -f -v

chmod 777 -R /opt

################################################################################
# Run the user's login shell, or a user specified command
################################################################################
%runscript
xelatex instance
```

## Collection

 - Name: [mmore500/reinterpretive-label](https://github.com/mmore500/reinterpretive-label)
 - License: [MIT License](https://api.github.com/licenses/mit)

