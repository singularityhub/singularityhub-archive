---
id: 14725
name: "NagaComBio/singularity_gcnvplotting"
branch: "master"
tag: "latest"
commit: "5039939ca9228de393747b040f2b21250a771b2d"
version: "a5c8ee183c84838bfa579f09a37796ba"
build_date: "2021-03-20T11:50:49.025Z"
size_mb: 4258.0
size: 1854439455
sif: "https://datasets.datalad.org/shub/NagaComBio/singularity_gcnvplotting/latest/2021-03-20-5039939c-a5c8ee18/a5c8ee183c84838bfa579f09a37796ba.sif"
url: https://datasets.datalad.org/shub/NagaComBio/singularity_gcnvplotting/latest/2021-03-20-5039939c-a5c8ee18/
recipe: https://datasets.datalad.org/shub/NagaComBio/singularity_gcnvplotting/latest/2021-03-20-5039939c-a5c8ee18/Singularity
collection: NagaComBio/singularity_gcnvplotting
---

# NagaComBio/singularity_gcnvplotting:latest

```bash
$ singularity pull shub://NagaComBio/singularity_gcnvplotting:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: rocker/tidyverse:3.5.1

%files
  install_script.R
  samplot_env.yml

%environment
  CONDA_INSTALL_PATH="/usr/local/miniconda3"
  CONDA_BIN_PATH="/usr/local/miniconda3/bin"
  CONDA_ENV_PATH="/usr/local/miniconda3/envs/samplot/bin"

%post
  echo "Installing R packages"
  /usr/local/bin/Rscript install_script.R

  echo "Installing miniconda"
  apt-get update && apt-get -y install wget
  wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
  chmod +x Miniconda3-latest-Linux-x86_64.sh
  CONDA_INSTALL_PATH="/usr/local/miniconda3"
  ./Miniconda3-latest-Linux-x86_64.sh -b -p $CONDA_INSTALL_PATH
  export PATH="/usr/local/miniconda3/bin:$PATH"
  conda create -n samplot -c anaconda -c bioconda -c conda-forge --file samplot_env.yml
  echo "PATH=/usr/local/miniconda3/envs/samplot/bin:$PATH" >> /usr/local/lib/R/etc/Renviron

%runscript
  source /usr/local/miniconda3/etc/profile.d/conda.sh
  conda activate samplot

%startscript
  source /usr/local/miniconda3/etc/profile.d/conda.sh
  conda acticate samplot
```

## Collection

 - Name: [NagaComBio/singularity_gcnvplotting](https://github.com/NagaComBio/singularity_gcnvplotting)
 - License: None

