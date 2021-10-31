---
id: 14285
name: "willgpaik/visit_aci"
branch: "master"
tag: "latest"
commit: "e44d54725000b4845920ee214e65ba09f31f40fa"
version: "805c9bfe79b70e7d70c5c18f3f6a9736"
build_date: "2021-01-14T11:54:06.049Z"
size_mb: 4096.0
size: 1362845727
sif: "https://datasets.datalad.org/shub/willgpaik/visit_aci/latest/2021-01-14-e44d5472-805c9bfe/805c9bfe79b70e7d70c5c18f3f6a9736.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/willgpaik/visit_aci/latest/2021-01-14-e44d5472-805c9bfe/
recipe: https://datasets.datalad.org/shub/willgpaik/visit_aci/latest/2021-01-14-e44d5472-805c9bfe/Singularity
collection: willgpaik/visit_aci
---

# willgpaik/visit_aci:latest

```bash
$ singularity pull shub://willgpaik/visit_aci:latest
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: willgpaik/centos7_aci

%environment
        export PATH=$PATH:/opt/sw/visit/bin/

%post
        yum update -y
        yum -y install libfabric-devel

        mkdir -p /opt/sw/
        cd /opt/sw
        wget https://github.com/visit-dav/visit/releases/download/v3.1.2/visit3_1_2.linux-x86_64-rhel7-wmesa.tar.gz
        tar -xf visit3_1_2.linux-x86_64-rhel7-wmesa.tar.gz
        mv visit3_1_2.linux-x86_64 visit
        rm visit3_1_2.linux-x86_64-rhel7-wmesa.tar.gz
```

## Collection

 - Name: [willgpaik/visit_aci](https://github.com/willgpaik/visit_aci)
 - License: None

