---
id: 15245
name: "draguar/vip_simulators"
branch: "sofidone"
tag: "0.10.0"
commit: "3480789039812e58ce7b6d7b53a4ebbd9827a897"
version: "8c2678caa1999d35242a4aa4591d62a6d3370445729d8b3f262ac0f7ad075042"
build_date: "2021-01-05T09:42:14.470Z"
size_mb: 2022.78515625
size: 2121043968
sif: "https://datasets.datalad.org/shub/draguar/vip_simulators/0.10.0/2021-01-05-34807890-8c2678ca/8c2678caa1999d35242a4aa4591d62a6d3370445729d8b3f262ac0f7ad075042.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/draguar/vip_simulators/0.10.0/2021-01-05-34807890-8c2678ca/
recipe: https://datasets.datalad.org/shub/draguar/vip_simulators/0.10.0/2021-01-05-34807890-8c2678ca/Singularity
collection: draguar/vip_simulators
---

# draguar/vip_simulators:0.10.0

```bash
$ singularity pull shub://draguar/vip_simulators:0.10.0
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:fedora:29

%help
  Container for running microscopy simulation software on VI (creatis.insalyon.fr/vip)

%setup

%files
  chain_chrom/chain_chrom_standalone /opt/chain_chrom/
  chain_chrom/run_chain_chrom_standalone.sh /opt/chain_chrom/
  model_PSF/model_PSF_standalone /opt/model_PSF/
  model_PSF/run_model_PSF_standalone.sh /opt/model_PSF/
  simulation3D/Simulation3D_standalone /opt/simulation3D/
  simulation3D/run_Simulation3D_standalone.sh /opt/simulation3D/
  micro_img_simulation/micro_img_simulation_standalone /opt/micro_img_simulation/
  micro_img_simulation/run_micro_img_simulation_standalone.sh /opt/micro_img_simulation/
  Brightfield_pap_smear/Brightfield_pap_smear /opt/Brightfield_pap_smear/
  Brightfield_pap_smear/run_Brightfield_pap_smear.sh /opt/Brightfield_pap_smear/
  SIMCEP/SIMCEP_standalone /opt/SIMCEP/
  SIMCEP/run_SIMCEP_standalone.sh /opt/SIMCEP/
  MicroVIP/read_ini.sh /opt/MicroVIP/
  SOFI/SOFI_standalone /opt/micro_img_simulation/

%labels
  Maintainer VanelGuillaume
  Version v1.0

%environment
  MCRROOT=/usr/local/MATLAB/MATLAB_Runtime/v95
  # Last entry adds dipimage libraries
  LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$MCRROOT/runtime/glnxa64:$MCRROOT/bin/glnxa64:$MCRROOT/sys/os/glnxa64:$MCRROOT/sys/java/jre/glnxa64/jre/lib/amd64/native_threads:$MCRROOT/sys/java/jre/glnxa64/jre/lib/amd64/server:$MCRROOT/sys/java/jre/glnxa64/jre/lib/amd64:$MCRROOT/sys/opengl/lib/glnxa64:/opt/dip/Linuxa64/lib
  XAPPLRESDIR=$MCRROOT/X11/app-defaults
  MCR_CACHE_VERBOSE=true
  export MCRROOT LD_LIBRARY_PATH XAPPLRESDIR MCR_CACHE_VERBOSE
  
%post
  echo "Installing dependencies"
  dnf install wget unzip libXext libXt-devel libXmu findutils crudini bzip2 which \
   libstdc++-static gcc -y
  echo "Installing dipimage"
  cd /opt && wget -nv ftp://qiftp.tudelft.nl/DIPimage/2.9/dipimage_2.9_lin64.tbz && \
   tar -xf  dipimage_2.9_lin64.tbz && rm dipimage_2.9_lin64.tbz && \
   rm /opt/dip/Linuxa64/lib/libpthread.so.0
  echo "Installing MCR"
  ulimit -n 10000 && mkdir /mcr-install && cd /mcr-install && \
   wget -nv https://ssd.mathworks.com/supportfiles/downloads/R2018b/deployment_files/R2018b/installers/glnxa64/MCR_R2018b_glnxa64_installer.zip && \
   unzip MCR_R2018b_glnxa64_installer.zip && \
   ./install -mode silent -agreeToLicense yes
  rm -Rf /mcr-install
  MCRROOT=/usr/local/MATLAB/MATLAB_Runtime/v95
  # Last entry adds dipimage libraries
  LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$MCRROOT/runtime/glnxa64:$MCRROOT/bin/glnxa64:$MCRROOT/sys/os/glnxa64:$MCRROOT/sys/java/jre/glnxa64/jre/lib/amd64/native_threads:$MCRROOT/sys/java/jre/glnxa64/jre/lib/amd64/server:$MCRROOT/sys/java/jre/glnxa64/jre/lib/amd64:$MCRROOT/sys/opengl/lib/glnxa64:/opt/dip/Linuxa64/lib
  echo "export MCRROOT=$MCRROOT LD_LIBRARY_PATH=$LD_LIBRARY_PATH" >> $SINGULARITY_ENVIRONMENT
  #mkdir /opt/chain_chrom && mkdir /opt/model_PSF && mkdir /opt/simulation3D && 
  mkdir $MCRROOT/bin/glnxa64/old && \
   mv $MCRROOT/bin/glnxa64/libmwcoder_types.so $MCRROOT/bin/glnxa64/old/
   ldconfig
   
%runscript

%test
```

## Collection

 - Name: [draguar/vip_simulators](https://github.com/draguar/vip_simulators)
 - License: None

