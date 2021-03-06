---
id: 2714
name: "verysure/miniconda3-rdkit-dftb"
branch: "master"
tag: "latest"
commit: "f217079fe1958724675cc8f07f05cb0988e6af6a"
version: "98a219c5e37951f9c95b8eed99719e29"
build_date: "2018-05-03T20:08:01.956Z"
size_mb: 2521
size: 819482655
sif: "https://datasets.datalad.org/shub/verysure/miniconda3-rdkit-dftb/latest/2018-05-03-f217079f-98a219c5/98a219c5e37951f9c95b8eed99719e29.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/verysure/miniconda3-rdkit-dftb/latest/2018-05-03-f217079f-98a219c5/
recipe: https://datasets.datalad.org/shub/verysure/miniconda3-rdkit-dftb/latest/2018-05-03-f217079f-98a219c5/Singularity
collection: verysure/miniconda3-rdkit-dftb
---

# verysure/miniconda3-rdkit-dftb:latest

```bash
$ singularity pull shub://verysure/miniconda3-rdkit-dftb:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:latest

%labels
MAINTAINER verysure

%files
files/environment.yml /
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
conda install -y -n base conda
conda env create -f /environment.yml

# install dftb
wget --quiet http://www.dftbplus.org/fileadmin/DFTBPLUS/public/dftbplus/18.1/dftbplus-18.1.x86_64-linux.tar.xz -O /dftbplus.tar.xz
tar -xf /dftbplus.tar.xz -oC /
mv /dftbplus-18.1.x86_64-linux /dftb

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
rm /environment.yml

%environment
export DFTB_PREFIX=/dftb/slako/3ob/3ob-3-1/
export DFTB_COMMAND=/dftb/bin/dftb+
export OMP_NUM_THREADS=1
export SINGULARITY_SHELL=/bin/shell.sh
```

## Collection

 - Name: [verysure/miniconda3-rdkit-dftb](https://github.com/verysure/miniconda3-rdkit-dftb)
 - License: [MIT License](https://api.github.com/licenses/mit)

