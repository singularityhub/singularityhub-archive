---
id: 6311
name: "Michael-Stevens-27/silverblaze"
branch: "master"
tag: "latest"
commit: "67bd33badb85f935fbb5abb539ac99ec33b597b0"
version: "368fb6f0e19bcd337080d415c03bda03"
build_date: "2019-06-10T17:24:17.393Z"
size_mb: 2010
size: 871047199
sif: "https://datasets.datalad.org/shub/Michael-Stevens-27/silverblaze/latest/2019-06-10-67bd33ba-368fb6f0/368fb6f0e19bcd337080d415c03bda03.simg"
url: https://datasets.datalad.org/shub/Michael-Stevens-27/silverblaze/latest/2019-06-10-67bd33ba-368fb6f0/
recipe: https://datasets.datalad.org/shub/Michael-Stevens-27/silverblaze/latest/2019-06-10-67bd33ba-368fb6f0/Singularity
collection: Michael-Stevens-27/silverblaze
---

# Michael-Stevens-27/silverblaze:latest

```bash
$ singularity pull shub://Michael-Stevens-27/silverblaze:latest
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSversion: xenial
MirrorURL: http://archive.ubuntu.com/ubuntu/


%post
        mkdir /data
        apt-get update
        ## Add more repos
        apt-get install -y software-properties-common
        ## Add universe
        add-apt-repository universe

        apt-get update
        apt-get install -y vim git wget tar unzip sharutils sudo curl
        apt-get install -y libxml2-dev freeglut3-dev libgeos-dev libcurl4-openssl-dev libssl-dev libssh2-1-dev libfftw3-dev libfftw3-doc apt-transport-https libpng-dev
        add-apt-repository 'deb [arch=amd64,i386] https://cran.rstudio.com/bin/linux/ubuntu xenial/'
        apt-get update
        apt-get install -y --allow-unauthenticated r-base
	
	# download repo for GDAL
	add-apt-repository -y ppa:ubuntugis/ppa
	apt-get update
	apt-get install -y gdal-bin libproj-dev libgdal-dev

	# set locale
	locale-gen en_GB.UTF-8

        # R PACKAGES
        R --vanilla <<END
	Sys.setlocale("LC_ALL", "en_GB.UTF-8")
	        
	# CRAN packages
        Sys.setenv("PKG_CXXFLAGS"="-std=c++11")

        install.packages("geosphere", repos='http://cran.us.r-project.org')
        install.packages("scales", repos='http://cran.us.r-project.org')
        install.packages("jpeg", repos='http://cran.us.r-project.org')
        install.packages("proto", repos='http://cran.us.r-project.org')
        install.packages("rjson", repos='http://cran.us.r-project.org')
        install.packages("devtools", repos='http://cran.us.r-project.org')
	install.packages("rgdal", repos='http://cran.us.r-project.org')
	install.packages("RgoogleMaps", repos='http://cran.us.r-project.org')

        library(devtools)  
	install_github("dkahle/ggmap")
        install_github("bobverity/Rgeoprofile")
	install_github("michael-stevens-27/silverblaze")
```

## Collection

 - Name: [Michael-Stevens-27/silverblaze](https://github.com/Michael-Stevens-27/silverblaze)
 - License: [MIT License](https://api.github.com/licenses/mit)

