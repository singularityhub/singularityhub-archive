---
id: 282
name: "alaindomissy/scbatch"
branch: "master"
tag: "master"
commit: "6628389b6813f9eb763983ef8bfeb6e1be0e2eb5"
version: "61d931484dc718f49b6e4c255f0d31c0"
build_date: "2017-10-17T20:41:50.004Z"
size_mb: 8323
size: 2265439651
sif: "https://datasets.datalad.org/shub/alaindomissy/scbatch/master/2017-10-17-6628389b-61d93148/61d931484dc718f49b6e4c255f0d31c0.img.gz"
datalad_url: https://datasets.datalad.org?dir=/shub/alaindomissy/scbatch/master/2017-10-17-6628389b-61d93148/
recipe: https://datasets.datalad.org/shub/alaindomissy/scbatch/master/2017-10-17-6628389b-61d93148/Singularity
collection: alaindomissy/scbatch
---

# alaindomissy/scbatch:master

```bash
$ singularity pull shub://alaindomissy/scbatch:master
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
MirrorURL: http://us.archive.ubuntu.com/ubuntu
OSVersion: xenial


#BootStrap: docker
#From: ubuntu:16.04


  ####
%setup
  ####
  # initial setups from outside the container
  # this is run from outside the container to start setting it up

  echo "Looking in directory '$SINGULARITY_ROOTFS' for /bin/sh"
  if [ ! -x "$SINGULARITY_ROOTFS/bin/sh" ]; then
      echo "Hrmm, this container does not have /bin/sh installed..."
      exit 1
  fi


  # for SDSC mounts
  mkdir -p $SINGULARITY_ROOTFS/oasis/tscc/scratch
  mkdir -p $SINGULARITY_ROOTFS/projects/ps-yeolab
  mkdir -p $SINGULARITY_ROOTFS/projects/ps-yeolab3
  mkdir -p $SINGULARITY_ROOTFS/projects/ps-scrm
  mkdir -p $SINGULARITY_ROOTFS/oasis/projects/nsf

  # for Cincinnati Children's Hospital mounts
  mkdir -p $SINGULARITY_ROOTFS/users
  mkdir -p $SINGULARITY_ROOTFS/data
  mkdir -p $SINGULARITY_ROOTFS/scratch

  # for West Virginia University mounts
  mkdir -p $SINGULARITY_ROOTFS/users
  mkdir -p $SINGULARITY_ROOTFS/gpfs
  mkdir -p $SINGULARITY_ROOTFS/group

  # for Alain's laptop
  mkdir -p $SINGULARITY_ROOTFS/media/mis


  mkdir -p $SINGULARITY_ROOTFS/opt/condaenvexports
  mkdir -p $SINGULARITY_ROOTFS/opt/donewith
  mkdir -p $SINGULARITY_ROOTFS/opt/datasets
  mkdir -p $SINGULARITY_ROOTFS/opt/members
  mkdir -p $SINGULARITY_ROOTFS/opt/patches
  mkdir -p $SINGULARITY_ROOTFS/opt/demos/

  # these are needed early for post section
  cp -r ./datasets/* $SINGULARITY_ROOTFS/opt/datasets/
  cp -r ./members/*  $SINGULARITY_ROOTFS/opt/members/
  cp -r ./patches/*  $SINGULARITY_ROOTFS/opt/patches/

  cp -r ./demos/*    $SINGULARITY_ROOTFS/opt/demos/

  ################
%post -c /bin/bash
  ################
  # running post scriptlet
  # this is run inside the container to install all necessary packages

  set -o xtrace
  set -o nounset
  # set -o errexit
  # set -o pipefail



  # ubuntu does not have bash in /usr/bin/env ??
  ln -s /bin/bash /usr/bin/bash

  ##############
  # UBUNTU NAKED

  export LC_ALL=C

  apt-get -y install ubuntu-standard
  apt-get -y install ubuntu-server

  add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION} main"
  add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION} universe"
  add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION} multiverse"
  add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION} restricted"

  add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION}-updates main"
  add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION}-updates universe"
  add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION}-updates multiverse"
  add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION}-updates restricted"

  add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION}-backports main"
  add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION}-backports universe"
  add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION}-backports multiverse"
  add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION}-backports restricted"

  add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION}-security main"
  add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION}-security universe"
  add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION}-security multiverse"
  add-apt-repository -y "deb ${MIRRORURL} ${OSVERSION}-security restricted"

  apt-get -y update && apt-get -y upgrade

  echo "======================================================================"
  touch /opt/donewith/ubuntu_naked
  echo "======================================================================"



  ########
  # UBUNTU

  #apt-get -y update
  apt-get -y install make gcc g++ zlib1g-dev libncurses5-dev nano unzip
  apt-get install -y xorg
  # cleanup   x? M
  apt-get clean
  g++ --version

  # fix for /bin/gtar: not found when running devtools::install_git()
  ln -s /bin/tar /bin/gtar

  echo "======================================================================"
  touch /opt/donewith/ubuntu
  echo "======================================================================"


  ###########
  # MINICONDA  # instead of having: From: continuumio/miniconda:4.3.11
  # from https://hub.docker.com/r/continuumio/miniconda/~/dockerfile/

  # ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

  apt-get update --fix-missing

  apt-get install -y wget bzip2 ca-certificates \
    libglib2.0-0 libxext6 libsm6 libxrender1 \
    git mercurial subversion

  #echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh
  wget --quiet https://repo.continuum.io/miniconda/Miniconda2-4.3.14-Linux-x86_64.sh -O ~/miniconda.sh
  /bin/bash ~/miniconda.sh -b -p /opt/conda
  rm ~/miniconda.sh

  #apt-get install -y curl grep sed dpkg
  #TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o "/v.*\"" | sed 's:^..\(.*\).$:\1:'`
  #curl -L "https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb" > tini.deb
  #dpkg -i tini.deb
  #rm tini.deb
  #apt-get clean

  #ENV PATH /opt/conda/bin:$PATH
  #ENTRYPOINT [ "/usr/bin/tini", "--" ]
  #CMD [ "/bin/bash" ]

  # this is required here as the environment section is not processed yet
  PATH=/opt/conda/bin:$PATH
  export PATH
  echo "======================================================================"
  touch /opt/donewith/conda
  echo "======================================================================"


  # jupyter=1.0.0
  echo "======================================================================"
  NAME=jupyternotebook
  VERSION=5.0.0
  echo "======================================================================"
  conda create --yes -n jupyternotebook python=3.6.2 notebook=5.0.0
  conda env export -n jupyternotebook > /opt/condaenvexports/jupyternotebook-5.0.0.yaml
  PATH="/opt/conda/envs/jupyternotebook/bin:$PATH"
  export PATH
  JUPYTER_PATH=/opt/conda/envs/jupyternotebook/share/jupyter
  export JUPYTER_PATH
  KERNELS=${JUPYTER_PATH}/kernels
  export KERNELS
  mkdir -p $KERNELS
  echo "======================================================================"
  touch /opt/donewith/jupyternotebook
  echo "======================================================================"



  # TODO IRKERNEL: replace devtools::install_github('IRkernel/IRkernel') with devtools::install_url
  # devtools::install_url('https://github.com/IRkernel/IRkernel/archive/0.8.8.tar.gz ');

  # TODO how to check things out in R
  # /opt/conda/envs/basics/bin/R --no-restore --no-save -e "library(); loadedNamespaces();"


  add_algorithm()
  {
    echo "===================================================================="
    NAME=$1
    VERSION=$2
    echo "===================================================================="
    PYVERSION=$3
    RVERSION=$4
    DESCRIPTION=$5
    CHANNELS=$6
    PACKAGES=$7
    PIPS=$8
    BIOCLITE=$9
    GITHUB=${10}
    URL=${11}

    PYTHONPACKAGE=""; if [ ${PYVERSION} != "none" ] ; then PYTHONPACKAGE="python=${PYVERSION}"; fi
    RBASEPACKAGE="" ; if [ ${RVERSION}  != "none" ] ; then RBASEPACKAGE="r-base=${RVERSION}"  ; fi
    conda create --yes --name ${NAME} ${CHANNELS} ${PYTHONPACKAGE} ${RBASEPACKAGE} ${PACKAGES}
    #conda env export --name ${NAME} > /opt/condaenvexports/${NAME}_ROOTENV.yaml

    ENVLIB="/opt/conda/envs/${NAME}/lib"
    ENVPYTHON="/opt/conda/envs/${NAME}/bin/python"
    ENVR="/opt/conda/envs/${NAME}/lib/R/bin/R"
    ENVPIPINSTALL="/opt/conda/envs/${NAME}/bin/pip install"
    ENVREXEC="/opt/conda/envs/${NAME}/bin/R --no-restore --no-save -e"

    PYDISPLAYNAME=$(echo "${NAME} ${DESCRIPTION} v${VERSION} python${PYVERSION}")                #  | sed -e 's/ /_/g'
    RDISPLAYNAME=$(echo "${NAME} ${DESCRIPTION} v${VERSION} r${RVERSION}" )
    PYKERNELSPEC='{"argv": ["fix_ld_library_path", "'${NAME}'" , "'${ENVPYTHON}'" , "-m", "ipykernel_launcher", "-f", "{connection_file}"], "display_name":"'${PYDISPLAYNAME}'", "language":"python"}'
    RKERNELSPEC='{"argv":  ["fix_ld_library_path", "'${NAME}'" , "'${ENVR}'", "--slave", "-e", "IRkernel::main()", "--args", "{connection_file}"], "display_name":"'${RDISPLAYNAME}'", "language":"R"}'
    if [ ${PYVERSION} != "none" ] ; then
      cp -r  /opt/patches/jupyter/kernels/python3 ${KERNELS}/"${NAME}_python"
      echo "${PYKERNELSPEC}" > ${KERNELS}/"${NAME}_python"/kernel.json
#      ${ENVPYTHON} -m pip uninstall ipykernel
#      ${ENVPYTHON} -m pip install ipykernel
    fi
    if [ ${RVERSION} != "none" ] ; then
      cp -r  /opt/patches/jupyter/kernels/ir ${KERNELS}/"${NAME}_r"
      echo "${RKERNELSPEC}" > ${KERNELS}/"${NAME}_r"/kernel.json
    fi

    if [ "${PIPS}"     != "none" ]; then ${ENVPIPINSTALL} "${PIPS}"                          ; fi
    if [ "${BIOCLITE}" != "none" ]; then ${ENVREXEC} "BiocInstaller::biocLite('${BIOCLITE}')"; fi
    if [ "${GITHUB}"   != "none" ]; then ${ENVREXEC} "devtools::install_github('${GITHUB}')" ; fi
    if [ "${URL}"      != "none" ]; then ${ENVREXEC} "devtools::install_url('${URL}')"       ; fi

    echo "===================================================================="
    touch /opt/donewith/${NAME}
    echo "===================================================================="
  }









