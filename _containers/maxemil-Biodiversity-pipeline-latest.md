---
id: 1267
name: "maxemil/Biodiversity-pipeline"
branch: "master"
tag: "latest"
commit: "8dc5f10809cfd12dc30b904d0e81f5abf36d9616"
version: "dd9060cbeabadf2ac7917b3cffd47338"
build_date: "2020-03-27T12:15:22.763Z"
size_mb: 5695
size: 3474735135
sif: "https://datasets.datalad.org/shub/maxemil/Biodiversity-pipeline/latest/2020-03-27-8dc5f108-dd9060cb/dd9060cbeabadf2ac7917b3cffd47338.simg"
url: https://datasets.datalad.org/shub/maxemil/Biodiversity-pipeline/latest/2020-03-27-8dc5f108-dd9060cb/
recipe: https://datasets.datalad.org/shub/maxemil/Biodiversity-pipeline/latest/2020-03-27-8dc5f108-dd9060cb/Singularity
collection: maxemil/Biodiversity-pipeline
---

# maxemil/Biodiversity-pipeline:latest

```bash
$ singularity pull shub://maxemil/Biodiversity-pipeline:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: finalduty/archlinux:daily

%post

######## base system ########
echo "Server = http://mirror.de.leaseweb.net/archlinux/\$repo/os/\$arch" >> /etc/pacman.d/mirrorlist
echo "[lambdait]" >> /etc/pacman.conf
echo "SigLevel = Never" >> /etc/pacman.conf
echo "Server = https://lambda.informatik.uni-tuebingen.de/repo/mypkgs/" >> /etc/pacman.conf

pacman -Syu --noconfirm
pacman -S --noconfirm base-devel \
                      jdk \
                      git \
                      wget \
                      expect \
                      tk \
                      xorg-server-xvfb \
                      libxtst \
                      gcc-fortran \
                      r \
                      python3 \
                      python-pip \
                      python2

######## MEGAN6 ########
cd /usr/local/

wget http://ab.inf.uni-tuebingen.de/data/software/megan6/download/MEGAN_Community_unix_6_8_12.sh
chmod +x MEGAN_Community_unix_6_8_12.sh
./MEGAN_Community_unix_6_8_12.sh -q

cd megan
wget http://ab.inf.uni-tuebingen.de/data/software/megan6/download/nucl_acc2tax-May2017.abin.zip
unzip nucl_acc2tax-May2017.abin.zip
cd ..

######## MALT ########
wget http://ab.inf.uni-tuebingen.de/data/software/malt/download/MALT_unix_0_3_9.sh
chmod +x MALT_unix_0_3_9.sh
./MALT_unix_0_3_9.sh -q


######## python ########
pip install biopython pandas numpy requests scipy ete3

######## FUNGuild ########
cd /usr/local
git clone https://github.com/UMNFuN/FUNGuild.git
ln /usr/local/FUNGuild/Guilds_v1.1.py /usr/local/bin/


######## Vsearch ########
wget https://github.com/torognes/vsearch/archive/v2.4.3.tar.gz
tar xzf v2.4.3.tar.gz
cd vsearch-2.4.3
./autogen.sh
./configure
make
make install

######## R ########
wget https://cran.r-project.org/src/contrib/picante_1.6-2.tar.gz
wget https://cran.r-project.org/src/contrib/vegan_2.4-5.tar.gz
wget https://cran.r-project.org/src/contrib/permute_0.9-4.tar.gz
wget https://cran.r-project.org/src/contrib/ape_5.0.tar.gz
wget https://cran.r-project.org/src/contrib/futile.logger_1.4.3.tar.gz
wget https://cran.r-project.org/src/contrib/futile.options_1.0.0.tar.gz
wget https://cran.r-project.org/src/contrib/lambda.r_1.2.tar.gz
wget https://cran.r-project.org/src/contrib/VennDiagram_1.6.18.tar.gz
wget https://cran.r-project.org/src/contrib/Rcpp_0.12.14.tar.gz

R CMD INSTALL permute_0.9-4.tar.gz \
              Rcpp_0.12.14.tar.gz \
              ape_5.0.tar.gz \
              vegan_2.4-5.tar.gz \
              picante_1.6-2.tar.gz \
              lambda.r_1.2.tar.gz \
              futile.options_1.0.0.tar.gz \
              futile.logger_1.4.3.tar.gz \
              VennDiagram_1.6.18.tar.gz


%files
binaries/spaced /usr/local/bin/spaced


%test
/usr/local/malt/malt-build -h
/usr/local/malt/malt-run -h
/usr/local/megan/tools/rma2info -h
vsearch --version
python3 /usr/local/bin/Guilds_v1.1.py -h


%labels
Maintainer	max-emil.schon@icm.uu.se
```

## Collection

 - Name: [maxemil/Biodiversity-pipeline](https://github.com/maxemil/Biodiversity-pipeline)
 - License: [MIT License](https://api.github.com/licenses/mit)

