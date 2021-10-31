---
id: 929
name: "apeltzer/EAGER-GUI"
branch: "master"
tag: "latest"
commit: "07f519999ac34e068773ec0e1b052cb4694c6650"
version: "ed6c9812552e081c87fb9bafd01cde2b"
build_date: "2021-04-12T13:57:45.879Z"
size_mb: 2089
size: 1409404959
sif: "https://datasets.datalad.org/shub/apeltzer/EAGER-GUI/latest/2021-04-12-07f51999-ed6c9812/ed6c9812552e081c87fb9bafd01cde2b.simg"
url: https://datasets.datalad.org/shub/apeltzer/EAGER-GUI/latest/2021-04-12-07f51999-ed6c9812/
recipe: https://datasets.datalad.org/shub/apeltzer/EAGER-GUI/latest/2021-04-12-07f51999-ed6c9812/Singularity
collection: apeltzer/EAGER-GUI
---

# apeltzer/EAGER-GUI:latest

```bash
$ singularity pull shub://apeltzer/EAGER-GUI:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: finalduty/archlinux:daily 

%post

#Adding mirrors to pacman mirrorlist
echo "Server = http://mirror.de.leaseweb.net/archlinux/\$repo/os/\$arch" >> /etc/pacman.d/mirrorlist
echo "[lambdait]" >> /etc/pacman.conf
echo "SigLevel = Never" >> /etc/pacman.conf
echo "Server = https://lambda.informatik.uni-tuebingen.de/repo/mypkgs/" >> /etc/pacman.conf


#Installing basic dependencies
pacman -Sy --noconfirm freetype2 ttf-dejavu git libcups mesa-libgl rsync strace r python2 gsl libxtst intel-tbb

#Clean up
paccache -r -k0

#Install all the dependencies of my pipeline
#JDK8, BT2, BWA, Samtools, etc.

pacman -Sy --noconfirm --force jdk bam2tdf dedup circularmapper clipandmerge fastqc preseq vcf2genome damageprofiler

#Clean up intermediate files
paccache -r -k0

pacman -Sy --noconfirm --force fastx_toolkit htslib qualimap mapdamage bwa eager-reportengine eagerstat eagerversions

#Clean up intermediate files
paccache -r -k0

pacman -Sy --noconfirm --force bowtie2 picard-tools stampy angsd gatk schmutzi

#Clean up intermediate files
paccache -r -k0

pacman -Sy --noconfirm --force eager-gui eager-cli

#Create analysis mountpoint
mkdir -p /data

#Clean up
paccache -r -k0 #clean up

%files
# Add GATK Licence to image to be consistent with Licencing Permission by Broad Institute
GATKLicence.txt /usr/share/licenses/common/GATKLicence.txt


%labels
Maintainer	alexander.peltzer@uni-tuebingen.de
Version	1.92

%test

#cant test bwa and samtools unfortunately...
bwa || true
samtools || true
mapDamage -h
damageprofiler -h
dedup -h
ClipAndMerge
AdapterRemoval --version 
fastqc -h
vcf2genome -h
qualimap -h
ReportTable -h
schmutzi -h
bowtie2 -h
eagercli
picard || true
gatk --version
```

## Collection

 - Name: [apeltzer/EAGER-GUI](https://github.com/apeltzer/EAGER-GUI)
 - License: None

