---
id: 15005
name: "asafpr/singularity"
branch: "main"
tag: "latest"
commit: "26cf16d09b6f754c04dd292a0ad77b605c75e273"
version: "ee872f87c1de675e2f6c6ee282d1dfd5"
build_date: "2021-04-05T15:30:30.388Z"
size_mb: 4822.0
size: 1770323999
sif: "https://datasets.datalad.org/shub/asafpr/singularity/latest/2021-04-05-26cf16d0-ee872f87/ee872f87c1de675e2f6c6ee282d1dfd5.sif"
url: https://datasets.datalad.org/shub/asafpr/singularity/latest/2021-04-05-26cf16d0-ee872f87/
recipe: https://datasets.datalad.org/shub/asafpr/singularity/latest/2021-04-05-26cf16d0-ee872f87/Singularity
collection: asafpr/singularity
---

# asafpr/singularity:latest

```bash
$ singularity pull shub://asafpr/singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
from: bioconductor/bioconductor_docker:RELEASE_3_10

%post
    apt-get update
    apt-get install -y sqlite3 wget libxml2-dev libgit2-dev
    
    # Install INRICH
    wget https://bitbucket.org/statgen/inrich/get/30c7f7e93e2a.zip
    unzip 30c7f7e93e2a.zip
    cd statgen-inrich-30c7f7e93e2a && make
    cp inrich /usr/local/bin
    # Install mousegwas
    Rscript -e 'install.packages("XML", repos = "http://www.omegahat.net/R")'
    Rscript -e 'install.packages("devtools", repos="http://cran.us.r-project.org")'
    Rscript -e 'library(devtools); local({r <- getOption("repos"); r["CRAN"] <- "http://cran.us.r-project.org"; options(repos=r)}); install_github("TheJacksonLaboratory/mousegwas")'
    # Install GEMMA
    curl -L https://github.com/genetics-statistics/GEMMA/releases/download/0.98.1/gemma-0.98.1-linux-static.gz |zcat - > /usr/local/bin/gemma
    chmod a+x /usr/local/bin/gemma
    # Install pyLMM
    pip install numpy
    pip install scipy
    wget https://github.com/brielin/pylmm/archive/master.zip
    unzip master.zip
    cp pylmm-master/pylmmGWAS.py /usr/local/bin
    cp pylmm-master/pylmmKinship.py /usr/local/bin
    chmod a+x /usr/local/bin/pylmmGWAS.py
    chmod a+x /usr/local/bin/pylmmKinship.py
    apt-get clean

%apprun run_GWAS
    Rscript -e 'source(file=system.file("exec/run_GWAS.R", package="mousegwas"))' "$@"

%apprun postprocess_mv
    Rscript -e 'source(file=system.file("exec/postprocess_mv.R", package="mousegwas"))' "$@"
```

## Collection

 - Name: [asafpr/singularity](https://github.com/asafpr/singularity)
 - License: None

