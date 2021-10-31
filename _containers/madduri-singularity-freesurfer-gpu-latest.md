---
id: 5976
name: "madduri/singularity-freesurfer-gpu"
branch: "master"
tag: "latest"
commit: "4f1c0ce1e56e27e8b046855a15657bdaac256a71"
version: "efd97cdfcdbfc8c2677de3122564dc7e"
build_date: "2021-01-01T15:55:18.246Z"
size_mb: 16468
size: 7998976031
sif: "https://datasets.datalad.org/shub/madduri/singularity-freesurfer-gpu/latest/2021-01-01-4f1c0ce1-efd97cdf/efd97cdfcdbfc8c2677de3122564dc7e.simg"
url: https://datasets.datalad.org/shub/madduri/singularity-freesurfer-gpu/latest/2021-01-01-4f1c0ce1-efd97cdf/
recipe: https://datasets.datalad.org/shub/madduri/singularity-freesurfer-gpu/latest/2021-01-01-4f1c0ce1-efd97cdf/Singularity
collection: madduri/singularity-freesurfer-gpu
---

# madduri/singularity-freesurfer-gpu:latest

```bash
$ singularity pull shub://madduri/singularity-freesurfer-gpu:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04
%files
    license.txt
%post
    # Links
    GET_PIP=https://bootstrap.pypa.io/get-pip.py
    TESLA=http://us.download.nvidia.com/tesla/396.44/NVIDIA-Linux-x86_64-396.44.run
    CUDA5=http://developer.download.nvidia.com/compute/cuda/5_0/rel-update-1/installers/cuda_5.0.35_linux_64_ubuntu11.10-1.run
    CUDA8=https://developer.nvidia.com/compute/cuda/8.0/Prod2/local_installers/cuda_8.0.61_375.26_linux-run
    FREESURFER=ftp://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/6.0.0/freesurfer-Linux-centos6_x86_64-stable-pub-v6.0.0.tar.gz
    BEDPOSTX_GPU=http://users.fmrib.ox.ac.uk/~moisesf/Bedpostx_GPU/CUDA_8.0/bedpostx_gpu.zip
    mkdir /share
    apt-get -y update
    apt-get install -y apt-transport-https
    apt-get install -y software-properties-common
    add-apt-repository -y universe
    apt-get -y update
    apt-get -y install wget tcsh build-essential python3 python3-dev curl libtool unzip kmod initramfs-tools locales vim-tiny dkms
    locale-gen en_US.UTF-8
    rm /bin/sh
    ln -s /bin/bash /bin/sh
    # Python3 and Parsl
    curl -Ok $GET_PIP
    python3 get-pip.py
    python3 -m pip install parsl
    # Nvidia Drivers
    apt-get -y install linux-headers-`uname -r`
    echo "blacklist nouveau" >> /etc/modprobe.d/blacklist-nouveau.conf
    echo "options nouveau modeset=0" >> /etc/modprobe.d/blacklist-nouveau.conf
    update-initramfs -u
    TESLA_RUN=$(basename $TESLA)
    wget --no-check-certificate $TESLA
    sh $TESLA_RUN --dkms -s --no-drm
    # CUDA 5.0
    CUDA5_RUN=$(basename $CUDA5)
    wget --no-check-certificate $CUDA5
    sh $CUDA5_RUN -silent -override -toolkit
    # CUDA 8.0
    CUDA8_RUN=$(basename $CUDA8)
    wget --no-check-certificate $CUDA8
    sh $CUDA8_RUN -silent -override -toolkit
    # FSL
    gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv 9BDB3D89CE49EC21
    wget -O- http://neuro.debian.net/lists/xenial.us-nh.full | tee /etc/apt/sources.list.d/neurodebian.sources.list
    apt-key adv --recv-keys --keyserver hkp://pool.sks-keyservers.net:80 0xA5D32F012649A5A9
    apt-get -y update
    apt-get -y install fsl-5.0-complete
    # Bedpostx GPU
    BEDPOSTX_GPU_ZIP=$(basename $BEDPOSTX_GPU)
    wget --no-check-certificate $BEDPOSTX_GPU
    unzip -o -d /usr/share/fsl/5.0 $BEDPOSTX_GPU_ZIP
    cp /usr/share/fsl/5.0/bin/*.so /usr/share/fsl/5.0/lib/
    # Freesurfer
    FREESURFER_GZ=$(basename $FREESURFER)
    wget --no-check-certificate $FREESURFER
    tar -xzf $FREESURFER_GZ -C /opt
    # Fake License - should be replaced by a real one
    touch license.txt
    cp license.txt /opt/freesurfer/license.txt
    # Cleanup
    rm -rf get-pip.py
    rm -rf $TESLA_RUN
    rm -rf $CUDA5_RUN
    rm -rf $CUDA8_RUN
    rm -rf $FREESURFER_GZ
    rm -rf $BEDPOSTX_GPU_ZIP
    rm -rf /license.txt
    apt-get -y clean
%environment
    export FSLDIR=/usr/share/fsl/5.0
    FSL_DIR=$FSLDIR
    FSLOUTPUTTYPE=NIFTI_GZ
    FSLMULTIFILEQUIT=TRUE
    FSLTCLSH=${FSLDIR}/bin/fsltclsh
    FSLWISH=${FSLDIR}/bin/fslwish
    FSLGECUDAQ="cuda.q"
    FSL_BIN=${FSLDIR}/bin
    FS_OVERRIDE=0
    COMPILE_GPU=1
    export FSL_DIR FSLOUTPUTTYPE FSLMULTIFILEQUIT FSLTCLSH FSLWISH FSLGECUDAQ FSL_BIN FS_OVERRIDE COMPILE_GPU
    export FREESURFER_HOME=/opt/freesurfer
    LOCAL_DIR=${FREESURFER_HOME}/local
    PERL5LIB=${FREESURFER_HOME}/mni/share/perl5
    FSFAST_HOME=${FREESURFER_HOME}/fsfast
    FMRI_ANALYSIS_DIR=${FREESURFER_HOME}/fsfast
    FSF_OUTPUT_FORMAT="nii.gz"
    MNI_DIR=${FREESURFER_HOME}/mni
    MNI_DATAPATH=${FREESURFER_HOME}/mni/data
    MNI_PERL5LIB=${FREESURFER_HOME}/mni/share/perl5
    MINC_BIN_DIR=${FREESURFER_HOME}/mni/bin
    MINC_LIB_DIR=${FREESURFER_HOME}/mni/lib
    SUBJECTS_DIR=/share
    FUNCTIONALS_DIR=${FREESURFER_HOME}/sessions
    export LOCAL_DIR PERL5LIB FSFAST_HOME FMRI_ANALYSIS_DIR FSF_OUTPUT_FORMAT MNI_DIR MNI_DATAPATH MNI_PERL5LIB MINC_BIN_DIR MINC_LIB_DIR SUBJECTS_DIR FUNCTIONALS_DIR
    export CUDA_5_LIB_DIR=/usr/local/cuda-5.0/lib64
    export CUDA_8_LIB_DIR=/usr/local/cuda-8.0/lib64
    export PATH="${FREESURFER_HOME}/bin:${MNI_DIR}/bin:${FSLDIR}/bin:$PATH"
    export LD_LIBRARY_PATH="${FSLDIR}/lib:$LD_LIBRARY_PATH"
    export OS=LINUX
```

## Collection

 - Name: [madduri/singularity-freesurfer-gpu](https://github.com/madduri/singularity-freesurfer-gpu)
 - License: [Apache License 2.0](https://api.github.com/licenses/apache-2.0)

