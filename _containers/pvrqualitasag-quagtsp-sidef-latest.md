---
id: 11833
name: "pvrqualitasag/quagtsp-sidef"
branch: "tsp-sa"
tag: "latest"
commit: "8ec9616e1cf4192bd2bee4eae01d5a9b80935daf"
version: "256812578c2b702720f3fcc23eafad5a"
build_date: "2020-06-16T09:45:50.301Z"
size_mb: 954.0
size: 336109599
sif: "https://datasets.datalad.org/shub/pvrqualitasag/quagtsp-sidef/latest/2020-06-16-8ec9616e-25681257/256812578c2b702720f3fcc23eafad5a.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/pvrqualitasag/quagtsp-sidef/latest/2020-06-16-8ec9616e-25681257/
recipe: https://datasets.datalad.org/shub/pvrqualitasag/quagtsp-sidef/latest/2020-06-16-8ec9616e-25681257/Singularity
collection: pvrqualitasag/quagtsp-sidef
---

# pvrqualitasag/quagtsp-sidef:latest

```bash
$ singularity pull shub://pvrqualitasag/quagtsp-sidef:latest
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: bionic
MirrorURL: http://archive.ubuntu.com/ubuntu/

%post
  sed -i 's/main/main restricted universe/g' /etc/apt/sources.list
  apt-get update

  # install software properties commons for add-apt-repository
  apt-get install -y software-properties-common apt-utils
  apt-get update

  # Install system software for TheSNPpit
  apt-get install -y gcc perl make wget vim less screen curl locales time rsync gawk tzdata git dos2unix sshpass htop
  apt-get install -y libdbd-pg-perl libecpg6 libecpg-dev libdbi-perl libinline-perl libmodern-perl-perl libcloog-ppl1 libcloog-ppl-dev libfile-slurp-perl libpq5 libjudy-dev
  apt-get update -y
  echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list
  wget -q https://www.postgresql.org/media/keys/ACCC4CF8.asc -O - | apt-key add -
  apt-get install -y postgresql postgresql-contrib
  apt-get update -y
  apt clean
  
  # Install additional perl-modules for TSP
  curl -sSL "https://raw.githubusercontent.com/pvrqualitasag/quagtsp-sidef/master/etc/needed_perl_modules_tsp" > needed_perl_modules_tsp
  curl -sSL "https://raw.githubusercontent.com/pvrqualitasag/quagtsp-sidef/master/bash/install_perlmd_tsp.pl" > install_perlmd_tsp.pl
  perl -w install_perlmd_tsp.pl --install
  rm -rf install_perlmd_tsp.pl needed_perl_modules_tsp
  
  # Install TSP software
  cd /usr/local
  wget --no-check-certificate https://tsp-repo.thesnppit.net/download/TheSNPpit-latest.tar.gz
  tar xzvf TheSNPpit-latest.tar.gz
  cd TheSNPpit-1.1.4
  curl -sSL "https://raw.githubusercontent.com/pvrqualitasag/quagtsp-sidef/tsp-sa/bash/install_tsp_sa.sh" > bin/install_tsp_sa.sh
  chmod 755 bin/install_tsp_sa.sh
  ./bin/install_tsp_sa.sh
  

  # install OpenJDK 8 (LTS) from https://adoptopenjdk.net
  curl -sSL "https://github.com/AdoptOpenJDK/openjdk8-binaries/releases/download/jdk8u222-b10/OpenJDK8U-jdk_x64_linux_hotspot_8u222b10.tar.gz" > openjdk8.tar.gz
  mkdir -p /opt/openjdk
  tar -C /opt/openjdk -xf openjdk8.tar.gz
  rm -f openjdk8.tar.gz

  # permissions for postgres
  chmod -R 755 /var/lib/postgresql/10/main
  chmod -R 777 /var/run/postgresql

  # dconf problem
  mkdir -p /run/user/501
  chmod -R 777 /run/user
  
  # locales
  locale-gen en_US.UTF-8
  locale-gen de_CH.UTF-8

  # timezone
  echo 'Europe/Berlin' > /etc/timezone

  # hostname
  echo '1-htz.quagzws.com' > /etc/hostname

%environment
  export PATH=${PATH}:/opt/openjdk/jdk8u222-b10/bin:/qualstorzws01/data_projekte/linuxBin
  export TZ=$(cat /etc/timezone)
```

## Collection

 - Name: [pvrqualitasag/quagtsp-sidef](https://github.com/pvrqualitasag/quagtsp-sidef)
 - License: None

