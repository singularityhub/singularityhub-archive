---
id: 10601
name: "stephansmit/license_containers"
branch: "master"
tag: "latest"
commit: "b2c2fd794502a864d0934ab0a2b1a7e9576d919f"
version: "f965d9e618527e45ad0501e86cecfbd0"
build_date: "2020-08-07T09:32:17.539Z"
size_mb: 154.0
size: 76697631
sif: "https://datasets.datalad.org/shub/stephansmit/license_containers/latest/2020-08-07-b2c2fd79-f965d9e6/f965d9e618527e45ad0501e86cecfbd0.sif"
url: https://datasets.datalad.org/shub/stephansmit/license_containers/latest/2020-08-07-b2c2fd79-f965d9e6/
recipe: https://datasets.datalad.org/shub/stephansmit/license_containers/latest/2020-08-07-b2c2fd79-f965d9e6/Singularity
collection: stephansmit/license_containers
---

# stephansmit/license_containers:latest

```bash
$ singularity pull shub://stephansmit/license_containers:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%environment
    pwid_LICENSE=26800@localhost
    export pwid_LICENSE

%post
    apt-get update &&     apt-get install -y dos2unix wget 
    echo 'Download the License files'
    wget -O /opt/LicenseServer.tar.gz https://file.io/WRpWGl
    wget -O /opt/Vendors.tar.gz https://file.io/4vvfKu
    echo 'Extract the files to the correct locations'
    tar -xzvf /opt/LicenseServer.tar.gz -C /opt/
    tar -xzvf /opt/Vendors.tar.gz -C /opt/SolidSQUAD_License_Servers/

    echo 'Setting the license'
    sh /opt/SolidSQUAD_License_Servers/install_or_update.sh
    chmod -R 777 /opt/SolidSQUAD_License_Servers/

%startscript
    /opt/SolidSQUAD_License_Servers/Bin/start_services.sh
   
%runscript
    exec '$@'
```

## Collection

 - Name: [stephansmit/license_containers](https://github.com/stephansmit/license_containers)
 - License: None

