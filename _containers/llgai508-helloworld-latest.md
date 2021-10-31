---
id: 6299
name: "llgai508/helloworld"
branch: "master"
tag: "latest"
commit: "7c53137af827bca2bbe626b77182ad4e18b28dd7"
version: "09121ba5e7e7881187a2cbceccdad63f"
build_date: "2019-08-19T12:55:47.655Z"
size_mb: 4396
size: 1180921887
sif: "https://datasets.datalad.org/shub/llgai508/helloworld/latest/2019-08-19-7c53137a-09121ba5/09121ba5e7e7881187a2cbceccdad63f.simg"
url: https://datasets.datalad.org/shub/llgai508/helloworld/latest/2019-08-19-7c53137a-09121ba5/
recipe: https://datasets.datalad.org/shub/llgai508/helloworld/latest/2019-08-19-7c53137a-09121ba5/Singularity
collection: llgai508/helloworld
---

# llgai508/helloworld:latest

```bash
$ singularity pull shub://llgai508/helloworld:latest
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
&& conda clean --all -tipsy 
pip install sos-notebook==0.17.3 jupyter_contrib_nbextensions==0.5.0 --no-cache-dir

# Packages for building and running susieR vignettes
conda install -c conda-forge r-devtools r-testthat r-openssl r-reshape r-ggplot2 r-cowplot \
r-profvis r-microbenchmark r-pkgdown r-dplyr r-stringr r-readr r-magrittr \
r-matrixstats r-glmnet \
libiconv && conda clean --all -tipsy 
ln -s /bin/tar /bin/gtar

# Large scale regression related tools for running some susieR vignettes
R --slave -e "devtools::install_github('glmgen/genlasso')"
R --slave -e "devtools::install_github('hazimehh/L0Learn')"

# Fine-mapping tools
apt-get update && apt-get install -y --no-install-recommends libgsl-dev libgsl2 libatlas3-base liblapack-dev && apt-get clean
curl -L https://github.com/fhormoz/caviar/tarball/743038a32ae66ea06ee599670cb7939fb80a923f -o caviar.tar.gz \
&& tar -zxvf caviar.tar.gz && cd fhormoz-caviar-*/CAVIAR-C++ && make \
&& mv CAVIAR eCAVIAR mupCAVIAR setCAVIAR /usr/local/bin 


curl -L https://github.com/xqwen/dap/tarball/ef11b263ae5e11b9e2e295757927877c03274095 -o dap.tar.gz \
&& tar -zxvf dap.tar.gz && cd xqwen-dap-*/dap_src && make && mv dap-g /usr/local/bin 

curl -L http://www.christianbenner.com/finemap_v1.1_x86_64.tgz -o finemap.tgz \
&& tar zxvf finemap.tgz && mv finemap_v1.1_x86_64/finemap_v1.1_x86_64 /usr/local/bin/finemap \
&& chmod +x /usr/local/bin/finemap 

SuSiE_VERSION=8a4f7177c0031255901083fa0f62555307acb6d9

# Supporting files
curl -L https://raw.githubusercontent.com/stephenslab/susieR/${SuSiE_VERSION}/inst/code/finemap.R -o /usr/local/bin/finemap.R \
&& chmod +x /usr/local/bin/finemap.R

curl -L https://raw.githubusercontent.com/stephenslab/susieR/${SuSiE_VERSION}/inst/code/caviar.R -o /usr/local/bin/caviar.R \
&& chmod +x /usr/local/bin/caviar.R

curl -L https://raw.githubusercontent.com/stephenslab/susieR/${SuSiE_VERSION}/inst/code/dap-g.py -o /usr/local/bin/dap-g.py \
&& chmod +x /usr/local/bin/dap-g.py

# DSC R-utils
R --slave -e "devtools::install_github('rstudio/reticulate')"
R --slave -e "devtools::install_github('stephenslab/dsc@v0.3.1.2', subdir = 'dscrutils')"

# susieR 
R --slave -e "devtools::install_github('stephenslab/susieR', ref = '"${SuSiE_VERSION}"')"

# Benchmark related
R --slave -e "install.packages('abind', repos='http://cran.us.r-project.org')"


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
exec /bin/bash "$@"
```

## Collection

 - Name: [llgai508/helloworld](https://github.com/llgai508/helloworld)
 - License: [Apache License 2.0](https://api.github.com/licenses/apache-2.0)

