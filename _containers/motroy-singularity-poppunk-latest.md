---
id: 7393
name: "motroy/singularity-poppunk"
branch: "master"
tag: "latest"
commit: "f1c535b821fd3119ffaed4dcea63267edf96722c"
version: "5008453c36d2930448006acf4cc6bbdd"
build_date: "2020-08-06T15:21:37.965Z"
size_mb: 3087.0
size: 1447620639
sif: "https://datasets.datalad.org/shub/motroy/singularity-poppunk/latest/2020-08-06-f1c535b8-5008453c/5008453c36d2930448006acf4cc6bbdd.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/motroy/singularity-poppunk/latest/2020-08-06-f1c535b8-5008453c/
recipe: https://datasets.datalad.org/shub/motroy/singularity-poppunk/latest/2020-08-06-f1c535b8-5008453c/Singularity
collection: motroy/singularity-poppunk
---

# motroy/singularity-poppunk:latest

```bash
$ singularity pull shub://motroy/singularity-poppunk:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:latest

%environment
export PATH="/miniconda/miniconda3/bin:/Software/PopPUNK/:/Software/PopPUNK/scripts:/Software/PopPUNK/PopPUNK/:$PATH"
export CONDARC="/.condarc"



%post
mkdir /miniconda && cd /miniconda
apt update && apt install -y git curl wget less locate build-essential openssh-server
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod +x Miniconda3-latest-Linux-x86_64.sh 
./Miniconda3-latest-Linux-x86_64.sh -b -p /miniconda/miniconda3
/miniconda/miniconda3/bin/conda config --file /.condarc --add channels defaults
/miniconda/miniconda3/bin/conda config --file /.condarc --add channels bioconda
/miniconda/miniconda3/bin/conda config --file /.condarc --add channels conda-forge
export PATH="/miniconda/miniconda3/bin:$PATH"
export CONDARC="/.condarc"
/miniconda/miniconda3/bin/conda install -y poppunk

mkdir /Software && cd /Software
git clone https://github.com/johnlees/PopPUNK.git && cd PopPUNK
#/miniconda/miniconda3/bin/python3 poppunk-runner.py
cd test && /miniconda/miniconda3/bin/python3 run_test.py
/miniconda/miniconda3/bin/python3 clean_test.py
```

## Collection

 - Name: [motroy/singularity-poppunk](https://github.com/motroy/singularity-poppunk)
 - License: [MIT License](https://api.github.com/licenses/mit)

