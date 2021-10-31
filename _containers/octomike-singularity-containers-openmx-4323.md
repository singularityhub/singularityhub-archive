---
id: 1471
name: "octomike/singularity-containers"
branch: "master"
tag: "openmx-4323"
commit: "50526368f4ae5e8a2752dc3c7eb99034f0403ca2"
version: "25d01d1a7257e8c1a3feb91b89854feb"
build_date: "2018-01-25T14:23:39.384Z"
size_mb: 8053
size: 4273877023
sif: "https://datasets.datalad.org/shub/octomike/singularity-containers/openmx-4323/2018-01-25-50526368-25d01d1a/25d01d1a7257e8c1a3feb91b89854feb.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/octomike/singularity-containers/openmx-4323/2018-01-25-50526368-25d01d1a/
recipe: https://datasets.datalad.org/shub/octomike/singularity-containers/openmx-4323/2018-01-25-50526368-25d01d1a/Singularity
collection: octomike/singularity-containers
---

# octomike/singularity-containers:openmx-4323

```bash
$ singularity pull shub://octomike/singularity-containers:openmx-4323
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: neurodebian/neurodebian

%runscript
mkdir R
# build OpenM
cat <<EOF > install.R
chooseCRANmirror(ind=30)
.libPaths('./R')
source('http://openmx.psyc.virginia.edu/getOpenMx.R')
EOF
Rscript install.R
# test OpenMx
cat <<EOF > test.R
.libPaths('./R')
require(OpenMx)
data(demoOneFactor)
nvar <- ncol(demoOneFactor)
varnames <- colnames(demoOneFactor)
ssModel <- mxModel(model="State Space Manual Example",
   mxMatrix("Full", 1, 1, TRUE, .3, name="A"),
   mxMatrix("Zero", 1, 1, name="B"),
   mxMatrix("Full", nvar, 1, TRUE, .6, name="C", dimnames=list(varnames, "F1")),
   mxMatrix("Zero", nvar, 1, name="D"),
   mxMatrix("Diag", 1, 1, FALSE, 1, name="Q"),
   mxMatrix("Diag", nvar, nvar, TRUE, .2, name="R"),
   mxMatrix("Zero", 1, 1, name="x0"),
   mxMatrix("Diag", 1, 1, FALSE, 1, name="P0"),
   mxMatrix("Zero", 1, 1, name="u"),
   mxData(observed=demoOneFactor[1:100,], type="raw"),#fewer rows = fast
   mxExpectationStateSpace("A", "B", "C", "D", "Q", "R", "x0", "P0", "u"),
   mxFitFunctionML()
)
mxOption(NULL, 'Default optimizer', 'NPSOL')
ssRun <- mxRun(ssModel)
summary(ssRun)
EOF
Rscript test.R

%labels
   AUTHOR krause@mpib-berlin.mpg.de

%post
   apt-get update && apt-get -y install r-recommended libopenblas-base libxml2-dev
```

## Collection

 - Name: [octomike/singularity-containers](https://github.com/octomike/singularity-containers)
 - License: None

