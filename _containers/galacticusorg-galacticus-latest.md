---
id: 12731
name: "galacticusorg/galacticus"
branch: "master"
tag: "latest"
commit: "7aadaa9567adfd8f40983a6527e207f28548f492"
version: "c41f85057ce529aebbc2a3fe8706e3df"
build_date: "2021-03-26T17:41:36.062Z"
size_mb: 5451.0
size: 2843136031
sif: "https://datasets.datalad.org/shub/galacticusorg/galacticus/latest/2021-03-26-7aadaa95-c41f8505/c41f85057ce529aebbc2a3fe8706e3df.sif"
url: https://datasets.datalad.org/shub/galacticusorg/galacticus/latest/2021-03-26-7aadaa95-c41f8505/
recipe: https://datasets.datalad.org/shub/galacticusorg/galacticus/latest/2021-03-26-7aadaa95-c41f8505/Singularity
collection: galacticusorg/galacticus
---

# galacticusorg/galacticus:latest

```bash
$ singularity pull shub://galacticusorg/galacticus:latest
```

## Singularity Recipe

```singularity
# Galacticus Singularity image
# Uses SingularityHub to build Galacticus.
# Version: 2021-03-26

Bootstrap:docker
From:galacticusorg/galacticus:latest

%environment
	export INSTALL_PATH=/usr/local
	export PATH=$INSTALL_PATH/gcc-11/bin:$INSTALL_PATH/bin:$PATH
	export LD_LIBRARY_PATH=$INSTALL_PATH/lib64:$INSTALL_PATH/lib:$INSTALL_PATH/gcc-11/lib64:$INSTALL_PATH/gcc-11/lib:/usr/lib/x86_64-linux-gnu
	export LIBRARY_PATH=/usr/lib/x86_64-linux-gnu
	export GALACTICUS_FCFLAGS="-fintrinsic-modules-path $INSTALL_PATH/finclude -fintrinsic-modules-path $INSTALL_PATH/include -fintrinsic-modules-path $INSTALL_PATH/include/gfortran -fintrinsic-modules-path $INSTALL_PATH/lib/gfortran/modules -L$INSTALL_PATH/lib -L$INSTALL_PATH/lib64 -fuse-ld=bfd"
	export GALACTICUS_CFLAGS="-fuse-ld=bfd"
	export GALACTICUS_CPPFLAGS="-fuse-ld=bfd"
	export GALACTICUS_EXEC_PATH=/opt/galacticus
	export GALACTICUS_DATA_PATH=/opt/datasets

%runscript
	echo "Building Galacticus container..."

%post
	echo Begin begin: `date`
        export INSTALL_PATH=/usr/local
	export PATH=$INSTALL_PATH/gcc-11/bin:$INSTALL_PATH/bin:$PATH
	export LD_LIBRARY_PATH=$INSTALL_PATH/lib64:$INSTALL_PATH/lib:$INSTALL_PATH/gcc-11/lib64:$INSTALL_PATH/gcc-11/lib:/usr/lib/x86_64-linux-gnu
	export LIBRARY_PATH=/usr/lib/x86_64-linux-gnu
	export GALACTICUS_FCFLAGS="-fintrinsic-modules-path $INSTALL_PATH/finclude -fintrinsic-modules-path $INSTALL_PATH/include -fintrinsic-modules-path $INSTALL_PATH/include/gfortran -fintrinsic-modules-path $INSTALL_PATH/lib/gfortran/modules -L$INSTALL_PATH/lib -L$INSTALL_PATH/lib64 -fuse-ld=bfd"
	export GALACTICUS_CFLAGS="-fuse-ld=bfd"
	export GALACTICUS_CPPFLAGS="-fuse-ld=bfd"
	export GALACTICUS_EXEC_PATH=/opt/galacticus
	export GALACTICUS_DATA_PATH=/opt/datasets
```

## Collection

 - Name: [galacticusorg/galacticus](https://github.com/galacticusorg/galacticus)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

