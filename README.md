# Tutorial: Computational Approaches for Identifying Context-Specific Transcription Factors using Single-Cell Multi-Omics Datasets (ISMB 2024)

## Table of Contents

<!-- vscode-markdown-toc -->

- [Tutorial: Computational Approaches for Identifying Context-Specific Transcription Factors using Single-Cell Multi-Omics Datasets (ISMB 2024)](#tutorial-computational-approaches-for-identifying-context-specific-transcription-factors-using-single-cell-multi-omics-datasets-ismb-2024)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Learning Objectives for Tutorial](#learning-objectives-for-tutorial)
  - [Intended Audience and Level](#intended-audience-and-level)
  - [Environment Set up](#environment-set-up)
  - [Schedule](#schedule)
  - [Hands-on Tutorial](#hands-on-tutorial)
    - [Session 1 :  Hands-on experience in applying tools and interpreting results using multiple TF activity inference methods using public scRNA-seq](#session-1---hands-on-experience-in-applying-tools-and-interpreting-results-using-multiple-tf-activity-inference-methods-using-public-scrna-seq)
    - [Session 2: Hands-on experience in applying tools and interpreting results using multiple TF activity inference methods using public scATAC-seq and multiome](#session-2-hands-on-experience-in-applying-tools-and-interpreting-results-using-multiple-tf-activity-inference-methods-using-public-scatac-seq-and-multiome)
    - [Session 3: Hands-on experience in applying tools and interpreting results using TF activity inference methods using public CITE-seq](#session-3-hands-on-experience-in-applying-tools-and-interpreting-results-using-tf-activity-inference-methods-using-public-cite-seq)

<!-- vscode-markdown-toc-config
	numbering=true
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->


##  <a name='Introduction'></a>Introduction
Development of specialized cell types and their functions are controlled by external signals that initiate and propagate cell-type specific transcriptional programs. Activation or repression of genes by key combinations of transcription factors (TFs) drive these transcriptional programs and control cellular identity and functional state. For example, ectopic expression of the TF factors Oct4, Sox2, Klf4 and c-Myc are sufficient to reprogram fibroblasts into induced pluripotent stem cells. Conversely, disruption of TF activity can cause a broad range of diseases including cancer. Hence, identifying context-specific TFs is particularly relevant to human health and disease.

Systematically identifying key TFs for each cell-type represents a formidable challenge. Determination of TF activity in bulk tissue is confounded by cell-type heterogeneity. Single-cell technologies now measure different modalities from individual cells such as RNA, protein, and chromatin states. For example, recent technological breakthroughs have coupled the relatively sparse single cell RNA sequencing (scRNA-seq) signal with robust detection of highly abundant and well-characterized surface proteins using index sorting and barcoded antibodies such as cellular indexing of transcriptomes and epitopes by sequencing (CITE-seq). But these approaches are limited to surface proteins, whereas TFs are intracellular. Single-cell sequencing assay for transposase-accessible chromatin (scATAC-seq) measures genome-wide chromatin accessibility and reveals cellular memory and response to stimuli or developmental decisions. Recently several computational methods have leveraged these omics datasets to systematically estimate TF activity influencing cell states. We will cover these TF activity inference methods using scRNA-seq, scATAC-seq, Multiome and CITE-seq data through hybrid lectures and hand-on-training sessions. We will cover the principles underlying these methods, their assumptions and trade-offs. We will apply multiple methods, interpret results and discuss strategies for further in silico validation. The audience will be equipped with practical knowledge, essential skills to conduct TF activity inference independently on their own datasets and interpret results.
##  <a name='LearningObjectivesforTutorial'></a>Learning Objectives for Tutorial
At the completion of the tutorial, participants will gain understanding into the basic concepts and recent advances in transcription factor inference methods for single-cell omics datasets including scRNA-seq, scATAC-seq, CITE-seq and Multiome. Four learning objectives are proposed:
1. Understand the basics principles underlying TF activity inference from single-cell omics
2. Understand the specific methodologies, assumptions, and trade-offs between computational inference methods
3. Gain hands-on experience in applying tools and interpreting results using multiple TF activity inference methods on public scRNA-seq, scATAC-seq, multiome and CITE-seq datasets
4. Discuss current bottlenecks, gaps in the field, and opportunities for future work.

##  <a name='IntendedAudienceandLevel'></a>Intended Audience and Level
This tutorial is designed for individuals at the beginner to intermediate level, specifically targeting bioinformaticians or computational biologists with some prior experience in analyzing single-cell RNA sequencing (scRNA-seq), single-cell assay for transposase-accessible chromatin sequencing (scATAC-seq), Cellular Indexing of Transcriptomes and Epitopes by Sequencing (CITE-seq), and Multiome data, or those familiar with next-generation sequencing (NGS) methods. A foundational understanding of basic statistics is assumed.

While participants are expected to be beginners, a minimum level of experience in handling NGS datasets is required. The workshop will be conducted using Python and JupyterLab, necessitating prior proficiency in Python programming and familiarity with command-line tools.

To facilitate the learning process, participants will be provided with pre-processed count matrices derived from real datasets. All analyses, including JupyterLab notebooks and tutorial steps, will be available on GitHub for reference.

The tutorial will employ publicly accessible data, with examples showcased using datasets that will be made available through repositories such as the Gene Expression Omnibus or similar public platforms. This hands-on workshop aims to equip participants with practical skills and knowledge, enabling them to navigate and analyze complex datasets in the field of single-cell omics.

##  <a name='EnvironmentSetup'></a>Environment Set up
We use Jupyter Python notebook in google Colab for running our tutorial. The instruction for Python packages installation are showed at the beginning of each tutorial notebook 

##  <a name='Schedule'></a>Schedule
Tuesday, July 9, 2024 14:00 – 18:00 EDT
Time  | Tutorial
-------|-------------------
`14:00` | Welcome remarks and tutorial overview  <br /> Hatice 
`14:05` | Basic principles behind TF activity inference methods <br>  &nbsp;  &nbsp; *  Overview of the importance of context-specific TF regulation in biological systems. <br> &nbsp;  &nbsp;* Significance of TF dynamics in health and disease.<br> &nbsp;  &nbsp;* Single-cell multi-omics technologies for TF activity inference (scRNA-seq, scATAC-seq, Multiome<br /> Hatice
`14:45` | Overview of computational TF inference methods based on single cell omics <br /> Merve
`15:45` | Break
`16:00` | Hands-on experience in applying tools and interpreting results using multiple TF activity inference methods using public scRNA-seq <br />Linan and Merve
`16:45` | Hands-on experience in applying tools and interpreting results using multiple TF activity inference methods using public scATAC-seq and multiome <br />Parham and Merve
`17:30` | Hands-on experience in applying tools and interpreting results using TF activity inference methods using public CITE-seq <br />Parham and Hatice
`17:55` |Discuss current bottlenecks, gaps in the field, and opportunities for future work <br />Hatice

##  <a name='Hands-onTutorial'></a>Hands-on Tutorial
###   <a name='Session1:Hands-onexperienceinapplyingtoolsandinterpretingresultsusingmultipleTFactivityinferencemethodsusingpublicscRNA-seq'></a>Session 1 :  Hands-on experience in applying tools and interpreting results using multiple TF activity inference methods using public scRNA-seq
* 1.1:  XXXXXXX (Linan)

* 1.2:  XXXXXXX (Merve)

###   <a name='Session2:Hands-onexperienceinapplyingtoolsandinterpretingresultsusingmultipleTFactivityinferencemethodsusingpublicscATAC-seqandmultiome'></a>Session 2: Hands-on experience in applying tools and interpreting results using multiple TF activity inference methods using public scATAC-seq and multiome
* 2.1:  XXXXXXX (Parham)

* 2.2:  XXXXXXX (Merve)
  

###   <a name='Session3:Hands-onexperienceinapplyingtoolsandinterpretingresultsusingTFactivityinferencemethodsusingpublicCITE-seq'></a>Session 3: Hands-on experience in applying tools and interpreting results using TF activity inference methods using public CITE-seq
* 3.1:  XXXXXXX (Parham)

* 3.2:  XXXXXXX (Hatice)
