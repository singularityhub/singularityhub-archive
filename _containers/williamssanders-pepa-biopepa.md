---
id: 7206
name: "williamssanders/pepa"
branch: "master"
tag: "biopepa"
commit: "fe1f07628ebfcab3dafb8833109f6063bbe11722"
version: "45bce1f6c76ac2011bb06daab90c40e3"
build_date: "2019-02-14T08:45:05.107Z"
size_mb: 928
size: 544141343
sif: "https://datasets.datalad.org/shub/williamssanders/pepa/biopepa/2019-02-14-fe1f0762-45bce1f6/45bce1f6c76ac2011bb06daab90c40e3.simg"
url: https://datasets.datalad.org/shub/williamssanders/pepa/biopepa/2019-02-14-fe1f0762-45bce1f6/
recipe: https://datasets.datalad.org/shub/williamssanders/pepa/biopepa/2019-02-14-fe1f0762-45bce1f6/Singularity
collection: williamssanders/pepa
---

# williamssanders/pepa:biopepa

```bash
$ singularity pull shub://williamssanders/pepa:biopepa
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:centos:6

%labels
	MAINTAINER Shane Sanders
	
%files
	# Files for Build Go Here

%post
	echo "Updating system"
	yum update -y
	echo "Installing xauth and xterm"
	yum install -y xauth xterm wget unzip libXtst.x86_64 mesa-libGL.x86_64
	echo "Installing OPEN JDK 8 JRE (java-1.8.0-openjdk)"
	yum install -y java-1.8.0-openjdk
	echo "Installing GTK"
	yum install -y gtk2 libcanberra-gtk2 PackageKit-gtk-module
	cd /opt
	wget https://archive.eclipse.org/technology/epp/downloads/release/mars/2/eclipse-jee-mars-2-linux-gtk-x86_64.tar.gz
	tar xvfz eclipse-jee-mars-2-linux-gtk-x86_64.tar.gz -C /opt/
	ln -s /opt/eclipse/eclipse /usr/local/bin/eclipse
	rm eclipse-jee-mars-2-linux-gtk-x86_64.tar.gz
	# Installing PEPA || BioPEPA
	eclipse -clean -purgeHistory -noSplash -application org.eclipse.equinox.p2.director -repository https://download.eclipse.org/releases/mars/ -installIU org.eclipse.birt.feature.group/
	eclipse -clean -purgeHistory -noSplash -application org.eclipse.equinox.p2.director -repository http://www.dcs.ed.ac.uk/pepa/group/update-site -installIU uk.ac.ed.inf.common.feature.feature.group
	eclipse -clean -purgeHistory -noSplash -application org.eclipse.equinox.p2.director -repository https://download.eclipse.org/releases/mars/ -installIU org.eclipse.zest.core/
	#eclipse -clean -purgeHistory -noSplash -application org.eclipse.equinox.p2.director -repository http://www.dcs.ed.ac.uk/pepa/group/update-site -installIU uk.ac.ed.inf.pepa.feature.feature.group
	eclipse -clean -purgeHistory -noSplash -application org.eclipse.equinox.p2.director -repository http://www.dcs.ed.ac.uk/pepa/group/update-site -installIU uk.ac.ed.inf.biopepa.feature.group

%runscript
	#java -version
/opt/eclipse/eclipse
```

## Collection

 - Name: [williamssanders/pepa](https://github.com/williamssanders/pepa)
 - License: None