#      #  # r-rbase=       r-rbase=3.3.2
#      #  # r-rcpp=0.12.11 r-rcpp=0.12.8
#
#      #  add_algorithm basics \
#      #     0.7.27 \
#      #    "none" \
#      #     3.3.2 \
#      #    "Bayesian Analysis of Single-Cell Sequencing Data" \
#      #    "-c r -c bioconda" \
#      #    "r-argparse=1.0.4 r-irkernel=0.7.1 r-devtools=1.12.0 bioconductor-biocinstaller=1.24.0  r-knitr=1.15.1 r-xml=3.98_1.5 r-httpuv=1.3.3 r-shiny=0.14.2 r-shinydashboard=0.5.3 bioconductor-biomart=2.28.0 r-rcpp=0.12.8 bioconductor-biocgenerics=0.20.0" \
#      #    "none" \
#      #    "scran" \
#      #    "catavallejos/BASiCS" \
#      #    "none"
#
#      #  #
#      #  #  '/opt/conda/envs/basics/lib/R/bin/R' --no-site-file --no-environ --no-save  \
#      #  #    --no-restore --quiet CMD INSTALL  \
#      #  #    '/tmp/RtmpSyaYl5/devtools299a7f9af35f/catavallejos-BASiCS-7ecd7f2'  \
#      #  #    --library='/opt/conda/envs/basics/lib/R/library' --install-tests
#      #  #
#      #  #  ERROR: dependency 'scran' is not available for package 'BASiCS'
#      #  #  * removing '/opt/conda/envs/basics/lib/R/library/BASiCS'
#





      #library(statmod)
      #require(ggplot2)
      #library(gplots)
      #require(DESeq2)
      #library(scLVM)

      #  # -c chasehere r-rpython
      #  # -c bioconda limix
      #  # -c conda-forge gpy

      #  # r-argparse

      #  # hdf5

      ##  r-rpython=0.0_ neeeds rbase-3.2.2  !!
      #  add_algorithm sclvm \
      #    0.1.8 \
      #    2.7.13 \
      #    3.2.2 \
      #    "Modelling framework for single-cell RNA-seq data that can be used to dissect the observed heterogeneity into different sources, thereby allowing for the correction of confounding sources of variation" \
      #    "-c r -c bioconda -c chasehere -c conda-forge" \
      #    "r-irkernel  h5py=2.7.0 matplotlib=2.0.2 gpy=1.7.7 limix=0.7.12 r-rpython=0.0_6 r-statmod=1.4.29 r-gplots=3.0.1 bioconductor-deseq2=1.14.1 bioconductor-genefilter=1.58.1" \
      #    "scLVM==0.1.8" \
      #    "none" \
      #    "none" \
      #    "none"

      #    #'/opt/conda/envs/sclvm/bin/R --no-restore --no-save -e "devtools::install_github('PMBio/scLVM')";'
      #    # https://github.com/PMBio/scLVM/archive/V0.1.tar.gz





