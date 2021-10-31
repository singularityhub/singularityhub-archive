---
id: 11909
name: "seb-mueller/singularity_srna_phasing"
branch: "master"
tag: "latest"
commit: "37cec0c87f65c76194db57cdade0a586bb1936d5"
version: "1cf4ebbb856e98f86786cbb93685e6ab"
build_date: "2019-12-23T19:02:39.311Z"
size_mb: 585.0
size: 186830879
sif: "https://datasets.datalad.org/shub/seb-mueller/singularity_srna_phasing/latest/2019-12-23-37cec0c8-1cf4ebbb/1cf4ebbb856e98f86786cbb93685e6ab.sif"
url: https://datasets.datalad.org/shub/seb-mueller/singularity_srna_phasing/latest/2019-12-23-37cec0c8-1cf4ebbb/
recipe: https://datasets.datalad.org/shub/seb-mueller/singularity_srna_phasing/latest/2019-12-23-37cec0c8-1cf4ebbb/Singularity
collection: seb-mueller/singularity_srna_phasing
---

# seb-mueller/singularity_srna_phasing:latest

```bash
$ singularity pull shub://seb-mueller/singularity_srna_phasing:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3:4.7.12

%labels
AUTHOR sebmu@posteo.de
Version v1.0

%environment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This sets global environment variables for anything run within the container
export PATH="/opt/conda/bin:/usr/local/bin:/usr/bin:/bin:"
unset CONDA_DEFAULT_ENV
export ANACONDA_HOME=/opt/conda

%files
  # copies local file into /
  phasetank.yaml

%post
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This is going to be executed after the base container has been downloaded
wget 'https://sourceforge.net/projects/phasetank/files/PhaseTank_V1.0_BETE/PhaseTank_v1.0.tar.gz/download'
tar xvzf download
cd PhaseTank_v1.0
PATH=$PATH:PhaseTank_v1.0:$PATH

# apt-get update

export PATH=/opt/conda/bin:$PATH
# conda update conda
# conda config --set ssl_verify false
conda config --set ssl_verify /opt/conda/ssl/cacert.pem
conda env update -n base --file /phasetank.yaml
# conda init bash
# bash
# conda activate base

conda clean --index-cache --tarballs --packages --yes
# pip install snakemake


# save a list of all installed packages within the container
conda list > conda_list_packages.txt
pip list > pip_list_packages.txt

#clean up
apt-get -y remove --auto-remove gcc
apt-get -y autoremove --purge
apt-get -y autoclean
apt-get -y clean
```

## Collection

 - Name: [seb-mueller/singularity_srna_phasing](https://github.com/seb-mueller/singularity_srna_phasing)
 - License: None

