---
id: 458
name: "michael-tn/bioconductor"
branch: "master"
tag: "latest"
commit: "a96c55fce3743acf5a545f887adc746dd799a581"
version: "1a6e34e5f43b698ca2e19b16f330cfc8"
build_date: "2020-12-17T13:37:30.568Z"
size_mb: 8625
size: 4157444127
sif: "https://datasets.datalad.org/shub/michael-tn/bioconductor/latest/2020-12-17-a96c55fc-1a6e34e5/1a6e34e5f43b698ca2e19b16f330cfc8.simg"
url: https://datasets.datalad.org/shub/michael-tn/bioconductor/latest/2020-12-17-a96c55fc-1a6e34e5/
recipe: https://datasets.datalad.org/shub/michael-tn/bioconductor/latest/2020-12-17-a96c55fc-1a6e34e5/Singularity
collection: michael-tn/bioconductor
---

# michael-tn/bioconductor:latest

```bash
$ singularity pull shub://michael-tn/bioconductor:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: bioconductor/release_core2

%labels
Maintainer mgx@ornl.gov based on dockerup file from: cag104@ucsd.edu
Version 1.0

%environment
export PATH="/opt/anaconda2/bin:$PATH"

%post

	apt-get update

	apt-get install -y curl wget libboost-all-dev
	
	R --slave -e "source('https://bioconductor.org/biocLite.R'); \
		      biocLite('ChIPQC')"

	R --slave -e "source('https://bioconductor.org/biocLite.R'); \
                      biocLite('groHMM')"

	R --slave -e "source('https://bioconductor.org/biocLite.R'); \
                      biocLite('RUVSeq')"

	R --slave -e "source('https://bioconductor.org/biocLite.R'); \
                      biocLite('edgeR')"

	R --slave -e "source('https://bioconductor.org/biocLite.R'); \
                      biocLite('DESeq2')"

	R --slave -e "source('https://bioconductor.org/biocLite.R'); \
                      biocLite('ChIPseeker')"

	R --slave -e 'install.packages(c("ggplot2", "data.table", "RColorBrewer", "devtools"), repos="https://cloud.r-project.org/")'

	R --slave -e 'install.packages("http://hartleys.github.io/QoRTs/QoRTs_LATEST.tar.gz", repos=NULL, type="source")'

	R --slave -e "library(devtools); \
	                  devtools::install_github('hms-dbmi/spp', build_vignettes = FALSE)"

	wget https://repo.continuum.io/archive/Anaconda2-5.0.0-Linux-x86_64.sh
	bash Anaconda2-5.0.0-Linux-x86_64.sh -b -p /opt/anaconda2

	/opt/anaconda2/bin/conda install -c bioconda --yes bbmap samtools epic sambamba deeptools macs2 bedtools bedops multiqc subread stringtie nextflow bowtie2 bwa hisat2 star fastqc gimmemotifs nucleoatac
```

## Collection

 - Name: [michael-tn/bioconductor](https://github.com/michael-tn/bioconductor)
 - License: None

