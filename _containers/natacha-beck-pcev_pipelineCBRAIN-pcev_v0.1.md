---
id: 3471
name: "natacha-beck/pcev_pipelineCBRAIN"
branch: "singularity"
tag: "pcev_v0.1"
commit: "fb3310792861a2e3d96511e8868a3bd4d95f7d96"
version: "8ab36308ddb06f5697d92374f693d076"
build_date: "2018-07-11T01:44:04.439Z"
size_mb: 1272
size: 454942751
sif: "https://datasets.datalad.org/shub/natacha-beck/pcev_pipelineCBRAIN/pcev_v0.1/2018-07-11-fb331079-8ab36308/8ab36308ddb06f5697d92374f693d076.simg"
url: https://datasets.datalad.org/shub/natacha-beck/pcev_pipelineCBRAIN/pcev_v0.1/2018-07-11-fb331079-8ab36308/
recipe: https://datasets.datalad.org/shub/natacha-beck/pcev_pipelineCBRAIN/pcev_v0.1/2018-07-11-fb331079-8ab36308/Singularity
collection: natacha-beck/pcev_pipelineCBRAIN
---

# natacha-beck/pcev_pipelineCBRAIN:pcev_v0.1

```bash
$ singularity pull shub://natacha-beck/pcev_pipelineCBRAIN:pcev_v0.1
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

 - Name: [natacha-beck/pcev_pipelineCBRAIN](https://github.com/natacha-beck/pcev_pipelineCBRAIN)
 - License: None