#      # https://github.com/sandhya212/BISCUIT_SingleCell_IMM_ICML_2016
#      # https://genomicscomputbiol.org/ojs/index.php/GCB/article/view/46
#      #  add_algorithm biscuit \
#  add_algorithm biscuit \
#    0.0.20170829 \
#    none \
#    3.4.1  \
#    "Infinite Mixture Model to cluster and impute single cells"  \
#    "-c r" \
#    "r-argparse=1.0.4 r-irkernel=0.7.1 r-devtools=1.13.2     MCMCpack r-mvtnorm r-ellipse r-coda r-Matrix r-Rtsne r-gtools r-foreach r-doParallel r-doSNOW r-snow r-lattice r-MASS r-bayesm r-robustbase r-chron r-mnormt r-schoolmath r-devtools r-RColorBrewer   " \
#    none \
#    none \
#    none \
#    none



# Bayesian Regression Models using Stan
# brms=1.9.0
# https://cran.r-project.org/src/contrib/brms_1.9.0.tar.gz
#  add_algorithm pystan \
#    2.15.0.1 \
#    3.6.2 \
#    none  \
#    none  \
#    "-c conda-forge" \
#    "pystan=2.15.0.1" \
#    none \
#    none \
#    none \
#    none



#  # Batch effects and the effective design of single cell gene expression studies
#  # http://www.biorxiv.org/content/biorxiv/early/2016/07/08/062919.full.pdf
#  # https://www.nature.com/articles/srep33892
#  add_algorithm ccremover \
#    1.0.4 \
#    none \
#    3.3.2\
#    "Removes the Cell-Cycle Effect from Single-Cell RNA-Sequencing Data" \
#    "-c r -c bioconda" \
#    "r-argparse=1.0.4 r-irkernel=0.7.1 r-devtools=1.13.2 r-knitr=1.16 r-rmarkdown=1.5" \
#    none \
#    none \
#    none \
#    "https://cran.r-project.org/src/contrib/ccRemover_1.0.4.tar.gz"


