---
id: 8521
name: "tpall/singularity-r"
branch: "master"
tag: "3.5.2"
commit: "a8d47247b8a49e5a88a77f57798653eb0f418140"
version: "66fbd70ff8026e843cdc3f3242a301c2"
build_date: "2020-10-20T14:44:12.266Z"
size_mb: 613
size: 239824927
sif: "https://datasets.datalad.org/shub/tpall/singularity-r/3.5.2/2020-10-20-a8d47247-66fbd70f/66fbd70ff8026e843cdc3f3242a301c2.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/tpall/singularity-r/3.5.2/2020-10-20-a8d47247-66fbd70f/
recipe: https://datasets.datalad.org/shub/tpall/singularity-r/3.5.2/2020-10-20-a8d47247-66fbd70f/Singularity
collection: tpall/singularity-r
---

# tpall/singularity-r:3.5.2

```bash
$ singularity pull shub://tpall/singularity-r:3.5.2
```

## Singularity Recipe

```singularity
BootStrap: docker
From: debian:stretch

%labels
  Maintainer tpall
  R_Version 3.5.2

%apprun R
  exec R "${@}"

%apprun Rscript
  exec Rscript "${@}"

%runscript
  exec R "${@}"

%environment
  LC_ALL=en_US.UTF-8
  LANG=en_US.UTF-8
  TERM=xterm
  export LC_ALL LANG TERM

%post
  # Software versions
  export R_VERSION=${R_VERSION:-3.5.2}

 # Get dependencies
  apt-get update \
  && apt-get install -y --no-install-recommends \
    locales

  # Configure default locale
  echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
  locale-gen en_US.utf8
  /usr/sbin/update-locale LANG=en_US.UTF-8
  export LC_ALL=en_US.UTF-8
  export LANG=en_US.UTF-8
  
  # Configure term
  export TERM=xterm

  # Install R
  apt-get update \
  && apt-get install -y --no-install-recommends \
    bash-completion \
    ca-certificates \
    file \
    fonts-texgyre \
    g++ \
    gfortran \
    gsfonts \
    libblas-dev \
    libbz2-1.0 \
    libcurl3 \
    libicu57 \
    libjpeg62-turbo \
    libopenblas-dev \
    libpangocairo-1.0-0 \
    libpcre3 \
    libpng16-16 \
    libreadline7 \
    libtiff5 \
    liblzma5 \
    make \
    unzip \
    zip \
    zlib1g \
  && BUILDDEPS="curl \
    default-jdk \
    libbz2-dev \
    libcairo2-dev \
    libcurl4-openssl-dev \
    libpango1.0-dev \
    libjpeg-dev \
    libicu-dev \
    libpcre3-dev \
    libpng-dev \
    libreadline-dev \
    libtiff5-dev \
    liblzma-dev \
    libx11-dev \
    libxt-dev \
    unixodbc-dev
    perl \
    tcl8.6-dev \
    tk8.6-dev \
    texinfo \
    texlive-extra-utils \
    texlive-fonts-recommended \
    texlive-fonts-extra \
    texlive-latex-recommended \
    x11proto-core-dev \
    xauth \
    xfonts-base \
    xvfb \
    zlib1g-dev" \
  && apt-get install -y --no-install-recommends $BUILDDEPS \
  && cd tmp/
  
  ## Download source code
  curl -O https://cran.r-project.org/src/base/R-3/R-${R_VERSION}.tar.gz
  
  ## Extract source code
  tar -xf R-${R_VERSION}.tar.gz \
  && cd R-${R_VERSION}
  
  ## Set compiler flags
  R_PAPERSIZE=letter \
    R_BATCHSAVE="--no-save --no-restore" \
    R_BROWSER=xdg-open \
    PAGER=/usr/bin/pager \
    PERL=/usr/bin/perl \
    R_UNZIPCMD=/usr/bin/unzip \
    R_ZIPCMD=/usr/bin/zip \
    R_PRINTCMD=/usr/bin/lpr \
    LIBnn=lib \
    AWK=/usr/bin/awk \
    CFLAGS="-g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g" \
    CXXFLAGS="-g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g"
  
  ## Configure options
  ./configure --enable-R-shlib \
               --enable-memory-profiling \
               --with-readline \
               --with-blas \
               --with-tcltk \
               --disable-nls \
               --with-recommended-packages
  
  ## Build and install
  make \
  && make install
  
  ## Add a default CRAN mirror
  echo "options(repos = c(CRAN = 'https://cran.rstudio.com/'), download.file.method = 'libcurl')" >> /usr/local/lib/R/etc/Rprofile.site
  
  ## Add a library directory (for user-installed packages)
  mkdir -p /usr/local/lib/R/site-library
  
  ## Set site library path
  echo "R_LIBS_SITE='/usr/local/lib/R/site-library'" >> /usr/local/lib/R/etc/Renviron
  
  ## Install packages from date-locked MRAN snapshot of CRAN
  [ -z "$BUILD_DATE" ] && BUILD_DATE=$(TZ="America/Los_Angeles" date -I) || true \
  && MRAN=https://mran.microsoft.com/snapshot/${BUILD_DATE} \
  && echo MRAN=$MRAN >> /etc/environment \
  && export MRAN=$MRAN \
  && echo "options(repos = c(CRAN = '$MRAN'), download.file.method = 'libcurl')" >> /usr/local/lib/R/etc/Rprofile.site
  
  ## Use littler installation scripts
  Rscript -e "install.packages(c('littler', 'docopt'), repo = '$MRAN')" \
  && ln -s /usr/local/lib/R/site-library/littler/examples/install2.r /usr/local/bin/install2.r \
  && ln -s /usr/local/lib/R/site-library/littler/examples/installGithub.r /usr/local/bin/installGithub.r \
  && ln -s /usr/local/lib/R/site-library/littler/bin/r /usr/local/bin/r
  
  ## Clean up from R source install
  cd / \
  && rm -rf /tmp/* \
  && apt-get remove --purge -y $BUILDDEPS \
  && apt-get autoremove -y \
  && apt-get autoclean -y \
  && rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [tpall/singularity-r](https://github.com/tpall/singularity-r)
 - License: [MIT License](https://api.github.com/licenses/mit)

