---
id: 15839
name: "dcgc-bfx/dcgc-single-cell"
branch: "main"
tag: "0.2.1"
commit: "ea7bae084396c9b90a4b2ffa5f12b97eecb14274"
version: "de3832f014a513a90939f820d41059bcde1817edd06f85ad54478003c243b924"
build_date: "2021-04-15T08:33:58.367Z"
size_mb: 2674.93359375
size: 2804871168
sif: "https://datasets.datalad.org/shub/dcgc-bfx/dcgc-single-cell/0.2.1/2021-04-15-ea7bae08-de3832f0/de3832f014a513a90939f820d41059bcde1817edd06f85ad54478003c243b924.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/dcgc-bfx/dcgc-single-cell/0.2.1/2021-04-15-ea7bae08-de3832f0/
recipe: https://datasets.datalad.org/shub/dcgc-bfx/dcgc-single-cell/0.2.1/2021-04-15-ea7bae08-de3832f0/Singularity
collection: dcgc-bfx/dcgc-single-cell
---

# dcgc-bfx/dcgc-single-cell:0.2.1

```bash
$ singularity pull shub://dcgc-bfx/dcgc-single-cell:0.2.1
```

## Singularity Recipe

```singularity
Bootstrap: shub
From:  dcgc-bfx/dcgc-jupyter-rstudio:0.2.0

%help
  Container for single cell analysis.

  Start jupyter lab:
    singularity run --writable-tmpfs --app jupyter library://fabianrost84/dcgc/single-cell.sif

  Start rstudio server listening on port 8787:
    singularity run --writable-tmpfs --app rserver library://fabianrost84/dcgc/single-cell.sif 8787

%environment
  DEBIAN_FRONTEND=noninteractive

%post
  export PATH=/opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

  apt-get update -q
  apt-get install -y -q libatlas-base-dev
  apt-get clean -q
  rm -rf /var/lib/apt/lists/*

  # install python packages with mamba
  mamba install --quiet --yes \
    anndata \
    anndata2ri \
    bbknn \
    bioservices \
    cellrank \
    cython \
    gsl \
    h5py \
    joblib \
    leidenalg \
    libtiff=4.1 `# version 4.2 breaks plotting` \
    loompy \
    louvain \
    pybedtools \
    pybiomart \
    pypairs \
    pytables \
    python-igraph \
    scanpy \
    scikit-learn \
    scrublet \
    scvi \
    statsmodels \
    xlrd \
    xlwt \
    `# R packages` \
    bioconductor-annotationhub \
    bioconductor-biomart \
    bioconductor-clusterexperiment \
    bioconductor-complexheatmap \
    bioconductor-deseq2 \
    bioconductor-dropletutils \
    bioconductor-genomeinfodb \
    bioconductor-genomeinfodbdata \
    bioconductor-hsmmsinglecell \
    bioconductor-loomexperiment \
    bioconductor-mast \
    bioconductor-monocle \
    bioconductor-scater \
    bioconductor-scran \
    bioconductor-singlecellexperiment \
    bioconductor-slingshot \
    r-argparse \
    r-biocmanager \
    r-enrichr \
    r-factoextra \
    r-fastmatch \
    r-future \
    r-gam \
    r-kableextra \
    r-loomr \
    r-monocle3 \
    r-openxlsx \
    r-parallelly \
    r-pheatmap \
    r-readr \
    r-refmanager \
    r-rgl \
    r-sctransform \
    r-seurat=4 \
    r-spatstat=1.64_1 \
    r-spatstat.core \
    r-upsetr \
    r-utf8 \
    r-venndiagram \
    `# cerebro app deps` \
    bioconductor-biocparallel \
    bioconductor-delayedarray \
    bioconductor-gseabase  \
    bioconductor-gsva \
    bioconductor-iranges \
    bioconductor-matrixgenerics \
    bioconductor-qvalue \
    bioconductor-s4vectors \
    r-colourpicker \
    r-formatr \
    r-msigdbr \
    r-shinycssloaders \
    r-shinydashboard \
    r-shinyfiles \
    r-shinyjs \
    r-shinywidgets

  # clean conda cache
  mamba clean -ai --quiet --yes

  # pip
  pip -q --no-cache-dir install -U \
    fa2 \
    gprofiler-official \
    magic-impute
  pip install -q --no-cache-dir git+https://github.com/theislab/diffxpy
  pip install -q --no-cache-dir git+https://github.com/DmitryUlyanov/Multicore-TSNE.git
  pip install -q --no-cache-dir git+https://github.com/theislab/scachepy
  pip install -q --no-cache-dir git+https://github.com/calico/solo.git

  # install R dependencies not available from conda
  R --quiet -e "devtools::install_github(repo = 'yanlinlin82/ggvenn', dependencies = FALSE, quiet = TRUE)"
  R --quiet -e 'devtools::install_github("cellgeni/sceasy", dependencies = FALSE, quiet = TRUE)'

  R --quiet -e 'BiocManager::install(c(
      "GenomeInfoDbData",
      "romanhaa/cerebroApp"
    ), ask = FALSE, update = FALSE, dependencies = FALSE, quiet = TRUE)'

  R --quiet -e "devtools::install_github(repo = 'cboettig/knitcitations', quiet = TRUE)"
  R --quiet -e 'install.packages(c(
        "PoiClaClu",
        "hutils",
        "singleCellHaystack"), repos="http://cran.r-project.org", quiet = TRUE)'

  chmod -R a+w /opt
```

## Collection

 - Name: [dcgc-bfx/dcgc-single-cell](https://github.com/dcgc-bfx/dcgc-single-cell)
 - License: None