#  add_algorithm citrus \
#    0.99.0 \
#    none \
#    3.4.1 \
#    "Includes scPLS , Normalization of single cell RNA sequencing data using both control and target genes" \
#    "-c r" \
#    "r-argparse=1.0.4 r-irkernel=0.7.1 r-devtools=1.13.2 r-rcpp=0.12.11 r-rcpparmadillo=0.7.900.2.0 r-cairo=1.5_9" \
#    "none" \
#    "none" \
#    "ChenMengjie/Citrus" \
#    "none"


  add_algorithm combatpy \
    0.0.20170804 \
    3.6.2 \
    3.3 \
    "Combatting batch effects when combining batches of gene expression microarray data" \
    "-c bioconda -c r" \
    "r-argparse=1.0.4 r-irkernel=0.7.1 r-devtools=1.12.0 bioconductor-biocinstaller=1.24.0 bioconductor-sva=3.20.0 pandas=0.20.3 patsy=0.4.1 ipykernel=4.6.1" \
    none \
    "bladderbatch" \
    none \
    none

  # to dissect single-cell transcriptome heterogeneity, thereby allowing to identify biological drivers of cell-to-cell variability and model confounding factors
  add_algorithm fsclvm \
    1.0.0.dev10 \
    3.6.2 \
    none \
    "Scalable modelling framework for single-cell RNA-seq data that uses gene set annotations" \
    "-c defaults" \
    "r-argparse=1.0.4 r-devtools=1.12.0 scipy=0.19.1 h5py=2.7.0 numpy=1.13.1 matplotlib=2.0.2 scikit-learn=0.19.0 ipykernel=4.6.1" \
    "fscLVM==1.0.0.dev10" \
    none \
    none \
    none

  add_algorithm limma \
    3.30.13 \
    none \
    3.3.2 \
    "Includes removebatcheffect. Linear Models for Microarray and RNA-Seq Data" \
    "-c bioconda -c r" \
    "r-argparse=1.0.4 r-irkernel=0.7.1 r-devtools=1.12.0 bioconductor-limma=3.30.13" \
    none \
    none \
    none \
    none

  # TODO -c pjones whar was that for ?
  add_algorithm ruvseq \
    1.8.0 \
    none \
    3.3.2 \
    "Remove Unwanted Variation from RNA-Seq Data" \
    "-c bioconda  -c r" \
    "r-argparse=1.0.4 r-irkernel=0.7.1 r-devtools=1.12.0 bioconductor-edger=3.16.5 bioconductor-edaseq=2.8.0 bioconductor-ruvseq=1.10.0" \
    none \
    none \
    none \
    none




