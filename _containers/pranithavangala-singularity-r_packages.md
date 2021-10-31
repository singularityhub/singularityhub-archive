---
id: 4004
name: "pranithavangala/singularity"
branch: "master"
tag: "r_packages"
commit: "98c72227183cf57cc030deae7c3679618e62a465"
version: "81ca6de9d9acf0b78309d1a04cbc32dd"
build_date: "2018-12-12T19:33:36.401Z"
size_mb: 4072
size: 1608908831
sif: "https://datasets.datalad.org/shub/pranithavangala/singularity/r_packages/2018-12-12-98c72227-81ca6de9/81ca6de9d9acf0b78309d1a04cbc32dd.simg"
url: https://datasets.datalad.org/shub/pranithavangala/singularity/r_packages/2018-12-12-98c72227-81ca6de9/
recipe: https://datasets.datalad.org/shub/pranithavangala/singularity/r_packages/2018-12-12-98c72227-81ca6de9/Singularity
collection: pranithavangala/singularity
---

# pranithavangala/singularity:r_packages

```bash
$ singularity pull shub://pranithavangala/singularity:r_packages
```

## Singularity Recipe

```singularity
BootStrap: shub
From: shub://pranithavangala/singularity:r-3-4-3

%labels

    AUTHOR Pranitha Vangala <pranitha.vangala@gmail.com>
    Version v1.0

%environment
    export SRC=/usr/local/src
    export BIN=/usr/local/bin
    export R_VERSION=R-3.4.3

%post
    	echo install.packages\(\"biclust\"\, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
    	echo install.packages\(\"dplyr\"\, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
    	echo install.packages\(\"reshape2\"\, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
    	echo install.packages\(\"gplots\"\, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
    	echo install.packages\(\"stringdist\"\, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
    	echo install.packages\(\"stringr\"\, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
    	echo install.packages\(\"data.table\"\, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
    	R --slave -e 'source("http://bioconductor.org/biocLite.R");library(BiocInstaller); biocLite("Sushi", dep = TRUE)'
	echo install.packages\(\"readr\"\, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
	echo install.packages\(\"purrr\"\, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
	echo install.packages\(\"dplyr\"\, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
	echo install.packages\(\"data.table\"\, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
	echo install.packages\(\"caret\"\, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
	echo install.packages\(\"h2o\"\, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
	echo install.packages\(\"pROC\"\, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
	echo install.packages\(\"PRROC\"\, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
	echo install.packages\(\"parallel\"\, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
	echo install.packages\(\"doParallel\"\, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
	echo install.packages\(\"randomForest\"\, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
	echo install.packages\(\"optparse\"\, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
```

## Collection

 - Name: [pranithavangala/singularity](https://github.com/pranithavangala/singularity)
 - License: None

