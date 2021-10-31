---
id: 2277
name: "CNC-UMCG/cnc_meica"
branch: "master"
tag: "latest"
commit: "ddb509d99dbca1128bb18bdfb74c62e5fb5891bb"
version: "4df93b0332122927e8b7e49c14dc136f"
build_date: "2018-03-29T09:26:05.795Z"
size_mb: 7392
size: 3343052831
sif: "https://datasets.datalad.org/shub/CNC-UMCG/cnc_meica/latest/2018-03-29-ddb509d9-4df93b03/4df93b0332122927e8b7e49c14dc136f.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/CNC-UMCG/cnc_meica/latest/2018-03-29-ddb509d9-4df93b03/
recipe: https://datasets.datalad.org/shub/CNC-UMCG/cnc_meica/latest/2018-03-29-ddb509d9-4df93b03/Singularity
collection: CNC-UMCG/cnc_meica
---

# CNC-UMCG/cnc_meica:latest

```bash
$ singularity pull shub://CNC-UMCG/cnc_meica:latest
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: CNC-UMCG/cnc_base

%runscript
        exec meica.py "$@"

%environment
        PATH=$PATH:/usr/abin
        export PATH
%post
	apt-get install -y software-properties-common
	add-apt-repository universe
	apt-get update -y
	
	apt-get install -y tcsh xfonts-base python-qt4       \
        	                gsl-bin netpbm gnome-tweak-tool   \
                	        libjpeg62 xvfb xterm vim curl     \
                        	gedit evince                      \
	                        libxm4 build-essential	
	
	# install SciPy
	apt-get install -y python-numpy python-scipy python-matplotlib \
	 	  	   ipython ipython-notebook \
			   python-pandas python-sympy python-nose
	mkdir /usr/abin
	cd
	curl -O https://afni.nimh.nih.gov/pub/dist/bin/linux_ubuntu_16_64/@update.afni.binaries
	tcsh @update.afni.binaries -package linux_ubuntu_16_64  -do_extras -bindir /usr/abin
	export R_LIBS=$HOME/R
	export PATH=$PATH:/usr/abin

	bash
	################
	# Install R   #
	################
	
	mkdir $R_LIBS
	echo 'export R_LIBS=$HOME/R' >> ~/.bashrc
	
	bash
	
	curl -O https://afni.nimh.nih.gov/pub/dist/src/scripts_src/@add_rcran_ubuntu.tcsh
	tcsh @add_rcran_ubuntu.tcsh

	/usr/abin/rPkgsInstall -pkgs ALL
```

## Collection

 - Name: [CNC-UMCG/cnc_meica](https://github.com/CNC-UMCG/cnc_meica)
 - License: [GNU General Public License v2.0](https://api.github.com/licenses/gpl-2.0)

