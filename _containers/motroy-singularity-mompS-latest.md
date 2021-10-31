---
id: 11761
name: "motroy/singularity-mompS"
branch: "master"
tag: "latest"
commit: "d5828aca2684c5322ad288895db0f50976b805ec"
version: "4de65854950c09626c778e999c2e1287"
build_date: "2020-12-14T21:52:55.114Z"
size_mb: 3297.0
size: 1263816735
sif: "https://datasets.datalad.org/shub/motroy/singularity-mompS/latest/2020-12-14-d5828aca-4de65854/4de65854950c09626c778e999c2e1287.sif"
url: https://datasets.datalad.org/shub/motroy/singularity-mompS/latest/2020-12-14-d5828aca-4de65854/
recipe: https://datasets.datalad.org/shub/motroy/singularity-mompS/latest/2020-12-14-d5828aca-4de65854/Singularity
collection: motroy/singularity-mompS
---

# motroy/singularity-mompS:latest

```bash
$ singularity pull shub://motroy/singularity-mompS:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:latest

%environment
export PATH="/miniconda/miniconda2/:/miniconda/miniconda2/bin:/mompS:/mompS/schema/:$PATH"
export PERL5LIB="/miniconda/miniconda2/lib:$PERL5LIB"
export CONDARC=/.condarc
export LC_ALL=C

%post
#install miniconda2
export CONDARC=/.condarc
mkdir /miniconda && cd /miniconda
apt update && apt install -y git curl wget less locate build-essential openssh-server zlib1g-dev libboost-all-dev perl libmoo-perl liblist-moreutils-perl libjson-perl default-jre #python3 python3-numpy python3-scipy python3-pip
wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh
chmod +x Miniconda2-latest-Linux-x86_64.sh
./Miniconda2-latest-Linux-x86_64.sh -b -p /miniconda/miniconda2
/miniconda/miniconda2/bin/conda config --file /.condarc --add channels defaults && /miniconda/miniconda2/bin/conda config --file /.condarc --add channels conda-forge && /miniconda/miniconda2/bin/conda config --file /.condarc --add channels bioconda
/miniconda/miniconda2/bin/conda install -c bioconda freebayes=1.0.2 picard=1.139 samtools=1.3.1 bwa=0.7.8 blast=2.5.0 legsta
export PATH="/miniconda/miniconda2/:/miniconda/miniconda2/bin:$PATH"
export PERL5LIB="/miniconda/miniconda2/lib:$PERL5LIB"
cd /
git clone https://github.com/ODiogoSilva/mompS && cd mompS
sed -i 's@/bioinfo_apps/ncbi-blast-2.4.0+/bin@/miniconda/miniconda2/bin/@g' /mompS/config.txt
sed -i 's@/bioinfo_apps/bin@/miniconda/miniconda2/bin/@g' /mompS/config.txt
sed -i 's@/bioinfo_apps/samtools/bin@/miniconda/miniconda2/bin/@g' /mompS/config.txt
sed -i 's@/bioinfo_apps/jre1.8.0_73/bin/java -jar /bioinfo_apps/picard-1.139/dist/picard.jar@java -jar /miniconda/miniconda2/bin/picard.jar@g' /mompS/config.txt
sed -i 's@/bioinfo_apps/freebayse/bin@/miniconda/miniconda2/bin/@g' /mompS/config.txt
sed -i 's@#!/usr/bin/perl@#!/miniconda/miniconda2/bin/perl@g' /mompS/*.pl
sed -i 's@CONFIG, "config.txt"@CONFIG, "/mompS/config.txt"@g' /mompS/momps.pl
sed -i 's@perl mompS_2_pipe.pl@perl /mompS/mompS_2_pipe.pl@g' /mompS/momps.pl
sed -i 's@perl Extract_MLST_Legionella_mompS.pl@perl /mompS/Extract_MLST_Legionella_mompS.pl@g' /mompS/momps.pl
sed -i 's@MLST_Representative_Legionella.fasta@/mompS/MLST_Representative_Legionella.fasta@g' /mompS/momps.pl
sed -i 's@Ref_Paris_mompS_2.fasta@/mompS/Ref_Paris_mompS_2.fasta@g' /mompS/mompS_2_pipe.pl
sed -i 's@CONFIG, "config.txt"@CONFIG, "/mompS/config.txt"@g' /mompS/mompS_2_pipe.pl
sed -i 's@perl Extract_concensus_based_on_filter_and_unfilter_vcf.pl@perl /mompS/Extract_concensus_based_on_filter_and_unfilter_vcf.pl@g' /mompS/mompS_2_pipe.pl
sed -i 's@perl Find_mompS_ST_from_mompS_regen_fq.pl@perl /mompS/Find_mompS_ST_from_mompS_regen_fq.pl@g' /mompS/mompS_2_pipe.pl
sed -i 's@perl Filter_mompS2_boards_reads.pl@perl /mompS/Filter_mompS2_boards_reads.pl@g' /mompS/mompS_2_pipe.pl
sed -i 's@$bwa_path/bwa mem -t@bwa mem -t@g' /mompS/mompS_2_pipe.pl
sed -i 's@threads /mompS/Ref_Paris_mompS_2.fasta@threads -M /mompS/Ref_Paris_mompS_2.fasta@g' /mompS/mompS_2_pipe.pl
sed -i "s#-R '\\\@RG\\\tID\\:group1\\\tSM\\:sample81\\\tPL\\:illumina\\\tLB\\:Technion\\\tPU\\:unit1'  ##g" /mompS/mompS_2_pipe.pl
sed -i 's@CONFIG, "config.txt"@CONFIG, "/mompS/config.txt"@g' /mompS/Find_mompS_ST_from_mompS_regen_fq.pl
sed -i 's@MLST_mompS_Representative_Legionella.fasta@/mompS/MLST_mompS_Representative_Legionella.fasta@g' /mompS/Find_mompS_ST_from_mompS_regen_fq.pl
sed -i 's@perl Extract_MLST_mompS_Legionella.pl@perl /mompS/Extract_MLST_mompS_Legionella.pl@g' /mompS/Find_mompS_ST_from_mompS_regen_fq.pl
sed -i 's@#!/usr/local/bin/perl@#!/miniconda/miniconda2/bin/perl@g' /mompS/*.pl
sed -i 's@CONFIG, "config.txt"@CONFIG, "/mompS/config.txt"@g' /mompS/Extract_concensus_based_on_filter_and_unfilter_vcf.pl
sed -i 's@mompS, "schema/mompS.fas"@mompS, "/mompS/schema/mompS.fas"@g' /mompS/Extract_MLST_mompS_Legionella.pl
sed -i 's@, "schema/@, "/mompS/schema/@g' /mompS/Extract_MLST_Legionella_mompS.pl

cd /mompS
/miniconda/miniconda2/bin/bwa index -p Ref_Paris_mompS_2.fasta Ref_Paris_mompS_2.fasta
sed -e 's@>asd_@>@g' /miniconda/miniconda2/pkgs/legsta-0.3.7-0/db/asd.tfa >/mompS/schema/asd.fas
sed -e 's@>flaA_@>@g' /miniconda/miniconda2/pkgs/legsta-0.3.7-0/db/flaA.tfa >/mompS/schema/flaA.fas
sed -e 's@>mip_@>@g' /miniconda/miniconda2/pkgs/legsta-0.3.7-0/db/mip.tfa >/mompS/schema/mip.fas
sed -e 's@>mompS_@>@g' /miniconda/miniconda2/pkgs/legsta-0.3.7-0/db/mompS.tfa >/mompS/schema/mompS.fas
sed -e 's@>neuAh_@>@g' -e 's@>neuA_@>@g' /miniconda/miniconda2/pkgs/legsta-0.3.7-0/db/neuA.tfa >/mompS/schema/neuA.fas
sed -e 's@>pilE_@>@g' /miniconda/miniconda2/pkgs/legsta-0.3.7-0/db/pilE.tfa >/mompS/schema/pilE.fas
sed -e 's@>proA_@>@g' /miniconda/miniconda2/pkgs/legsta-0.3.7-0/db/proA.tfa >/mompS/schema/proA.fas
cp /miniconda/miniconda2/pkgs/legsta-0.3.7-0/db/legionella.txt /mompS/schema/profiles.txt
sed -i 's@$@\n@g' /mompS/schema/profiles.txt
sed -i '${/^$/d}' /mompS/schema/profiles.txt
cd /mompS/schema/
/miniconda/miniconda2/bin/makeblastdb -in mompS.fas -dbtype nucl
export PATH="/mompS/:/mompS/schema/:$PATH"
```

## Collection

 - Name: [motroy/singularity-mompS](https://github.com/motroy/singularity-mompS)
 - License: [MIT License](https://api.github.com/licenses/mit)

