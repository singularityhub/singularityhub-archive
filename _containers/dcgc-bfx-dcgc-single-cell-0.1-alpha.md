---
id: 15684
name: "dcgc-bfx/dcgc-single-cell"
branch: "main"
tag: "0.1-alpha"
commit: "7c852fc45c928ce944740b5778dac04aa3265caa"
version: "90af2c015a0596049693a5098431e714809215d1e81d5682c2b2b9e1c298c714"
build_date: "2021-04-01T11:33:21.601Z"
size_mb: 2671.96484375
size: 2801758208
sif: "https://datasets.datalad.org/shub/dcgc-bfx/dcgc-single-cell/0.1-alpha/2021-04-01-7c852fc4-90af2c01/90af2c015a0596049693a5098431e714809215d1e81d5682c2b2b9e1c298c714.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/dcgc-bfx/dcgc-single-cell/0.1-alpha/2021-04-01-7c852fc4-90af2c01/
recipe: https://datasets.datalad.org/shub/dcgc-bfx/dcgc-single-cell/0.1-alpha/2021-04-01-7c852fc4-90af2c01/Singularity
collection: dcgc-bfx/dcgc-single-cell
---

# dcgc-bfx/dcgc-single-cell:0.1-alpha

```bash
$ singularity pull shub://dcgc-bfx/dcgc-single-cell:0.1-alpha
```

## Singularity Recipe

```singularity
Bootstrap: shub
From:  dcgc-bfx/dcgc-jupyter-rstudio:0.1

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
    bioconductor-hsmmsinglecell \
    bioconductor-loomexperiment \
    bioconductor-mast \
    bioconductor-monocle \
    bioconductor-scater \
    bioconductor-scran \
    bioconductor-slingshot \
    r-argparse \
    r-biocmanager \
    r-kableextra \
    r-enrichr \
    r-factoextra \
    r-future \
    r-gam \
    r-loomr \
    r-monocle3 \
    r-openxlsx \
    r-pheatmap \
    r-readr \
    r-rgl \
    r-sctransform \
    r-seurat=4 \
    r-upsetr \
    r-venndiagram \
    `# cerebro app deps` \
    bioconductor-gseabase  \
    bioconductor-gsva \
    bioconductor-qvalue \
    r-colourpicker \
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
    FlowKit \
    gprofiler-official \
    magic-impute
  pip install -q --no-cache-dir git+https://github.com/theislab/diffxpy
  pip install -q --no-cache-dir git+https://github.com/DmitryUlyanov/Multicore-TSNE.git
  pip install -q --no-cache-dir git+https://github.com/theislab/scachepy
  pip install -q --no-cache-dir git+https://github.com/calico/solo.git

  # install R dependencies not available from conda
  R --quiet -e "devtools::install_github(repo = 'yanlinlin82/ggvenn', quiet = TRUE)"
  R --quiet -e 'devtools::install_github("cellgeni/sceasy", quiet = TRUE)'
  R --quiet -e 'BiocManager::install(c(
    "romanhaa/cerebroApp"),
    ask = FALSE, update = FALSE, quiet = TRUE)'

  R --quiet -e "devtools::install_github(repo = 'cboettig/knitcitations', quiet = TRUE)"
  R --quiet -e 'install.packages(c(
        "PoiClaClu",
        "hutils",
        "singleCellHaystack"), repos="http://cran.r-project.org", quiet = TRUE)'
```

## Collection

 - Name: [dcgc-bfx/dcgc-single-cell](https://github.com/dcgc-bfx/dcgc-single-cell)
 - License: None

