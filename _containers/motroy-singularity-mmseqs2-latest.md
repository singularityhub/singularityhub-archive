---
id: 9475
name: "motroy/singularity-mmseqs2"
branch: "master"
tag: "latest"
commit: "03ec628e765fb9f2abaa4605ee8fcbbb537097f5"
version: "34d7b251c886aefb9684375956888d48"
build_date: "2019-08-25T22:09:04.557Z"
size_mb: 2916.0
size: 1204375583
sif: "https://datasets.datalad.org/shub/motroy/singularity-mmseqs2/latest/2019-08-25-03ec628e-34d7b251/34d7b251c886aefb9684375956888d48.sif"
url: https://datasets.datalad.org/shub/motroy/singularity-mmseqs2/latest/2019-08-25-03ec628e-34d7b251/
recipe: https://datasets.datalad.org/shub/motroy/singularity-mmseqs2/latest/2019-08-25-03ec628e-34d7b251/Singularity
collection: motroy/singularity-mmseqs2
---

# motroy/singularity-mmseqs2:latest

```bash
$ singularity pull shub://motroy/singularity-mmseqs2:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%environment
export PATH="/Software/mmseqs2/bin:/Software/plass/bin:/Databases/:/Software/hmmer:$PATH"

%post
apt update && apt install -y git curl wget less locate unzip build-essential zlib1g-dev libbz2-dev
mkdir -p /Software/ && cd /Software/
#Install MMseqs2
wget https://github.com/soedinglab/MMseqs2/releases/download/10-6d92c/MMseqs2-Linux-AVX2.tar.gz
tar xvf MMseqs2-Linux-AVX2.tar.gz
export PATH="/Software/mmseqs2/bin:$PATH"

#Install Plass
cd /Software
wget https://github.com/soedinglab/plass/releases/download/2-c7e35/Plass-Linux.tar.gz
tar xvf Plass-Linux.tar.gz
export PATH="/Software/plass/bin/:$PATH"

#get databases
mkdir /Databases && cd /Databases
#wget ftp://ftp.ebi.ac.uk/pub/databases/Pfam/releases/Pfam31.0/Pfam-A.fasta.gz
#gzip -d Pfam-A.fasta.gz
#rm Pfam-A.fasta
#Building dbs
#MMSeqs
#wget ftp://ftp.ebi.ac.uk/pub/databases/Pfam/releases/Pfam31.0/Pfam-A.full.gz
#mmseqs convertmsa Pfam-A.full.gz pfamMsa
#mmseqs msa2profile pfamMsa pfamProfiles --match-mode 1
#rm -f pfamMsa pfamMsa.index
#rm -f Pfam-A.full.gz
#mmseqs createindex pfamProfiles tmp -k 5 -s 7
#ln -sf /Databases/pfamProfiles_seq_h /Databases/pfamProfiles_consensus_h
#ln -sf /Databases/pfamProfiles_seq_h.index /Databases/pfamProfiles_consensus_h.index
#mmseqs convert2fasta pfamProfiles_consensus pfamProfiles_consensus.faa

#HMMER
mkdir -p /Software/hmmer && cd /Software/hmmer
wget http://wwwuser.gwdg.de/~mmirdit/scratch/hmmer.tar.gz
tar zxvf hmmer.tar.gz
rm -f hmmer.tar.gz
export PATH="/Software/hmmer/:$PATH"
```

## Collection

 - Name: [motroy/singularity-mmseqs2](https://github.com/motroy/singularity-mmseqs2)
 - License: [MIT License](https://api.github.com/licenses/mit)

