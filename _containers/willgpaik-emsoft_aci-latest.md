---
id: 11648
name: "willgpaik/emsoft_aci"
branch: "master"
tag: "latest"
commit: "360bb29b2cdc245f61b195766fa531394cafeab2"
version: "fee09fb486147eae141a196c7d60da779d743c7be720846cca8c68fec5a27adb"
build_date: "2019-11-19T22:33:49.105Z"
size_mb: 3032.0
size: 1197256704
sif: "https://datasets.datalad.org/shub/willgpaik/emsoft_aci/latest/2019-11-19-360bb29b-fee09fb4/fee09fb486147eae141a196c7d60da779d743c7be720846cca8c68fec5a27adb.sif"
url: https://datasets.datalad.org/shub/willgpaik/emsoft_aci/latest/2019-11-19-360bb29b-fee09fb4/
recipe: https://datasets.datalad.org/shub/willgpaik/emsoft_aci/latest/2019-11-19-360bb29b-fee09fb4/Singularity
collection: willgpaik/emsoft_aci
---

# willgpaik/emsoft_aci:latest

```bash
$ singularity pull shub://willgpaik/emsoft_aci:latest
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: willgpaik/centos7_aci

%setup

%files

%environment

%runscript

%post
    yum -y install lapack-devel blas-devel ocl-icd-devel
    
    set +e

    
    source /opt/rh/devtoolset-8/enable
    
    export PATH=/usr/local/bin:$PATH
        
    mkdir -p /opt/sw
    cd /opt/sw
    
    wget https://raw.githubusercontent.com/willgpaik/emsoft_aci/master/emsoft_install.sh
    chmod +x emsoft_install.sh
    ./emsoft_install.sh
    rm emsoft_install.sh
```

## Collection

 - Name: [willgpaik/emsoft_aci](https://github.com/willgpaik/emsoft_aci)
 - License: None

