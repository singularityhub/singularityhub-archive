---
id: 5549
name: "chrarnold/Singularity_images"
branch: "master"
tag: "atac_seq_conda"
commit: "d84f44d8358346a0756b906102d58c8beed08f03"
version: "83579cc949d8612dcb68e7a64126c271"
build_date: "2021-03-24T08:58:13.269Z"
size_mb: 4095
size: 1817354271
sif: "https://datasets.datalad.org/shub/chrarnold/Singularity_images/atac_seq_conda/2021-03-24-d84f44d8-83579cc9/83579cc949d8612dcb68e7a64126c271.simg"
url: https://datasets.datalad.org/shub/chrarnold/Singularity_images/atac_seq_conda/2021-03-24-d84f44d8-83579cc9/
recipe: https://datasets.datalad.org/shub/chrarnold/Singularity_images/atac_seq_conda/2021-03-24-d84f44d8-83579cc9/Singularity
collection: chrarnold/Singularity_images
---

# chrarnold/Singularity_images:atac_seq_conda

```bash
$ singularity pull shub://chrarnold/Singularity_images:atac_seq_conda
```

## Singularity Recipe

```singularity
Bootstrap: docker
FROM: continuumio/miniconda3

%labels
  Version v1.0

%help
  Singularity image for the ATAC-Seq pipeline (Python 3)



%post

  # Add channels for Bioconda
  /opt/conda/bin/conda config --add channels defaults
  /opt/conda/bin/conda config --add channels bioconda
  /opt/conda/bin/conda config --add channels conda-forge

  # Install the tools
  /opt/conda/bin/conda install --yes bedtools samtools fastqc trimmomatic multiqc bowtie2 picard gatk deeptools

%environment

%test
   # bedtools --version
   # samtools --version
   # fastqc --version
   # trimmomatic -version
   # bowtie2 --version
   # picard SortSam --version
   # gatk --version
   # deeptools --version
```

## Collection

 - Name: [chrarnold/Singularity_images](https://github.com/chrarnold/Singularity_images)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

