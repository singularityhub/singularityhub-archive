---
id: 3913
name: "TMCantwell/pulsar_timing_containers"
branch: "master"
tag: "pulsar.v1.2"
commit: "6cbe6f3559ae24f8fc021622a3e087cbfc677b1e"
version: "b52264409282ea75b8cc6efff87b76f1"
build_date: "2018-08-10T20:17:50.110Z"
size_mb: 2115
size: 678621215
sif: "https://datasets.datalad.org/shub/TMCantwell/pulsar_timing_containers/pulsar.v1.2/2018-08-10-6cbe6f35-b5226440/b52264409282ea75b8cc6efff87b76f1.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TMCantwell/pulsar_timing_containers/pulsar.v1.2/2018-08-10-6cbe6f35-b5226440/
recipe: https://datasets.datalad.org/shub/TMCantwell/pulsar_timing_containers/pulsar.v1.2/2018-08-10-6cbe6f35-b5226440/Singularity
collection: TMCantwell/pulsar_timing_containers
---

# TMCantwell/pulsar_timing_containers:pulsar.v1.2

```bash
$ singularity pull shub://TMCantwell/pulsar_timing_containers:pulsar.v1.2
```

## Singularity Recipe

```singularity
BootStrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum wget


%files

GBNCC_J1911+37_period.fits /scratch
J1911+37_t2.par /scratch
1911+37_820MHz.std /scratch

%post
yum -y update
yum -y install yum-utils
yum -y groupinstall development
yum -y install https://centos7.iuscommunity.org/ius-release.rpm
yum -y localinstall --nogpgcheck https://download1.rpmfusion.org/free/el/rpmfusion-free-release-7.noarch.rpm https://download1.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-7.noarch.rpm
yum -y install build-essential curl git man vim autoconf libtool debootstrap squashfs-tools
yum -y install python2-pip
yum -y install python-devel
yum -y install fftw fftw-devel
yum -y install libpng libpng-devel
yum -y install cfitsio cfitsio-devel
yum -y install pgplot pgplot-devel
yum -y install qt qt-devel
yum -y install java java-devel
yum -y install libxml2 libxml2-devel
wget http://www.pulsarastronomy.net/psrsoft/psrsoft.tar.gz
tar -xzf psrsoft.tar.gz
cd psrsoft/config
cp profile.example profile
cd ..
cd ..
export PATH=/psrsoft/bin:$PATH
echo 'y' | psrsoft psrchive

%environment
export PATH=/psrsoft/bin:$PATH
export PSRSOFT_USR=/psrsoft/usr
for env in $PSRSOFT_USR/var/psrsoft/env/bash/* ; do . $env ; done
export PATH=$PSRSOFT_USR/bin:$PATH

%runscript
pam -FT -e FT -E /scratch/J1911+37_t2.par /scratch/GBNCC_J1911+37_period.fits
pat -s /scratch/1911+37_820MHz.std -f tempo2 /scratch/GBNCC_J1911+37_period.FT > toa.txt
```

## Collection

 - Name: [TMCantwell/pulsar_timing_containers](https://github.com/TMCantwell/pulsar_timing_containers)
 - License: None

