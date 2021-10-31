---
id: 5550
name: "chrarnold/Singularity_images"
branch: "master"
tag: "atac_seq_conda2"
commit: "d84f44d8358346a0756b906102d58c8beed08f03"
version: "9845999248f159ada03e9436154b7a82"
build_date: "2021-03-18T16:05:19.867Z"
size_mb: 2115
size: 943001631
sif: "https://datasets.datalad.org/shub/chrarnold/Singularity_images/atac_seq_conda2/2021-03-18-d84f44d8-98459992/9845999248f159ada03e9436154b7a82.simg"
url: https://datasets.datalad.org/shub/chrarnold/Singularity_images/atac_seq_conda2/2021-03-18-d84f44d8-98459992/
recipe: https://datasets.datalad.org/shub/chrarnold/Singularity_images/atac_seq_conda2/2021-03-18-d84f44d8-98459992/Singularity
collection: chrarnold/Singularity_images
---

# chrarnold/Singularity_images:atac_seq_conda2

```bash
$ singularity pull shub://chrarnold/Singularity_images:atac_seq_conda2
```

## Singularity Recipe

```singularity
Bootstrap: docker
FROM: continuumio/miniconda2

%labels
  Version v1.0

%help
  Singularity image for the ATAC-Seq pipeline (Python version 2)



%post

  # Add channels for Bioconda
  /opt/conda/bin/conda config --add channels defaults
  /opt/conda/bin/conda config --add channels bioconda
  /opt/conda/bin/conda config --add channels conda-forge

  # Install the tools
  /opt/conda/bin/conda install --yes macs2

%environment

%test
   # macs2 --version
```

## Collection

 - Name: [chrarnold/Singularity_images](https://github.com/chrarnold/Singularity_images)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

