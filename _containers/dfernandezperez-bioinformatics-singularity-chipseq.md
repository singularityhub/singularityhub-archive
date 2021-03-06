---
id: 5116
name: "dfernandezperez/bioinformatics-singularity"
branch: "master"
tag: "chipseq"
commit: "887cfa86df32f4e7519e99c30dbe96e2a9b68bbb"
version: "14f8d6ed1b4eebcc9a86c2a0fc7a97cf"
build_date: "2019-05-17T20:05:25.822Z"
size_mb: 7611
size: 3050463263
sif: "https://datasets.datalad.org/shub/dfernandezperez/bioinformatics-singularity/chipseq/2019-05-17-887cfa86-14f8d6ed/14f8d6ed1b4eebcc9a86c2a0fc7a97cf.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/dfernandezperez/bioinformatics-singularity/chipseq/2019-05-17-887cfa86-14f8d6ed/
recipe: https://datasets.datalad.org/shub/dfernandezperez/bioinformatics-singularity/chipseq/2019-05-17-887cfa86-14f8d6ed/Singularity
collection: dfernandezperez/bioinformatics-singularity
---

# dfernandezperez/bioinformatics-singularity:chipseq

```bash
$ singularity pull shub://dfernandezperez/bioinformatics-singularity:chipseq
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: bioconductor/release_core2

%environment
export PATH="/opt/miniconda2/bin:$PATH"
export PATH=/usr/local/bin:$PATH

%post

	echo "Here we are installing software and other dependencies for the container!"

	echo "Installing basic dependencies"
	apt-get update
	apt-get install -y curl wget libboost-all-dev libudunits2-dev gawk
	
	# Install miniconda
	wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh
	bash Miniconda2-latest-Linux-x86_64.sh -b -p /opt/miniconda2
	/opt/miniconda2/bin/conda config --add channels defaults
	/opt/miniconda2/bin/conda config --add channels conda-forge
	/opt/miniconda2/bin/conda config --add channels bioconda
	
	# Install software required for chipseq pipeline with bioconda
	/opt/miniconda2/bin/conda install -c bioconda samtools=1.9 bowtie=1.2.2 macs2=2.1.1.20160309 preseq=2.0.3 \
	deeptools=3.1.1 multiqc=1.7 samblaster=0.1.24 wiggletools=1.2.2 pysam=0.15.0.1 bedops=2.4.35 r-spp=1.15.2 \
	ucsc-bedgraphtobigwig=366 fastqc=0.11.8 picard=2.18.7
	
	# Install fastp manually because bioconda verison is not the latest
	wget http://opengene.org/fastp/fastp
	chmod a+x ./fastp
	mv ./fastp /usr/local/bin
  
	# R packages and bioconductor
	R --slave -e "source('https://bioconductor.org/biocLite.R'); \
                      biocLite(c('ChIPseeker', 'org.Mm.eg.db', 'org.Hs.eg.db', 'TxDb.Mmusculus.UCSC.mm9.knownGene', 'TxDb.Mmusculus.UCSC.mm10.knownGene', 'TxDb.Hsapiens.UCSC.hg19.knownGene', 'TxDb.Hsapiens.UCSC.hg18.knownGene', 'TxDb.Hsapiens.UCSC.hg38.knownGene'))" 
		      
	R --slave -e 'install.packages(c("ggplot2", "data.table", "RColorBrewer", "devtools", "spp"), repos="https://cloud.r-project.org/")'
```

## Collection

 - Name: [dfernandezperez/bioinformatics-singularity](https://github.com/dfernandezperez/bioinformatics-singularity)
 - License: None

