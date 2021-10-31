---
id: 5490
name: "chrarnold/Singularity_images"
branch: "master"
tag: "difftf_conda"
commit: "efe809f40dc8602abbefa8f6e1c42c57a298a91d"
version: "6ac680d8ff9577eefaa01be4028baf27"
build_date: "2021-04-16T19:30:22.441Z"
size_mb: 2663
size: 1123541023
sif: "https://datasets.datalad.org/shub/chrarnold/Singularity_images/difftf_conda/2021-04-16-efe809f4-6ac680d8/6ac680d8ff9577eefaa01be4028baf27.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/chrarnold/Singularity_images/difftf_conda/2021-04-16-efe809f4-6ac680d8/
recipe: https://datasets.datalad.org/shub/chrarnold/Singularity_images/difftf_conda/2021-04-16-efe809f4-6ac680d8/Singularity
collection: chrarnold/Singularity_images
---

# chrarnold/Singularity_images:difftf_conda

```bash
$ singularity pull shub://chrarnold/Singularity_images:difftf_conda
```

## Singularity Recipe

```singularity
Bootstrap: docker
FROM: continuumio/miniconda3

%labels
  Version v1.0

%help
  Singularity image for diffTF ( snakemake bedtools samtools subread via conda)



%post
  /opt/conda/bin/conda config --add channels defaults
  /opt/conda/bin/conda config --add channels bioconda
  /opt/conda/bin/conda config --add channels conda-forge
  /opt/conda/bin/conda install --yes snakemake bedtools samtools subread

%environment

%test
#   snakemake --version
  # bedtools --version
  # samtools --version
  # featureCounts -v
```

## Collection

 - Name: [chrarnold/Singularity_images](https://github.com/chrarnold/Singularity_images)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

