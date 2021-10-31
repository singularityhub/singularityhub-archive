---
id: 6951
name: "connor-lab/singularity-recipes"
branch: "master"
tag: "assembly_improvement"
commit: "2583535411903625da9ca664dd7548537bbbc2da"
version: "3c17b81b554732cfa72077ece599fdbf"
build_date: "2019-02-07T15:45:22.882Z"
size_mb: 877
size: 193204255
sif: "https://datasets.datalad.org/shub/connor-lab/singularity-recipes/assembly_improvement/2019-02-07-25835354-3c17b81b/3c17b81b554732cfa72077ece599fdbf.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/connor-lab/singularity-recipes/assembly_improvement/2019-02-07-25835354-3c17b81b/
recipe: https://datasets.datalad.org/shub/connor-lab/singularity-recipes/assembly_improvement/2019-02-07-25835354-3c17b81b/Singularity
collection: connor-lab/singularity-recipes
---

# connor-lab/singularity-recipes:assembly_improvement

```bash
$ singularity pull shub://connor-lab/singularity-recipes:assembly_improvement
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: alpine:3.8

%environment
    PATH=$PATH:/usr/local/bin/MUMmer3.23
    export PATH

%post
    apk update
    apk upgrade
    apk add bash boost-dev cmake curl db-dev expat-dev g++ gcc gd-dev libxml2-dev make musl-dev perl-app-cpanminus perl-dev zlib-dev 

    curl -fsSL http://www.cpan.org/authors/id/M/MI/MIROD/XML-DOM-XPath-0.14.tar.gz | tar -xz
    cd XML-DOM-XPath-0.14
    #sed "s/use encoding 'utf8'/use utf8/g" t/test_non_ascii.t
    perl Makefile.PL && make && make install
    cd ..
    rm -rf XML-DOM-XPath-0.14

    cpanm --no-wget -f Bio::AssemblyImprovement 
    
    wget https://downloads.sourceforge.net/project/mummer/mummer/3.23/MUMmer3.23.tar.gz -O /usr/local/bin/MUMmer3.23.tar.gz
    cd /usr/local/bin && tar xvzf MUMmer3.23.tar.gz
    cd MUMmer3.23 && make && make install 

    export PATH=$PATH:/usr/local/bin/MUMmer3.23

    cd /tmp/
    curl -fsSL https://www.cs.helsinki.fi/u/lmsalmel/Gap2Seq/Gap2Seq-2.1.tar.gz | tar xz
    cd Gap2Seq-2.1/ 
    mkdir build; cd build; cmake ..; make
    find . -maxdepth 1 -perm /u=x -exec mv {} /usr/local/bin/ \;
    chmod 775 /usr/local/bin/Gap2Seq.sh
    rm -rf /tmp/Gap2Seq-2.1
```

## Collection

 - Name: [connor-lab/singularity-recipes](https://github.com/connor-lab/singularity-recipes)
 - License: None

