---
id: 10695
name: "vaofford/Bio-Deago"
branch: "master"
tag: "latest"
commit: "b469f7a3aac5d0a338be3a126e3f33be99f1a917"
version: "0c25784875dab149846710d9516df38f"
build_date: "2019-09-03T07:24:27.534Z"
size_mb: 3452.0
size: 1097035807
sif: "https://datasets.datalad.org/shub/vaofford/Bio-Deago/latest/2019-09-03-b469f7a3-0c257848/0c25784875dab149846710d9516df38f.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/vaofford/Bio-Deago/latest/2019-09-03-b469f7a3-0c257848/
recipe: https://datasets.datalad.org/shub/vaofford/Bio-Deago/latest/2019-09-03-b469f7a3-0c257848/Singularity
collection: vaofford/Bio-Deago
---

# vaofford/Bio-Deago:latest

```bash
$ singularity pull shub://vaofford/Bio-Deago:latest
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
        cp -r ./markdown_templates /usr/local/share/
```

## Collection

 - Name: [vaofford/Bio-Deago](https://github.com/vaofford/Bio-Deago)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

