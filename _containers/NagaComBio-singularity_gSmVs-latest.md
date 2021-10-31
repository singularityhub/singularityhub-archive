---
id: 15124
name: "NagaComBio/singularity_gSmVs"
branch: "master"
tag: "latest"
commit: "a61ce6c071bf28356c5586c7cc4f6fefb880f9db"
version: "4d7135ade8f6c56c17392932567057a2"
build_date: "2021-03-19T16:02:40.041Z"
size_mb: 2760.0
size: 1077669919
sif: "https://datasets.datalad.org/shub/NagaComBio/singularity_gSmVs/latest/2021-03-19-a61ce6c0-4d7135ad/4d7135ade8f6c56c17392932567057a2.sif"
url: https://datasets.datalad.org/shub/NagaComBio/singularity_gSmVs/latest/2021-03-19-a61ce6c0-4d7135ad/
recipe: https://datasets.datalad.org/shub/NagaComBio/singularity_gSmVs/latest/2021-03-19-a61ce6c0-4d7135ad/Singularity
collection: NagaComBio/singularity_gSmVs
---

# NagaComBio/singularity_gSmVs:latest

```bash
$ singularity pull shub://NagaComBio/singularity_gSmVs:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: rocker/tidyverse:3.6.3

%files
  install_script.R

%post
  echo "Updating..."
  apt-get update && apt-get -y install wget python-pip ghostscript

  echo "Installing python packages"
  pip install https://github.com/NagaComBio/BioMine/archive/master.zip
  pip install https://github.com/NagaComBio/CharGer/archive/master.zip
  pip install cython==0.29.14
  pip install cyvcf2==0.9.0
  pip install futures==3.3.0
  pip install pandas==0.24.2
  pip install matplotlib==2.0.2

  echo "Installing R packages"
  /usr/local/bin/Rscript install_script.R

%runscript

%startscript
```

## Collection

 - Name: [NagaComBio/singularity_gSmVs](https://github.com/NagaComBio/singularity_gSmVs)
 - License: None

