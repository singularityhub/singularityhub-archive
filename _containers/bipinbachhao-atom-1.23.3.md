---
id: 1855
name: "bipinbachhao/atom"
branch: "master"
tag: "1.23.3"
commit: "f90805675c2f18b17b12fd7721b1e01dd5cc215d"
version: "685fb1be3b839ceda7f6e3c72e7dcd55"
build_date: "2018-10-19T01:59:45.277Z"
size_mb: 1151
size: 377483295
sif: "https://datasets.datalad.org/shub/bipinbachhao/atom/1.23.3/2018-10-19-f9080567-685fb1be/685fb1be3b839ceda7f6e3c72e7dcd55.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bipinbachhao/atom/1.23.3/2018-10-19-f9080567-685fb1be/
recipe: https://datasets.datalad.org/shub/bipinbachhao/atom/1.23.3/2018-10-19-f9080567-685fb1be/Singularity
collection: bipinbachhao/atom
---

# bipinbachhao/atom:1.23.3

```bash
$ singularity pull shub://bipinbachhao/atom:1.23.3
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: artful
MirrorURL: http://us.archive.ubuntu.com/ubuntu/


%post
    echo "Hello from inside the container"
    sed -i 's/$/ universe/' /etc/apt/sources.list
    apt -y --force-yes install software-properties-common
    add-apt-repository -y ppa:webupd8team/atom
    apt update
    apt -y --force-yes install wget libxss1
    apt -y --force-yes install python git libgtk2.0-0
    apt -y --force-yes install libnotify4 libxtst6 libnss3 gvfs-bin xdg-utils
    apt -y --force-yes install atom

%apprun git
  exec atom "$@"

%runscript
  exec atom "$@"

%help
  For help use --help
```

## Collection

 - Name: [bipinbachhao/atom](https://github.com/bipinbachhao/atom)
 - License: None

