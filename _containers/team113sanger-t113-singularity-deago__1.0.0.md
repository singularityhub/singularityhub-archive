---
id: 10141
name: "team113sanger/t113-singularity"
branch: "master"
tag: "deago__1.0.0"
commit: "82940c59cb98386ca041c1da7f1628d830b9ceb2"
version: "ebe81407470f38b9afb1699f2833ec4b"
build_date: "2019-08-22T16:37:35.420Z"
size_mb: 3444
size: 1094705183
sif: "https://datasets.datalad.org/shub/team113sanger/t113-singularity/deago__1.0.0/2019-08-22-82940c59-ebe81407/ebe81407470f38b9afb1699f2833ec4b.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/team113sanger/t113-singularity/deago__1.0.0/2019-08-22-82940c59-ebe81407/
recipe: https://datasets.datalad.org/shub/team113sanger/t113-singularity/deago__1.0.0/2019-08-22-82940c59-ebe81407/Singularity
collection: team113sanger/t113-singularity
---

# team113sanger/t113-singularity:deago__1.0.0

```bash
$ singularity pull shub://team113sanger/t113-singularity:deago__1.0.0
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: team113sanger/t113-singularity:r-3.6.0.base-1.0.0
IncludeCmd: no

%help
Help message

%labels
        Maintainer Victoria Offord, Wellcome Sanger Institute
        Version v1.0.0
        R_Version 3.6.0

%environment
        export LC_ALL=en_US.UTF-8
        export LANG=en_US.UTF-8

%post
        yum install -y perl-core perl-App-cpanminus
        rpm -Uvh http://repo.openfusion.net/centos7-x86_64/openfusion-release-0.7-1.of.el7.noarch.rpm
        yum install -y perl-Dist-Zilla
        
        yum -y install epel-release
        yum -y install haskell-platform
        yum -y install pandoc

        Rscript -e "install.packages('BiocManager', repos='https://www.stats.bris.ac.uk/R/', dependencies=TRUE, clean = TRUE)"
        Rscript -e "BiocManager::install(c('DESeq2', 'genefilter', 'GenomicRanges', 'graph', 'limma', 'S4Vectors', 'SummarizedExperiment', 'topGO'))"
        Rscript -e "library(devtools); install_github('vaofford/deago')"

        git clone https://github.com/sanger-pathogens/Bio-Deago.git
        cd Bio-Deago
        cpanm aliased File::pushd
        dzil authordeps --missing | cpanm --notest -f
        cpanm CPAN::Meta::Requirements
        dzil listdeps --missing | cpanm
        dzil test
        dzil install
```

## Collection

 - Name: [team113sanger/t113-singularity](https://github.com/team113sanger/t113-singularity)
 - License: None

