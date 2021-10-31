---
id: 5664
name: "romxero/nco_singularity"
branch: "master"
tag: "latest"
commit: "09778dd3e26e5a3d777ec00bf2e732022202562a"
version: "eefb6e14d3958de5fb538c6522e881a2"
build_date: "2020-02-11T00:00:02.273Z"
size_mb: 1278
size: 426467359
sif: "https://datasets.datalad.org/shub/romxero/nco_singularity/latest/2020-02-11-09778dd3-eefb6e14/eefb6e14d3958de5fb538c6522e881a2.simg"
url: https://datasets.datalad.org/shub/romxero/nco_singularity/latest/2020-02-11-09778dd3-eefb6e14/
recipe: https://datasets.datalad.org/shub/romxero/nco_singularity/latest/2020-02-11-09778dd3-eefb6e14/Singularity
collection: romxero/nco_singularity
---

# romxero/nco_singularity:latest

```bash
$ singularity pull shub://romxero/nco_singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%labels
Author "Randall Cab White - rcwhite@stanford.edu"

#########
#%setup
#########

##Just grabbing default packages from ubuntu repository
%post
	apt-get -ym update
	apt-get -ym install git libcgal-dev
    apt-get -ym install antlr libantlr-dev # ANTLR
    apt-get -ym install libcurl4-gnutls-dev libexpat1-dev libxml2-dev # DAP-prereqs (curl, expat XML parser)
    apt-get -ym install bison cmake flex gcc g++ # GNU toolchain
    apt-get -ym install gsl-bin libgsl-dev # GSL
    apt-get -ym install libnetcdf11 libnetcdf-dev netcdf-bin # netCDF and DAP
    apt-get -ym install libhdf5-serial-dev # HDF5
    apt-get -ym install ncl-ncarg # ESMF_RegridWeightGen (for ncremap)
    apt-get -ym install udunits-bin libudunits2-0 libudunits2-dev # UDUnits
    apt-get -ym install libcgal-qt5-dev
    apt-get -ym install libatlas-base-dev libsuitesparse-dev
    apt-get -ym install nco

%environment
	export IMAGE_NAME="NCO"
```

## Collection

 - Name: [romxero/nco_singularity](https://github.com/romxero/nco_singularity)
 - License: None

