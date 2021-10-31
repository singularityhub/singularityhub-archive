---
id: 14613
name: "tgac-vumc/BLADE"
branch: "master"
tag: "latest"
commit: "7734dfb49fc3d1296a0ddd39e7ee31fa041c8e92"
version: "92b372245270a944910bf00c2b5af412"
build_date: "2021-03-12T15:20:08.207Z"
size_mb: 2930.0
size: 1135489055
sif: "https://datasets.datalad.org/shub/tgac-vumc/BLADE/latest/2021-03-12-7734dfb4-92b37224/92b372245270a944910bf00c2b5af412.sif"
url: https://datasets.datalad.org/shub/tgac-vumc/BLADE/latest/2021-03-12-7734dfb4-92b37224/
recipe: https://datasets.datalad.org/shub/tgac-vumc/BLADE/latest/2021-03-12-7734dfb4-92b37224/Singularity
collection: tgac-vumc/BLADE
---

# tgac-vumc/BLADE:latest

```bash
$ singularity pull shub://tgac-vumc/BLADE:latest
```

## Singularity Recipe

```singularity
Bootstrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-7/7/os/x86_64/
Include: yum

%environment    
    export PATH=/usr/local/bin:$PATH

%post
    ./environment

    yum -y update
    yum -qq -y install curl tar bzip2 git zip
    curl -sSL https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o /tmp/miniconda.sh
    bash /tmp/miniconda.sh -bfp /usr/local
    conda update conda -y
    
    conda install mamba -c conda-forge -y
    mamba install -c conda-forge -c bioconda jupyter numpy numba scikit-learn joblib multiprocess time scipy qgrid seaborn
    pip install -y BLADE-Deconvolution==0.0.4
    jupyter nbextension enable --py --sys-prefix qgrid
    jupyter nbextension enable --py --sys-prefix widgetsnbextension
 


    rm -rf /tmp/miniconda.sh
```

## Collection

 - Name: [tgac-vumc/BLADE](https://github.com/tgac-vumc/BLADE)
 - License: [MIT License](https://api.github.com/licenses/mit)

