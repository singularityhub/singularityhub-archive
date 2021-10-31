---
id: 2668
name: "Smahane/HPC-Container"
branch: "master"
tag: "latest"
commit: "42078783b69c1aaa4fceaf4840fc5dd1a829e0ee"
version: "83c54a4d6963820ca669e5e8468a3fb6"
build_date: "2018-05-08T13:50:23.740Z"
size_mb: 2709
size: 894783519
sif: "https://datasets.datalad.org/shub/Smahane/HPC-Container/latest/2018-05-08-42078783-83c54a4d/83c54a4d6963820ca669e5e8468a3fb6.simg"
url: https://datasets.datalad.org/shub/Smahane/HPC-Container/latest/2018-05-08-42078783-83c54a4d/
recipe: https://datasets.datalad.org/shub/Smahane/HPC-Container/latest/2018-05-08-42078783-83c54a4d/Singularity
collection: Smahane/HPC-Container
---

# Smahane/HPC-Container:latest

```bash
$ singularity pull shub://Smahane/HPC-Container:latest
```

## Singularity Recipe

```singularity
BootStrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/

Include: yum

%help
This is a container to run AMREX binarie on SKL machine. just type ./amrex.img and it should run

%setup
	#Create a working directory 
        mkdir -p $SINGULARITY_ROOTFS/tempdir
        if [ ! -x "$SINGULARITY_ROOTFS/tempdir" ]; then
           echo "failed to create tempdir directory..."
           exit 1
        fi
	
	wget https://github.com/Smahane/Intel-HPC-Container/blob/master/containers/amrex/Nyx3d.intel.MPI.OMP.SKLAVX512.ex
	wget https://github.com/Smahane/Intel-HPC-Container/blob/master/containers/amrex/inputs
	wget https://github.com/Smahane/Intel-HPC-Container/blob/master/containers/amrex/runlog
	wget https://github.com/Smahane/Intel-HPC-Container/blob/master/containers/amrex/probin
	
	 cp -rf Nyx3d.intel.MPI.OMP.SKLAVX512.ex $SINGULARITY_ROOTFS/tempdir
	 cp -rf inputs $SINGULARITY_ROOTFS/tempdir  
	 cp -rf runlog $SINGULARITY_ROOTFS/tempdir 
	 cp -rf probin $SINGULARITY_ROOTFS/tempdir 
	    
        if [ "$(ls -A $SINGULARITY_ROOTFS/tempdir/)" ]; then
                   echo "Files are copies here $SINGULARITY_ROOTFS/tempdir"
                   ls $SINGULARITY_ROOTFS/tempdir/
        fi

        chmod -R 777 $SINGULARITY_ROOTFS/tempdir/*

        exit 0
	
	
%post
	yum install wget -y
       		
	#installing runtime libs for virtual machines
        rpm --import https://yum.repos.intel.com/2018/setup/RPM-GPG-KEY-intel-psxe-runtime-2018
	rpm -Uhv https://yum.repos.intel.com/2018/setup/intel-psxe-runtime-2018-reposetup-1-0.noarch.rpm
	yum install intel-psxe-runtime -y

	#installing gcc
        yum install gcc -y
        yum install bc -y

%environment
#	export OMP_NUM_THREADS=40
	
%runscript 
        echo "This is what happens when you run the container..."
	
	cd $SINGULARITY_ROOTFS/tempdir/
	pwd
	source /opt/intel/psxe_runtime/linux/bin/psxevars.sh
	ls -l Nyx3d.intel.MPI.OMP.SKLAVX512.ex
	result="$SINGULARITY_ROOTFS/tempdir/Nyx3d.intel.MPI.OMP.SKLAVX512.log"
	./Nyx3d.intel.MPI.OMP.SKLAVX512.ex inputs |tee $result
	echo "find results in /tmp/Nyx3d.intel.MPI.OMP.SKLAVX512.ex.log"
```

## Collection

 - Name: [Smahane/HPC-Container](https://github.com/Smahane/HPC-Container)
 - License: None

