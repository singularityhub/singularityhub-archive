---
id: 5308
name: "ANGSD-wrapper/angsd-wrapper"
branch: "dev_containers"
tag: "latest"
commit: "9200983d85beaa6d8c76d5e5b37c27dd90ccd402"
version: "6817b159bdb0f66e69904a26d76696b5"
build_date: "2021-04-01T14:23:19.110Z"
size_mb: 779
size: 247328799
sif: "https://datasets.datalad.org/shub/ANGSD-wrapper/angsd-wrapper/latest/2021-04-01-9200983d-6817b159/6817b159bdb0f66e69904a26d76696b5.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ANGSD-wrapper/angsd-wrapper/latest/2021-04-01-9200983d-6817b159/
recipe: https://datasets.datalad.org/shub/ANGSD-wrapper/angsd-wrapper/latest/2021-04-01-9200983d-6817b159/Singularity
collection: ANGSD-wrapper/angsd-wrapper
---

# ANGSD-wrapper/angsd-wrapper:latest

```bash
$ singularity pull shub://ANGSD-wrapper/angsd-wrapper:latest
```

## Singularity Recipe

```singularity
Bootstrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum

%runscript
	echo "Angsd-Wrapper install test.\n"
	declare -a args=("$@")
	INPUTSOURCE="${args[0]}"
        BASESOURCE="${args[1]}"

        if [[ -d "${INPUTSOURCE}" ]]; then  # Checks if cluster has enabled 'overlayfs'. Which allows for full filepath.
                SOURCE="${INPUTSOURCE}"
        else # If full file paths are not allow on your cluster than operate from users locale directory 
                SOURCE="${BASESOURCE}"
        fi

        cd ${SOURCE}
        
        cd dependencies
        ROOT=$(pwd)

        wget  https://github.com/samtools/samtools/releases/download/1.8/samtools-1.8.tar.bz2
        tar -jxvf samtools-1.8.tar.bz2
        rm samtools-1.8.tar.bz2
        cd samtools-1.8
        samPath=$(pwd)
        echo "export PATH=$(pwd)/bin:"'${PATH}' >> ~/.bash_profile # Add the path to bash_profile
        HTSLIB_DIR=$(pwd -P)/htslib-1.8

        cd "${HTSLIB_DIR}"
        ./configure --prefix=$(pwd)
        make
        make install
        cd "${samPath}"

        ./configure --with-htslib=${HTSLIB_DIR} --prefix=$(pwd)
        make
        make install
        make clean

        cd "${ROOT}"

        git clone https://github.com/fgvieira/ngsF.git
        cd ngsF
        git reset --hard d980b85c0746c297285e2e415193914aa0d0412a

        cd "${ROOT}"

        wget http://popgen.dk/software/download/angsd/angsd0.920.tar.gz
        tar -xvf angsd0.920.tar.gz
        rm angsd0.920.tar.gz
        cd angsd
        make HTSSRC="${HTSLIB_DIR}"

        cd "${ROOT}"

        mkdir ngsAdmix
        cd ngsAdmix
        wget http://popgen.dk/software/download/NGSadmix/ngsadmix32.cpp
        g++ ngsadmix32.cpp -O3 -lpthread -lz -o NGSadmix

        cd "${ROOT}"

        git clone https://github.com/mfumagalli/ngsPopGen.git
        cd ngsPopGen
        git reset --hard 8ead2d469f42942f413f6c93664b568d2eb8a124
        make

        cd "${ROOT}"

        echo alias "angsd-wrapper='${SOURCE}/angsd-wrapper'" >> ~/.bash_profile
        echo "export PATH=${samPath}:"'${PATH}' >> ~/.bash_profile # Add the path to bash_profile

%post
        yum group install -y "Development Tools"
    	yum -y install wget
    	yum install -y tar.x86_64	
	yum install -y git
	yum install -y bzip2
	yum install -y gcc
	yum install -y ncurses-devel
	yum install -y zlib-devel
	yum install -y bzip2-devel
	yum install -y xz-devel
	#yum groupinstall -y "Development Tools"
	yum install -y xz 
	yum install -y curl-devel
	yum -y update	

	yum clean all
```

## Collection

 - Name: [ANGSD-wrapper/angsd-wrapper](https://github.com/ANGSD-wrapper/angsd-wrapper)
 - License: [MIT License](https://api.github.com/licenses/mit)

