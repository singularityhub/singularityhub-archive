---
id: 2666
name: "Smahane/HPC-Container"
branch: "master"
tag: "milc"
commit: "c6f597768125dfd9cd253c7f18b5e7f8d742ae9e"
version: "7f84db5ba2e12a8467564670cc2ce015"
build_date: "2018-05-08T13:50:23.758Z"
size_mb: 2645
size: 875155487
sif: "https://datasets.datalad.org/shub/Smahane/HPC-Container/milc/2018-05-08-c6f59776-7f84db5b/7f84db5ba2e12a8467564670cc2ce015.simg"
url: https://datasets.datalad.org/shub/Smahane/HPC-Container/milc/2018-05-08-c6f59776-7f84db5b/
recipe: https://datasets.datalad.org/shub/Smahane/HPC-Container/milc/2018-05-08-c6f59776-7f84db5b/Singularity
collection: Smahane/HPC-Container
---

# Smahane/HPC-Container:milc

```bash
$ singularity pull shub://Smahane/HPC-Container:milc
```

## Singularity Recipe

```singularity
BootStrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/

Include: yum

%help
echo "this is a container to run MILC binarie on SKL machine"

%setup
echo $PWD
        
        #create a working directory
        mkdir -p $SINGULARITY_ROOTFS/tempdir
        if [ ! -x "$SINGULARITY_ROOTFS/tempdir" ]; then
           echo "failed to create tempdir directory..."
           exit 1
        fi
	wget https://github.com/Smahane/Intel-HPC-Container/tree/master/containers/milc/run.tar.gz
	 tar -zxvf run.tar.gz -C $SINGULARITY_ROOTFS/tempdir
	 
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
	echo "set the env variable"
	OMP_NUM_THREADS=5
	KMP_AFFINITY='granularity=fine,scatter'

%runscript 

	source /opt/intel/psxe_runtime/linux/bin/compilervars.sh intel64
	echo "run milc for SKL"

	cd $SINGULARITY_ROOTFS/tempdir/run/	
	mpiexec.hydra -n 8 $SINGULARITY_ROOTFS/tempdir/su3_rhmd_hisq.skx < $SINGULARITY_ROOTFS/tempdir/params.24x24x24x24 

	./parse_milc.sh -l qphix -m flops -r milc.su3_rhmd_hisq.log
```

## Collection

 - Name: [Smahane/HPC-Container](https://github.com/Smahane/HPC-Container)
 - License: None

