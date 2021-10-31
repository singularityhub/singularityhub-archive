---
id: 4776
name: "natacha-beck/methylation450KPipeline"
branch: "singularity"
tag: "methylation450kpipeline_v1.0"
commit: "376969813a73b7294df9823a8e3caaafbb179e61"
version: "e157ace66950c63240433bcec22af993"
build_date: "2018-09-12T19:58:35.161Z"
size_mb: 4040
size: 1583108127
sif: "https://datasets.datalad.org/shub/natacha-beck/methylation450KPipeline/methylation450kpipeline_v1.0/2018-09-12-37696981-e157ace6/e157ace66950c63240433bcec22af993.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/natacha-beck/methylation450KPipeline/methylation450kpipeline_v1.0/2018-09-12-37696981-e157ace6/
recipe: https://datasets.datalad.org/shub/natacha-beck/methylation450KPipeline/methylation450kpipeline_v1.0/2018-09-12-37696981-e157ace6/Singularity
collection: natacha-beck/methylation450KPipeline
---

# natacha-beck/methylation450KPipeline:methylation450kpipeline_v1.0

```bash
$ singularity pull shub://natacha-beck/methylation450KPipeline:methylation450kpipeline_v1.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:6.6

%labels
MAINTAINER Natacha Beck <natabeck@gmail.com>


%files
. /methylation450KPipeline

%post
# Install prerequisite
yum update  -y

# Install basic packages
yum install -y gcc \
               perl \
               make \
               autoconf \
               automake \
               gcc-gfortran \
               compat-gcc-34-g77.x86_64 \
               wget \
               tar \
               gcc-c++ \
               readline-devel \
               libXt-devel \
               java-1.8.0-openjdk-devel \
               which \
               git \
               libcurl libcurl-devel \
               openssl-devel \
               libxml2-devel \
               libpng-devel \
               mesa-libGLU-devel.x86_64 \
               texlive-latex \
               pango \
               pango-devel \
               libX11-devel \
               libxt-dev


yum -y groupinstall "X Window System" "Desktop" "Fonts" "General Purpose Desktop"

# Install rstudio
wget https://download2.rstudio.org/rstudio-server-rhel-0.99.896-x86_64.rpm
yum install -y --nogpgcheck rstudio-server-rhel-0.99.896-x86_64.rpm
ln -s /usr/lib/rstudio-server/bin/pandoc/pandoc /usr/local/bin
ln -s /usr/lib/rstudio-server/bin/pandoc/pandoc-citeproc /usr/local/bin

# Install R-3.2.0
wget http://cran.r-project.org/src/base/R-3/R-3.2.0.tar.gz; tar -zxvf R-3.2.0.tar.gz; cd R-3.2.0; ./configure; make; cp /R-3.2.0/bin/R /bin/; cp /R-3.2.0/bin/Rscript /bin/

# Install all biocLite R packages
echo 'source("http://bioconductor.org/biocLite.R"); biocLite(ask=FALSE); biocLite(c("minfi","minfiData","wateRmelon","shinyMethyl","shinyMethylData"), ask=FALSE)' > /tmp/packages_bioc.R
Rscript /tmp/packages_bioc.R

# Install all other R packages
echo 'install.packages(c("httpuv", "devtools", "matrixStats", "RColorBrewer", "shiny", "rmarkdown", "knitr", "DT"), repos= "http://cran.us.r-project.org")' > /tmp/packages.R
Rscript /tmp/packages.R

# chmod
chmod 755 /methylation450KPipeline
chmod 755 /methylation450KPipeline/methylation450kpipeline_cbrain_process.sh

%environment
PIPELINE_450K=/methylation450KPipeline
PATH=$PATH:$PIPELINE_450K
export PIPELINE_450K

%runscript
exec /bin/bash "$@"
```

## Collection

 - Name: [natacha-beck/methylation450KPipeline](https://github.com/natacha-beck/methylation450KPipeline)
 - License: [GNU General Public License v2.0](https://api.github.com/licenses/gpl-2.0)

