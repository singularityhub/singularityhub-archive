---
id: 8290
name: "motroy/singularity-c-SSTAR"
branch: "master"
tag: "latest"
commit: "8d5451173b2bd17b5fa86dfa2a07518c6d428278"
version: "d2893590de7320acd7bfd58b32cf808a"
build_date: "2019-04-10T11:51:51.260Z"
size_mb: 709
size: 266244127
sif: "https://datasets.datalad.org/shub/motroy/singularity-c-SSTAR/latest/2019-04-10-8d545117-d2893590/d2893590de7320acd7bfd58b32cf808a.simg"
url: https://datasets.datalad.org/shub/motroy/singularity-c-SSTAR/latest/2019-04-10-8d545117-d2893590/
recipe: https://datasets.datalad.org/shub/motroy/singularity-c-SSTAR/latest/2019-04-10-8d545117-d2893590/Singularity
collection: motroy/singularity-c-SSTAR
---

# motroy/singularity-c-SSTAR:latest

```bash
$ singularity pull shub://motroy/singularity-c-SSTAR:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:latest

%environment
export PATH="/c-SSTAR/c-SSTAR/:/usr/bin:$PATH"

%post
apt update && apt install -y git curl wget less locate build-essential openssh-server python python-pip ncbi-blast+
mkdir /c-SSTAR && cd /c-SSTAR
pip install biopython
git clone https://github.com/chrisgulvik/c-SSTAR.git
cd /c-SSTAR/c-SSTAR/
sed -i -e 's#/usr/bin/env python#/usr/bin/env python2.7#g' c-SSTAR
wget https://github.com/tomdeman-bio/Sequence-Search-Tool-for-Antimicrobial-Resistance-SSTAR-/blob/master/Latest_AR_database/ResGANNOT_srst2.fasta
export PATH="/c-SSTAR/c-SSTAR/:/usr/bin:$PATH"
```

## Collection

 - Name: [motroy/singularity-c-SSTAR](https://github.com/motroy/singularity-c-SSTAR)
 - License: [MIT License](https://api.github.com/licenses/mit)

