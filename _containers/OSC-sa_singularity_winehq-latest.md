---
id: 11805
name: "OSC/sa_singularity_winehq"
branch: "master"
tag: "latest"
commit: "cd680372ebcd51b9a0a88cca0414d880435c6576"
version: "9a293eb1c4365935f18b99b66dae49a5"
build_date: "2020-09-09T10:30:47.125Z"
size_mb: 1462.0
size: 504950815
sif: "https://datasets.datalad.org/shub/OSC/sa_singularity_winehq/latest/2020-09-09-cd680372-9a293eb1/9a293eb1c4365935f18b99b66dae49a5.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/OSC/sa_singularity_winehq/latest/2020-09-09-cd680372-9a293eb1/
recipe: https://datasets.datalad.org/shub/OSC/sa_singularity_winehq/latest/2020-09-09-cd680372-9a293eb1/Singularity
collection: OSC/sa_singularity_winehq
---

# OSC/sa_singularity_winehq:latest

```bash
$ singularity pull shub://OSC/sa_singularity_winehq:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:18.04

%labels
    Maintainer zyou@osc.edu
    Recipe https://github.com/OSC/sa_singularity_winehq

%post
    apt update
    apt upgrade -y
    dpkg --add-architecture i386 
    DEBIAN_FRONTEND=noninteractive apt install -y software-properties-common wget
    wget -nc https://dl.winehq.org/wine-builds/winehq.key
    apt-key add winehq.key

    apt-add-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ bionic main'
    apt update
    # https://askubuntu.com/questions/1145473/how-do-i-install-libfaudio0 
    # Beginning with Wine 4.5 the wine-devel packages from WineHQ require libfaudio0 as a dependency.
    wget -nc https://download.opensuse.org/repositories/Emulators:/Wine:/Debian/xUbuntu_18.04/amd64/libfaudio0_19.07-0~bionic_amd64.deb
    wget -nc https://download.opensuse.org/repositories/Emulators:/Wine:/Debian/xUbuntu_18.04/i386/libfaudio0_19.07-0~bionic_i386.deb
    dpkg -i libfaudio0_19.07-0~bionic_amd64.deb libfaudio0_19.07-0~bionic_i386.deb || true
    DEBIAN_FRONTEND=noninteractive apt install -f -y
    DEBIAN_FRONTEND=noninteractive apt install -y winehq-stable=5.0.0~bionic

    # Clean up
    apt autoclean
    apt autoremove --purge -y
    rm -rf /var/lib/apt/lists/*

%runscript
    exec wine64 "$@"
```

## Collection

 - Name: [OSC/sa_singularity_winehq](https://github.com/OSC/sa_singularity_winehq)
 - License: [MIT License](https://api.github.com/licenses/mit)

