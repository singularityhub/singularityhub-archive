---
id: 4661
name: "GreenwoodLab/pcev_pipelineCBRAIN"
branch: "master"
tag: "pcev_v0.1"
commit: "fb3310792861a2e3d96511e8868a3bd4d95f7d96"
version: "596462e07d795f15851d2e86fbe0044b"
build_date: "2018-09-04T20:03:30.006Z"
size_mb: 1278
size: 456687647
sif: "https://datasets.datalad.org/shub/GreenwoodLab/pcev_pipelineCBRAIN/pcev_v0.1/2018-09-04-fb331079-596462e0/596462e07d795f15851d2e86fbe0044b.simg"
url: https://datasets.datalad.org/shub/GreenwoodLab/pcev_pipelineCBRAIN/pcev_v0.1/2018-09-04-fb331079-596462e0/
recipe: https://datasets.datalad.org/shub/GreenwoodLab/pcev_pipelineCBRAIN/pcev_v0.1/2018-09-04-fb331079-596462e0/Singularity
collection: GreenwoodLab/pcev_pipelineCBRAIN
---

# GreenwoodLab/pcev_pipelineCBRAIN:pcev_v0.1

```bash
$ singularity pull shub://GreenwoodLab/pcev_pipelineCBRAIN:pcev_v0.1
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

