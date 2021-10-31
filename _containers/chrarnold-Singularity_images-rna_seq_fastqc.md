---
id: 6034
name: "chrarnold/Singularity_images"
branch: "master"
tag: "rna_seq_fastqc"
commit: "c159994feb3ccb8cafaac79ab4c312a73e5aa015"
version: "d1d42b1ecde63da3cef89fd99da67c0b"
build_date: "2018-12-21T17:01:16.896Z"
size_mb: 1333
size: 701100063
sif: "https://datasets.datalad.org/shub/chrarnold/Singularity_images/rna_seq_fastqc/2018-12-21-c159994f-d1d42b1e/d1d42b1ecde63da3cef89fd99da67c0b.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/chrarnold/Singularity_images/rna_seq_fastqc/2018-12-21-c159994f-d1d42b1e/
recipe: https://datasets.datalad.org/shub/chrarnold/Singularity_images/rna_seq_fastqc/2018-12-21-c159994f-d1d42b1e/Singularity
collection: chrarnold/Singularity_images
---

# chrarnold/Singularity_images:rna_seq_fastqc

```bash
$ singularity pull shub://chrarnold/Singularity_images:rna_seq_fastqc
```

## Singularity Recipe

```singularity
Bootstrap: docker
FROM: continuumio/miniconda3

%labels
  Version v1.0

%help
  Singularity image for the RNA-Seq pipeline (Python 3)



%post

  # Add channels for Bioconda
  /opt/conda/bin/conda config --add channels defaults
  /opt/conda/bin/conda config --add channels bioconda
  /opt/conda/bin/conda config --add channels conda-forge

  # Install the tools
  /opt/conda/bin/conda install --yes fastqc

%environment

%test
   # fastqc --version
```

## Collection

 - Name: [chrarnold/Singularity_images](https://github.com/chrarnold/Singularity_images)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

