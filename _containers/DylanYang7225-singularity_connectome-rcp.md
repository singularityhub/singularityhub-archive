---
id: 13047
name: "DylanYang7225/singularity_connectome"
branch: "master"
tag: "rcp"
commit: "cef4d97870e01de350d9b7d0015b8e4a4a59da06"
version: "4696c260591064c15d667226134511e9f8d5b7e60af88382bc578522dbd24ded"
build_date: "2020-05-17T17:03:54.411Z"
size_mb: 969.6015625
size: 1016700928
sif: "https://datasets.datalad.org/shub/DylanYang7225/singularity_connectome/rcp/2020-05-17-cef4d978-4696c260/4696c260591064c15d667226134511e9f8d5b7e60af88382bc578522dbd24ded.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/DylanYang7225/singularity_connectome/rcp/2020-05-17-cef4d978-4696c260/
recipe: https://datasets.datalad.org/shub/DylanYang7225/singularity_connectome/rcp/2020-05-17-cef4d978-4696c260/Singularity
collection: DylanYang7225/singularity_connectome
---

# DylanYang7225/singularity_connectome:rcp

```bash
$ singularity pull shub://DylanYang7225/singularity_connectome:rcp
```

## Singularity Recipe

```singularity
BootStrap: library
From: granek/default/singularity-rstudio-base:3.6.1


%labels
    Maintainer Hang(Dylan) Yang
    Image_Name connectome
    Image_Version connectome_01

%environment
    export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python3.7/site-packages
%post
  # Install extra stuff
  export DEBIAN_FRONTEND=noninteractive
  apt-get update
  apt-get install -y --no-install-recommends \
    curl \
    wget \
    samtools \
    git \
    ssh \
    less \
    make \
    htop \
    libxml2-dev \
    libgsl0-dev \
    libglu1-mesa \
    python-pip \
    python3-pip\
    python-setuptools \
    python3-setuptools \
    python-dev \
    python3-dev \

    
    python3 -m pip install --upgrade pip
    # pandoc is installed to support embedding of images generated from the R package plotly
    apt-get install -y pandoc
    apt-get clean
   
   python3 -m pip install wheel
   python3 -m pip install notebook
   python3 -m pip install bash_kernel
   python3 -m bash_kernel.install
   
   python3 -m pip install scipy
   python3 -m pip install pandas
   python3 -m pip install matplotlib
   python3 -m pip install seaborn
   python3 -m pip install patsy
   python3 -m pip install numpy
   python3 -m pip install statsmodels
   python3 -m pip install hurst
   python3 -m pip install scikit-learn
  
 #--------------------------------------------------------------------------------
 # Install R packages for time series-analysis
   Rscript -e "install.packages(c('IRkernel','repr', 'IRdisplay', 'pbdZMQ', 'devtools'), repos = 'https://cloud.r-project.org/')"
   Rscript -e "IRkernel::installspec(user = FALSE)"

   Rscript -e "install.packages(pkgs = c('argparse','R.utils','fs','here','foreach'), repos='https://cran.revolutionanalytics.com/', dependencies=TRUE, clean = TRUE)"
   Rscript -e "install.packages(c('pracma','nsarfima','longmemo','forecast','methods','t-series','sandwich','ltsa'), repos = 'https://cloud.r-project.org/', dependencies=TRUE, clean=TRUE)"
   Rscript -e "install.packages(c('stats','urca','arfima'), repos = 'https://cloud.r-project.org/', dependencies=TRUE, clean=TRUE)"
   Rscript -e "install.packages(c('fracdiff','zoo'), repos = 'https://cloud.r-project.org/', dependencies=TRUE, clean=TRUE)"
   Rscript -e "install.packages(c('dynlm'), repos = 'https://cloud.r-project.org/', dependencies=TRUE, clean=TRUE)"
   Rscript -e "install.packages(c('CADFtest'), repos = 'https://cloud.r-project.org/', dependencies=TRUE, clean=TRUE)"
 
 #--------------------------------------------------------------------------------
 mkdir -p /data
 mkdir -p /work
 mkdir -p /output
```

## Collection

 - Name: [DylanYang7225/singularity_connectome](https://github.com/DylanYang7225/singularity_connectome)
 - License: None

