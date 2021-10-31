---
id: 5379
name: "oliviermattelaer/singularity-recipe"
branch: "master"
tag: "cowsay"
commit: "a9c6e9777ede248f6447ec8e3f3ecc2dd6316f7e"
version: "6e1a5e8b4a4049925f50f60fb0067255"
build_date: "2018-10-30T15:18:48.362Z"
size_mb: 353
size: 152510495
sif: "https://datasets.datalad.org/shub/oliviermattelaer/singularity-recipe/cowsay/2018-10-30-a9c6e977-6e1a5e8b/6e1a5e8b4a4049925f50f60fb0067255.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/oliviermattelaer/singularity-recipe/cowsay/2018-10-30-a9c6e977-6e1a5e8b/
recipe: https://datasets.datalad.org/shub/oliviermattelaer/singularity-recipe/cowsay/2018-10-30-a9c6e977-6e1a5e8b/Singularity
collection: oliviermattelaer/singularity-recipe
---

# oliviermattelaer/singularity-recipe:cowsay

```bash
$ singularity pull shub://oliviermattelaer/singularity-recipe:cowsay
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: stable
MirrorURL: http://ftp.us.debian.org/debian/

%runscript
    echo "This is what happens when you run the container..."
    infile=
    outfile=

    usage() {
      >&2 echo "Usage:"
      >&2 echo "$SINGULARITY_NAME -i <infile> -o <outfile> [ -- <cowsay options> ]"
      exit 1
    }

    while getopts i:o: argument
    do
    case $argument in
        i)
          infile="$OPTARG"
	  ;;
	  o)
	  outfile="$OPTARG"
	  ;;
	  ?)
	  usage
	  ;;
    esac
    done

    shift "$((OPTIND - 1))"

    if [ -z "$infile" ] || [ -z "$outfile" ]
        then
	usage
    fi

    cat "$infile" | cowsay "$@" > "$outfile"


%post
    echo "Hello from inside the container"
    apt-get update
    apt-get -y install fortune cowsay lolcat
    #	        apt-get clean

%labels
   author Olivier Mattelaer

%environment
    export PATH=$PATH:/usr/games
    export LC_ALL=C
```

## Collection

 - Name: [oliviermattelaer/singularity-recipe](https://github.com/oliviermattelaer/singularity-recipe)
 - License: None

