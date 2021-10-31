---
id: 9052
name: "sonnhammergroup/Domainoid"
branch: "master"
tag: "def"
commit: "b3567341f5a553ec647df39614f363dc1b7dfcff"
version: "82f412030c3a2e1e7ade5b290d22867a"
build_date: "2021-02-05T15:08:52.597Z"
size_mb: 4646
size: 1612140575
sif: "https://datasets.datalad.org/shub/sonnhammergroup/Domainoid/def/2021-02-05-b3567341-82f41203/82f412030c3a2e1e7ade5b290d22867a.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/sonnhammergroup/Domainoid/def/2021-02-05-b3567341-82f41203/
recipe: https://datasets.datalad.org/shub/sonnhammergroup/Domainoid/def/2021-02-05-b3567341-82f41203/Singularity
collection: sonnhammergroup/Domainoid
---

# sonnhammergroup/Domainoid:def

```bash
$ singularity pull shub://sonnhammergroup/Domainoid:def
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:latest

%post
apt-get update && apt-get -y install wget build-essential
apt-get install python3 python3-pip bioperl hmmer libmoose-perl git -y
pip3 install biopython networkx sortedcontainers joblib

git clone https://bitbucket.org/sonnhammergroup/domainoid.git /home/domainoid

wget -P  /home/pfam/Pfam  ftp://ftp.ebi.ac.uk/pub/databases/Pfam/releases/Pfam32.0/Pfam-A.hmm.gz
wget -P  /home/pfam/Pfam ftp://ftp.ebi.ac.uk/pub/databases/Pfam/releases/Pfam32.0/Pfam-A.hmm.dat.gz
wget -P  /home/pfam/Pfam ftp://ftp.ebi.ac.uk/pub/databases/Pfam/releases/Pfam32.0/active_site.dat.gz
wget -P  /home/pfam ftp://ftp.ebi.ac.uk/pub/databases/Pfam/Tools/PfamScan.tar.gz

cd /home/pfam
tar xvfz PfamScan.tar.gz

cd /home/pfam/Pfam
gunzip -d Pfam-A.hmm.gz
gunzip -d Pfam-A.hmm.dat.gz
gunzip -d active_site.dat.gz
hmmpress Pfam-A.hmm

wget -P  /home/blast ftp://ftp.ncbi.nlm.nih.gov/blast/executables/legacy.NOTSUPPORTED/2.2.18/blast-2.2.18-x64-linux.tar.gz
cd /home/blast
tar xvfz blast-2.2.18-x64-linux.tar.gz 

cp -a /home/blast/blast-2.2.18/bin/. /home/domainoid/inParanoid
cp /home/blast/blast-2.2.18/data/BLOSUM45 /home/domainoid/inParanoid
cp /home/blast/blast-2.2.18/data/BLOSUM62 /home/domainoid/inParanoid
cp /home/blast/blast-2.2.18/data/BLOSUM80 /home/domainoid/inParanoid
cp /home/blast/blast-2.2.18/data/PAM30 /home/domainoid/inParanoid
cp /home/blast/blast-2.2.18/data/PAM70 /home/domainoid/inParanoid

%environment
export PATH=.:$PATH
export LC_ALL=C
export LANGUAGE=C

%runscript
cd /home/domainoid/
echo "Running: $*"
python3 runDomainoid.py "$@"
```

## Collection

 - Name: [sonnhammergroup/Domainoid](https://github.com/sonnhammergroup/Domainoid)
 - License: None

