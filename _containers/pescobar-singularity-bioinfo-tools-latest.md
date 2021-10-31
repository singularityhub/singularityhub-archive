---
id: 3899
name: "pescobar/singularity-bioinfo-tools"
branch: "master"
tag: "latest"
commit: "333e72f53612f69fb7012cd1b88331a196da2595"
version: "e2c9d4ca4c0fddeb41b48e384d5ff31d2ba853bd6b75062bb8f69e05b640d21d"
build_date: "2020-09-23T13:43:46.648Z"
size_mb: 1455.76953125
size: 1526484992
sif: "https://datasets.datalad.org/shub/pescobar/singularity-bioinfo-tools/latest/2020-09-23-333e72f5-e2c9d4ca/e2c9d4ca4c0fddeb41b48e384d5ff31d2ba853bd6b75062bb8f69e05b640d21d.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/pescobar/singularity-bioinfo-tools/latest/2020-09-23-333e72f5-e2c9d4ca/
recipe: https://datasets.datalad.org/shub/pescobar/singularity-bioinfo-tools/latest/2020-09-23-333e72f5-e2c9d4ca/Singularity
collection: pescobar/singularity-bioinfo-tools
---

# pescobar/singularity-bioinfo-tools:latest

```bash
$ singularity pull shub://pescobar/singularity-bioinfo-tools:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: continuumio/miniconda3

%post

    export PATH=/opt/conda/bin:$PATH

    # make sure to have the latest conda version
    conda update -n base conda

    # add some extra channels
    conda config --add channels conda-forge
    conda config --add channels bioconda

    # install some bioinfo tools from Bioconda
    # to force the app version use appname==1.1.1
    conda install --yes -c bioconda samtools
    conda install --yes -c bioconda fastqc
    conda install --yes -c bioconda trimmomatic
    conda install --yes -c bioconda rseqc
    conda install --yes -c bioconda star
    conda install --yes -c bioconda salmon
    conda install --yes -c bioconda kallisto
    conda install --yes -c bioconda htseq
    conda install --yes -c bioconda sra-tools
    conda install --yes -c bioconda subread
    conda install --yes -c bioconda multiqc
    conda install --yes -c bioconda bedtools
    conda install --yes -c bioconda gffread

%environment
    export PATH=/opt/conda/bin:$PATH
    export XDG_RUNTIME_DIR=""

%apprun samtools
    samtools "$@"

%apprun fastqc
    fastqc "$@"

%apprun trimmomatic
    trimmomatic "@"

%apprun STAR
    START "@"

%apprun STARlong
    STARTlong "@"

%apprun salmon
    salmon "@"

%apprun kallisto
    kallisto "@"

%apprun htseq_count
    htseq-count "@"

%apprun htseq_qa
    htseq-qa "@"

%apprun sra_sort
    sra-sort "@"

%apprun sra_stat
    sra-stat "@"

%apprun multiqc
    multiqc "@"

%apprun bedtools
    bedtools "@"

%apprun gffread
    gffread "@"
```

## Collection

 - Name: [pescobar/singularity-bioinfo-tools](https://github.com/pescobar/singularity-bioinfo-tools)
 - License: None

