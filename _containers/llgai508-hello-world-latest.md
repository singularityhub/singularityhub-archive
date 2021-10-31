---
id: 6303
name: "llgai508/hello-world"
branch: "master"
tag: "latest"
commit: "1b86cbecdea9ff6371b0a9cb132e00587a058bdc"
version: "73c0d7b27a0eb6676864342dae0d7e6d"
build_date: "2019-08-19T14:27:55.937Z"
size_mb: 3773
size: 1173295135
sif: "https://datasets.datalad.org/shub/llgai508/hello-world/latest/2019-08-19-1b86cbec-73c0d7b2/73c0d7b27a0eb6676864342dae0d7e6d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/llgai508/hello-world/latest/2019-08-19-1b86cbec-73c0d7b2/
recipe: https://datasets.datalad.org/shub/llgai508/hello-world/latest/2019-08-19-1b86cbec-73c0d7b2/Singularity
collection: llgai508/hello-world
---

# llgai508/hello-world:latest

```bash
$ singularity pull shub://llgai508/hello-world:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: debian:stretch-slim
%labels
MAINTAINER Gao Wang, gaow@uchicago.edu
%post

cd /tmp

# Install dev libraries
apt-get update \
&& apt-get install -y --no-install-recommends \
curl \
unzip \
gzip \
bzip2 \
ca-certificates \
build-essential \
gfortran \
libgfortran-6-dev \
libgomp1 \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/* /var/log/dpkg.log

# R, Python, SoS and DSC
MINICONDA_VERSION=4.5.11
PATH=/opt/miniconda3/bin:$PATH
curl https://repo.continuum.io/miniconda/Miniconda3-$MINICONDA_VERSION-Linux-x86_64.sh -o MCON.sh \
&& /bin/bash MCON.sh -b -p /opt/miniconda3 \
&& ln -s /opt/miniconda3/etc/profile.d/conda.sh /etc/profile.d/conda.sh \
&& conda install matplotlib==3.0.2 seaborn==0.9.0 \
&& conda install -c conda-forge r-base==3.5.1 sos==0.17.7 dsc==0.3.1.2 rpy2==2.9.4 \
&& conda clean --all -tipsy && rm -rf /tmp/* $HOME/.cache
pip install sos-notebook==0.17.3 jupyter_contrib_nbextensions==0.5.0 --no-cache-dir

# Packages for building and running susieR vignettes
conda install -c conda-forge r-devtools r-testthat r-openssl r-reshape r-ggplot2 r-cowplot \
r-profvis r-microbenchmark r-pkgdown r-dplyr r-stringr r-readr r-magrittr \
r-matrixstats r-glmnet \
libiconv && conda clean --all -tipsy && rm -rf /tmp/* $HOME/.cache
ln -s /bin/tar /bin/gtar

# Large scale regression related tools for running some susieR vignettes
R --slave -e "devtools::install_github('glmgen/genlasso')"
R --slave -e "devtools::install_github('hazimehh/L0Learn')"

# Fine-mapping tools
apt-get update && apt-get install -y --no-install-recommends libgsl-dev libgsl2 libatlas3-base liblapack-dev && apt-get clean
curl -L https://github.com/fhormoz/caviar/tarball/743038a32ae66ea06ee599670cb7939fb80a923f -o caviar.tar.gz \
&& tar -zxvf caviar.tar.gz && cd fhormoz-caviar-*/CAVIAR-C++ && make \
&& mv CAVIAR eCAVIAR mupCAVIAR setCAVIAR /usr/local/bin && rm -rf /tmp/*

curl -L https://github.com/xqwen/dap/tarball/ef11b263ae5e11b9e2e295757927877c03274095 -o dap.tar.gz \
&& tar -zxvf dap.tar.gz && cd xqwen-dap-*/dap_src && make && mv dap-g /usr/local/bin && rm -rf /tmp/*

curl -L http://www.christianbenner.com/finemap_v1.1_x86_64.tgz -o finemap.tgz \
&& tar zxvf finemap.tgz && mv finemap_v1.1_x86_64/finemap_v1.1_x86_64 /usr/local/bin/finemap \
&& chmod +x /usr/local/bin/finemap && rm -rf /tmp/*

SuSiE_VERSION=8a4f7177c0031255901083fa0f62555307acb6d9

# Supporting files
curl -L https://raw.githubusercontent.com/stephenslab/susieR/${SuSiE_VERSION}/inst/code/finemap.R -o /usr/local/bin/finemap.R \
&& chmod +x /usr/local/bin/finemap.R

curl -L https://raw.githubusercontent.com/stephenslab/susieR/${SuSiE_VERSION}/inst/code/caviar.R -o /usr/local/bin/caviar.R \
&& chmod +x /usr/local/bin/caviar.R

curl -L https://raw.githubusercontent.com/stephenslab/susieR/${SuSiE_VERSION}/inst/code/dap-g.py -o /usr/local/bin/dap-g.py \
&& chmod +x /usr/local/bin/dap-g.py



# Prevent local config / packages from being loaded
R_ENVIRON_USER=""
R_PROFILE_USER=""
R_LIBS_USER=' '

# In response to the following numpy error
# Error: Numpy + Intel(R) MKL: MKL_THREADING_LAYER=INTEL is incompatible with libgomp.so.1 library.
# Try to import numpy first or set the threading layer accordingly. Set NPY_MKL_FORCE_INTEL to force it.
MKL_THREADING_LAYER=GNU

%environment
export MINICONDA_VERSION=4.5.11
export PATH=/opt/miniconda3/bin:$PATH
export SuSiE_VERSION=8a4f7177c0031255901083fa0f62555307acb6d9
export R_ENVIRON_USER=""
export R_PROFILE_USER=""
export R_LIBS_USER=' '
export MKL_THREADING_LAYER=GNU
%runscript
echo "hello world from Lili"
```

## Collection

 - Name: [llgai508/hello-world](https://github.com/llgai508/hello-world)
 - License: [MIT License](https://api.github.com/licenses/mit)

