---
id: 3564
name: "verysure/miniconda3-rdkit-dftb"
branch: "master"
tag: "17"
commit: "0fe0b0648d4f9202378569479a5a517333ebf4d7"
version: "5c16a9d8093aa2316b3ac653b8aa52be"
build_date: "2018-07-17T22:43:33.742Z"
size_mb: 2550
size: 829599775
sif: "https://datasets.datalad.org/shub/verysure/miniconda3-rdkit-dftb/17/2018-07-17-0fe0b064-5c16a9d8/5c16a9d8093aa2316b3ac653b8aa52be.simg"
url: https://datasets.datalad.org/shub/verysure/miniconda3-rdkit-dftb/17/2018-07-17-0fe0b064-5c16a9d8/
recipe: https://datasets.datalad.org/shub/verysure/miniconda3-rdkit-dftb/17/2018-07-17-0fe0b064-5c16a9d8/Singularity
collection: verysure/miniconda3-rdkit-dftb
---

# verysure/miniconda3-rdkit-dftb:17

```bash
$ singularity pull shub://verysure/miniconda3-rdkit-dftb:17
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:xenial

%labels
MAINTAINER verysure

%files
files/environment-stable.yml /
files/initrc /
files/shell.sh /bin/

%post
apt-get -qq update --fix-missing 
apt-get install -yq wget bzip2 xz-utils libxrender-dev libxext-dev
chmod a+x /bin/shell.sh

# install conda
wget --quiet https://repo.continuum.io/miniconda/Miniconda3-4.5.1-Linux-x86_64.sh -O /miniconda.sh
bash /miniconda.sh -b -p /opt/conda
rm /miniconda.sh

# install rdkit and ase dependencies
. /opt/conda/etc/profile.d/conda.sh
conda config --set auto_update_conda False
conda install -y -n base conda=4.5.2
conda env create -f /environment-stable.yml

# install dftb
wget --quiet http://www.dftbplus.org/fileadmin/DFTBPLUS/public/dftbplus/17.1/dftbplus-17.1.x86_64-linux.tar.xz -O /dftbplus.tar.xz
tar -xf /dftbplus.tar.xz -oC /
mv /dftbplus-17.1.x86_64-linux /dftb

# install sk files
wget --quiet http://www.dftb.org/fileadmin/DFTB/public/slako-unpacked.tar.xz -O /dftbsk.tar.xz
tar -xf /dftbsk.tar.xz -oC /dftb

# change 
chmod a+rX -R /dftb

# clean up
conda clean -y -a
apt-get clean -yq
rm /dftbsk.tar.xz
rm /dftbplus.tar.xz
rm /environment-stable.yml

%environment
export DFTB_PREFIX=/dftb/slako/3ob/3ob-3-1/
export DFTB_COMMAND=/dftb/bin/dftb+
export OMP_NUM_THREADS=1
export SINGULARITY_SHELL=/bin/shell.sh
```

## Collection

 - Name: [verysure/miniconda3-rdkit-dftb](https://github.com/verysure/miniconda3-rdkit-dftb)
 - License: [MIT License](https://api.github.com/licenses/mit)

