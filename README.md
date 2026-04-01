
**The contribution of this paper:**

Ⅰ. LGP-FPN is the core of our framework. In contrast to conventional feature pyramids with repeated downsampling and lateral connections, LGP-FPN uses a scale-preserving top-down pathway with progressive upsampling. 
This maintains both spatial resolution and semantic consistency through context-aware aggregation, enhancing small-object detection while reducing parameters and computational cost.

Ⅱ. We design the DRFAM module, which employs dilated convolutions to expand the receptive field without introducing computational overhead, allowing the network to capture richer contextual cues
while preserving fine details of small objects and maintaining global semantics.

Ⅲ. The designed LGP-YOLO is a lightweight traffic sign detection framework that inherits the classical three-stage structure of the YOLO series while integrating the LGP-FPN as its core. By incorporating a context-aware and scale-preserving feature fusion strategy,
the framework effectively enhances the representation of small and multi-scale traffic signs, maintaining high accuracy with reduced computational cost.

**The proposed Method:**

<img width="4330" height="1508" alt="LGP-YOLO-v3" src="https://github.com/user-attachments/assets/932f6b49-c1ba-45f3-9609-4508b2cf236c" />

**The structure of LGP-YOLO network**


<img width="620" height="340" alt="DRFAM-v3" src="https://github.com/user-attachments/assets/04f5747e-b17d-4f01-9f66-1bc2fdd5595e" />

**The structure of proposed DRFAM**



# LGP-YOLO: A lightweight granular perception feature pyramid network with context-awareness for small traffic sign detection

[paper link](https://www.sciencedirect.com/science/article/abs/pii/S0957417426007980)

Abstract: Traffic sign detection plays a vital role in intelligent transportation systems and autonomous driving, yet traffic
sign detection remains challenging since most signs are inherently small objects, which makes them prone to
spatial information degradation, semantic ambiguity during feature fusion, and feature instability in dynamic
driving environments. Although deep learning has improved performance, conventional feature pyramids such as
FPN, PAN, and Bi-FPN struggle to preserve fine-grained spatial details across scales, leading to missed detections
of small signs. This paper presents the lightweight granular perception feature pyramid network (LGP-FPN), a
novel feature fusion architecture designed with scale-preserving and context-aware mechanisms. Previous feature
fusion networks primarily relied on repeated downsampling and dense lateral connections, which often led to
the loss of fine-grained spatial information and weakened feature distinctiveness. In contrast, LGP-FPN preserves
low-level spatial details while progressively integrating high-level semantics through scale-consistent upsampling
and context-guided aggregation, thereby achieving a better balance between semantic abstraction and spatial
precision. The dilated receptive field aggregation module (DRFAM), which expands receptive fields to enhance
contextual perception with only a modest increase in computational cost, is embedded within the LGP-FPN to
further strengthen multi-scale feature fusion. Based on LGP-FPN, we develop LGP-YOLO, a lightweight detector
that achieves both high accuracy and real-time efficiency. Evaluated on TT100K and CCTSDB datasets, LGP-YOLO
achieves precisions of 91.6% and 93.8%, surpassing YOLOv8 by 7.9% and 5.4% respectively, thereby validating
the superiority of the proposed methods.

<!-- PROJECT SHIELDS -->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<img width="512.8" height="550.4" alt="image" src="https://github.com/user-attachments/assets/2dbb3446-1e35-480f-b618-bd7761ba8025" />

<br />

<p align="center">
  <a href="https://github.com/shaojintian/Best_README_template/">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">"完美的"README模板</h3>
  <p align="center">
    一个"完美的"README模板去快速开始你的项目！
    <br />
    <a href="https://github.com/shaojintian/Best_README_template"><strong>探索本项目的文档 »</strong></a>
    <br />
    <br />
    <a href="https://github.com/shaojintian/Best_README_template">查看Demo</a>
    ·
    <a href="https://github.com/shaojintian/Best_README_template/issues">报告Bug</a>
    ·
    <a href="https://github.com/shaojintian/Best_README_template/issues">提出新特性</a>
  </p>

</p>


 本篇README.md面向开发者
 
## 目录

- [上手指南](#上手指南)
  - [开发前的配置要求](#开发前的配置要求)
  - [安装步骤](#安装步骤)
- [文件目录说明](#文件目录说明)
- [开发的架构](#开发的架构)
- [部署](#部署)
- [使用到的框架](#使用到的框架)
- [贡献者](#贡献者)
  - [如何参与开源项目](#如何参与开源项目)
- [版本控制](#版本控制)
- [作者](#作者)
- [鸣谢](#鸣谢)

### 上手指南

请将所有链接中的“shaojintian/Best_README_template”改为“your_github_name/your_repository”



###### 开发前的配置要求

1. xxxxx x.x.x
2. xxxxx x.x.x

###### **安装步骤**

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo

```sh
git clone https://github.com/shaojintian/Best_README_template.git
```

### 文件目录说明
eg:

```
filetree 
├── ARCHITECTURE.md
├── LICENSE.txt
├── README.md
├── /account/
├── /bbs/
├── /docs/
│  ├── /rules/
│  │  ├── backend.txt
│  │  └── frontend.txt
├── manage.py
├── /oa/
├── /static/
├── /templates/
├── useless.md
└── /util/

```





### 开发的架构 

请阅读[ARCHITECTURE.md](https://github.com/shaojintian/Best_README_template/blob/master/ARCHITECTURE.md) 查阅为该项目的架构。

### 部署

暂无

### 使用到的框架

- [xxxxxxx](https://getbootstrap.com)
- [xxxxxxx](https://jquery.com)
- [xxxxxxx](https://laravel.com)

### 贡献者

请阅读**CONTRIBUTING.md** 查阅为该项目做出贡献的开发者。

#### 如何参与开源项目

贡献使开源社区成为一个学习、激励和创造的绝佳场所。你所作的任何贡献都是**非常感谢**的。


1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



### 版本控制

该项目使用Git进行版本管理。您可以在repository参看当前可用版本。

### 作者

xxx@xxxx

知乎:xxxx  &ensp; qq:xxxxxx    

 *您也可以在贡献者名单中参看所有参与该项目的开发者。*

### 版权说明

该项目签署了MIT 授权许可，详情请参阅 [LICENSE.txt](https://github.com/shaojintian/Best_README_template/blob/master/LICENSE.txt)

### 鸣谢


- [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
- [Img Shields](https://shields.io)
- [Choose an Open Source License](https://choosealicense.com)
- [GitHub Pages](https://pages.github.com)
- [Animate.css](https://daneden.github.io/animate.css)
- [xxxxxxxxxxxxxx](https://connoratherton.com/loaders)

<!-- links -->
[your-project-path]:shaojintian/Best_README_template
[contributors-shield]: https://img.shields.io/github/contributors/shaojintian/Best_README_template.svg?style=flat-square
[contributors-url]: https://github.com/shaojintian/Best_README_template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/shaojintian/Best_README_template.svg?style=flat-square
[forks-url]: https://github.com/shaojintian/Best_README_template/network/members
[stars-shield]: https://img.shields.io/github/stars/shaojintian/Best_README_template.svg?style=flat-square
[stars-url]: https://github.com/shaojintian/Best_README_template/stargazers
[issues-shield]: https://img.shields.io/github/issues/shaojintian/Best_README_template.svg?style=flat-square
[issues-url]: https://img.shields.io/github/issues/shaojintian/Best_README_template.svg
[license-shield]: https://img.shields.io/github/license/shaojintian/Best_README_template.svg?style=flat-square
[license-url]: https://github.com/shaojintian/Best_README_template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/shaojintian
