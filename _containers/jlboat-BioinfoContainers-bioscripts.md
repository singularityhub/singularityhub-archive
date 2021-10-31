---
id: 8768
name: "jlboat/BioinfoContainers"
branch: "master"
tag: "bioscripts"
commit: "5f15386e1057282311ce1b4a7cae3f747425ed6b"
version: "af1b276d1b549820603804b6be0fa6cd"
build_date: "2019-05-08T15:55:10.469Z"
size_mb: 624
size: 205623327
sif: "https://datasets.datalad.org/shub/jlboat/BioinfoContainers/bioscripts/2019-05-08-5f15386e-af1b276d/af1b276d1b549820603804b6be0fa6cd.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jlboat/BioinfoContainers/bioscripts/2019-05-08-5f15386e-af1b276d/
recipe: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/bioscripts/2019-05-08-5f15386e-af1b276d/Singularity
collection: jlboat/BioinfoContainers
---

# jlboat/BioinfoContainers:bioscripts

```bash
$ singularity pull shub://jlboat/BioinfoContainers:bioscripts
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: ubuntu:latest

%labels
    Topic Bioinformatics
    Language Python

%environment
    export PATH="$PATH:/opt/miniconda/bin/:/opt/bioscripts/"

%post
    apt-get update --fix-missing && apt-get install -y wget git
    wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh
    bash Miniconda2-latest-Linux-x86_64.sh -b -p /opt/miniconda
    rm Miniconda2-latest-Linux-x86_64.sh
    PATH="$PATH:/opt/miniconda/bin/"
    cd /opt/
    git clone https://github.com/uf-icbr-bioinformatics/bioscripts
    conda update -y conda
    conda install -y -c bioconda pysam biopython scipy sqlite
    conda clean -y -all
    mkdir -p /ufrc /orange /bio /rlts /scratch/local
    
####
# bamToWig
####

%apprun bamToWig
    exec /opt/miniconda/bin/python /opt/bioscripts/bamToWig.py "$@"

%apphelp bamToWig
    exec /opt/miniconda/bin/python /opt/bioscripts/bamToWig.py -h

####
# bisconv
####

%apprun bisconv
exec /opt/miniconda/bin/python /opt/bioscripts/bisconv.py "$@"

%apphelp bisconv
exec /opt/miniconda/bin/python /opt/bioscripts/bisconv.py -h

####
# chromCoverage
####

%apprun chromCoverage
exec /opt/miniconda/bin/python /opt/bioscripts/chromCoverage.py "$@"

%apphelp chromCoverage
exec /opt/miniconda/bin/python /opt/bioscripts/chromCoverage.py -h

####
# compareIntrons
####

%apprun compareIntrons
exec /opt/miniconda/bin/python /opt/bioscripts/compareIntrons.py "$@"

%apphelp compareIntrons
exec /opt/miniconda/bin/python /opt/bioscripts/compareIntrons.py -h

####
# countseqs
####

%apprun countseqs
exec /opt/miniconda/bin/python /opt/bioscripts/countseqs.py "$@"

%apphelp countseqs
exec /opt/miniconda/bin/python /opt/bioscripts/countseqs.py -h

####
# demux
####
/opt/miniconda/bin/
%apprun demux
exec /opt/miniconda/bin/python /opt/bioscripts/demux.py "$@"

%apphelp demux
exec /opt/miniconda/bin/python /opt/bioscripts/demux.py -h

####
# dmaptools
####

%apprun dmaptools
exec /opt/miniconda/bin/python /opt/bioscripts/dmaptools.py "$@"

%apphelp dmaptools
exec /opt/miniconda/bin/python /opt/bioscripts/dmaptools.py -h

####
# genes
####

%apprun genes
exec /opt/miniconda/bin/python /opt/bioscripts/genes.py "$@"

%apphelp genes
exec /opt/miniconda/bin/python /opt/bioscripts/genes.py -h

####
# mergeCols
####

%apprun mergeCols
exec /opt/miniconda/bin/python /opt/bioscripts/mergeCols.py "$@"

%apphelp mergeCols
exec /opt/miniconda/bin/python /opt/bioscripts/mergeCols.py -h

####
# methreport
####

%apprun methreport
exec /opt/miniconda/bin/python /opt/bioscripts/methreport.py "$@"

%apphelp methreport
exec /opt/miniconda/bin/python /opt/bioscripts/methreport.py -h

####
# methylfilter
####

%apprun methylfilter
exec /opt/miniconda/bin/python /opt/bioscripts/methylfilter.py "$@"

%apphelp methylfilter
exec /opt/miniconda/bin/python /opt/bioscripts/methylfilter.py -h

####
# pileupToBED
####

%apprun pileupToBED
exec /opt/miniconda/bin/python /opt/bioscripts/pileupToBED.py "$@"

%apphelp pileupToBED
exec /opt/miniconda/bin/python /opt/bioscripts/pileupToBED.py -h

####
# regionsCount
####

%apprun regionsCount
exec /opt/miniconda/bin/python /opt/bioscripts/regionsCount.py "$@"

%apphelp regionsCount
exec /opt/miniconda/bin/python /opt/bioscripts/regionsCount.py -h

####
# removeN
####

%apprun removeN
exec /opt/miniconda/bin/python /opt/bioscripts/removeN.py "$@"

%apphelp removeN
exec /opt/miniconda/bin/python /opt/bioscripts/removeN.py -h

####
# rnaseqtools
####

%apprun rnaseqtools
exec /opt/miniconda/bin/python /opt/bioscripts/rnaseqtools.py "$@"

%apphelp rnaseqtools
exec /opt/miniconda/bin/python /opt/bioscripts/rnaseqtools.py -h
```

## Collection

 - Name: [jlboat/BioinfoContainers](https://github.com/jlboat/BioinfoContainers)
 - License: [MIT License](https://api.github.com/licenses/mit)

