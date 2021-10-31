---
id: 7436
name: "magoapu/sing_af"
branch: "master"
tag: "ubuntu3"
commit: "c7355df6ca820b9d28dc407228f7f1b9e9301579"
version: "71aad75350fa06471108d498ce35f47c"
build_date: "2019-02-25T16:42:17.560Z"
size_mb: 2360
size: 1206079519
sif: "https://datasets.datalad.org/shub/magoapu/sing_af/ubuntu3/2019-02-25-c7355df6-71aad753/71aad75350fa06471108d498ce35f47c.simg"
url: https://datasets.datalad.org/shub/magoapu/sing_af/ubuntu3/2019-02-25-c7355df6-71aad753/
recipe: https://datasets.datalad.org/shub/magoapu/sing_af/ubuntu3/2019-02-25-c7355df6-71aad753/Singularity
collection: magoapu/sing_af
---

# magoapu/sing_af:ubuntu3

```bash
$ singularity pull shub://magoapu/sing_af:ubuntu3
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:latest


%post

apt-get update && apt-get install -y libcurl4-gnutls-dev libxml2-dev libssl-dev libmariadb-client-lgpl-dev ibglib2.0-dev libcairo2-dev ghostscript 
apt-get update && apt-get -y install r-base
apt-get update && apt-get install -y libxt-dev 

Rscript -e 'install.packages("devtools", dependencies = TRUE)'
Rscript -e 'library(devtools); install_github("brentp/celltypes450")'   
Rscript -e 'source("https://bioconductor.org/biocLite.R"); biocLite("sva")'
Rscript -e 'source("https://bioconductor.org/biocLite.R"); biocLite(pkgs=c("minfi","FlowSorted.Blood.450k"))'
Rscript -e 'source("https://bioconductor.org/biocLite.R"); biocLite(pkgs=c("DEXSeq","impute","wateRmelon","methylumi"))'
Rscript -e 'install.packages(c("gam","Hmisc","devtools","MASS","lmtest","markdown","Cairo","knitr","doParallel","compareGroups","MatrixEQTL","plyr","dplyr","matrixStats","sandwich","ggplot2","glmnet","parallel"))'
Rscript -e 'install.packages("devtools", dependencies = TRUE)'
Rscript -e 'library(devtools); install_github("brentp/celltypes450")'   
Rscript -e 'source("https://bioconductor.org/biocLite.R"); biocLite("sva")'
Rscript -e 'source("https://bioconductor.org/biocLite.R"); biocLite(pkgs=c("minfi","FlowSorted.Blood.450k"))'
Rscript -e 'source("https://bioconductor.org/biocLite.R"); biocLite(pkgs=c("DEXSeq","impute","wateRmelon","methylumi"))'
Rscript -e 'install.packages(c("gam","Hmisc","devtools","MASS","lmtest","markdown","Cairo","knitr","doParallel","compareGroups","MatrixEQTL","plyr","dplyr","matrixStats","sandwich","ggplot2","glmnet","parallel"))'
```

## Collection

 - Name: [magoapu/sing_af](https://github.com/magoapu/sing_af)
 - License: None

