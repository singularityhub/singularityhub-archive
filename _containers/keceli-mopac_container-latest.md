---
id: 1648
name: "keceli/mopac_container"
branch: "master"
tag: "latest"
commit: "22714425c575cdd9204184537ce9627437efd84b"
version: "d5848894174082d8a1aea272b148ce32"
build_date: "2018-02-07T19:54:06.576Z"
size_mb: 151
size: 57491487
sif: "https://datasets.datalad.org/shub/keceli/mopac_container/latest/2018-02-07-22714425-d5848894/d5848894174082d8a1aea272b148ce32.simg"
url: https://datasets.datalad.org/shub/keceli/mopac_container/latest/2018-02-07-22714425-d5848894/
recipe: https://datasets.datalad.org/shub/keceli/mopac_container/latest/2018-02-07-22714425-d5848894/Singularity
collection: keceli/mopac_container
---

# keceli/mopac_container:latest

```bash
$ singularity pull shub://keceli/mopac_container:latest
```

## Singularity Recipe

```singularity
From: ubuntu:latest
Bootstrap: docker
%help
A container for MOPAC quantum chemistry package.
More info on MOPAC: http://openmopac.net/
You need a license to run MOPAC. See http://openmopac.net/download-c.html (Free for academic)
To install the license you need to create a persistent overlay where you add your license
through the shell.(See http://singularity.lbl.gov/docs-overlay)
You can do that by:

singularity image.create -s 5 license_overlay.img
singularity shell --overlay license_overlay.img keceli-mopac_container-master-latest.simg

Once you are in the shell type below after replacing 1234a1234 with your own license-key.
`/opt/mopac/MOPAC2016.exe 1234a1234`
Follow the instructions to install the license and then type `exit` to exit the shell.
Now you can run the container with two arguments <input file> <number of threads>
singularity run --overlay license_overlay.img keceli-mopac_container-master-latest.simg input.mop 4
%labels
AUTHOR Murat Keceli
REPO https://github.com/keceli/mopac_container
%post
echo "************************************************************"
echo "Installling required components"
echo "************************************************************" 
  apt-get -y install wget unzip
echo "************************************************************"
echo "Installling MOPAC"
echo "************************************************************"    
  mkdir -p /opt/mopac
  chmod 777 /opt/mopac
  cd /opt/mopac
  wget http://openmopac.net/MOPAC2016_for_Linux_64_bit.zip
  unzip MOPAC2016_for_Linux_64_bit.zip
  export LD_LIBRARY_PATH=/opt/mopac
  chmod +x /opt/mopac/MOPAC2016.exe
%environment
  LD_LIBRARY_PATH=/opt/mopac
  export LD_LIBRARY_PATH
%runscript
if [ $# -gt 1  ]; then
    echo "Using $2 threads"
    export OMP_NUM_THREADS=$2
else
    echo "Using 1 thread, you can specify the number of threads as the second argument"
    export OMP_NUM_THREADS=$1
fi
if [ $# -gt 0  ]; then
    if [ -f  $1 ] ; then
        echo "Running mopac with input file $1"
        exec /opt/mopac/MOPAC2016.exe "$1"
    else
        echo "Cannot find input file $1"
    fi
else
    echo "You need to specify the input file as the first argument"
fi
```

## Collection

 - Name: [keceli/mopac_container](https://github.com/keceli/mopac_container)
 - License: None

