---
id: 5005
name: "nuitrcs/biobakery"
branch: "master"
tag: "diamondv0822"
commit: "1ac59d86c14fa5dc5763fa37aaf1d6fbe6391ca0"
version: "b25e97f55692eab6a7f2778a153f19fa"
build_date: "2020-06-04T12:37:32.427Z"
size_mb: 11522
size: 5630832671
sif: "https://datasets.datalad.org/shub/nuitrcs/biobakery/diamondv0822/2020-06-04-1ac59d86-b25e97f5/b25e97f55692eab6a7f2778a153f19fa.simg"
url: https://datasets.datalad.org/shub/nuitrcs/biobakery/diamondv0822/2020-06-04-1ac59d86-b25e97f5/
recipe: https://datasets.datalad.org/shub/nuitrcs/biobakery/diamondv0822/2020-06-04-1ac59d86-b25e97f5/Singularity
collection: nuitrcs/biobakery
---

# nuitrcs/biobakery:diamondv0822

```bash
$ singularity pull shub://nuitrcs/biobakery:diamondv0822
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: biobakery/biobakery

%setup

%post 

	apt-get update
	apt-get install -y wget git locales

	#MC issue with locale (LC_ALL, LANGUAGE), to get it right:
	locale-gen "en_US.UTF-8"
	dpkg-reconfigure locales
	export LANGUAGE="en_US.UTF-8"
	echo 'LANGUAGE="en_US.UTF-8"' >> /etc/default/locale
	echo 'LC_ALL="en_US.UTF-8"' >> /etc/default/locale

	# install USEARCH. See https://github.com/CHPC-UofU/Singularity-bioBakery/blob/master/Singularity.
	# TODO: change license
	USEARCH_URL="https://drive5.com/cgi-bin/upload3.py?license=2018091412560519949"
	wget -O /usr/local/bin/usearch $USEARCH_URL
	chmod 111 /usr/local/bin/usearch

	# install missing biobakery tools not installed in the biobakery/biobakery Docker image
	# Note: `brew install metaphlan2` fails on biom package install (gcc compiler issue; not remedied by installing gcc-5)
	pip install numpy
	pip install pandas biopython scipy 'matplotlib>=2.2.3,<3.0' h5py biom-format
	cd /opt
	curl https://bitbucket.org/biobakery/metaphlan2/get/default.zip --output metaphlan2.zip
	unzip metaphlan2.zip
	cd biobakery-metaphlan2-*
	chmod 755 /home/linuxbrew

	cd /opt
	wget http://github.com/bbuchfink/diamond/releases/download/v0.8.22/diamond-linux64.tar.gz
	tar xzf diamond-linux64.tar.gz

	echo 'export PATH=/opt:$PATH:/home/linuxbrew/.linuxbrew/bin:$(pwd):$(pwd)/utils' >> $SINGULARITY_ENVIRONMENT

%test

	export PATH=/opt:/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:/home/linuxbrew/.linuxbrew/bin:/opt/biobakery-metaphlan2-*:/opt/biobakery-metaphlan2-*/utils

	mkdir ~/test_output
	
	# graphlan tests
	graphlan_annotate.py /opt/hmptree.xml ~/test_output/hmptree.annot.xml --annot /opt/annot.txt

	# humann2 tests
	humann2_test
	
	# kneaddata tests
	kneaddata -i /home/linuxbrew/.linuxbrew/Cellar/kneaddata/0.6.1/libexec/lib/python2.7/site-packages/kneaddata/tests/data/demo.fastq --output ~/test_output/kneaddata_output

	# halla tests
	halla -X /opt/X_16_100.txt -Y /opt/Y_16_100.txt --output ~/test_output/halla_output

	# ppanini tests
	# note: ppanini has "unittest.loader.ModuleImportFailure" tests that are designed to fail, I think for compatitibility purposes?
	ppanini_test

	# shortbred tests
	shortbred_identify.py --goi /home/linuxbrew/.linuxbrew/Cellar/biobakery_demos/1.6/libexec/lib/python2.7/site-packages/biobakery_demos/data/shortbred/input/input_prots.faa --ref /home/linuxbrew/.linuxbrew/Cellar/biobakery_demos/1.6/libexec/lib/python2.7/site-packages/biobakery_demos/data/shortbred/input/ref_prots.faa --markers mytestmarkers.faa --tmp ~/test_output/shortbred_output

	# (shortbred clean up)
	rm mytestmarkers.faa

	# metaphlan tests
	mkdir ~/test_output/metaphlan2_output
	cd ~/test_output/metaphlan2_output
	curl -O https://bitbucket.org/biobakery/biobakery/raw/tip/demos/biobakery_demos/data/metaphlan2/input/SRS014476-Supragingival_plaque.fasta.gz
	metaphlan2.py SRS014476-Supragingival_plaque.fasta.gz  --input_type fasta > SRS014476-Supragingival_plaque_profile.txt

	# (clean up from tests)
	cd ~
	rm -rf ~/test_output

%files

    singularity_logo.txt /opt
	test_files/annot.txt /opt
	test_files/hmptree.xml /opt
	test_files/X_16_100.txt /opt
	test_files/Y_16_100.txt /opt

%runscript

    cat /opt/singularity_logo.txt

%environment
```

## Collection

 - Name: [nuitrcs/biobakery](https://github.com/nuitrcs/biobakery)
 - License: [MIT License](https://api.github.com/licenses/mit)

