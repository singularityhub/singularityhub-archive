---
id: 6818
name: "chrarnold/Singularity_images"
branch: "master"
tag: "variant-calling_conda"
commit: "5ca192fd291e6d79ff808f2eb04d240d8218e837"
version: "ac3bccee30ee3db3e0c327b08ea778b6"
build_date: "2019-03-05T12:44:55.496Z"
size_mb: 3122
size: 1552502815
sif: "https://datasets.datalad.org/shub/chrarnold/Singularity_images/variant-calling_conda/2019-03-05-5ca192fd-ac3bccee/ac3bccee30ee3db3e0c327b08ea778b6.simg"
url: https://datasets.datalad.org/shub/chrarnold/Singularity_images/variant-calling_conda/2019-03-05-5ca192fd-ac3bccee/
recipe: https://datasets.datalad.org/shub/chrarnold/Singularity_images/variant-calling_conda/2019-03-05-5ca192fd-ac3bccee/Singularity
collection: chrarnold/Singularity_images
---

# chrarnold/Singularity_images:variant-calling_conda

```bash
$ singularity pull shub://chrarnold/Singularity_images:variant-calling_conda
```

## Singularity Recipe

```singularity
Bootstrap: docker
FROM: continuumio/miniconda3

%labels
  Version v1.0

%help
  Singularity image for the variant calling pipeline (Python 3)



%post

  # Add channels for Bioconda
  /opt/conda/bin/conda config --add channels defaults
  /opt/conda/bin/conda config --add channels bioconda
  /opt/conda/bin/conda config --add channels conda-forge

  # Install the tools
  /opt/conda/bin/conda install --yes bedtools samtools openssl=1.0 bwa fastqc trimmomatic cutadapt multiqc picard vcftools bcftools

  # wget --no-check-certificate -O gatk.tar.bz2 https://github.com/chrarnold/Singularity_images/raw/master/files/GenomeAnalysisTK-3.8-1-0-gf15c1c3ef.tar.bz2?raw=true

  # gatk-register gatk.tar.bz2

%environment

%test
   # bedtools --version
   # samtools --version
   # fastqc --version
   # bowtie2 --version
   # picard SortSam --version
```

## Collection

 - Name: [chrarnold/Singularity_images](https://github.com/chrarnold/Singularity_images)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

