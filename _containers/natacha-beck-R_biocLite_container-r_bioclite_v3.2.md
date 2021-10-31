---
id: 3464
name: "natacha-beck/R_biocLite_container"
branch: "master"
tag: "r_bioclite_v3.2"
commit: "b5b8c30cef05b3c20e22de509bbfc6224a018f17"
version: "7c783a25f80cef6889b72fb3ff055276"
build_date: "2018-07-10T19:29:39.798Z"
size_mb: 3906
size: 1487421471
sif: "https://datasets.datalad.org/shub/natacha-beck/R_biocLite_container/r_bioclite_v3.2/2018-07-10-b5b8c30c-7c783a25/7c783a25f80cef6889b72fb3ff055276.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/natacha-beck/R_biocLite_container/r_bioclite_v3.2/2018-07-10-b5b8c30c-7c783a25/
recipe: https://datasets.datalad.org/shub/natacha-beck/R_biocLite_container/r_bioclite_v3.2/2018-07-10-b5b8c30c-7c783a25/Singularity
collection: natacha-beck/R_biocLite_container
---

# natacha-beck/R_biocLite_container:r_bioclite_v3.2

```bash
$ singularity pull shub://natacha-beck/R_biocLite_container:r_bioclite_v3.2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:6.6


#############################################################
#                                                           #
# MCIN (McGill Centre for Integrative Neuroscience)         #
#                                                           #
# Singularity recipe for Bioclite (R) to build a            #
# container used in CBRAIN (https://github.com/aces/cbrain) #
#                                                           #
#############################################################

%labels
  Maintainer Natacha Beck

%help
This is an attempt to package a singularity container with all the R library to run genomic pipeline 
such as the methylation pipeline(https://github.com/GreenwoodLab/methylation450KPipeline) 

%post
yum update  -y
yum install -y gcc                      \
               perl                     \
               make                     \
               autoconf                 \
               automake                 \
               gcc-gfortran             \
               compat-gcc-34-g77.x86_64 \
               wget                     \
               tar                      \
               gcc-c++                  \
               readline-devel           \
               libXt-devel              \
               java-1.8.0-openjdk-devel \
               which                    \
               git                      \
               libcurl libcurl-devel    \
               openssl-devel            \
               libxml2-devel            \
               libpng-devel             \
               mesa-libGLU-devel.x86_64 \
               texlive-latex            \
               pango                    \
               pango-devel              \
               libX11-devel             \
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
echo 'source("http://bioconductor.org/biocLite.R"); biocLite(ask=FALSE); biocLite(c("minfi","wateRmelon","shinyMethyl","shinyMethylData"), ask=FALSE)' > /tmp/packages_bioc.R
Rscript /tmp/packages_bioc.R

# Install all other R packages
echo 'install.packages(c("httpuv", "devtools", "matrixStats", "RColorBrewer", "shiny", "rmarkdown", "knitr", "DT"), repos= "http://cran.us.r-project.org")' > /tmp/packages.R
Rscript /tmp/packages.R
```

## Collection

 - Name: [natacha-beck/R_biocLite_container](https://github.com/natacha-beck/R_biocLite_container)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

