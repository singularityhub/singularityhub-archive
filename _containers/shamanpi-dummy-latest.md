---
id: 13615
name: "shamanpi/dummy"
branch: "master"
tag: "latest"
commit: "e6ccb97bcedd72bad12450cf934a1a0cce0b4595"
version: "d3b23148e9a1eba5058609052b0fcdca"
build_date: "2020-07-14T15:21:30.569Z"
size_mb: 796.0
size: 251617311
sif: "https://datasets.datalad.org/shub/shamanpi/dummy/latest/2020-07-14-e6ccb97b-d3b23148/d3b23148e9a1eba5058609052b0fcdca.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/shamanpi/dummy/latest/2020-07-14-e6ccb97b-d3b23148/
recipe: https://datasets.datalad.org/shub/shamanpi/dummy/latest/2020-07-14-e6ccb97b-d3b23148/Singularity
collection: shamanpi/dummy
---

# shamanpi/dummy:latest

```bash
$ singularity pull shub://shamanpi/dummy:latest
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

        wget  https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2
        tar -jxvf samtools-1.9.tar.bz2
        rm samtools-1.9.tar.bz2
        cd samtools-1.9
        samPath=$(pwd)
        echo "export PATH=$(pwd)/bin:"'${PATH}' >> ~/.bash_profile # Add the path to bash_profile
        HTSLIB_DIR=$(pwd -P)/htslib-1.9

        cd "${HTSLIB_DIR}"
        ./configure --prefix=$(pwd)
        make
        make install
        cd "${samPath}"

        ./configure --with-htslib=${HTSLIB_DIR} --prefix=$(pwd)
        make
        make install

        cd "${ROOT}"

        git clone https://github.com/fgvieira/ngsF.git
        cd ngsF
        git reset --hard d980b85c0746c297285e2e415193914aa0d0412a
        make

        cd "${ROOT}"

	# wget http://popgen.dk/software/download/angsd/angsd0.928.tar.gz
        # tar -xvf angsd0.928.tar.gz
        # rm angsd0.928.tar.gz
	git clone https://github.com/ANGSD/angsd
	git clone https://github.com/samtools/htslib/
        cd "${ROOT}"/htslib
        make

        cd "${ROOT}"/angsd
        #make HTSSRC="${HTSLIB_DIR}"
        make HTSSRC="${ROOT}"/htslib

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
        yum install -y openssl-devel
        yum install -y epel-release
	yum -y update	

	yum clean all
```

## Collection

 - Name: [shamanpi/dummy](https://github.com/shamanpi/dummy)
 - License: None

