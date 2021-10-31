---
id: 3019
name: "CNC-UMCG/cnc_fbirn"
branch: "master"
tag: "latest"
commit: "9eb2de4bb99ce4427ce58773c4f6bd5406f42381"
version: "65e69f751b3d74450c0fab057b2c1081"
build_date: "2018-06-05T00:16:52.216Z"
size_mb: 1827
size: 626303007
sif: "https://datasets.datalad.org/shub/CNC-UMCG/cnc_fbirn/latest/2018-06-05-9eb2de4b-65e69f75/65e69f751b3d74450c0fab057b2c1081.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/CNC-UMCG/cnc_fbirn/latest/2018-06-05-9eb2de4b-65e69f75/
recipe: https://datasets.datalad.org/shub/CNC-UMCG/cnc_fbirn/latest/2018-06-05-9eb2de4b-65e69f75/Singularity
collection: CNC-UMCG/cnc_fbirn
---

# CNC-UMCG/cnc_fbirn:latest

```bash
$ singularity pull shub://CNC-UMCG/cnc_fbirn:latest
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: CNC-UMCG/cnc_base


%environment

%files
    scripts/* /usr/bin/cnc

%post

    apt-get install -y lsb-core
    wget https://www.nitrc.org/frs/download.php/10144/bxh_xcede_tools-1.11.14-lsb30.x86_64.tgz
    tar xvzf bxh_xcede_tools-1.11.14-lsb30.x86_64.tgz -C /usr/share
    
    echo "PATH=$PATH:/usr/share/bxh_xcede_tools-1.11.14-lsb30.x86_64" >> /etc/profile
```

## Collection

 - Name: [CNC-UMCG/cnc_fbirn](https://github.com/CNC-UMCG/cnc_fbirn)
 - License: None

