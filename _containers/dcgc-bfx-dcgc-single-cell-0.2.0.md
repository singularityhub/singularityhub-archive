---
id: 15834
name: "dcgc-bfx/dcgc-single-cell"
branch: "main"
tag: "0.2.0"
commit: "42e4069b99a125c759a6e80304f98fad0017ef16"
version: "9c2725d795a87a95960accf5bcf51aec8f1242d1bae17f5a1d8c001f6b5ff5f3"
build_date: "2021-04-01T11:50:06.529Z"
size_mb: 2665.94140625
size: 2795442176
sif: "https://datasets.datalad.org/shub/dcgc-bfx/dcgc-single-cell/0.2.0/2021-04-01-42e4069b-9c2725d7/9c2725d795a87a95960accf5bcf51aec8f1242d1bae17f5a1d8c001f6b5ff5f3.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/dcgc-bfx/dcgc-single-cell/0.2.0/2021-04-01-42e4069b-9c2725d7/
recipe: https://datasets.datalad.org/shub/dcgc-bfx/dcgc-single-cell/0.2.0/2021-04-01-42e4069b-9c2725d7/Singularity
collection: dcgc-bfx/dcgc-single-cell
---

# dcgc-bfx/dcgc-single-cell:0.2.0

```bash
$ singularity pull shub://dcgc-bfx/dcgc-single-cell:0.2.0
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
    FlowKit \
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
```

## Collection

 - Name: [dcgc-bfx/dcgc-single-cell](https://github.com/dcgc-bfx/dcgc-single-cell)
 - License: None

