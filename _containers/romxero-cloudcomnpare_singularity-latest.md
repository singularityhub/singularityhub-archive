---
id: 13939
name: "romxero/cloudcomnpare_singularity"
branch: "master"
tag: "latest"
commit: "a2e5cf31de8386f03efe8320df38193138ad2a3c"
version: "8e074f4633f83d46dcc58519ed5d2fed"
build_date: "2020-09-22T22:24:43.639Z"
size_mb: 2257.0
size: 736776223
sif: "https://datasets.datalad.org/shub/romxero/cloudcomnpare_singularity/latest/2020-09-22-a2e5cf31-8e074f46/8e074f4633f83d46dcc58519ed5d2fed.sif"
url: https://datasets.datalad.org/shub/romxero/cloudcomnpare_singularity/latest/2020-09-22-a2e5cf31-8e074f46/
recipe: https://datasets.datalad.org/shub/romxero/cloudcomnpare_singularity/latest/2020-09-22-a2e5cf31-8e074f46/Singularity
collection: romxero/cloudcomnpare_singularity
---

# romxero/cloudcomnpare_singularity:latest

```bash
$ singularity pull shub://romxero/cloudcomnpare_singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%labels
Author "Randall Cab White - rcwhite@stanford.edu"

#########
#%setup
#########
#########
export DEBIAN_FRONTEND=noninteractive

##Just grabbing default packages from ubuntu repository
%post

	apt-get -ym update
    ln -fs /usr/share/zoneinfo/America/Los_Angeles /etc/localtime
    apt-get install -y tzdata
    dpkg-reconfigure --frontend noninteractive tzdata


	  apt-get -ymq install wget libatlas3-base curl make tar gzip gfortran gcc g++ git cmake build-essential libreadline-dev libx11-dev libxt-dev libbz2-dev liblzma-dev \
	  ca-certificates libcairo2 unzip zip libtcl8.6 ucf libtk8.6 libpcre3-dev libpcre++-dev libcurl4-openssl-dev  autotools-dev  automake autoconf autogen pkg-config libgtk-3-dev sqlite3 libsqlite3-dev libudunits2-dev \
	   software-properties-common build-essential ca-certificates \
            git make cmake wget unzip libtool automake \
            zlib1g-dev libsqlite3-dev pkg-config sqlite3 \
            libcharls-dev libopenjp2-7-dev libcairo2-dev \
       python-dev python-numpy \
       libpng-dev libjpeg-dev libgif-dev liblzma-dev libgeos-dev \
       libxml2-dev libexpat-dev libxerces-c-dev \
       libnetcdf-dev libpoppler-dev libpoppler-private-dev \
       libspatialite-dev swig libhdf4-alt-dev libhdf5-serial-dev \
       libfreexl-dev unixodbc-dev libwebp-dev libepsilon-dev \
       liblcms2-2 libpcre3-dev libcrypto++-dev libdap-dev libfyba-dev \
       libkml-dev libmysqlclient-dev libogdi3.2-dev \
       libcfitsio-dev openjdk-8-jdk libzstd1-dev \
       libpq-dev libssl-dev libboost-dev \
       autoconf automake bash-completion libarmadillo-dev \
       libcharls1 libopenjp2-7 libcairo2 python-numpy \
        libpng16-16 libjpeg-turbo8 libgif7 liblzma5 libgeos-3.6.2 libgeos-c1v5 \
        libcurl4 libxml2 libexpat1 \
        libxerces-c3.2 libnetcdf-c++4 netcdf-bin libpoppler73 libspatialite7 gpsbabel \
        libhdf4-0-alt libhdf5-100 libhdf5-cpp-100 poppler-utils libfreexl1 unixodbc libwebp6 \
        libepsilon1 liblcms2-2 libpcre3 libcrypto++ libdap25 libdapclient6v5 libfyba0 \
        libkmlbase1 libkmlconvenience1 libkmldom1 libkmlengine1 libkmlregionator1 libkmlxsd1 \
        libmysqlclient20 libogdi3.2 libcfitsio5 openjdk-8-jre \
        libzstd1 bash bash-completion libpq5 libssl1.1 \
        libarmadillo8

#grabing the pdal stuff now:

apt-get -ymq install libpdal-* qtbase5-dev qttools5-dev  libqt5svg5-dev libjson-c-dev libjsoncpp-dev

#stupid quick fix 
ln -s /usr/include/jsoncpp/json/ /usr/include/json
######
#
# Now building the other stuff here => 

mkdir /cloudCompareBuild
cd /cloudCompareBuild

wget https://github.com/CloudCompare/CloudCompare/archive/v2.11.1.tar.gz
tar zxvf v2.11.1.tar.gz 
cd CloudCompare-2.11.1/

mkdir build
cd build

cmake -DPLUGIN_IO_QPDAL=TRUE -DJSON_ROOT_DIR="/usr/include/jsoncpp" ../

make -j4 && make install

cd /
rm -rf /cloudCompareBuild


###########
#######
#######


#%runscript
#	exec /usr/local/bin/ruby "$@"

%environment
	export IMAGE_NAME="gdal"
```

## Collection

 - Name: [romxero/cloudcomnpare_singularity](https://github.com/romxero/cloudcomnpare_singularity)
 - License: None

