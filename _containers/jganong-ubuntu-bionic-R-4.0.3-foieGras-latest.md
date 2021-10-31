---
id: 15033
name: "jganong/ubuntu-bionic-R-4.0.3-foieGras"
branch: "master"
tag: "latest"
commit: "386f6e0f1d5e1aa9398e3e5508f82c5638955c1e"
version: "9555b4ad09b06069a846704627eb937c"
build_date: "2020-12-04T23:39:23.627Z"
size_mb: 1388.0
size: 496209951
sif: "https://datasets.datalad.org/shub/jganong/ubuntu-bionic-R-4.0.3-foieGras/latest/2020-12-04-386f6e0f-9555b4ad/9555b4ad09b06069a846704627eb937c.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/jganong/ubuntu-bionic-R-4.0.3-foieGras/latest/2020-12-04-386f6e0f-9555b4ad/
recipe: https://datasets.datalad.org/shub/jganong/ubuntu-bionic-R-4.0.3-foieGras/latest/2020-12-04-386f6e0f-9555b4ad/Singularity
collection: jganong/ubuntu-bionic-R-4.0.3-foieGras
---

# jganong/ubuntu-bionic-R-4.0.3-foieGras:latest

```bash
$ singularity pull shub://jganong/ubuntu-bionic-R-4.0.3-foieGras:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:ubuntu:18.04

%labels
MAINTAINER jganong@stanford.edu

%environment
### because singularity also connects to my home directory on the host,
### R packages installed there can interfere with foieGras within singularity, i get this error.
### > library(foieGras)
### Error: package or namespace load failed for ‘foieGras’:
###  .onLoad failed in loadNamespace() for 'TMB', details:
###   call: dyn.load(file, DLLpath = DLLpath, ...)
###   error: unable to load shared object '/home/jeg/R/x86_64-pc-linux-gnu-library/4.0/TMB/libs/TMB.so':
###   libopenblas.so.3: cannot open shared object file: No such file or directory
###
### here i set R_LIBS_USER to empty to avoid this issue
export R_LIBS_USER=

%runscript
exec /usr/bin/R "$@"  

%post  
echo "This singularity image was built to get Ian Jonsen's foieGras R package installed."  
echo "In email, he mentioned that he uses Ubuntu 18.04 and R 4.0.2 and foieGras just works."
echo "So I tried to recreate that, but ended up installing R 4.0.3, but that seems to work OK."
apt update
apt install --yes gnupg
apt install --yes apt-transport-https software-properties-common
export DEBIAN_FRONTEND=noninteractive DEBCONF_NONINTERACTIVE_SEEN=true
echo '
locales locales/locales_to_be_generated multiselect     en_US.UTF-8 UTF-8
locales locales/default_environment_locale      select  en_US.UTF-8
' | debconf-set-selections 
apt install --yes locales
### i figured out how to set the timezone, but singularity ignores it & uses the timezone of your host
### sigh -- but i guess that is usually what you want anyway, because the user could be far away.
### it is still useful to do all this even though it is ignored, otherwise R tries to install tzdata
### and that pops up an interactive thing in the middle of this script that you need to be noninteractive.
echo '
tzdata tzdata/Areas select Etc
tzdata tzdata/Zones/Etc select UTC
' | debconf-set-selections 
echo Etc/UTC > /etc/timezone
ln -fs /usr/share/zoneinfo/Etc/UTC /etc/localtime
apt install --yes tzdata
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu bionic-cran40/'
apt update
# these are ubuntu libraries that the foieGras R package needs to have pre-installed.
apt install --yes libproj-dev
apt install --yes libudunits2-dev
apt install --yes libgdal-dev
# install R
apt install --yes r-base
# finally, install the R package foieGras
echo "install.packages('foieGras',repos='https://cloud.r-project.org')" | R --vanilla
# also install ncdf4 because we will need it for the WC grid files
echo "install.packages('ncdf4',repos='https://cloud.r-project.org')" | R --vanilla
echo "install.packages('rgeos',repos='https://cloud.r-project.org')" | R --vanilla
```

## Collection

 - Name: [jganong/ubuntu-bionic-R-4.0.3-foieGras](https://github.com/jganong/ubuntu-bionic-R-4.0.3-foieGras)
 - License: None

