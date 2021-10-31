---
id: 2966
name: "YSanchezAraujo/singularity"
branch: "master"
tag: "latest"
commit: "5ce9784e5e357905079c10395cbdc0967e028e6c"
version: "60f0d323460285906ab40c21b415b19d"
build_date: "2018-05-30T18:54:57.440Z"
size_mb: 1274
size: 472555551
sif: "https://datasets.datalad.org/shub/YSanchezAraujo/singularity/latest/2018-05-30-5ce9784e-60f0d323/60f0d323460285906ab40c21b415b19d.simg"
url: https://datasets.datalad.org/shub/YSanchezAraujo/singularity/latest/2018-05-30-5ce9784e-60f0d323/
recipe: https://datasets.datalad.org/shub/YSanchezAraujo/singularity/latest/2018-05-30-5ce9784e-60f0d323/Singularity
collection: YSanchezAraujo/singularity
---

# YSanchezAraujo/singularity:latest

```bash
$ singularity pull shub://YSanchezAraujo/singularity:latest
```

## Singularity Recipe

```singularity
BootStrap:docker
From:r-base
%runscript
R
%post
R -e 'install.packages(c("car","randomForest","fuzzyforest","caret","pROC"))'
R -e 'setRepositories(ind=1:2);install.packages(c("WGCNA"))'
R -e 'source("http://bioconductor.org/biocLite.R");biocLite("AnnotationDbi", type="source");biocLite("GO.db")'
R -e 'install.packages(c("PMA","h5"))'
R -e 'install.packages("varbvs")'
```

## Collection

 - Name: [YSanchezAraujo/singularity](https://github.com/YSanchezAraujo/singularity)
 - License: None

