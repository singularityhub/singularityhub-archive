---
id: 15041
name: "harvard-nrg/anatqc"
branch: "main"
tag: "latest"
commit: "a0ae7be0ea094157c621b5980422d079b489f7fb"
version: "af2bf34472256fd47855c3019604e2ff"
build_date: "2021-01-11T22:56:18.693Z"
size_mb: 20506.0
size: 8453095455
sif: "https://datasets.datalad.org/shub/harvard-nrg/anatqc/latest/2021-01-11-a0ae7be0-af2bf344/af2bf34472256fd47855c3019604e2ff.sif"
url: https://datasets.datalad.org/shub/harvard-nrg/anatqc/latest/2021-01-11-a0ae7be0-af2bf344/
recipe: https://datasets.datalad.org/shub/harvard-nrg/anatqc/latest/2021-01-11-a0ae7be0-af2bf344/Singularity
collection: harvard-nrg/anatqc
---

# harvard-nrg/anatqc:latest

```bash
$ singularity pull shub://harvard-nrg/anatqc:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:8

%post
  # python, git, vim
  dnf install -y python3 python3-devel git vim
  alternatives --set python /usr/bin/python3
  pip3 install pipenv

%appinstall freesurfer
  mkdir -p /sw/apps/freesurfer/
  URI="https://www.dropbox.com/s/bzpqywglrhommfw/freesurfer-Linux-centos6_x86_64-stable-pub-v6.0.1.tar.gz?dl=0"
  curl -L -s "${URI}" | tar -C "/sw/apps/freesurfer" -xzf - \
    --strip-components=1 \
    --exclude="freesurfer/diffusion" \
    --exclude="freesurfer/docs" \
    --exclude="freesurfer/fsfast" \
    --exclude="freesurfer/lib/cuda" \
    --exclude="freesurfer/matlab" \
    --exclude="freesurfer/mni/share/man" \
    --exclude="freesurfer/subjects/fsaverage_sym" \
    --exclude="freesurfer/subjects/fsaverage3" \
    --exclude="freesurfer/subjects/fsaverage4" \
    --exclude="freesurfer/subjects/cvs_avg35" \
    --exclude="freesurfer/subjects/cvs_avg35_inMNI152" \
    --exclude="freesurfer/subjects/bert" \
    --exclude="freesurfer/subjects/lh.EC_average" \
    --exclude="freesurfer/subjects/rh.EC_average" \
    --exclude="freesurfer/subjects/sample-*.mgz" \
    --exclude="freesurfer/subjects/V1_average" \
    --exclude="freesurfer/trctrain"
 
  dnf install -y tcsh libgomp bc mesa-libGLU libXmu
  dnf install -y epel-release
  dnf install -y libpng12 perl perl-core ImageMagick glx-utils \
                 mesa-libGL mesa-libGLU-devel mesa-libGL-devel \
                 mesa-dri-drivers libXmu libXmu-devel libX11 \
                 libX11-devel libXt-devel xorg-x11-server-Xorg \
                 xorg-x11-server-Xvfb mesa-libxatracker xorg-x11-drivers \
                 xorg-x11-drv-vmware libXScrnSaver dbus GConf2

%appinstall mriqc
  dnf groupinstall -y "Development Tools"
  dnf install -y xorg-x11-server-Xvfb 
  MRIQCDIR="/sw/apps/mriqc"
  mkdir -p "${MRIQCDIR}" && cd "${MRIQCDIR}"
  export PIPENV_VENV_IN_PROJECT=1
  pipenv install --skip-lock \
    "dipy" \
    "jinja2" \
    "matplotlib==2.2.2" \
    "nibabel>=3.0.1,<4.0" \
    "nilearn>=0.2.6,!= 0.5.0,!= 0.5.1" \
    "nipype~=1.4" \
    "nitime" \
    "niworkflows==1.1.12" \
    "numpy==1.15.4" \
    "pandas==0.23.4" \
    "pybids>=0.10.2" \
    "PyYAML" \
    "scikit-learn==0.19.1" \
    "scipy==1.1.0" \
    "seaborn" \
    "statsmodels" \
    "svgutils==0.3.1" \
    "templateflow>=0.5.2" \
    "toml" \
    "xvfbwrapper"
  pipenv install --skip-lock "mriqc==0.15.2"

  # change matplotlib backend to Agg
  MATPLOTLIBRC=$(pipenv run python -c "import matplotlib; print(matplotlib.matplotlib_fname())")
  sed -i 's/\(backend *: \).*$/\1Agg/g' "${MATPLOTLIBRC}" 

  # https://github.com/poldracklab/mriqc/issues/844
  FILE="/sw/apps/mriqc/.venv/lib/python3.6/site-packages/mriqc/cli/parser.py"
  patch "${FILE}" << EOF
  --- parser.py 2020-08-19 11:22:45.427986762 -0400
  +++ parser.py 2020-08-20 10:52:27.888967260 -0400
  @@ -392,7 +392,7 @@
           config.loggers.cli.warning(
               "Per-process threads (--omp-nthreads=%d) exceed total "
               "threads (--nthreads/--n_cpus=%d)",
  -            config.nipype.omp_nthread,
  +            config.nipype.omp_nthreads,
               config.nipype.nprocs,
           )
EOF

%appinstall fsl
  dnf install -y libquadmath
  mkdir -p /sw/apps/fsl/
  URI="https://www.dropbox.com/s/p8go1t8kcoe41pz/fsl-6.0.4-centos7_64.tar.gz"
  curl -L -s "${URI}" | tar -C "/sw/apps/fsl" -xzf - \
    --strip-components=1

%appinstall afni
  dnf install -y epel-release
  dnf install -y curl tcsh python2-devel libpng15 motif
  AFNIDIR="/sw/apps/afni"
  mkdir -p "${AFNIDIR}" && cd "${AFNIDIR}"
  curl -O "https://afni.nimh.nih.gov/pub/dist/bin/misc/@update.afni.binaries"
  tcsh @update.afni.binaries -package linux_centos_7_64 -do_extras -bindir "${AFNIDIR}"

%appinstall ants
  dnf install -y libGLw libGLU gsl
  ln -s /usr/lib64/libgsl.so.23 /usr/lib64/libgsl.so.0
  ANTSPATH="/sw/apps/ants"
  mkdir -p "${ANTSPATH}" && cd "${ANTSPATH}"
  TARBALL="https://dl.dropbox.com/s/2f4sui1z6lcgyek/ANTs-Linux-centos5_x86_64-v2.2.0-0740f91.tar.gz"
  curl -sSL "${TARBALL}" \
    | tar -xzC "${ANTSPATH}" --strip-components 1

%appinstall dcm2niix
  D2NPATH="/sw/apps/dcm2niix"
  mkdir -p "${D2NPATH}" && cd "${D2NPATH}"
  dnf install -y unzip
  ZIPFILE="https://github.com/rordenlab/dcm2niix/releases/download/v1.0.20200331/dcm2niix_lnx.zip"
  curl -sL "${ZIPFILE}" -o "/tmp/dcm2niix_lnx.zip"
  unzip "/tmp/dcm2niix_lnx.zip"
  rm "/tmp/dcm2niix_lnx.zip"

%appinstall anatqc
  dnf install -y compat-openssl10
  AQCPATH="/sw/apps/anatqc"
  mkdir -p "${AQCPATH}" && cd "${AQCPATH}"
  export PIPENV_VENV_IN_PROJECT=1
  pipenv install anatqc
 
%environment
  # freesurfer
  export OS="Linux"
  export FS_OVERRIDE=0
  export FIX_VERTEX_AREA=""
  export FSF_OUTPUT_FORMAT="nii.gz"
  export FREESURFER_HOME="/sw/apps/freesurfer"
  export SUBJECTS_DIR="${FREESURFER_HOME}/subjects"
  export FUNCTIONALS_DIR="${FREESURFER_HOME}/sessions"
  export MNI_DIR="${FREESURFER_HOME}/mni"
  export LOCAL_DIR="${FREESURFER_HOME}/local"
  export MINC_BIN_DIR="${FREESURFER_HOME}/mni/bin"
  export MINC_LIB_DIR="${FREESURFER_HOME}/mni/lib"
  export MNI_DATAPATH="${FREESURFER_HOME}/mni/data"
  export PERL5LIB="${MINC_LIB_DIR}/perl5/5.8.5"
  export MNI_PERL5LIB="${MINC_LIB_DIR}/perl5/5.8.5"
  export PATH="${FREESURFER_HOME}/bin:${FSFAST_HOME}/bin:${FREESURFER_HOME}/tktools:${MINC_BIN_DIR}:${PATH}"

  # fsl
  export FSLDIR="/sw/apps/fsl"
  export FSLGECUDAQ="cuda.q"
  export FSLMULTIFILEQUIT="TRUE"
  export FSLOUTPUTTYPE="NIFTI_GZ"
  export FSLWISH="${FSLDIR}/bin/fslwish"
  export FSLTCLSH="${FSLDIR}/bin/fsltclsh"
  export FSLMACHINELIST=
  export FSLREMOTECALL=
  export FSLLOCKDIR=
  export PATH="${FSLDIR}/bin:${PATH}"

  # afni
  export PATH="/sw/apps/afni:${PATH}"

  # ants
  export PATH="/sw/apps/ants:${PATH}"

  # dcm2niix
  export PATH="/sw/apps/dcm2niix:${PATH}"

%apprun mriqc
  cd /sw/apps/mriqc
  exec pipenv run mriqc "$@"

%apprun morphometry
  cd /sw/apps/anatqc
  exec pipenv run surpher.py "$@"

%apprun vnav
  cd /sw/apps/anatqc
  exec pipenv run parse_vNav_Motion_MH.py "$@"

%apprun anatqc
  cd /sw/apps/anatqc
  exec pipenv run anatQC.py "$@"
```

## Collection

 - Name: [harvard-nrg/anatqc](https://github.com/harvard-nrg/anatqc)
 - License: None

