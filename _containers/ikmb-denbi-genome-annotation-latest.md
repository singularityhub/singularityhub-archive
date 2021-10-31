---
id: 12607
name: "ikmb-denbi/genome-annotation"
branch: "tblastn-revert"
tag: "latest"
commit: "3e0a83e9b9bb4bdd3f00980845919fcac9adc80e"
version: "c05b6f1e7449010a9afca4ce9cbafa5b"
build_date: "2020-04-03T12:27:38.462Z"
size_mb: 6325.0
size: 1746927647
sif: "https://datasets.datalad.org/shub/ikmb-denbi/genome-annotation/latest/2020-04-03-3e0a83e9-c05b6f1e/c05b6f1e7449010a9afca4ce9cbafa5b.sif"
url: https://datasets.datalad.org/shub/ikmb-denbi/genome-annotation/latest/2020-04-03-3e0a83e9-c05b6f1e/
recipe: https://datasets.datalad.org/shub/ikmb-denbi/genome-annotation/latest/2020-04-03-3e0a83e9-c05b6f1e/Singularity
collection: ikmb-denbi/genome-annotation
---

# ikmb-denbi/genome-annotation:latest

```bash
$ singularity pull shub://ikmb-denbi/genome-annotation:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:nfcore/base

%labels
    MAINTAINER Marc Hoeppner <m.hoeppner@ikmb.uni-kiel.de>
    DESCRIPTION Singularity image containing all requirements for the annotation pipeline
    VERSION 0.1

%environment
    PATH=/opt/conda/envs/genome-annotation-1.0/bin:/opt/conda/envs/genome-annotation-1.0/opt/pasa-2.3.3/bin:/opt/bin:$PATH
    export PATH

    PERL5LIB=$PERL5LIB:/usr/local/share/perl/5.24.1
    export PERL5LIB

    PASAHOME=/opt/conda/envs/genome-annotation-1.0/opt/pasa-2.3.3
    export PASAHOME

    EVM_HOME=/opt/conda/envs/genome-annotation-1.0/opt/evidencemodeler-1.1.1
    export EVM_HOME

%files
    environment.yml /

%post
    /opt/conda/bin/conda env create -f /environment.yml
    /opt/conda/bin/conda clean -a

# Prereqs for Nextflow
apt-get -y install procps make gcc

cpan -i inc::latest  URI::Encode 
# Create mount point for RZCluster
mkdir -p /ifs

# Create the default config file
cp /opt/conda/envs/genome-annotation-1.0/opt/pasa-2.3.3/pasa_conf/pasa.CONFIG.template /opt/conda/envs/genome-annotation-1.0/opt/pasa-2.3.3/pasa_conf/conf.txt

# Install rapid fasta splitter
mkdir -p /opt/bin && cd /opt/bin && wget -q ftp://saf.bio.caltech.edu/pub/software/molbio/fastasplitn.c && gcc -o fastasplitn fastasplitn.c && chmod +x fastasplitn

# Install local Blast+ to circumvent buggy version shipping with RepeatMasker
mkdir /opt/blast+ && cd /opt/blast+ && wget -q ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.10.0/ncbi-blast-2.10.0+-x64-linux.tar.gz && tar -xvf ncbi-blast-2.10.0+-x64-linux.tar.gz && \
rm *.tar.gz && mv ncbi-blast-2.10.0+ 2.10.0
```

## Collection

 - Name: [ikmb-denbi/genome-annotation](https://github.com/ikmb-denbi/genome-annotation)
 - License: [MIT License](https://api.github.com/licenses/mit)

