---
id: 10671
name: "Simontuk/singularity-r"
branch: "master"
tag: "latest"
commit: "0c63df498a86f5770acaae8ea963e86030a444ba"
version: "2094c9451da14e245c23ce490917c47b"
build_date: "2019-08-21T07:31:45.780Z"
size_mb: 1255.0
size: 473653279
sif: "https://datasets.datalad.org/shub/Simontuk/singularity-r/latest/2019-08-21-0c63df49-2094c945/2094c9451da14e245c23ce490917c47b.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/Simontuk/singularity-r/latest/2019-08-21-0c63df49-2094c945/
recipe: https://datasets.datalad.org/shub/Simontuk/singularity-r/latest/2019-08-21-0c63df49-2094c945/Singularity
collection: Simontuk/singularity-r
---

# Simontuk/singularity-r:latest

```bash
$ singularity pull shub://Simontuk/singularity-r:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: centos:latest
IncludeCmd: yes


%labels
  Maintainer Simon Steiger
  R_Version 3.6.1

%apprun R
  exec R "${@}"

%apprun Rscript
  exec Rscript "${@}"

%runscript
  exec R "${@}"

%post
  # Software versions
  export R_VERSION=3.6.1
  
  # Configure default locale
  localedef -c -f UTF-8 -i en_US en_US.UTF-8
  export LC_ALL=en_US.UTF-8
  export LANG=en_US.UTF-8
  echo "LC_ALL=en_US.UTF-8" >> /etc/environment
  echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
  echo "LANG=en_US.UTF-8" > /etc/locale.conf
  

# Get dependencies
  yum install -y epel-release
  yum update -y

  yum groupinstall -y "Development Tools"
  yum install -y libcurl-devel openssl-devel libxml2-devel hdf5-devel libssh2-devel
  yum install -y libpng-devel libjpeg-turbo-devel cairo-devel

  yum install -y R

  # Add a default CRAN mirror
  echo "options(repos = c(CRAN = 'https://cran.rstudio.com/'), download.file.method = 'libcurl')" >> /usr/lib64/R/etc/Rprofile.site

  # Add a directory for host R libraries
  mkdir -p /library
  echo "R_LIBS_SITE=/library:\${R_LIBS_SITE}" >> /usr/lib64/R/etc/Renviron.site


  # Clean up
  yum clean all
```

## Collection

 - Name: [Simontuk/singularity-r](https://github.com/Simontuk/singularity-r)
 - License: [MIT License](https://api.github.com/licenses/mit)

