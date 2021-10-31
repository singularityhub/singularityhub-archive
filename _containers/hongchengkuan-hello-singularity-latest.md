---
id: 3947
name: "hongchengkuan/hello-singularity"
branch: "master"
tag: "latest"
commit: "fb117540601fc2c025ae0bf899b13ba0184d93c7"
version: "642338d191174dd6086c30d3570bf7cb"
build_date: "2020-11-08T20:09:07.310Z"
size_mb: 280
size: 83046431
sif: "https://datasets.datalad.org/shub/hongchengkuan/hello-singularity/latest/2020-11-08-fb117540-642338d1/642338d191174dd6086c30d3570bf7cb.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/hongchengkuan/hello-singularity/latest/2020-11-08-fb117540-642338d1/
recipe: https://datasets.datalad.org/shub/hongchengkuan/hello-singularity/latest/2020-11-08-fb117540-642338d1/Singularity
collection: hongchengkuan/hello-singularity
---

# hongchengkuan/hello-singularity:latest

```bash
$ singularity pull shub://hongchengkuan/hello-singularity:latest
```

## Singularity Recipe

```singularity
BootStrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum

# If you want the updates (available at the bootstrap date) to be installed
# inside the container during the bootstrap instead of the General Availability
# point release (7.x) then uncomment the following line
#UpdateURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/updates/$basearch/


%runscript
    echo "This is what happens when you run the container..."


    %post
        echo "Hello from inside the container"
            yum -y install vim-minimal
```

## Collection

 - Name: [hongchengkuan/hello-singularity](https://github.com/hongchengkuan/hello-singularity)
 - License: None

