---
id: 4662
name: "GreenwoodLab/pcev_pipelineCBRAIN"
branch: "master"
tag: "pcev_v1.0"
commit: "df740bbe6a102e1bf83f5c45658367a4751f2a52"
version: "f541c966553b13a5ce4d95cc096422ba"
build_date: "2021-03-12T01:20:39.715Z"
size_mb: 1278
size: 456691743
sif: "https://datasets.datalad.org/shub/GreenwoodLab/pcev_pipelineCBRAIN/pcev_v1.0/2021-03-12-df740bbe-f541c966/f541c966553b13a5ce4d95cc096422ba.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/GreenwoodLab/pcev_pipelineCBRAIN/pcev_v1.0/2021-03-12-df740bbe-f541c966/
recipe: https://datasets.datalad.org/shub/GreenwoodLab/pcev_pipelineCBRAIN/pcev_v1.0/2021-03-12-df740bbe-f541c966/Singularity
collection: GreenwoodLab/pcev_pipelineCBRAIN
---

# GreenwoodLab/pcev_pipelineCBRAIN:pcev_v1.0

```bash
$ singularity pull shub://GreenwoodLab/pcev_pipelineCBRAIN:pcev_v1.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:6.9

%labels
  Maintainer Natacha Beck && Marie Forest

%files
  . pcev_CBRAIN

%post
  yum update -y
  yum install -y unzip \
                 wget  \
                 epel-release \
                 java-1.8.0-openjdk-headless

  yum install -y  R 
  
  echo 'install.packages(c("pcev"), repos= "http://cran.us.r-project.org")' > /tmp/packages.R
  Rscript /tmp/packages.R 

  chmod 755 pcev_CBRAIN/run_pcevCBRAIN.sh \
                   && cp pcev_CBRAIN/run_pcevCBRAIN.sh /bin/

  chmod 755 pcev_CBRAIN/reportRedaction.sh \
                   && cp pcev_CBRAIN/reportRedaction.sh /bin/

  chmod 755 pcev_CBRAIN/pcev_for_cbrain.R \
                   && cp pcev_CBRAIN/pcev_for_cbrain.R /bin/
```

## Collection

 - Name: [GreenwoodLab/pcev_pipelineCBRAIN](https://github.com/GreenwoodLab/pcev_pipelineCBRAIN)
 - License: None

