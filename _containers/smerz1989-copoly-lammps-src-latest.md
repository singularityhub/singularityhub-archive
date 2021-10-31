---
id: 8432
name: "smerz1989/copoly-lammps-src"
branch: "master"
tag: "latest"
commit: "4bcd5d315256cada988d24da475b39d61495ff82"
version: "ad3783b45fce7b87c7444a8812d7798d"
build_date: "2019-08-14T23:24:04.501Z"
size_mb: 1740.0
size: 827068447
sif: "https://datasets.datalad.org/shub/smerz1989/copoly-lammps-src/latest/2019-08-14-4bcd5d31-ad3783b4/ad3783b45fce7b87c7444a8812d7798d.sif"
url: https://datasets.datalad.org/shub/smerz1989/copoly-lammps-src/latest/2019-08-14-4bcd5d31-ad3783b4/
recipe: https://datasets.datalad.org/shub/smerz1989/copoly-lammps-src/latest/2019-08-14-4bcd5d31-ad3783b4/Singularity
collection: smerz1989/copoly-lammps-src
---

# smerz1989/copoly-lammps-src:latest

```bash
$ singularity pull shub://smerz1989/copoly-lammps-src:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04


%files
    ./src /opt/

%environment
	export PATH=/usr/local/bin:$PATH
        export PATH=$PATH:/opt/.openmpi/bin
        export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/.openmpi/lib/

%post
    cd /opt
	apt-get -y update
	apt-get -y install git\
			 cmake\
			build-essential\
			python3-dev\
			libpython3-dev\
			python3\
                        python3-pip\
                        openssh-client openssh-server
        wget https://download.open-mpi.org/release/open-mpi/v2.1/openmpi-2.1.5.tar.gz
        tar -xvf openmpi-*
        cd openmpi-*
        ./configure --prefix="/opt/.openmpi" 
        make
        make install
        cd ..
	git clone -b stable_5Jun2019 https://github.com/lammps/lammps.git
	cp src/dump.cpp src/dump.h src/fix_print_if.cpp src/fix_print_if.h src/pair_lj_expand_twopiece.cpp src/pair_lj_expand_twopiece.h src/pair_lj_twopiece.cpp src/pair_lj_twopiece.h src/pair_soft_shift.cpp src/pair_soft_shift.h lammps/src
	cd lammps
	mkdir build
	cd build
	cmake -D CMAKE_INSTALL_PREFIX=/usr/local -D PKG_PYTHON=on -D PKG_MC=on -D PKG_MOLECULE=on -D PKG_RIGID=on -D PKG_USER-MISC=on -D PKG_KSPACE=on -D PKG_CLASS2=on ../cmake
	make
	make install
        pip3 install numpy        

%runscript

	lmp "$@"
```

## Collection

 - Name: [smerz1989/copoly-lammps-src](https://github.com/smerz1989/copoly-lammps-src)
 - License: None

