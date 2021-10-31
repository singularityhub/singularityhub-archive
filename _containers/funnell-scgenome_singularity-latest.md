---
id: 13113
name: "funnell/scgenome_singularity"
branch: "master"
tag: "latest"
commit: "2fd3586dd06bb49486e976ccb8ebbd6395423db3"
version: "3660863302d5e3323ac9804731f9d9d5"
build_date: "2020-05-26T16:13:13.731Z"
size_mb: 2276.0
size: 912261151
sif: "https://datasets.datalad.org/shub/funnell/scgenome_singularity/latest/2020-05-26-2fd3586d-36608633/3660863302d5e3323ac9804731f9d9d5.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/funnell/scgenome_singularity/latest/2020-05-26-2fd3586d-36608633/
recipe: https://datasets.datalad.org/shub/funnell/scgenome_singularity/latest/2020-05-26-2fd3586d-36608633/Singularity
collection: funnell/scgenome_singularity
---

# funnell/scgenome_singularity:latest

```bash
$ singularity pull shub://funnell/scgenome_singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: archlinux

%runscript
    echo "scgenome"

%environment
    export PATH=/opt/miniconda3/bin:$PATH

%post
    echo "scgenome"

    # set time zone
    ln -s /usr/share/zoneinfo/UTC /etc/localtime

    # set locale
    echo 'en_US.UTF-8 UTF-8' > /etc/locale.gen
    locale-gen
    echo 'LANG=en_US.UTF-8' > /etc/locale.conf

    # set the package mirror server
    echo 'Server = https://mirrors.kernel.org/archlinux/$repo/os/$arch' > \
        /etc/pacman.d/mirrorlist
    # add fail-over servers
    echo 'Server = https://archlinux.honkgong.info/$repo/os/$arch' >> \
        /etc/pacman.d/mirrorlist

    # install arch packages
    pacman -Syu --noconfirm wget
    pacman -Syu --noconfirm unzip
    pacman -Syu --noconfirm --needed base-devel
    pacman -Syu --noconfirm git

    # install miniconda
    wget https://repo.anaconda.com/miniconda/Miniconda3-py37_4.8.2-Linux-x86_64.sh
    bash Miniconda3-py37_4.8.2-Linux-x86_64.sh -bfp /opt/miniconda3
    rm -f Miniconda3-py37_4.8.2-Linux-x86_64.sh
    export PATH=/opt/miniconda3/bin:$PATH

    # install scgenome and dependencies
    wget https://codeload.github.com/shahcompbio/scgenome/zip/master -O scgenome.zip
    unzip scgenome.zip
    cd scgenome-master
    pip install numpy cython
    pip install -r requirements.txt
    pip install numpy cython umap matplotlib --upgrade
    python setup.py install

    # Remove the packages downloaded to Pacman cache dir.
    pacman -Syu --noconfirm pacman-contrib
    paccache -r -k0
```

## Collection

 - Name: [funnell/scgenome_singularity](https://github.com/funnell/scgenome_singularity)
 - License: None

