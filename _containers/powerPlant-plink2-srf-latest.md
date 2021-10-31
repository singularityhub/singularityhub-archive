---
id: 11433
name: "powerPlant/plink2-srf"
branch: "master"
tag: "latest"
commit: "537bdf39b884c4a646fe1cb6015ac45fb8282c34"
version: "0088a8633e39b8fd9287fd016869766aefcb13b85ad5f8067a49d924a6f71d2b"
build_date: "2019-10-30T02:14:09.226Z"
size_mb: 78.203125
size: 82001920
sif: "https://datasets.datalad.org/shub/powerPlant/plink2-srf/latest/2019-10-30-537bdf39-0088a863/0088a8633e39b8fd9287fd016869766aefcb13b85ad5f8067a49d924a6f71d2b.sif"
url: https://datasets.datalad.org/shub/powerPlant/plink2-srf/latest/2019-10-30-537bdf39-0088a863/
recipe: https://datasets.datalad.org/shub/powerPlant/plink2-srf/latest/2019-10-30-537bdf39-0088a863/Singularity
collection: powerPlant/plink2-srf
---

# powerPlant/plink2-srf:latest

```bash
$ singularity pull shub://powerPlant/plink2-srf:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:7

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version v2.00a2LM

%post
  ## Install prerequisites
  yum -y install unzip wget
  
  ## Download and install
  wget http://s3.amazonaws.com/plink2-assets/plink2_linux_avx2_20191025.zip
  unzip plink2_linux_avx2_20191025.zip
  install -dm0755 /usr/local/bin
  install -Dm0755 plink2 /usr/local/bin

  ## Cleanup
  rm -f plink2*
  yum -y erase unzip wget
  yum -y autoremove
  yum clean all

%runscript
  exec plink2 "$@"
```

## Collection

 - Name: [powerPlant/plink2-srf](https://github.com/powerPlant/plink2-srf)
 - License: None

