---
id: 6226
name: "feilong/neurodebian_singularity"
branch: "master"
tag: "beaver_2019-01-14"
commit: "e82b01d596f02e5145d658fede7711b507cddcb0"
version: "9a7b227060cb09a8bdb6d022978dd929"
build_date: "2019-01-14T23:12:35.723Z"
size_mb: 14485
size: 6600216607
sif: "https://datasets.datalad.org/shub/feilong/neurodebian_singularity/beaver_2019-01-14/2019-01-14-e82b01d5-9a7b2270/9a7b227060cb09a8bdb6d022978dd929.simg"
url: https://datasets.datalad.org/shub/feilong/neurodebian_singularity/beaver_2019-01-14/2019-01-14-e82b01d5-9a7b2270/
recipe: https://datasets.datalad.org/shub/feilong/neurodebian_singularity/beaver_2019-01-14/2019-01-14-e82b01d5-9a7b2270/Singularity
collection: feilong/neurodebian_singularity
---

# feilong/neurodebian_singularity:beaver_2019-01-14

```bash
$ singularity pull shub://feilong/neurodebian_singularity:beaver_2019-01-14
```

## Singularity Recipe

```singularity
BootStrap: docker
From: neurodebian:bionic-non-free

%environment
export FS_LICENSE=${HOME}/FS_license.txt
export FREESURFER_HOME=/apps/freesurfer
source ${FREESURFER_HOME}/SetUpFreeSurfer.sh

. /etc/fsl/5.0/fsl.sh
. /etc/afni/afni.sh

alias emacs="TERM=xterm-256color emacs -nw"
export EDITOR='emacs -nw'
export VISUAL='emacs -nw'
export LANG='en_US.utf8'
export TERM=xterm-256color

export OMP_NUM_THREADS=1

alias ..="cd .."
alias ...='cd ..;cd ..'
{% raw %}PS1="🐙 \e[32m\D{%Y-%m-%d %H:%M:%S} \H:\w\e[0m\n[\W] \$> "{% endraw %}
alias ll="ls -lh --color"
alias ls="ls --color"
alias du='du -ch --max-depth=1'


%runscript
/bin/bash


%post
apt-get update
apt-get upgrade -y
apt-get install -y --no-install-recommends 
apt-get install -y --no-install-recommends adduser
apt-get install -y --no-install-recommends afni
apt-get install -y --no-install-recommends ants
apt-get install -y --no-install-recommends apt
apt-get install -y --no-install-recommends base-files
apt-get install -y --no-install-recommends base-passwd
apt-get install -y --no-install-recommends bash
apt-get install -y --no-install-recommends bsdutils
apt-get install -y --no-install-recommends bzip2
apt-get install -y --no-install-recommends ca-certificates
apt-get install -y --no-install-recommends connectome-workbench
apt-get install -y --no-install-recommends convert3d
apt-get install -y --no-install-recommends coreutils
apt-get install -y --no-install-recommends dash
apt-get install -y --no-install-recommends dcm2niix
apt-get install -y --no-install-recommends debconf
apt-get install -y --no-install-recommends debianutils
apt-get install -y --no-install-recommends diffutils
apt-get install -y --no-install-recommends dirmngr
apt-get install -y --no-install-recommends dpkg
apt-get install -y --no-install-recommends e2fsprogs
apt-get install -y --no-install-recommends emacs-nox
apt-get install -y --no-install-recommends fdisk
apt-get install -y --no-install-recommends findutils
apt-get install -y --no-install-recommends fsl-complete
apt-get install -y --no-install-recommends fsleyes
apt-get install -y --no-install-recommends g++
apt-get install -y --no-install-recommends gcc
apt-get install -y --no-install-recommends gcc-8-base
apt-get install -y --no-install-recommends git
apt-get install -y --no-install-recommends git-annex
apt-get install -y --no-install-recommends gnupg
apt-get install -y --no-install-recommends gpgv
apt-get install -y --no-install-recommends grep
apt-get install -y --no-install-recommends gzip
apt-get install -y --no-install-recommends hostname
apt-get install -y --no-install-recommends imagemagick
apt-get install -y --no-install-recommends init-system-helpers
apt-get install -y --no-install-recommends ipython
apt-get install -y --no-install-recommends ipython3
apt-get install -y --no-install-recommends jupyter
apt-get install -y --no-install-recommends libacl1
apt-get install -y --no-install-recommends libapt-pkg5.0
apt-get install -y --no-install-recommends libattr1
apt-get install -y --no-install-recommends libaudit-common
apt-get install -y --no-install-recommends libaudit1
apt-get install -y --no-install-recommends libblkid1
apt-get install -y --no-install-recommends libbz2-1.0
apt-get install -y --no-install-recommends libc-bin
apt-get install -y --no-install-recommends libc6
apt-get install -y --no-install-recommends libcap-ng0
apt-get install -y --no-install-recommends libcom-err2
apt-get install -y --no-install-recommends libdb5.3
apt-get install -y --no-install-recommends libdebconfclient0
apt-get install -y --no-install-recommends libext2fs2
apt-get install -y --no-install-recommends libfdisk1
apt-get install -y --no-install-recommends libffi6
apt-get install -y --no-install-recommends libgcc1
apt-get install -y --no-install-recommends libgcrypt20
apt-get install -y --no-install-recommends libgmp10
apt-get install -y --no-install-recommends libgnutls30
apt-get install -y --no-install-recommends libgpg-error0
apt-get install -y --no-install-recommends libhdf5-openmpi-100
apt-get install -y --no-install-recommends libhdf5-openmpi-dev
apt-get install -y --no-install-recommends libhogweed4
apt-get install -y --no-install-recommends libidn2-0
apt-get install -y --no-install-recommends liblz4-1
apt-get install -y --no-install-recommends liblzma5
apt-get install -y --no-install-recommends libmount1
apt-get install -y --no-install-recommends libncurses5
apt-get install -y --no-install-recommends libncursesw5
apt-get install -y --no-install-recommends libnettle6
apt-get install -y --no-install-recommends libp11-kit0
apt-get install -y --no-install-recommends libpam-modules
apt-get install -y --no-install-recommends libpam-modules-bin
apt-get install -y --no-install-recommends libpam-runtime
apt-get install -y --no-install-recommends libpam0g
apt-get install -y --no-install-recommends libpcre3
apt-get install -y --no-install-recommends libprocps6
apt-get install -y --no-install-recommends libseccomp2
apt-get install -y --no-install-recommends libselinux1
apt-get install -y --no-install-recommends libsemanage-common
apt-get install -y --no-install-recommends libsemanage1
apt-get install -y --no-install-recommends libsepol1
apt-get install -y --no-install-recommends libsmartcols1
apt-get install -y --no-install-recommends libss2
apt-get install -y --no-install-recommends libstdc++6
apt-get install -y --no-install-recommends libsystemd0
apt-get install -y --no-install-recommends libtasn1-6
apt-get install -y --no-install-recommends libtinfo5
apt-get install -y --no-install-recommends libudev1
apt-get install -y --no-install-recommends libunistring2
apt-get install -y --no-install-recommends libuuid1
apt-get install -y --no-install-recommends libzstd1
apt-get install -y --no-install-recommends locales
apt-get install -y --no-install-recommends login
apt-get install -y --no-install-recommends lsb-base
apt-get install -y --no-install-recommends mawk
apt-get install -y --no-install-recommends mount
apt-get install -y --no-install-recommends mpi-default-dev
apt-get install -y --no-install-recommends mricron
apt-get install -y --no-install-recommends ncurses-base
apt-get install -y --no-install-recommends ncurses-bin
apt-get install -y --no-install-recommends passwd
apt-get install -y --no-install-recommends perl-base
apt-get install -y --no-install-recommends procps
apt-get install -y --no-install-recommends python
apt-get install -y --no-install-recommends python-h5py
apt-get install -y --no-install-recommends python-mpi4py
apt-get install -y --no-install-recommends python-mvpa2
apt-get install -y --no-install-recommends python-pip
apt-get install -y --no-install-recommends python-pprocess
apt-get install -y --no-install-recommends python-setuptools
apt-get install -y --no-install-recommends python-tables
apt-get install -y --no-install-recommends python-wheel
apt-get install -y --no-install-recommends python3
apt-get install -y --no-install-recommends python3-dask
apt-get install -y --no-install-recommends python3-dev
apt-get install -y --no-install-recommends python3-dicom
apt-get install -y --no-install-recommends python3-distributed
apt-get install -y --no-install-recommends python3-funcsigs
apt-get install -y --no-install-recommends python3-future
apt-get install -y --no-install-recommends python3-h5py
apt-get install -y --no-install-recommends python3-joblib
apt-get install -y --no-install-recommends python3-matplotlib
apt-get install -y --no-install-recommends python3-nibabel
apt-get install -y --no-install-recommends python3-nose
apt-get install -y --no-install-recommends python3-numpy
apt-get install -y --no-install-recommends python3-pandas
apt-get install -y --no-install-recommends python3-pip
apt-get install -y --no-install-recommends python3-psutil
apt-get install -y --no-install-recommends python3-pytest
apt-get install -y --no-install-recommends python3-scipy
apt-get install -y --no-install-recommends python3-seaborn
apt-get install -y --no-install-recommends python3-setuptools
apt-get install -y --no-install-recommends python3-sklearn
apt-get install -y --no-install-recommends python3-sklearn-lib
apt-get install -y --no-install-recommends python3-statsmodels
apt-get install -y --no-install-recommends python-mpi4py
apt-get install -y --no-install-recommends python-mvpa2
apt-get install -y --no-install-recommends python-pip
apt-get install -y --no-install-recommends python-pprocess
apt-get install -y --no-install-recommends python-setuptools
apt-get install -y --no-install-recommends python-tables
apt-get install -y --no-install-recommends python-wheel
apt-get install -y --no-install-recommends python3
apt-get install -y --no-install-recommends python3-dask
apt-get install -y --no-install-recommends python3-dev
apt-get install -y --no-install-recommends python3-dicom
apt-get install -y --no-install-recommends python3-distributed
apt-get install -y --no-install-recommends python3-funcsigs
apt-get install -y --no-install-recommends python3-future
apt-get install -y --no-install-recommends python3-h5py
apt-get install -y --no-install-recommends python3-joblib
apt-get install -y --no-install-recommends python3-matplotlib
apt-get install -y --no-install-recommends python3-nibabel
apt-get install -y --no-install-recommends python3-nose
apt-get install -y --no-install-recommends python3-numpy
apt-get install -y --no-install-recommends python3-pandas
apt-get install -y --no-install-recommends python3-pip
apt-get install -y --no-install-recommends python3-psutil
apt-get install -y --no-install-recommends python3-pytest
apt-get install -y --no-install-recommends python3-scipy
apt-get install -y --no-install-recommends python3-seaborn
apt-get install -y --no-install-recommends python3-setuptools
apt-get install -y --no-install-recommends python3-sklearn
apt-get install -y --no-install-recommends python3-sklearn-lib
apt-get install -y --no-install-recommends python3-statsmodels
apt-get install -y --no-install-recommends python3-sympy
apt-get install -y --no-install-recommends python3-tk
apt-get install -y --no-install-recommends python3-vtk7
apt-get install -y --no-install-recommends python3-wheel
apt-get install -y --no-install-recommends sed
apt-get install -y --no-install-recommends sensible-utils
apt-get install -y --no-install-recommends swig
apt-get install -y --no-install-recommends sysvinit-utils
apt-get install -y --no-install-recommends tar
apt-get install -y --no-install-recommends tree
apt-get install -y --no-install-recommends tzdata
apt-get install -y --no-install-recommends ubuntu-keyring
apt-get install -y --no-install-recommends util-linux
apt-get install -y --no-install-recommends wget
apt-get install -y --no-install-recommends xvfb
apt-get install -y --no-install-recommends zlib1g

mkdir -p /apps
chmod a+rX /apps

cd /apps; curl -s ftp://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/6.0.1/freesurfer-Linux-centos6_x86_64-stable-pub-v6.0.1.tar.gz | tar xz

echo "Bootstrapping finished."
```

## Collection

 - Name: [feilong/neurodebian_singularity](https://github.com/feilong/neurodebian_singularity)
 - License: None

