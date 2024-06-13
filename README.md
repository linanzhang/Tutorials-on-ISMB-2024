<!-- vscode-markdown-toc -->
* 1. [Table of Contents<!-- omit in toc -->](#TableofContents--omitintoc--)
* 2. [Introduction](#Introduction)
* 3. [Learning Objectives for Tutorial](#LearningObjectivesforTutorial)
* 4. [Intended Audience and Level](#IntendedAudienceandLevel)
* 5. [Schedule](#Schedule)
* 6. [Environment Set up](#EnvironmentSetup)
	* 6.1. [Installation of Conda](#InstallationofConda)
	* 6.2. [Managing Environment](#ManagingEnvironment)
	* 6.3. [Managing Packages](#ManagingPackages)
* 7. [Hands-on Tutorial](#Hands-onTutorial)
		* 7.1. [Session 1 :  Hands-on experience in applying tools and interpreting results using multiple TF activity inference methods using public scRNA-seq](#Session1:Hands-onexperienceinapplyingtoolsandinterpretingresultsusingmultipleTFactivityinferencemethodsusingpublicscRNA-seq)
		* 7.2. [Session 2: Hands-on experience in applying tools and interpreting results using multiple TF activity inference methods using public scATAC-seq and multiome](#Session2:Hands-onexperienceinapplyingtoolsandinterpretingresultsusingmultipleTFactivityinferencemethodsusingpublicscATAC-seqandmultiome)
		* 7.3. [Session 3: Hands-on experience in applying tools and interpreting results using TF activity inference methods using public CITE-seq](#Session3:Hands-onexperienceinapplyingtoolsandinterpretingresultsusingTFactivityinferencemethodsusingpublicCITE-seq)

<!-- vscode-markdown-toc-config
	numbering=true
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc --># Tutorial: Computational Approaches for Identifying Context-Specific Transcription Factors using Single-Cell Multi-Omics Datasets (ISMB 2024)<!-- omit in toc -->

##  1. <a name='TableofContents--omitintoc--'></a>Table of Contents<!-- omit in toc -->

- [2. Introduction](#2-introduction)
- [3. Learning Objectives for Tutorial](#3-learning-objectives-for-tutorial)
- [4. Intended Audience and Level](#4-intended-audience-and-level)
- [5. Schedule](#5-schedule)
- [6. Environment Set up](#6-environment-set-up)
  - [6.1. Installation of Conda](#61-installation-of-conda)
  - [6.2. Managing Environment](#62-managing-environment)
  - [6.3. Managing Packages](#63-managing-packages)
- [7. Hands-on Tutorial](#7-hands-on-tutorial)
    - [7.1. Session 1 :  Hands-on experience in applying tools and interpreting results using multiple TF activity inference methods using public scRNA-seq](#71-session-1---hands-on-experience-in-applying-tools-and-interpreting-results-using-multiple-tf-activity-inference-methods-using-public-scrna-seq)
    - [7.2. Session 2: Hands-on experience in applying tools and interpreting results using multiple TF activity inference methods using public scATAC-seq and multiome](#72-session-2-hands-on-experience-in-applying-tools-and-interpreting-results-using-multiple-tf-activity-inference-methods-using-public-scatac-seq-and-multiome)
    - [7.3. Session 3: Hands-on experience in applying tools and interpreting results using TF activity inference methods using public CITE-seq](#73-session-3-hands-on-experience-in-applying-tools-and-interpreting-results-using-tf-activity-inference-methods-using-public-cite-seq)



##  2. <a name='Introduction'></a>Introduction
Development of specialized cell types and their functions are controlled by external signals that initiate and propagate cell-type specific transcriptional programs. Activation or repression of genes by key combinations of transcription factors (TFs) drive these transcriptional programs and control cellular identity and functional state. For example, ectopic expression of the TF factors Oct4, Sox2, Klf4 and c-Myc are sufficient to reprogram fibroblasts into induced pluripotent stem cells. Conversely, disruption of TF activity can cause a broad range of diseases including cancer. Hence, identifying context-specific TFs is particularly relevant to human health and disease.

Systematically identifying key TFs for each cell-type represents a formidable challenge. Determination of TF activity in bulk tissue is confounded by cell-type heterogeneity. Single-cell technologies now measure different modalities from individual cells such as RNA, protein, and chromatin states. For example, recent technological breakthroughs have coupled the relatively sparse single cell RNA sequencing (scRNA-seq) signal with robust detection of highly abundant and well-characterized surface proteins using index sorting and barcoded antibodies such as cellular indexing of transcriptomes and epitopes by sequencing (CITE-seq). But these approaches are limited to surface proteins, whereas TFs are intracellular. Single-cell sequencing assay for transposase-accessible chromatin (scATAC-seq) measures genome-wide chromatin accessibility and reveals cellular memory and response to stimuli or developmental decisions. Recently several computational methods have leveraged these omics datasets to systematically estimate TF activity influencing cell states. We will cover these TF activity inference methods using scRNA-seq, scATAC-seq, Multiome and CITE-seq data through hybrid lectures and hand-on-training sessions. We will cover the principles underlying these methods, their assumptions and trade-offs. We will apply multiple methods, interpret results and discuss strategies for further in silico validation. The audience will be equipped with practical knowledge, essential skills to conduct TF activity inference independently on their own datasets and interpret results.
##  3. <a name='LearningObjectivesforTutorial'></a>Learning Objectives for Tutorial
At the completion of the tutorial, participants will gain understanding into the basic concepts and recent advances in transcription factor inference methods for single-cell omics datasets including scRNA-seq, scATAC-seq, CITE-seq and Multiome. Four learning objectives are proposed:
1. Understand the basics principles underlying TF activity inference from single-cell omics
2. Understand the specific methodologies, assumptions, and trade-offs between computational inference methods
3. Gain hands-on experience in applying tools and interpreting results using multiple TF activity inference methods on public scRNA-seq, scATAC-seq, multiome and CITE-seq datasets
4. Discuss current bottlenecks, gaps in the field, and opportunities for future work.

##  4. <a name='IntendedAudienceandLevel'></a>Intended Audience and Level
This tutorial is designed for individuals at the beginner to intermediate level, specifically targeting bioinformaticians or computational biologists with some prior experience in analyzing single-cell RNA sequencing (scRNA-seq), single-cell assay for transposase-accessible chromatin sequencing (scATAC-seq), Cellular Indexing of Transcriptomes and Epitopes by Sequencing (CITE-seq), and Multiome data, or those familiar with next-generation sequencing (NGS) methods. A foundational understanding of basic statistics is assumed.

While participants are expected to be beginners, a minimum level of experience in handling NGS datasets is required. The workshop will be conducted using Python and JupyterLab, necessitating prior proficiency in Python programming and familiarity with command-line tools.

To facilitate the learning process, participants will be provided with pre-processed count matrices derived from real datasets. All analyses, including JupyterLab notebooks and tutorial steps, will be available on GitHub for reference.

The tutorial will employ publicly accessible data, with examples showcased using datasets that will be made available through repositories such as the Gene Expression Omnibus or similar public platforms. This hands-on workshop aims to equip participants with practical skills and knowledge, enabling them to navigate and analyze complex datasets in the field of single-cell omics.


##  5. <a name='Schedule'></a>Schedule
Tuesday, July 9, 2024 14:00 – 18:00 EDT
Time  | Tutorial
-------|-------------------
`14:00` | Welcome remarks and tutorial overview  <br /> Hatice 
`14:05` | Basic principles behind TF activity inference methods <br>  &nbsp; &nbsp; &nbsp;  * Overview of the importance of context-specific TF regulation in biological systems. <br> &nbsp;  &nbsp; &nbsp;  * Significance of TF dynamics in health and disease.<br> &nbsp;  &nbsp; &nbsp; * Single-cell multi-omics technologies for TF activity inference (scRNA-seq, scATAC-seq, Multiome<br /> Hatice
`14:45` | Overview of computational TF inference methods based on single cell omics <br /> Merve
`15:45` | Break
`16:00` | Hands-on experience in applying tools and interpreting results using multiple TF activity inference methods using public scRNA-seq <br />Linan and Merve
`16:45` | Hands-on experience in applying tools and interpreting results using multiple TF activity inference methods using public scATAC-seq and multiome <br />Parham and Merve
`17:30` | Hands-on experience in applying tools and interpreting results using TF activity inference methods using public CITE-seq <br />Parham and Hatice
`17:55` |Discuss current bottlenecks, gaps in the field, and opportunities for future work <br />Hatice



##  6. <a name='EnvironmentSetup'></a>Environment Set up
###  6.1. <a name='InstallationofConda'></a>Installation of Conda

1. [Download the installer by choosing the proper installer for your machine.](https://www.anaconda.com/download/)
2. [Verify your installer hashes using SHA-256 checksums.](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html#hash-verification)
3. Install the installer:
	- Windows: Double-click the `.exe` file. Follow the instructions on the screen. For a detailed reference, please read [this page](https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html#installing-on-windows).
	- macOS: double-click the `.pkg` file. Follow the instructions on the screen.For a detailed reference, please read [this page](https://docs.conda.io/projects/conda/en/latest/user-guide/install/macos.html#installing-on-macos).
	- Linux: In your terminal window, run: `bash Anaconda-latest-Linux-x86_64.sh`. Follow the prompts on the inConda is an open-source tool that provides package, dependency, and environment management for any programming language. To install conda, we must first pick the right installer for us. Below we will demonstrate how to install **Anaconda Distribution**, a full featured installer of Conda.
staller screens. For a detailed reference, please read [this page](https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html#installing-on-linux).


###  6.2. <a name='ManagingEnvironment'></a>Managing Environment

With conda, you can create, export, list, and update environments that have different versions of Python and/or packages installed in them. The JupyterLab, which can run in conda environment,  is a web application for computational documents so that our code can produce rich, interactive output.


Below we will demonstrate how to create an conda environment and install JupterLab for this tutorial on macOS/Linux. Use the **terminal** for the following steps. For a detailed reference, please read [this page](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

Use Mac **terminal** for the following steps:

1. Create an environment with the latest version of python 3: 
   
   `conda create --name <my-env> python=3`. Replace `<my-env>` with the name of your environment.
2. Activate the environment you just created: 
   
   `·conda activate <my-env>`
3. Install JupyterLab: 
   
    `pip install jupyterlab`
4. Run JupyterLab: 
   
   `jupyter lab` 

###  6.3. <a name='ManagingPackages'></a>Managing Packages

Please download the requirements.txt and use the following commands to install python packages required for running the tutorials

  `pip install -r requirements.txt`

Besides the packages listed in requirements.txt,  a few additional packages are required for each session. Please follow the steps below to install packages needed for your session of interest

Session 1: 
We will compare STAN with decoupler.

`pip install decoupler`

Session 2:

Session 3:

We will run our own pySPaRTAN package.

`pip install pySPaRTAN`

Our pySPaRTAN calls two customer built Cython extensions. We need to install cython first then compile the extension. Suppose your computer have c compiler preinstalled. Otherwise please check
<a href=”https://cython.readthedocs.io/en/latest/src/quickstart/install.html”>here</a>
 for C compiler installation on various operating systems

install Cython:
`pip install cython`

compile Cython extension: download this repository, navigate to /hands-on_tutorial/session-3/pySPaRTAN  directory, run the below command in terminal (Mac os). After sucessfully built the extentions, you will see two .so files (Mac OS) genereated in the current directory.

`python setup.py build_ext --inplace`








##  7. <a name='Hands-onTutorial'></a>Hands-on Tutorial
####  7.1. <a name='Session1:Hands-onexperienceinapplyingtoolsandinterpretingresultsusingmultipleTFactivityinferencemethodsusingpublicscRNA-seq'></a>Session 1 :  Hands-on experience in applying tools and interpreting results using multiple TF activity inference methods using public scRNA-seq


####  7.2. <a name='Session2:Hands-onexperienceinapplyingtoolsandinterpretingresultsusingmultipleTFactivityinferencemethodsusingpublicscATAC-seqandmultiome'></a>Session 2: Hands-on experience in applying tools and interpreting results using multiple TF activity inference methods using public scATAC-seq and multiome

  

####  7.3. <a name='Session3:Hands-onexperienceinapplyingtoolsandinterpretingresultsusingTFactivityinferencemethodsusingpublicCITE-seq'></a>Session 3: Hands-on experience in applying tools and interpreting results using TF activity inference methods using public CITE-seq




[def]: #session-3-hands-on-experience-in-applying-tools-and-interpreting-results-using-tf-activity-inference-methods-using-public-cite-seq