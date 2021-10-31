---
id: 13187
name: "Xentrics/jupyter-r-base"
branch: "master"
tag: "u18.r4-rserver-netdx"
commit: "39bb5bcb053ab7ca8027f8fdc305f62375a7fb18"
version: "22a66bbaa9a479260fe6389f243848eaf579f4fca432f2f48869cf8641ef3b3a"
build_date: "2020-09-11T08:46:25.655Z"
size_mb: 1930.0234375
size: 2023776256
sif: "https://datasets.datalad.org/shub/Xentrics/jupyter-r-base/u18.r4-rserver-netdx/2020-09-11-39bb5bcb-22a66bba/22a66bbaa9a479260fe6389f243848eaf579f4fca432f2f48869cf8641ef3b3a.sif"
url: https://datasets.datalad.org/shub/Xentrics/jupyter-r-base/u18.r4-rserver-netdx/2020-09-11-39bb5bcb-22a66bba/
recipe: https://datasets.datalad.org/shub/Xentrics/jupyter-r-base/u18.r4-rserver-netdx/2020-09-11-39bb5bcb-22a66bba/Singularity
collection: Xentrics/jupyter-r-base
---

# Xentrics/jupyter-r-base:u18.r4-rserver-netdx

```bash
$ singularity pull shub://Xentrics/jupyter-r-base:u18.r4-rserver-netdx
```

## Singularity Recipe

```singularity
BootStrap: shub
From: Xentrics/jupyter-r-base:u18.r4-rserver
#Bootstrap: localimage
#From: Singularity.U18.r4-rserver.sif

%labels

  LICENSE Copyright 2020 Bastian Seelbinder, 
     Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"),
     to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
     and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above
     copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. 
  Maintainer Bastian Seelbinder

%help
  This will run RStudio Server

%apprun rserver
  exec /usr/lib/rstudio-server/bin/rserver "${@}"

%runscript
  exec /usr/lib/rstudio-server/bin/rserver "${@}"

%environment
  export LC_ALL=C.UTF-8
  export LANG=C.UTF-8

%post
  # to solve the "locale.Error: unsupported locale setting" error [https://stackoverflow.com/questions/14547631/python-locale-error-unsupported-locale-setting ]
  export LC_ALL=C.UTF-8
  export LANG=C.UTF-8
  
  # install additional dependencies
  apt-get update
  apt-get install -y libgtk3-nocsd0
  apt-get install -y libzmq3-dev   # required by clustermq


  # Install Cytoscape
  wget https://github.com/cytoscape/cytoscape/releases/download/3.8.0/Cytoscape_3_8_0_unix.sh
  chmod u+x Cytoscape*
  sh Cytoscape* -q
  rm Cytoscape_3_8_0_unix.sh

  # Install R packages
  export R_LIBS_USER="/usr/local/lib/R/site-library" # make sure packages go here
  /usr/local/bin/R --vanilla -e ".libPaths()" # show the path to the R libraries
  /usr/local/bin/R --vanilla -e 'install.packages(c("clustermq", "future", "tidyverse", "magrittr", "readxl", "writexl"), repos="https://cloud.r-project.org", Ncpus = 10)'
  /usr/local/bin/R --vanilla -e 'install.packages("BiocManager", repos="https://cloud.r-project.org", Ncpus = 10)'
  /usr/local/bin/R --vanilla -e 'BiocManager::install("netDx", Ncpus = 10)'
  
  # Clean up
  rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [Xentrics/jupyter-r-base](https://github.com/Xentrics/jupyter-r-base)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

