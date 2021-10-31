---
id: 7887
name: "williamssanders/sdaps"
branch: "master"
tag: "sdaps"
commit: "aee9ab3c0549ecb4c7357959d28c39be7612e8a2"
version: "4976b92df073007b21d06b061b8b30ea"
build_date: "2019-03-21T21:17:42.683Z"
size_mb: 1427
size: 521412639
sif: "https://datasets.datalad.org/shub/williamssanders/sdaps/sdaps/2019-03-21-aee9ab3c-4976b92d/4976b92df073007b21d06b061b8b30ea.simg"
url: https://datasets.datalad.org/shub/williamssanders/sdaps/sdaps/2019-03-21-aee9ab3c-4976b92d/
recipe: https://datasets.datalad.org/shub/williamssanders/sdaps/sdaps/2019-03-21-aee9ab3c-4976b92d/Singularity
collection: williamssanders/sdaps
---

# williamssanders/sdaps:sdaps

```bash
$ singularity pull shub://williamssanders/sdaps:sdaps
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:ubuntu

%help
usage: sdaps [-h]
             {add,annotate,boxgallery,convert,cover,csv,gui,ids,info,recognize,reorder,report,report_tex,reset,setup,stamp}
             ...

SDAPS -- Paper based survey tool.

positional arguments:
  {add,annotate,boxgallery,convert,cover,csv,gui,ids,info,recognize,reorder,report,report_tex,reset,setup,stamp}
                        Commands:
    add                 Add scanned questionnaires to the survey.
    annotate            Annotate the questionnaire and show the recognized
                        positions.
    boxgallery          Create PDFs with boxes sorted by the detection
                        heuristics.
    convert             Convert a set of images to the correct image format.
    cover               Create a cover for the questionnaires.
    csv                 Import or export data to/from CSV files.
    gui                 Launch a GUI. You can view and alter the (recognized)
                        answers with it.
    ids                 Export and import questionnaire IDs.
    info                Display and modify metadata of project.
    recognize           Run the optical mark recognition.
    reorder             Reorder pages according to questionnaire ID.
    report              Create a PDF report.
    report_tex          Create a PDF report using LaTeX.
    reset               Reset project into original state
    setup               Create a new survey using a LaTeX document.
    stamp               Add marks for automatic processing.

optional arguments:
  -h, --help            show this help message and exit

%labels
	MAINTAINER Shane Sanders
	
%post
	#add-apt-repository ppa:benjamin-sipsolutions/sdaps
	apt-get update
	apt-get upgrade -y
	apt-get install -y software-properties-common
	add-apt-repository ppa:benjamin-sipsolutions/sdaps
	apt-get install -y sdaps
	
%runscript
	#echo "Hello from the Container!"
	sdaps "$@"
```

## Collection

 - Name: [williamssanders/sdaps](https://github.com/williamssanders/sdaps)
 - License: None

