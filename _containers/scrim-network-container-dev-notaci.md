---
id: 7725
name: "scrim-network/container-dev"
branch: "master"
tag: "notaci"
commit: "66ae533fb27b98838db5954f9346bca1f3b0bdc0"
version: "7ea08c654b4582f87aeaae3343c1ba82"
build_date: "2019-03-13T03:34:53.274Z"
size_mb: 1990
size: 581824543
sif: "https://datasets.datalad.org/shub/scrim-network/container-dev/notaci/2019-03-13-66ae533f-7ea08c65/7ea08c654b4582f87aeaae3343c1ba82.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/scrim-network/container-dev/notaci/2019-03-13-66ae533f-7ea08c65/
recipe: https://datasets.datalad.org/shub/scrim-network/container-dev/notaci/2019-03-13-66ae533f-7ea08c65/Singularity
collection: scrim-network/container-dev
---

# scrim-network/container-dev:notaci

```bash
$ singularity pull shub://scrim-network/container-dev:notaci
```

## Singularity Recipe

```singularity
# Last modified 9 January 2019 by Kelsey Ruckert <klr324@psu.edu>.

Bootstrap: debootstrap
OSVersion: xenial
MirrorURL: http://us.archive.ubuntu.com/ubuntu/
From: ubuntu:16.04

%post

# Upgrade packages in base image and install additional packages
apt-get -y update
DEBIAN_FRONTEND=noninteractive apt-get install -y git wget software-properties-common

# Install .NET
wget -q https://packages.microsoft.com/config/ubuntu/16.04/packages-microsoft-prod.deb
dpkg -i packages-microsoft-prod.deb
add-apt-repository universe
apt-get install -y apt-transport-https
apt-get update
apt-get install -y dotnet-sdk-2.0.0
apt-get clean
rm packages-microsoft-prod.deb

# Install LANDIS
git clone https://github.com/viff-cnh/Tool-Console.git
cd Tool-Console/src; dotnet build -c Release
apt-get install -y libjpeg62
apt-get install -y libpng16-16
mkdir /landis

%runscript
cd /landis
dotnet /Tool-Console/src/bin/Release/netcoreapp2.0/Landis.Console.dll "$@"
```

## Collection

 - Name: [scrim-network/container-dev](https://github.com/scrim-network/container-dev)
 - License: None

