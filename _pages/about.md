---
permalink: /
title: "Hi!"
excerpt: "About me"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

{% include base_path %}

I am Zihao Xu (徐 子昊), a third-year PhD candidate in the Computer Science program at Rutgers University. My advisor is Professor [Hao Wang](http://www.wanghao.in/), and my research focuses on **Bayesian Deep Learning and Domain Adaptation**.
I received my undergraduate degree in Computer Science from Shanghai Jiaotong University, a top-ranked university in China. During my time there, I was also a member of the ACM Honors Class, a prestigious program for the top 5% of Computer Science students at the university. Notable alumni of the program include [Tianqi Chen](https://tqchen.com/) (Assistant Professor at Carnegie Mellon University), [Mu Li](https://www.linkedin.com/in/mulicmu/) (former Senior Principal Scientist at Amazon), and [Bo Li](https://lilab-bcb.github.io/) (Assistant Professor at Harvard Medical School).

<!-- ## News
**Nov. 19th, 2023** Our paper: [Toward a Generalized Bayesian Model of Category Effects](https://osf.io/preprints/psyarxiv/9a7ft/) is accepted by Psychonomic 2023 (Oral).<br>
<br>**Oct. 6th, 2023**: The [official implementation](https://github.com/Wang-ML-Lab/TSDA) for TSDA is released!<br>
<br>**Jun. 30th, 2023**: Our paper: [Taxonomy-Structured Domain Adaptation](https://arxiv.org/abs/2306.07874) is accepted by ICML 2023. [Code](https://github.com/Wang-ML-Lab/TSDA) will be released soon.<br>
<br>**Jan. 21th, 2023**: Our paper: [Domain-Indexing Variational Bayes: Interpretable Domain Index for Domain Adaptation](https://arxiv.org/abs/2302.02561) is accepted by ICLR 2023 (spotlight). See our [code](https://github.com/Wang-ML-Lab/VDI) and [openreview page](https://openreview.net/forum?id=pxStyaf2oJ5) for more details.<br>
<br>**Feb. 8th, 2022**: Our paper: [Graph-Relational Domain Adaptation](https://arxiv.org/abs/2202.03628) is accepted by ICLR 2022. Code is released [here](https://github.com/Wang-ML-Lab/GRDA).<br> -->

## News
- Nov. 19th, 2023: *Our paper: [Toward a Generalized Bayesian Model of Category Effects](https://osf.io/preprints/psyarxiv/9a7ft/) is accepted by Psychonomic 2023 (Oral).*
- Jun. 30th, 2023: *Our paper: [Taxonomy-Structured Domain Adaptation](https://arxiv.org/abs/2306.07874) is accepted by ICML 2023. [Code](https://github.com/Wang-ML-Lab/TSDA) is released.*
- Jan. 21th, 2023: *Our paper: [Domain-Indexing Variational Bayes: Interpretable Domain Index for Domain Adaptation](https://arxiv.org/abs/2302.02561) is accepted by ICLR 2023 (spotlight). See our [code](https://github.com/Wang-ML-Lab/VDI) and [openreview page](https://openreview.net/forum?id=pxStyaf2oJ5) for more details.*
- Feb. 8th, 2022: *Our paper: [Graph-Relational Domain Adaptation](https://arxiv.org/abs/2202.03628) is accepted by ICLR 2022. Code is released [here](https://github.com/Wang-ML-Lab/GRDA).*

----

# Selected Publications 

"*" indicates equal contribution.

{% for post in site.publications reversed %}
  {% if post.selected %}
  {% include archive-pub-short.html %}
  {% endif %}
{% endfor %}



<!-- ----
#  -->

<!-- ** Research Opportunities **: I am always open for new cooperation. If you are a student of Rutgers and interested in generalization problem of machine learning (specifically, domain adaptation and domain generalization), send me an email (zihao.xu@rutgers.edu) to see if we could   -->

<!-- Welcome to my website! Just here for my CV? You can download that [here](/files/Kurchin_CV.pdf). Please check out ways to reach me as well as my various other homes on the web in the menu (either to the left or above, depending on your screen resolution) and click the links at the top of the page to check out some of my other experience and work!

## What do/did I do?

**As of September 1, 2022, I will be an Assistant Research Professor in Materials Science and Engineering at Carnegie Mellon!** Please feel free to reach out if you are interested in working together, either collaboratively or as a mentee.

I'm a computational materials scientist (with significant previous experimental experience), until recently a Molecular Sciences Software Institute Postdoctoral Fellow working in the group of [Venkat Viswanathan](http://www.andrew.cmu.edu/user/venkatv/index.html) on discovery of battery and catalyst materials, with affiliations in the Departments of Mechanical Engineering and Materials Science and Engineering. I am the lead developer of the [Chemellia](https://github.com/Chemellia) "machine learning with atoms" ecosystem, in particular the [ChemistryFeaturization](https://chemellia.github.io/ChemistryFeaturization.jl/stable/) and [AtomicGraphNets](https://github.com/Chemellia/AtomicGraphNets.jl) packages.

Previously, I did my PhD in Materials Science and Engineering in the [Photovoltaics Research Lab](http://pv.mit.edu) at MIT, where I performed first-principles simulations to understand defect physics in solar cell materials (in close collaboration with [Vladan Stevanovic](https://scholar.google.com/citations?user=itfRzZAAAAAJ&hl=en) of the Colorado School of Mines and National Renewable Energy Lab) as well as high-throughput device-level simulations to use Bayesian inference along with experimental data to more quickly and accurately measure fundamental materials properties. Prior to that, I received my MPhil in Materials Science and Metallurgy from the University of Cambridge, supported by a Gates Cambridge Scholarship.

## What do I care about?
My overarching goal in my work is to have an impact on the existential problem of climate change through improving renewable energy technology. I've also been involved in renewables-related outreach through [Project Bright](http://campuspress.yale.edu/projectbright/) at Yale as well as various organizations at MIT including the PVLab, the [MIT Energy Club](https://www.mitenergyclub.org) (where I led the Solar/Grid community for two years), the Office of Sustainability, Fossil Free MIT, and the [Science Policy Initiative](https://mitspi.squarespace.com).

Since my time as an undergrad in physics at Yale, I've also been devoted to the cause of increasing representation of women (and other URG's) in STEM fields. In 2012, I helped to organize the Northeast [Conference for Undergraduate Women in Physics](https://www.aps.org/programs/women/workshops/cuwip.cfm), and I returned to the conference as a graduate student speaker 2015. At MIT, I served as co-president of Women of Materials Science (WoMS).
-->
