---
layout: archive
title: "Tools"
permalink: /tools/
author_profile: true
redirect_from:
  - /tools
  - /tools_i_use
  - /tools-i-use
---

{% include base_path %}

Even though we don't work in a laboratory, computationalists use many tools that make our lives easier and more convenient every day! I want to highlight some (especially those that exist thanks to the uncompensanted efforts of open-source developers) here, to provide some acknowledgement to those developers and also in case you're looking for a tool to do something similar, or do it better!

I'm also always keen to learn new tools, so if you think you can improve my workflows, [give me a shout!](rkurchin@cmu.edu)

Progamming Languages
--------------------

[Julia](https://www.julialang.org) is my go-to language nowadays, though my Python isn't too bad...

Julia packages I rely on include [Flux](https://fluxml.ai) for building machine learning models, [UnicodePlots](https://github.com/Evizero/UnicodePlots.jl) for quick dataviz in the terminal, as well as various tools from the [JuliaGraphs](https://github.com/JuliaGraphs/LightGraphs.jl) and [SciML](https://sciml.ai) ecosystems.

Python packages of note: For data-wrangling, I couldn't live without [Pandas](https://pandas.pydata.org) or the rest of the [SciPy](https://www.scipy.org) ecosystem, especially NumPy for mathy things and matplotlib for visualization. [Seaborn](https://seaborn.pydata.org) is another great visualization package built on top of matplotlib. For simple parallelization tasks, [Joblib](https://joblib.readthedocs.io/en/latest/) makes life a lot easier. And for interacting with HDF5 files super simply, [deepdish](https://deepdish.readthedocs.io/en/latest/) (sadly no longer maintained) is also pretty great.

[Git](https://git-scm.com) is a great and near-ubiquitous version-control system. I'm at a pretty basic level of git competency, and like many people, I also use [GitHub](https://www.github.com) and [ungit](https://github.com/FredrikNoren/ungit) for visualizing the tree.

Maybe it hardly bears mentioning, but a big barrier for many new computationalists is getting familiar with a Unix environment. If this is something you are (or someone who know is) dealing with, I heartily recommend [Unix for the Beginning Mage](http://lab46.corning-cc.edu/_media/haas/ufbm.pdf) as a whimsical yet effective learning tool.

Programming Environments
------------------------

For interactive testing of Julia and Python code with inline output, I'm an extensive user of [Jupyter](https://jupyter.org). [Binder](https://www.mybinder.org) is a related useful tool that lets you spin up Jupyter kernels from git repos in the cloud!

I learned about [iTerm2](https://iterm2.com) from my amazing friend and mentor [Prashun](https://www.prashungorai.org/) and never looked back. Just a super reliable, customizable terminal app. I particularly love their Minimal theme and status bar customization options in the latest release! I also more recently found out about [oh my zsh](https://ohmyz.sh), which offers a lot of other cool CLI customization, including lots of aautocompletes, easy prompt customization to include all kinds of stuff, etc.

When I'm editing code on a cluster, I'm a very-much-not-power-user of Emacs, but when I'm able to edit locally, I love love love [Atom](https://atom.io). Super nice-looking out of the box but nearly infinitely customizable with extensions for every possible need! My favorite extensions include:
* [Juno](https://atom.io/packages/uber-juno) (also available as a [separate installation](https://junolab.org), optimizes Atom's setup as a Julia IDE – sadly this is also no longer supported and I'm working on shifting myself over to VS Code for Julia development)
* [file-icons](https://atom.io/packages/file-icons): file-specific icons in folder tree views
* [ftp-remote-edit](https://atom.io/packages/ftp-remote-edit): use Atom to edit files on remote servers! Woohoo! (though I still use Emacs for quick things)

All my IDE's of any kind are set up to use the [Source Code Pro](https://fonts.google.com/specimen/Source+Code+Pro) font with its gorgeous design and sexy ligatures.

Academic Life
-------------

* I manage my papers/bibliographies with [Zotero](https://www.zotero.org).

* I recently switched over to [Spark](https://sparkmailapp.com) as my email client. Once they fix some bugs with their calendaring, I will likely use it for that too, but for the moment I use Google Calendar for that.

* I keep notes using [Bear](https://bear.app), which I do pay for, but it's a quite modest fee for a totally gorgeous, functional app that syncs across all my devices.

* I've moved to [Overleaf](https://www.overleaf.com) almost exclusively as my LaTeX editor. I love not having to manage a TeX environment locally, and being able to easily collaborate with others, etc.

* I can get a bit obsessive about aiming for Inbox Zero with my email, which can be a distraction from other work. In addition to making liberal use of full-screen mode to completely shut out distractions, I've also started using [Unroll.me](https://unroll.me) to turn subscription emails into daily digests and reduce the number of push notifications I get while not filtering out things that might actually require urgent responses.
