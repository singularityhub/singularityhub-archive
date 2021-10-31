---
id: 6329
name: "ISU-HPC/big-scape"
branch: "master"
tag: "latest"
commit: "5cd09811ba3cabbe351341fe84c1a68301fd0237"
version: "863290126edd6304645168eedd1c91ba"
build_date: "2021-04-06T19:21:43.941Z"
size_mb: 6918
size: 3029467167
sif: "https://datasets.datalad.org/shub/ISU-HPC/big-scape/latest/2021-04-06-5cd09811-86329012/863290126edd6304645168eedd1c91ba.simg"
url: https://datasets.datalad.org/shub/ISU-HPC/big-scape/latest/2021-04-06-5cd09811-86329012/
recipe: https://datasets.datalad.org/shub/ISU-HPC/big-scape/latest/2021-04-06-5cd09811-86329012/Singularity
collection: ISU-HPC/big-scape
---

# ISU-HPC/big-scape:latest

```bash
$ singularity pull shub://ISU-HPC/big-scape:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
from: continuumio/miniconda3

%labels

MAINTAINER ynanyam@iastate.edu

%post

apt-get update -y

apt install -y wget git

export PATH=/opt/conda/bin:$PATH

echo 'export PATH=/usr/local/bin:/opt/conda/bin:$PATH' >>$SINGULARITY_ENVIRONMENT

#conda create --name bigscape

#source activate bigscape 

conda install -y numpy scipy scikit-learn

conda install -c bioconda hmmer biopython fasttree anaconda networkx

cd /usr/src

git clone https://git.wur.nl/medema-group/BiG-SCAPE.git

wget ftp://ftp.ebi.ac.uk/pub/databases/Pfam/releases/Pfam31.0/Pfam-A.hmm.gz

gunzip Pfam-A.hmm.gz && hmmpress Pfam-A.hmm && mv Pfam-A.* /usr/src/BiG-SCAPE/.

chmod +x /usr/src/BiG-SCAPE/*.py

echo 'export PATH=/usr/src/BiG-SCAPE:$PATH' >>$SINGULARITY_ENVIRONMENT

mkdir -p /local/scratch

chmod 777 /local/scratch

mkdir -p /local/scratch/input /local/scratch/output
```

## Collection

 - Name: [ISU-HPC/big-scape](https://github.com/ISU-HPC/big-scape)
 - License: None

