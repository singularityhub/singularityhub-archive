---
id: 2621
name: "eilon-s/sherlock_pVACseq"
branch: "master"
tag: "latest"
commit: "fb18fb0a1886a512f8ab80da2977817552bf7dc2"
version: "6a107cee2d349d9a0cca67f85d27072b"
build_date: "2018-05-10T15:50:08.171Z"
size_mb: None
size: 1624825887
sif: "https://datasets.datalad.org/shub/eilon-s/sherlock_pVACseq/latest/2018-05-10-fb18fb0a-6a107cee/6a107cee2d349d9a0cca67f85d27072b.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/eilon-s/sherlock_pVACseq/latest/2018-05-10-fb18fb0a-6a107cee/
recipe: https://datasets.datalad.org/shub/eilon-s/sherlock_pVACseq/latest/2018-05-10-fb18fb0a-6a107cee/Singularity
collection: eilon-s/sherlock_pVACseq
---

# eilon-s/sherlock_pVACseq:latest

```bash
$ singularity pull shub://eilon-s/sherlock_pVACseq:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: eilons/pvacseq-docker

%help
  This is a singularity file for running pVACtools with local installation of IEDB predictors.
  
%environment
    LANGUAGE=en_US
    LANG="en_US.UTF-8"
    LC_ALL=C
    PERL_MM_USE_DEFAULT=1
    export LANGUAGE LANG LC_ALL PERL_MM_USE_DEFAUL

%post
  # install mhc_i predictors  
  wget http://downloads.iedb.org/tools/mhci/LATEST-PACKAGE;
  mv LATEST-PACKAGE latest_mhc_i.tar.gz;
  tar -xzf latest_mhc_i.tar.gz;
  
  # setting to python2
  cd mhc_i;
  find . -type f -exec perl -pi -e 's/\/bin\/env python/\/bin\/python2.7/' {} \;
  find . -type f -exec perl -pi -e 's/\/bin\/python$/\/bin\/python2.7/' {} \;
  ./configure;
  cd ..;
  
  #installing mhc_ii
  wget http://downloads.iedb.org/tools/mhcii/LATEST-PACKAGE;
  mv LATEST-PACKAGE latest_mhc_ii.tar.gz;
  tar -xzf latest_mhc_ii.tar.gz;
  
  # setting to python2
  cd mhc_ii;
  find . -type f -exec perl -pi -e 's/\/bin\/env python/\/bin\/python2.7/' {} \; ;
  find . -type f -exec perl -pi -e 's/\/bin\/python$/\/bin\/python2.7/' {} \; ;
  sed -i -- 's/python /python2 /g' mhc_II_binding.py;
  sed -i -- 's/python /python2 /g' configure.py;
  cd ..;
  
  # downloading test data
  #pip install --upgrade pip;
  #pip install pvactools;
  #pvacseq download_example_data .;

%runscript
  exec pvacseq "$@"


# old code to document the versions that were used
  #wget http://downloads.iedb.org/tools/mhci/LATEST/IEDB_MHC_I-2.17.tar.gz;
  #wget http://downloads.iedb.org/tools/mhci/LATEST/IEDB_MHC_I-2.19.tar.gz;
  #tar -xzf IEDB_MHC_I-2.19.tar.gz;
  
  #wget http://downloads.iedb.org/tools/mhcii/LATEST/IEDB_MHC_II-2.17.3.tar.gz;
  #wget http://downloads.iedb.org/tools/mhcii/LATEST/IEDB_MHC_II-2.17.5.tar.gz;
  #tar -xzf IEDB_MHC_II-2.17.5.tar.gz;
  
    
  # fixing IEDB???
  #sed -i -- 's/.replace("\/"\,"-")//g' mhc_II_binding.py
```

## Collection

 - Name: [eilon-s/sherlock_pVACseq](https://github.com/eilon-s/sherlock_pVACseq)
 - License: None