## ERROR: dependencies 'quantreg', 'cluster', 'SummarizedExperiment' are not available for package 'SCnorm'
## bioconductor-summarizedexperiment 1.4.0* -> bioconductor-biobase -> bioconductor-biocgenerics >=0.3.2 -> r 3.2.2* -> r-base 3.2.2
## https://bioconductor.org/packages/release/bioc/src/contrib/SummarizedExperiment_1.6.3.tar.gz
#  add_algorithm scnorm \
#    0.99.7 \
#    "none" \
#    3.4.1 \
#    "Robust normalization of single-cell RNA-seq data" \
#    "-c bioconda -c r -c kurtwheeler" \
#    "r-argparse=1.0.4 r-irkernel=0.7.1 r-devtools=1.13.2 bioconductor-biocinstaller=1.26.0 r-cairo=1.5_9 r-quantreg=5.33 r-cluster=2.0.6" \
#    none \
#    "SummarizedExperiment" \
#    none \
#    "https://bioconductor.org/packages/devel/bioc/src/contrib/SCnorm_0.99.7.tar.gz"
#
#
#
## -c kurtwheeler bioconductor-biocinstaller=1.26.0
####################################################
#  add_algorithm scone \
#    1.1.2 \
#    "none" \
#    3.4.1 \
#    "Comparing and ranking the performance of different normalization schemes for single-cell RNA-seq and other high-throughput analyses" \
#    "-c r -c bioconda -c kurtwheeler" \
#    "r-argparse=1.0.4 r-irkernel=0.7.1 r-devtools=1.13.2 bioconductor-biocinstaller=1.26.0 r-cairo=1.5_9" \
#    none \
#    "scone" \
#    none \
#    none




  add_algorithm scran \
    1.4.5 \
    none \
    3.3.2 \
    "Includes mnnCorrect. Implements a variety of low-level analyses of single-cell RNA-seq data" \
    "-c r -c bioconda " \
    "r-argparse=1.0.4 r-irkernel=0.7.1 r-devtools=1.12.0 bioconductor-biocinstaller=1.24.0 r-knitr=1.15.1 r-xml=3.98_1.5 r-httpuv=1.3.3 r-shiny=0.14.2 r-shinydashboard=0.5.3 bioconductor-biomart=2.28.0 bioconductor-biocstyle=2.0.3" \
    none \
    "scran" \
    none \
    none


