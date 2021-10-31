---
id: 7855
name: "achiam21/GridFTP"
branch: "master"
tag: "latest"
commit: "6cdd397871911767f49f58f7bf91b801a5b35f41"
version: "c3735f60777cf7436f9d2e5d65afd170"
build_date: "2019-03-20T08:24:17.337Z"
size_mb: 372
size: 131285023
sif: "https://datasets.datalad.org/shub/achiam21/GridFTP/latest/2019-03-20-6cdd3978-c3735f60/c3735f60777cf7436f9d2e5d65afd170.simg"
url: https://datasets.datalad.org/shub/achiam21/GridFTP/latest/2019-03-20-6cdd3978-c3735f60/
recipe: https://datasets.datalad.org/shub/achiam21/GridFTP/latest/2019-03-20-6cdd3978-c3735f60/Singularity
collection: achiam21/GridFTP
---

# achiam21/GridFTP:latest

```bash
$ singularity pull shub://achiam21/GridFTP:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos

%runscript
exec echo "Centos7 image for use with GridFTP"

%files
# src dest

%environment
# export XYZ=/blah/

%labels
AUTHOR alvin@nscc.sg

%post
#echo "The post section is where you can install, and configure your container."
#
rpm -hUv http://www.globus.org/ftppub/gt6/installers/repo/globus-toolkit-repo-latest.noarch.rpm
yum -y update && yum -y install epel-release
yum -y install yum-plugin-priorities # globus installer needs this
yum -y install globus-data-management-client globus-data-management-server
/etc/init.d/globus-gridftp-sshftp reconfigure
```

## Collection

 - Name: [achiam21/GridFTP](https://github.com/achiam21/GridFTP)
 - License: None

