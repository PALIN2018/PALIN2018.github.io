---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I obtained my Ph.D. degree in Data Science and Analytics (DSA) from HKUST, where I was very fortunately supervised by Prof. <a href="https://www.cse.ust.hk/~hunkim/">Sunghun KIM</a> and Prof. <a href="https://seng.hkust.edu.hk/about/people/faculty/raymond-chi-wing-wong">Raymond Chi Wing WONG</a>. I received my master’s degree from the School of Electronic and Computer Engineering at Peking University (北京大学信息工程学院), where I was advised by [Prof. Yuexian Zou](https://web.pkusz.edu.cn/adsp), and earned my bachelor’s degree from the College of Internet of Things Engineering at Hohai University (河海大学物联网工程学院). I also work closely with [Prof. Shoujin Wang](https://shoujinwang1.github.io/) from the University of Technology Sydney.

I have published 20+ papers <a href='https://scholar.google.com/citations?user=3dx8O1AAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a> at top international AI conferences such as ACL, NeurIPS, IJCAI, SIGIR, WWW, KDD, CIKM, and RecSys.

My research broadly falls under the umbrella of <strong>Human-Centered AI</strong>, striving to bridge the gap between <strong>data-driven prediction</strong> and <strong>knowledge-driven reasoning</strong>. Specifically, I am building a systematic research framework that evolves from robust user modeling to complex clinical decision-making:

<ul>

    <li><strong>Robust Sequential Modeling (Foundation):</strong> Addressing fundamental data challenges (e.g., noise, sparsity, heterogeneity) in sequential recommender systems to build reliable user behavior models.</li>

    <li><strong>LLM-Empowered Reasoning (Methodology):</strong> Leveraging Large Language Models to enhance decision-making systems with reasoning capabilities, moving from simple matching to interpretable, agent-based planning.</li>

    <li><strong>AI for Healthcare (Application):</strong> Transferring robust sequential modeling and LLM reasoning capabilities to the medical domain to facilitate intelligent clinical decision-making and personalized care.</li>

</ul>

I am actively <strong>seeking job opportunities in both academia (faculty or postdoctoral positions) and industry</strong>. If you are interested in academic collaboration or would like to discuss potential opportunities, please feel free to email me at [zhoupalin@gmail.com](mailto:zhoupalin@gmail.com).


# 🔥 News
- *2026.01*: &nbsp;🎉 1 paper accepted by ICLR 2026. Congrats to Zhuo!
- *2026.01*: &nbsp;🎉 1 paper accepted by WWW 2026. Congrats to Yifan!
- *2025.12*: &nbsp;🎓 Successfully defended my Ph.D. thesis titled "**Mitigating Data Challenges in Sequential Recommender Systems**"!
- *2025.12*: &nbsp;🎉 1 paper accepted by KDD 2026. Congrats to Jian!
- *2025.05*: &nbsp;🚀 Our new benchmark paper "**BrowseComp-ZH: Benchmarking Web Browsing Ability of Large Language Models in Chinese**" is now available on ArXiv!  
  This is the **first high-difficulty benchmark** specifically built to evaluate LLMs’ real-world web browsing and reasoning abilities on the **Chinese internet**, spanning 289 multi-hop, verifiable questions across 11 domains.  
  📄 [Read the paper](https://arxiv.org/pdf/2504.19314)  
  📂 [Get the dataset on GitHub](https://github.com/PALIN2018/BrowseComp-ZH)  
  📢 [中文介绍](https://mp.weixin.qq.com/s/E8nLGUhbEPi0Z5E8RG4tew) — 欢迎转发支持！
- *2025.05*: &nbsp;🎉 1 paper accepted by KDD 2025. Congrats to Jian!
- *2025.02*: &nbsp;🧑‍🔧 Serving as a reviewer for CVPR 2025, ICCV 2025, and TOIS.
- *2025.01*: &nbsp;🎉 Milestone: Google Scholar citations exceed 1000!
- *2025.01*: &nbsp;🎉 1 paper accepted by WWW 2025. 
- *2025.01*: &nbsp;🎉 1 paper accepted by JMIR. Congrats to Wanxin!
- *2025.01*: &nbsp;🎉 Our paper "Application of Large Language Models in Medicine" accepted by Nature Reviews Bioengineering. Congrats to Fenglin!
- *2025.01*: &nbsp;🎉 Our survey paper "Cold-Start Recommendation Towards the Era of Large Language Models (LLMs): A Comprehensive Survey and Roadmap" is now available on ArXiv. [Read it here](https://arxiv.org/abs/2501.01945)
- *2024.10*: &nbsp;🧑‍🔧 serve as the reviewer for ICLR2025, WWW2025 and ICASSP 2025.
- *2024.06*: &nbsp;🧑‍🔧 serve as the reviewer for AAAI2025, NeurIPS2024 and COLING 2025.
- *2024.05*: &nbsp;🎉 1 paper is accepted by ACL 2024. Congrats to Jian!
- *2024.01*: &nbsp;🎉 1 paper is accepted by WWW 2024. 
- *2023.09*: &nbsp;🎉 Our paper "Is ChatGPT a Good Recommender? A Preliminary Study" is accepted by The 1st Workshop on Recommendation with Generative Models (organized by CIKM 2023).
- *2023.09*: &nbsp;🎉 1 paper is accepted by NeurIPS 2023.


# 📝 Publications 

## 📊 Recommender System
### 🧠 LLM/LVLM for RecSys
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CIKM 2023 GenRec Workshop</div><img src='images/chatgpt-rec.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Is ChatGPT a Good Recommender? A Preliminary Study](https://arxiv.org/pdf/2304.10149.pdf) <strong><span class='show_paper_citations' data='3dx8O1AAAAAJ:eQOLeE2rZwMC'></span></strong>\\
Junling Liu, Chao Liu, **Peilin Zhou**, Renjie Lv, Kang Zhou, Yan Zhang.

[<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />](https://github.com/williamliujl/LLMRec) 

- First work to utilize ChatGPT as a universal recommender, assessing its capabilities across five tasks.
- Provides valuable insights into the strengths and limitations of ChatGPT in recommendation systems.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">WWW 2025 (Oral)</div><img src='images/MSRBench.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[When Large Vision Language Models Meet Multimodal Sequential Recommendation: An Empirical Study](https://dl.acm.org/doi/10.1145/3696410.3714764) \\
**Peilin Zhou**, Chao Liu, Jing Ren, Xinfeng Zhou, Yueqi Xie, Meng Cao, Zhongtao Rao, You-Liang Huang, Dading Chong, Junling Liu, Jae Boum Kim, Shoujin Wang, Raymond Chi-Wing Wong, Sunghun Kim.

[<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />](https://github.com/PALIN2018/MSRBench) 

- Introduces **MSRBench**, the first benchmark to systematically evaluate the integration of Large Vision Language Models (LVLMs) in multimodal sequential recommendation.
- Compares five integration strategies (recommender, item enhancer, reranker, and two combinations), identifying **reranker** as the most effective.
- Constructs the enhanced dataset **Amazon Review Plus**, with LVLM-generated image descriptions to support more flexible item modeling.
</div>
</div>

- ``ArXiv`` [LLMRec: Benchmarking Large Language Models on Recommendation Task](https://arxiv.org/pdf/2308.12241), Jungling Liu, Chao Liu, **Peilin Zhou**, et al.
[![](https://img.shields.io/github/stars/williamliujl/LLMRec?style=social&label=Code+Stars)](https://github.com/williamliujl/LLMRec) 


- ``ArXiv`` [Exploring Recommendation Capabilities of GPT-4V (ision): A Preliminary Case Study](https://arxiv.org/pdf/2311.04199), **Peilin Zhou**, Meng Cao, Youliang Huang, Qichen Ye, et al.

### 🔁 Sequential Recommendation

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">SIGIR 2022</div><img src='images/dif.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Decoupled Side Information Fusion for Sequential Recommendation](https://arxiv.org/pdf/2204.11046) <strong><span class='show_paper_citations' data='3dx8O1AAAAAJ:qjMakFHDy7sC'></span></strong>\\
Yueqi Xie, **Peilin Zhou**, Sunghun Kim

[<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />](https://github.com/AIM-SE/DIF-SR) 

- **Motivation**: The early integration of various types of embeddings limits the expressiveness of attention matrices due to a rank bottleneck and constrains the flexibility of gradients.
- **Solution**: Move the side information from the input to the attention layer and decouples the attention calculation of various side information and item representation.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CIKM 2023</div><img src='images/ACTSR.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Attention Calibration for Transformer-based Sequential Recommendation](https://arxiv.org/pdf/2308.09419) <strong><span class='show_paper_citations' data='3dx8O1AAAAAJ:roLk4NBRz8UC'></span></strong>\\
**Peilin Zhou**, Qichen Ye, Yueqi Xie, Jingqi Gao, and Sunghun Kim.

[<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />](https://github.com/AIM-SE/AC-TSR) 

- AC-TSR framework can reduce the impact of sub-optimal position encoding and noisy input on the existing transformer-based SRS models with limited overhead.
- Two plug-and-play calibrators, namely spatial calibrator and adversarial calibrator, are designed to rectify the unreliable attention. 

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">RecSys 2023</div><img src='images/ECL.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Equivariant Contrastive Learning for Sequential Recommendation](https://arxiv.org/pdf/2211.05290) <strong><span class='show_paper_citations' data='3dx8O1AAAAAJ:Y0pCki6q_DkC'></span></strong>\\
**Peilin Zhou**, Jingqi Gao, Yueqi Xie, Qichen Ye, et al.

[<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />](https://github.com/Tokkiu/ECL) 

- **Motivation**: some augmentation strategies, such as item substitution, can lead to changes in user intent. Learning indiscriminately invariant representations for all augmentation strategies might be sub-optimal. 
- **Solution**: we propose Equivariant Contrastive Learning for Sequential Recommendation (ECL-SR), which endows SR models with great discriminative power, making the learned user behavior representations sensitive to invasive augmentations and insensitive to mild augmentations.

</div>
</div>

- ``WWW 2024`` [Is Contrastive Learning Necessary? A Study of Data Augmentation vs Contrastive Learning in Sequential Recommendation](https://arxiv.org/pdf/2403.11136), **Peilin Zhou**, Youliang Huang, Yueqi Xie, et al.

- ``RecSys 2023`` [Rethinking Multi-Interest Learning for Candidate Matching in Recommender Systems](https://arxiv.org/pdf/2302.14532), Yueqi Xie, Jingqi Gao, **Peilin Zhou**, Qichen Ye, et al. 
[![](https://img.shields.io/github/stars/Tokkiu/REMI?style=social&label=Code+Stars)](https://github.com/Tokkiu/REMI) 

## 🏥 AI for Healthcare
### 📱 Medical Social Media Dataset

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2022</div><img src='images/mets-cov.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[METS-CoV: A Dataset of Medical Entity and Targeted Sentiment on COVID-19 Related Tweets](https://proceedings.neurips.cc/paper_files/paper/2022/file/89a7ddfbc08b25ef8ff9029d7dd9e3d3-Paper-Datasets_and_Benchmarks.pdf) <strong><span class='show_paper_citations' data='3dx8O1AAAAAJ:Tyk-4Ss8FVUC'></span></strong>\\
**Peilin Zhou**, Zeqiang Wang, Dading Chong, Zhijiang Guo, et al.

[<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />](https://github.com/YLab-Open/METS-CoV)  

- Introduce METS-CoV, the first dataset to include medical entities and targeted sentiments on COVID-19-related tweets. 
- METS-CoV fully considers the characteristics of the medical field and can therefore be used to help researchers use natural language processing models to mine valuable medical information from tweets.
- Annotation guidelines, benchmark models, and source code are released for medical social medial research.
</div>
</div>

- ``Under Review`` [Streamlining Social Media Information Retrieval for Public Health Research with Deep Learning](https://arxiv.org/pdf/2306.16001),
Yining Hua, Shixu Lin, Minghui Li, Yujie Zhang, **Peilin Zhou**, Ying-Chih Lo, Li Zhou, Jie Yang

### 🧬 Large Languages Models for Healthcare

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2023</div><img src='images/cmexam.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Benchmarking Large Language Models on CMExam--A Comprehensive Chinese Medical Exam Dataset](https://proceedings.neurips.cc/paper_files/paper/2023/file/a48ad12d588c597f4725a8b84af647b5-Paper-Datasets_and_Benchmarks.pdf) <strong><span class='show_paper_citations' data='3dx8O1AAAAAJ:WF5omc3nYNoC'></span></strong>\\
Junling Liu, **Peilin Zhou**, Yining Hua, Dading Chong, et al.

[<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />](https://github.com/williamliujl/CMExam)  

- We construct CMExam, a dataset sourced from the stringent Chinese National Medical Licensing Examination, featuring 60,000+ multiple-choice questions, with detailed explanations. 
- This study aims to spur further exploration of LLMs in medicine by providing a comprehensive benchmark for their evaluation.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Under Review</div><img src='images/qilin-med.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Qilin-Med: Multi-stage Knowledge Injection Advanced Medical Large Language Model](https://arxiv.org/pdf/2310.09089.pdf) <strong><span class='show_paper_citations' data='3dx8O1AAAAAJ:hqOjcs7Dif8C'></span></strong>\\
Qichen Ye, Junling Liu, Dading Chong, **Peilin Zhou**, et al.

- Construct the ChiMed dataset, which contains diverse data types (QA, plain texts, knowledge graphs, and dialogues).
- Develop a Chinese medical LLM called Qilin-Med via a multi-stage knowledge injection pipeline.

</div>
</div>

- ``Under Review`` [Qilin-Med-VL: Towards Chinese Large Vision-language Model for General Healthcare](https://arxiv.org/pdf/2310.17956),
Junling Liu, Ziming Wang, Qichen Ye, Dading Chong, **Peilin Zhou**, Yining Hua
[![](https://img.shields.io/github/stars/williamliujl/Qilin-Med-VL?style=social&label=Code+Stars)](https://github.com/williamliujl/Qilin-Med-VL) 

- ``Under Review`` [A Survey of Large Language Models in Medicine: Progress, Application, and Challenge](https://arxiv.org/html/2311.05112v3) <strong><span class='show_paper_citations' data='3dx8O1AAAAAJ:kNdYIx-mwKoC'></span></strong>,
Hongjian Zhou, Boyang Gu, Xinyu Zou, Yiru Li, Sam S Chen, **Peilin Zhou**, Junling Liu, Yining Hua, Chengfeng Mao, Xian Wu, Zheng Li, Fenglin Liu
[![](https://img.shields.io/github/stars/AI-in-Health/MedLLMsPracticalGuide?style=social&label=Code+Stars)](https://github.com/AI-in-Health/MedLLMsPracticalGuide) 


- ``Under Review`` [Large Language Models in Mental Health Care: a Scoping Review](https://arxiv.org/pdf/2401.02984),
Yining Hua, Fenglin Liu, Kailai Yang, Zehan Li, Yi-han Sheu, **Peilin Zhou**，et al.

## 🌱 AI for Good
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IJCAI 2023</div><img src='images/greenplm.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[GreenPLM: Cross-lingual pre-trained language models conversion with (almost) no cost](https://arxiv.org/pdf/2211.06993.pdf) \\
Qingcheng Zeng, Lucas Garay, **Peilin Zhou**, Dading Chong, et al.

[<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />](https://github.com/qcznlp/GreenPLMs)  

- Propose a simple, heuristic pipeline utilizing bilingual lexicons to translate a source language PLM to a target language PLM with almost no computational cost,significantly reducing carbon emissions for building foundation PLMs in various languages.
</div>
</div>

## 🤖 NLP Tasks and Datasets
### 📂 Dataset
- ``ACL 2024`` [FinTextQA: A Dataset for Long-form Financial Question Answering](),
Jian Chen, **Peilin Zhou**, Yining Hua, et al.

### 🗣️ Spoken Language Understanding

- ``ICASSP 2022`` [Joint Multiple Intent Detection and Slot Filling via Self-distillation](https://arxiv.org/pdf/2108.08042),
Lisong Chen, **Peilin Zhou**, Yuexian Zou.
- ``INTERSPEECH 2022`` [Calibrate and Refine! A Novel and Agile Framework for ASR-error Robust Intent Detection](https://arxiv.org/pdf/2205.11008),
**Peilin Zhou**, Dading Chong, Helin Wang, and Qingcheng Zeng.
- ``INTERSPEECH 2022`` [Low-resource Accent Classification in Geographically-proximate Settings: A Forensic and Sociophonetics Perspective](https://arxiv.org/pdf/2206.12759),
Qingcheng Zeng, Dading Chong, **Peilin Zhou**, Jie Yang
- ``ICASSP 2021`` [Sentiment Injected Iteratively Co-Interactive Network for Spoken Language Understanding](https://web.pkusz.edu.cn/adsp/files/2021/03/黄芝琪ICASSP2021.pdf), Zhiqi Huang, Fenglin Liu, **Peilin Zhou**, Yuexian Zou.
- ``INTERSPEECH 2021`` [Semantic Transportation Prototypical Network for Few-shot Intent Detection](https://web.pkusz.edu.cn/adsp/files/2021/10/Semantic-Transportation-Prototypical-Network-for-Few-Shot-Intent-Detection.pdf), Weiyuan Xu, **Peilin Zhou**, Chenyu You, Yuexian Zou.
- ``ICPR 2020`` [PIN: A novel parallel interactive network for spoken language understanding](https://arxiv.org/pdf/2009.13431), **Peilin Zhou**, Zhiqi Huang, Fenglin Liu, Yuexian Zou.

### 📚 Machine Reading Comprehension
- ``ICASSP 2021`` [Adaptive bi-directional attention: Exploring multi-granularity representations for machine reading comprehension](https://arxiv.org/pdf/2012.10877),
Nuo Chen, Fenglin Liu, Chenyu You, **Peilin Zhou**, Yuexian Zou

### 🎙️ Audio Pretraining
- ``ICASSP 2023`` [Masked Spectrogram Prediction for Self-supervised Audio Pre-training](https://arxiv.org/pdf/2204.12768),
Dading Chong, Helin Wang, **Peilin Zhou**, Qingcheng Zeng

# 🎖 Honors and Awards
- *2023.10* The Third Prize of AI Hackathon (Healthcare Track) by Baichuan AI & Amazon Cloud. 
- *2020.10* The Second Prize of Few-shot Spoken Language Understanding Challenge by SMP. 
- *2020.10* The Second Prize Scholarship by Peking University.
- *2016.09* Academic Excellence Scholarship by Hohai University. 
- *2015.05* National Scholarship by Ministry of Education of the People’s Republic of China. 

# 📖 Educations
- *2022.09 - 2026.01*, Ph.D. in Data Science Analytics, HKUST. 
- *2018.09 - 2021.7*, M.Sc. in Computer Applied Technology, Peking University. 
- *2013.09 - 2017.7*, B.Eng. in Telecommunication Engineering, Hohai University.

# 🧑‍🔧 Academic Services
- Reviewer (or PC Member): TKDE, TOIS, KDD 2025, ICLR 2025, ICCV 2025, WWW 2025/2024, CVPR 2025/2024, AAAI 2025/2024, NeurIPS 2025/2024/2023/2022, EMNLP 2023, ACL 2025/2024/2023, ICASSP 2024/2023/2021, COLING 2023/2022, Interspeech 2021, Neural Computing and Application

# 💻 Internships
- *2022.07 - 2022.09*, Reseach Assistant, supervised by Sunghun KIM, Hong Kong University of Science and Technology.
- *2021.07 - 2022.08*, Reseach Assistant, supervised by Jie Yang, School of Medicine, Zhejiang University.
- *2021.05 - 2022.07*, AI Researcher, Upstage.
- *2021.07 - 2022.08*, Visiting Student, The Chinese University of Hong Kong (Shenzhen).

## 🗺️ Visitor Map
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.11.0/umd/popper.min.js" integrity="sha384-b/U6ypiBEHpOf/4+1nzFpr53nxSS+GLCkfwBdFNTxtclqqenISfwAzpKaMNFNmj4" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/js/bootstrap.min.js" integrity="sha384-h0AbiXch4ZDo7tp9hKZ4TsHbi047NrKGLO3SEJAg45jXxnGIfYzk4Si90RDIqNm1" crossorigin="anonymous"></script>

<script type="text/javascript" id="clustrmaps" src="//clustrmaps.com/map_v2.js?d=K2tNVrlNwuWYOsUQnfNtF89MRzHQLrAaCapBZ1t8oVg&cl=ffffff&w=a"></script>
