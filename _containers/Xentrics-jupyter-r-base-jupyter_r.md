---
id: 13199
name: "Xentrics/jupyter-r-base"
branch: "master"
tag: "jupyter_r"
commit: "ad5fc833ce409499be36a8322acb00a333dc2d7a"
version: "36cdcd818c3036b430d171fcbf56335ff11840fbaf7823bd480cb6ce17d08adc"
build_date: "2020-06-03T12:59:33.419Z"
size_mb: 887.37109375
size: 930476032
sif: "https://datasets.datalad.org/shub/Xentrics/jupyter-r-base/jupyter_r/2020-06-03-ad5fc833-36cdcd81/36cdcd818c3036b430d171fcbf56335ff11840fbaf7823bd480cb6ce17d08adc.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/Xentrics/jupyter-r-base/jupyter_r/2020-06-03-ad5fc833-36cdcd81/
recipe: https://datasets.datalad.org/shub/Xentrics/jupyter-r-base/jupyter_r/2020-06-03-ad5fc833-36cdcd81/Singularity
collection: Xentrics/jupyter-r-base
---

# Xentrics/jupyter-r-base:jupyter_r

```bash
$ singularity pull shub://Xentrics/jupyter-r-base:jupyter_r
```

## Singularity Recipe

```singularity
BootStrap: shub
From: Xentrics/jupyter-r-base:r3.6.3


%labels
    LICENSE Copyright 2020 Bastian Seelbinder, 
     Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"),
     to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
     and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above
     copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. 
    Maintainer Bastian Seelbinder

%post
    # make mount points
    mkdir -p /scratch/global /scratch/local
    
    # install deps
    apt-get update && apt-get install -y --no-install-recommends \
        python3 \
        python3-dev \
        python3-pip \
        python3-setuptools \
        python \
        python-dev \
        python-pip \
        python-setuptools \
        build-essential \
        gcc-multilib
    
    # install additional packages
    apt-get install -y nano git cmake gfortran curl wget autoconf bzip2 libtool libtool-bin sudo libxml2 libssl-dev libssl1.1
    
    # cleanup
    apt-get clean
    
    #install python pkgs
    pip3 install jupyter jupyterlab ipykernel scipy numpy pandas matplotlib
    
    # install R jupyter knerl
    export R_LIBS_USER="/usr/local/lib/R/site-library" # make sure packages go here
    R --vanilla -e 'install.packages("BiocManager", repos="https://cloud.r-project.org")'
    R --vanilla -e 'BiocManager::install("devtools")'
    R --vanilla -e 'devtools::install_github("IRkernel/IRkernel")'
    R --vanilla -e 'IRkernel::installspec()'
    
    # Install other R packages that are useful to have for machine learning
    R --vanilla -e 'BiocManager::install(c("tidyverse", "ggplot2", "ggstatsplot", "magrittr", "broom", "readxl", "writexl"))'
    R --vanilla -e 'BiocManager::install(c("caret", "parsnip"))'
```

## Collection

 - Name: [Xentrics/jupyter-r-base](https://github.com/Xentrics/jupyter-r-base)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

