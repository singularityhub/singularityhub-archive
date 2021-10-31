---
id: 11434
name: "powerPlant/plink2-srf"
branch: "master"
tag: "v2.00a2lm"
commit: "537bdf39b884c4a646fe1cb6015ac45fb8282c34"
version: "b45ca4ad7b8d50cbba761ab58a42a77dc21097e2e613f8f2e76db0f389a21b75"
build_date: "2019-10-30T02:14:53.878Z"
size_mb: 78.203125
size: 82001920
sif: "https://datasets.datalad.org/shub/powerPlant/plink2-srf/v2.00a2lm/2019-10-30-537bdf39-b45ca4ad/b45ca4ad7b8d50cbba761ab58a42a77dc21097e2e613f8f2e76db0f389a21b75.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/plink2-srf/v2.00a2lm/2019-10-30-537bdf39-b45ca4ad/
recipe: https://datasets.datalad.org/shub/powerPlant/plink2-srf/v2.00a2lm/2019-10-30-537bdf39-b45ca4ad/Singularity
collection: powerPlant/plink2-srf
---

# powerPlant/plink2-srf:v2.00a2lm

```bash
$ singularity pull shub://powerPlant/plink2-srf:v2.00a2lm
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

