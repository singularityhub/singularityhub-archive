---
id: 9703
name: "team113sanger/t113-singularity"
branch: "master"
tag: "r-3.6.0.base-1.0.0"
commit: "b1cb080945415c69c57040a4b02b82e5774adee1"
version: "266ee3720198381ab31065570d4d2968"
build_date: "2020-01-06T14:33:17.020Z"
size_mb: 1672
size: 615432223
sif: "https://datasets.datalad.org/shub/team113sanger/t113-singularity/r-3.6.0.base-1.0.0/2020-01-06-b1cb0809-266ee372/266ee3720198381ab31065570d4d2968.simg"
url: https://datasets.datalad.org/shub/team113sanger/t113-singularity/r-3.6.0.base-1.0.0/2020-01-06-b1cb0809-266ee372/
recipe: https://datasets.datalad.org/shub/team113sanger/t113-singularity/r-3.6.0.base-1.0.0/2020-01-06-b1cb0809-266ee372/Singularity
collection: team113sanger/t113-singularity
---

# team113sanger/t113-singularity:r-3.6.0.base-1.0.0

```bash
$ singularity pull shub://team113sanger/t113-singularity:r-3.6.0.base-1.0.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:centos7
IncludeCmd: no

%help
Help message

%labels
        Maintainer Team113 Wellcome Sanger Institute
        Version v1.0.0
        R_Version 3.6.0

%environment
        export LC_ALL=en_US.UTF-8
        export LANG=en_US.UTF-8

%files
        texlive.profile /tmp/texlive.profile

%apprun R
        exec R "$@"

%apprun Rscript
        exec Rscript "$@"

%runscript
        exec R "$@"

%post
        # Software versions
         export R_VERSION=3.6.0

        # Language
        export LC_ALL=en_US.UTF-8
        export LANG=en_US.UTF-8

        # Get dependencies
        yum update -y
        yum install -y \
                        autoconf \
                        bzip bzip2-devel \
                        cairo-devel \
                        firefox \
                        gcc \
                        gcc-gfortran \
                        gcc-c++ \
                        git \
                        java-1.8.0-openjdk-devel \
                        libcurl-devel \
                        libjpeg-turbo libjpeg-devel \
                        libpng libpng-devel \
                        libtiff libtiff-devel \
			libxml2-devel \
                        libXt-devel \
                        libX11-devel \
                        make \
			openssl-devel \
                        perl-Digest-MD5 \
                        perl-Tk \
                        pcre-devel \
                        readline-devel \
                        tar \
                        tcl-devel \
			texinfo \
                        tk-devel \
                        unzip \
                        vim-minimal \
                        wget \
                        which \
                        xdg-utils \
                        xorg-x11-server-devel \
                        xz-devel \
                        zlib zlib-devel 
        
        # Install basic texlive from profile
        cd /tmp
        wget http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
	tar -xzf install-tl-unx.tar.gz
	cd install-tl-20*
	./install-tl --profile=/tmp/texlive.profile
	tlmgr install titling framed inconsolata xkeyval
	tlmgr install collection-fontsrecommended
	tlmgr option -- autobackup 0

        # Download R
        curl -O https://cran.r-project.org/src/base/R-3/R-${R_VERSION}.tar.gz
        tar -xf R-${R_VERSION}.tar.gz
        cd R-${R_VERSION}

        # Configure
        ./configure     --enable-R-shlib \
                                --enable-memory-profiling \
                                --with-readline \
                                --with-blas \
                                --with-tcltk \
                                --disable-nls \
                                --with-cairo \
                                --with-recommended-packages
				
        # Build and install
        make -j4
        make install
        make install-libR
        make check
	
	# Install R packages from CRAN
	Rscript -e "install.packages(pkgs = c('devtools', 'tidyverse', 'argparse', 'pheatmap'), repos='https://www.stats.bris.ac.uk/R/', dependencies=TRUE, clean = TRUE)"
	
        # Clean up
        yum clean all && rm -rf /var/cache/yum
        rm -rf /tmp/${R_VERSION}
        rm -rf /tmp/install-tl*
```

## Collection

 - Name: [team113sanger/t113-singularity](https://github.com/team113sanger/t113-singularity)
 - License: None

