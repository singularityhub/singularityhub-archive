---
id: 5274
name: "bipinbachhao/atom"
branch: "master"
tag: "1.31.2"
commit: "ab0eac1abe5bfab3c021b9ed6f43a823e1e7c69c"
version: "38ebcf21ad2918763d22c342c1d7dad6"
build_date: "2018-10-19T18:21:05.360Z"
size_mb: 1238
size: 389300255
sif: "https://datasets.datalad.org/shub/bipinbachhao/atom/1.31.2/2018-10-19-ab0eac1a-38ebcf21/38ebcf21ad2918763d22c342c1d7dad6.simg"
url: https://datasets.datalad.org/shub/bipinbachhao/atom/1.31.2/2018-10-19-ab0eac1a-38ebcf21/
recipe: https://datasets.datalad.org/shub/bipinbachhao/atom/1.31.2/2018-10-19-ab0eac1a-38ebcf21/Singularity
collection: bipinbachhao/atom
---

# bipinbachhao/atom:1.31.2

```bash
$ singularity pull shub://bipinbachhao/atom:1.31.2
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

