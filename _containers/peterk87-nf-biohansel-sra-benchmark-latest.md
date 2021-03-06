---
id: 10699
name: "peterk87/nf-biohansel-sra-benchmark"
branch: "master"
tag: "latest"
commit: "5bffe183ff0a1a9f36bc37484dffec4c71fd9cc9"
version: "efcb6ac586e413d73bf50bf493c4313c"
build_date: "2019-08-22T14:49:25.000Z"
size_mb: 2727.0
size: 890335263
sif: "https://datasets.datalad.org/shub/peterk87/nf-biohansel-sra-benchmark/latest/2019-08-22-5bffe183-efcb6ac5/efcb6ac586e413d73bf50bf493c4313c.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/peterk87/nf-biohansel-sra-benchmark/latest/2019-08-22-5bffe183-efcb6ac5/
recipe: https://datasets.datalad.org/shub/peterk87/nf-biohansel-sra-benchmark/latest/2019-08-22-5bffe183-efcb6ac5/Singularity
collection: peterk87/nf-biohansel-sra-benchmark
---

# peterk87/nf-biohansel-sra-benchmark:latest

```bash
$ singularity pull shub://peterk87/nf-biohansel-sra-benchmark:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:continuumio/miniconda3:4.6.14

%labels
    MAINTAINER Peter Kruczkiewicz
    DESCRIPTION Singularity image containing all requirements for the peterk87/nf-biohansel-sra-benchmarking pipeline
    VERSION 1.0dev

%environment
    #export LC_ALL=C
    export PATH=/opt/conda/envs/nf-biohansel-sra-benchmarking-1.0dev/bin:$PATH

%files
    environment.yml /

%post
    export PATH=/opt/conda/bin:$PATH
    conda info
    apt-get update && apt-get install -y procps curl locales && apt-get clean -y
    sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
        echo 'LANG="en_US.UTF-8"'>/etc/default/locale && \
        dpkg-reconfigure --frontend=noninteractive locales && \
        update-locale LANG=en_US.UTF-8
    locale
    #conda install -c bioconda snpeff
    #snpEff -version
    conda install conda=4.7.11
    conda env create -f /environment.yml
    conda clean -a
```

## Collection

 - Name: [peterk87/nf-biohansel-sra-benchmark](https://github.com/peterk87/nf-biohansel-sra-benchmark)
 - License: None