#
##
##
#####  TODO  seurat needs to do URL before GITHUB
##
## 3.4.1
## r-fpc 2.1_10* -> r-base 3.3.2*
## r-devtools=1.13.2
##############################################################################################
## r-compositions  https://cran.r-project.org/src/contrib/compositions_1.40-1.tar.gz
## r-diffusionMap  https://cran.r-project.org/src/contrib/diffusionMap_1.1-0.tar.gz
##############################################################################################
## -c bioconda r-fpc=2.1_10
##
##During startup - Warning messages:
##1: Setting LC_CTYPE failed, using "C"
##2: Setting LC_TIME failed, using "C"
##3: Setting LC_MESSAGES failed, using "C"
##4: Setting LC_MONETARY failed, using "C"
##5: Setting LC_PAPER failed, using "C"
##6: Setting LC_MEASUREMENT failed, using "C"
#  add_algorithm seurat \
#    2.0.0 \
#    "none" \
#    3.3.2\
#    "QC , analysis , and exploration of single cell RNA-seq data. Identify and interpret sources of heterogeneity from single cell transcriptomic measurements, and to integrate diverse types of single cell data" \
#    "-c r -c bioconda" \
#    "r-argparse=1.0.4 r-irkernel=0.7.1 r-devtools=1.13.2 r-cairo=1.5_9 r-ROCR r-lars=1.2 r-fpc=2.1_10 r-ape=4.0 r-VGAM=1.0_2 r-igraph=1.0.1 r-caret=6.0_73 r-gplots=3.0.1  r-NMF=0.20.6 r-plotly=4.5.6  r-Hmisc" \
#    none \
#    none \
#    "satijalab/seurat" \
#    "https://cran.r-project.org/src/contrib/tclust_1.3-1.tar.gz"



#
#UnsatisfiableError: The following specifications were found to be in conflict:
#  - r-base 3.4.1*
#  - r-caret 6.0_73* -> r-base 3.3.2*
#- r-vgam 1.0_2* -> r-base 3.3.1*
# - r-vgam 1.0_2* -> r-base 3.3.1*

#
#UnsatisfiableError: The following specifications were found to be in conflict:
#  - r-devtools 1.13.2*
#  - r-fpc 2.1_10*
#

#UnsatisfiableError: The following specifications were found to be in conflict:
#  - r-devtools 1.13.2*
#  - r-fpc

