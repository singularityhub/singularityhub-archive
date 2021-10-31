---
id: 7521
name: "Computational-Plant-Science/Example-Workflow"
branch: "master"
tag: "latest"
commit: "de0bc240dcc9e96ecbcf2767252aafc51f78f40e"
version: "6ab24e090d9d096a3751bb4f48c3d4d1"
build_date: "2019-02-28T01:51:30.014Z"
size_mb: 1160
size: 515411999
sif: "https://datasets.datalad.org/shub/Computational-Plant-Science/Example-Workflow/latest/2019-02-28-de0bc240-6ab24e09/6ab24e090d9d096a3751bb4f48c3d4d1.simg"
url: https://datasets.datalad.org/shub/Computational-Plant-Science/Example-Workflow/latest/2019-02-28-de0bc240-6ab24e09/
recipe: https://datasets.datalad.org/shub/Computational-Plant-Science/Example-Workflow/latest/2019-02-28-de0bc240-6ab24e09/Singularity
collection: Computational-Plant-Science/Example-Workflow
---

# Computational-Plant-Science/Example-Workflow:latest

```bash
$ singularity pull shub://Computational-Plant-Science/Example-Workflow:latest
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: frederic-michaud/python3

%labels
  Maintainer Chris Cotter (cotter@uga.edu)
  Version v0.1

%setup
  mkdir -p ${SINGULARITY_ROOTFS}/code/

%files
  #Copy the nextflow file into the container
  # some_file /code/

%post
 #Install your workflow code here
 pip3 install scikit-image

# No run script is necessary. "sinqularity exec" is used to run process_sample
#%runscript
```

## Collection

 - Name: [Computational-Plant-Science/Example-Workflow](https://github.com/Computational-Plant-Science/Example-Workflow)
 - License: None

