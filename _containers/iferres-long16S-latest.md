---
id: 12465
name: "iferres/long16S"
branch: "master"
tag: "latest"
commit: "ab7d7f8519431fbd72f4eac38f09d95c277d03b4"
version: "aade05707a63b8b4562abef38e91a47f"
build_date: "2020-04-01T14:57:29.927Z"
size_mb: 5791.0
size: 3771953183
sif: "https://datasets.datalad.org/shub/iferres/long16S/latest/2020-04-01-ab7d7f85-aade0570/aade05707a63b8b4562abef38e91a47f.sif"
url: https://datasets.datalad.org/shub/iferres/long16S/latest/2020-04-01-ab7d7f85-aade0570/
recipe: https://datasets.datalad.org/shub/iferres/long16S/latest/2020-04-01-ab7d7f85-aade0570/Singularity
collection: iferres/long16S
---

# iferres/long16S:latest

```bash
$ singularity pull shub://iferres/long16S:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%post
	apt update -y
	apt upgrade -y
	apt install -y wget bzip2 zip git python3 python3-pip r-base libz-dev bc xvfb software-properties-common
	apt clean -y
	pip3 install --upgrade pip

	# Install OpenJDK 12
	wget -qO - https://adoptopenjdk.jfrog.io/adoptopenjdk/api/gpg/key/public |  apt-key add -
	add-apt-repository --yes https://adoptopenjdk.jfrog.io/adoptopenjdk/deb/
	apt install -y apt-transport-https
	apt update -y
	apt install -y adoptopenjdk-12-hotspot openjfx
	apt autoremove -y

	## Install NanoPlot nanofilt and (deprecated -> qcat)
	pip install NanoPlot==1.28.4 nanofilt # qcat

	## Install porechop
	pip install git+https://github.com/rrwick/Porechop.git

	## Install seqtk
	git clone https://github.com/lh3/seqtk.git
	cd seqtk/
	make
	mv seqtk /usr/local/bin
	cd ../

	## Install LAST
	cd /opt
	wget http://last.cbrc.jp/last-1047.zip
	unzip last-1047.zip
	cd last-1047
	make
	make install
	cd ..

	## Install megan6
	wget https://software-ab.informatik.uni-tuebingen.de/download/megan6/MEGAN_Community_unix_6_18_0.sh
	bash MEGAN_Community_unix_6_18_0.sh -q 
	MEGAN="/opt/megan"
	find "$MEGAN"/tools -type f | while read -r file; do b=$(basename "$file"); ln -fs "$file" /usr/local/bin/"$b"; sed -i -e "s@\"\$0\"@\"$file\"@" "$file"; done
	ln -fs "$MEGAN"/MEGAN /usr/local/bin/MEGAN
	sed -i -e "s@\"\$0\"@\"$MEGAN/MEGAN\"@" "$MEGAN"/MEGAN

	## Download DAA_Converter (jar) and make a executable script to call it
	wget https://github.com/BenjaminAlbrecht84/DAA_Converter/releases/download/v0.9.0/DAA_Converter_v0.9.0.jar


	## Download SILVA
	mkdir /opt/silva
	cd /opt/silva
	wget https://www.arb-silva.de/fileadmin/silva_databases/current/Exports/SILVA_138_SSURef_NR99_tax_silva.fasta.gz
	gunzip SILVA_138_SSURef_NR99_tax_silva.fasta.gz
	# subset bacteria and archaea
	grep -E "Archaea;|Bacteria;" SILVA_138_SSURef_NR99_tax_silva.fasta | cut -d " " -f1 | sed 's/>//g' > list.txt
	seqtk subseq SILVA_138_SSURef_NR99_tax_silva.fasta list.txt > SILVA_138_SSURef_NR99_tax_silva_subseq.fasta
	rm SILVA_138_SSURef_NR99_tax_silva.fasta list.txt
	## Make lastdb
	lastdb -cR01 -P1 silva SILVA_138_SSURef_NR99_tax_silva_subseq.fasta
	rm SILVA_138_SSURef_NR99_tax_silva_subseq.fasta

	wget https://www.arb-silva.de/fileadmin/silva_databases/current/Exports/taxonomy/taxmap_slv_ssu_ref_nr_138.txt.gz
	gunzip taxmap_slv_ssu_ref_nr_138.txt.gz
	
	wget https://www.arb-silva.de/fileadmin/silva_databases/current/Exports/taxonomy/tax_slv_ssu_138.acc_taxid.gz
	gunzip tax_slv_ssu_138.acc_taxid.gz
	cat tax_slv_ssu_138.acc_taxid | sed 's/\.\([0-9]\+\)\.\([0-9]\+\)//g' > SSURef_Nr99_138_tax_silva_to_NCBI_synonyms.map

	# Download silva to ncbi synonyms mapping file
	# wget https://software-ab.informatik.uni-tuebingen.de/download/megan6/SSURef_Nr99_132_tax_silva_to_NCBI_synonyms.map.gz
	# gunzip SSURef_Nr99_132_tax_silva_to_NCBI_synonyms.map.gz
	
	cd ../

	## Clean
	rm -rf MEGAN_Community_unix_6_15_0.sh last-1047 last-1047.zip

%labels
	Authors: Cecilia Salazar (csalazar@pasteur.edu.uy) & Ignacio Ferres (iferres@pasteur.edu.uy)
	Maintainer: Ignacio Ferres (iferres@pasteur.edu.uy)
```

## Collection

 - Name: [iferres/long16S](https://github.com/iferres/long16S)
 - License: None