#UnsatisfiableError: The following specifications were found to be in conflict:
#  - r-devtools 1.13.2*
#  - r-plotly 4.5.6*





  add_algorithm svaseq \
    1.8.0 \
    none \
    3.3 \
    "Removing batch effects and other unwanted variation in high-throughput experiments" \
    "-c bioconda -c r" \
    "r-argparse=1.0.4 r-irkernel r-devtools=1.12.0 bioconductor-sva=3.20.0" \
    none \
    none \
    none \
    none

  #  Removes batch effects in a real dataset without using labels and detects biological groups despite variable censoring in simulated data
  add_algorithm vamf \
    0.0.20170804 \
    none \
    3.4.1 \
    "Varying-Censoring Aware Matrix Factorization for Single Cell RNA-Sequencing." \
    "-c bioconda -c r" \
    "r-argparse=1.0.4 r-irkernel=0.7.1 r-devtools=1.13.2 bioconductor-biocinstaller=1.22.3 r-rstan=2.15.1 r-cairo=1.5_9" \
    none \
    none \
    "willtownes/vamf" \
    none

  touch /opt/donewith/members_envs

  /opt/conda/bin/conda env export -n root > /opt/condaenvexports/root_$(date +%Y-%m-%d-%H-%M).yaml
  # cleanup 666MB
  /opt/conda/bin/conda clean --index-cache --tarballs --packages --yes
  #chmod --recursive --changes +755 /opt/*
  chmod --recursive +755 /opt/*

  touch /opt/donewith/condaenvexportroot_condaclean_chmod

  set +x


  ##########
%environment
  ##########

  PATH="/opt/conda/bin:$PATH"
  PATH="/opt/conda/envs/jupyternotebook/bin:$PATH"

  PATH="/opt/members/activate:$PATH"
  PATH="/opt/members/scbatchget:$PATH"
  PATH="/opt/members/jupyternotebook:$PATH"

  PATH="/opt/members/basics:$PATH"
  PATH="/opt/members/combatpy:$PATH"
  PATH="/opt/members/fsclvm:$PATH"
  PATH="/opt/members/limma:$PATH"
  PATH="/opt/members/ruvseq:$PATH"
  PATH="/opt/members/sclvm:$PATH"
  PATH="/opt/members/scnorm:$PATH"
  PATH="/opt/members/scran:$PATH"
  PATH="/opt/members/seurat:$PATH"
  PATH="/opt/members/svaseq:$PATH"
  PATH="/opt/members/vamf:$PATH"

  export PATH

  HOSTIP=$(hostname -i)
  export HOSTIP

  JUPYTER_PATH=/opt/conda/envs/jupyternotebook/share/jupyter
  export JUPYTER_PATH

  KERNELS=${JUPYTER_PATH}/kernels
  export KERNELS

  alias echopathtr='echo $PATH | tr ":" "\n"'
  alias ll='ls -lhF'

  #####
%labels
  #####

  MAINTAINER alaindomissy@gmail.com
  VERSION 0.0.1-20170827
  BUILD_DATE "${date -Iminutes}"

  #    AUTHOR_NAME Marty Kandes
  #    AUTHOR_EMAIL mkandes@sdsc.edu
  #    APPLICATION_NAME none
  #    APPLICATION_VERSION none
  #    APPLICATION_URL none
  #    SYSTEM_NAME comet
  #    SYSTEM_SINGULARITY_VERSION 2.3.1
  #    SYSTEM_URL http://www.sdsc.edu/support/user_guides/comet.html
  #    VERSION 0.0.5
  #    LAST_UPDATED 20170811



  ####
%files
  ####
  # TODO permissions will nbe 700 !
  documentation      /opt/
  tests              /opt/


  ########
%runscript
  ########
  # this will get copied to /.singularity.d/runscript indide the container
  # which will run whenever the container is called as an executable

  echo ========================================================================
  echo container image downloaded, now setting shortcuts
  echo ========================================================================

  #set -o xtrace
  set -o nounset
  #set -o errexit
  #set -o pipefail

  if [ $# -eq 0 ]
  then
    IDATE=$(date -Iseconds)
    # IDATE=$(date -Iseconds | tr "\:" "-" | tr "T" "+")

    IMAGENAME=scbatch_${IDATE}_${SINGULARITY_NAME}
    mv ${SINGULARITY_NAME} ${IMAGENAME}
    ln -sf ${IMAGENAME} scbatch.img


    cp -r /opt/conda/envs/jupyternotebook/share/jupyter/kernels   ./
    cp -r /opt/demos            ./
    cp /opt/patches/scripts/*   ./


    ln -sf batcheffects scbatch_getdataset
    ln -sf batcheffects scbatch_notebook

    echo
    echo "===================================================================="
    echo "to complete this installation, please type:"
    echo
    echo "                     source SOURCEME"
    echo
    echo "to start jupyter, please type:"
    echo
    echo "                     scbatch_notebook"
    echo
    echo "Enjoy single-cell batcheffects !"
    echo "===================================================================="
    echo


    # scbatch_notebook

  else
      echo "batcheffects image called with run and some arguments - did you mean to exec instead ?"
  fi

 ####
%test
 ####

  # /opt/tests/test
```

## Collection

 - Name: [alaindomissy/scbatch](https://github.com/alaindomissy/scbatch)
 - License: None

