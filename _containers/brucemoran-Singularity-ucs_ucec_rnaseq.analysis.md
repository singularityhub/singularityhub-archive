---
id: 9955
name: "brucemoran/Singularity"
branch: "master"
tag: "ucs_ucec_rnaseq.analysis"
commit: "c574a3f18e7b1c408721d7a5d0d3bf4add0cc641"
version: "0fc1799f49674dddc5c26203f84de264"
build_date: "2019-06-21T13:53:24.552Z"
size_mb: 3484
size: 1427677215
sif: "https://datasets.datalad.org/shub/brucemoran/Singularity/ucs_ucec_rnaseq.analysis/2019-06-21-c574a3f1-0fc1799f/0fc1799f49674dddc5c26203f84de264.simg"
url: https://datasets.datalad.org/shub/brucemoran/Singularity/ucs_ucec_rnaseq.analysis/2019-06-21-c574a3f1-0fc1799f/
recipe: https://datasets.datalad.org/shub/brucemoran/Singularity/ucs_ucec_rnaseq.analysis/2019-06-21-c574a3f1-0fc1799f/Singularity
collection: brucemoran/Singularity
---

# brucemoran/Singularity:ucs_ucec_rnaseq.analysis

```bash
$ singularity pull shub://brucemoran/Singularity:ucs_ucec_rnaseq.analysis
```

## Singularity Recipe

```singularity
Bootstrap:shub
From:brucemoran/Singularity:centos7-r_3.5.1_jupyter

%post

    R --slave -e 'library("devtools"); devtools::install_github(c("renozao/rngtools", "renozao/NMF"), build_vignettes = FALSE); library("BiocManager"); BiocManager::install(c("CellMix"), site_repository="http://web.cbio.uct.ac.za/~renaud/CRAN")'

    #BiocManager to install packages
    R --slave -e 'library("BiocManager"); BiocManager::install(c("rngtools", "NMF", "CAMERA", "DEFormats", "apeglm", "ggpubr",  "roots", "viper", "mixtools", "bcellViper", "aracne.networks", "rgexf", "fgsea", "PoiClaClu", "GSVA"),  dependencies=c("Depends", "Imports", "LinkingTo"), update=TRUE, ask=FALSE, build_vignettes=FALSE, clean=TRUE)'
    
    cd /usr/local

    yum install -y java-1.8.0-openjdk ant

    git clone https://github.com/califano-lab/ARACNe-AP
    cd ARACNe-AP
    ant main

    echo -e "#! /bin/bash\njavamem=""\nif [[ \$1 =~ "-Xmx" ]];then javamem=\$1; shift 1; fi\nexec java \$javamem -jar /usr/local/src/ARACNe-AP/dist/aracne.jar "\$@"" > /usr/local/bin/ARACNe-AP
```

## Collection

 - Name: [brucemoran/Singularity](https://github.com/brucemoran/Singularity)
 - License: None

