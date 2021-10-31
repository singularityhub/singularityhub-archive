---
id: 4571
name: "josbake/GnuplotImage"
branch: "master"
tag: "latest"
commit: "6c18ea566c4042fb4d18f569128a3ad5d135708f"
version: "273888862b61bd6945bd0f164d328267"
build_date: "2018-08-31T03:21:36.678Z"
size_mb: 415
size: 179175455
sif: "https://datasets.datalad.org/shub/josbake/GnuplotImage/latest/2018-08-31-6c18ea56-27388886/273888862b61bd6945bd0f164d328267.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/josbake/GnuplotImage/latest/2018-08-31-6c18ea56-27388886/
recipe: https://datasets.datalad.org/shub/josbake/GnuplotImage/latest/2018-08-31-6c18ea56-27388886/Singularity
collection: josbake/GnuplotImage
---

# josbake/GnuplotImage:latest

```bash
$ singularity pull shub://josbake/GnuplotImage:latest
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: trusty
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%post
sed -i 's/$/ universe/' /etc/apt/sources.list
apt-get -y update
apt-get -y install gnuplot
```

## Collection

 - Name: [josbake/GnuplotImage](https://github.com/josbake/GnuplotImage)
 - License: None

