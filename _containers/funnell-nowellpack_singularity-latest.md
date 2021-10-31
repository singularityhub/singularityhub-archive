---
id: 12932
name: "funnell/nowellpack_singularity"
branch: "master"
tag: "latest"
commit: "53d50e1dce9cd61498f2ab08add451f7651455bc"
version: "85088263d3032e08222a573b929a2c34"
build_date: "2021-02-23T03:59:46.495Z"
size_mb: 1838.0
size: 894132255
sif: "https://datasets.datalad.org/shub/funnell/nowellpack_singularity/latest/2021-02-23-53d50e1d-85088263/85088263d3032e08222a573b929a2c34.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/funnell/nowellpack_singularity/latest/2021-02-23-53d50e1d-85088263/
recipe: https://datasets.datalad.org/shub/funnell/nowellpack_singularity/latest/2021-02-23-53d50e1d-85088263/Singularity
collection: funnell/nowellpack_singularity
---

# funnell/nowellpack_singularity:latest

```bash
$ singularity pull shub://funnell/nowellpack_singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: archlinux

%runscript
    echo "Nowellpack"

%environment
    PATH="/opt/nowellpack/build/install/nowellpack/bin:$PATH"
    export PATH
    JAVA_HOME="/usr/lib/jvm/default-runtime"
    export JAVA_HOME

%post
    echo "Nowellpack"

    # set time zone. Use whatever you prefer instead of UTC.
    ln -s /usr/share/zoneinfo/UTC /etc/localtime

    # set locale
    echo 'en_CA.UTF-8 UTF-8' > /etc/locale.gen
    # add more locales as needed, eg:
    locale-gen
    echo 'LANG=en_CA.UTF-8' > /etc/locale.conf

    # set the package mirror server
    echo 'Server = https://mirrors.kernel.org/archlinux/$repo/os/$arch' > /etc/pacman.d/mirrorlist
    # add fail-over servers
    echo 'Server = https://archlinux.honkgong.info/$repo/os/$arch' >> /etc/pacman.d/mirrorlist

    # install dependencies
    pacman -Syu --noconfirm git
    pacman -Syu --noconfirm --needed base-devel
    pacman -Syu --noconfirm jdk8-openjdk
    pacman -Syu --noconfirm xorg-server-xvfb libxrender libxtst libxi jre-openjdk

    # install nowellpack
    mkdir -p /opt
    git clone http://github.com/UBC-Stat-ML/nowellpack.git /opt/nowellpack
    this_dir=$(pwd)
    cd /opt/nowellpack
    ./setup-cli.sh

    # Remove the packages downloaded to Pacman cache dir.
    pacman -Sy --noconfirm pacman-contrib
    paccache -r -k0
```

## Collection

 - Name: [funnell/nowellpack_singularity](https://github.com/funnell/nowellpack_singularity)
 - License: None

