# LGP-YOLO: A lightweight granular perception feature pyramid network with context-awareness for small traffic sign detection

[paper link](https://www.sciencedirect.com/science/article/abs/pii/S0957417426007980)

<p align="center">
  <img width="4330" height="1508" alt="LGP-YOLO-v3" src="https://github.com/user-attachments/assets/932f6b49-c1ba-45f3-9609-4508b2cf236c" />
</p>

**The structure of LGP-YOLO network**

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

### Method
<p align="center">
<img width="620" height="340" alt="DRFAM-v3" src="https://github.com/user-attachments/assets/04f5747e-b17d-4f01-9f66-1bc2fdd5595e" />
</p>

**The structure of proposed DRFAM**

<p align="center">
<img width="3121" height="807" alt="FPNbattle" src="https://github.com/user-attachments/assets/12c80715-5cfe-4aab-8d3b-af7d3ac3dafb" />
</p>

**The structure of proposed LGP-FPN**


### Contribution of this paper

Ⅰ. LGP-FPN is the core of our framework. In contrast to conventional feature pyramids with repeated downsampling and lateral connections, LGP-FPN uses a scale-preserving top-down pathway with progressive upsampling. 
This maintains both spatial resolution and semantic consistency through context-aware aggregation, enhancing small-object detection while reducing parameters and computational cost.

Ⅱ. We design the DRFAM module, which employs dilated convolutions to expand the receptive field without introducing computational overhead, allowing the network to capture richer contextual cues
while preserving fine details of small objects and maintaining global semantics.

Ⅲ. The designed LGP-YOLO is a lightweight traffic sign detection framework that inherits the classical three-stage structure of the YOLO series while integrating the LGP-FPN as its core. By incorporating a context-aware and scale-preserving feature fusion strategy,
the framework effectively enhances the representation of small and multi-scale traffic signs, maintaining high accuracy with reduced computational cost.


### **How to use**

1. Environment
Configure in Python environment
```sh
pip install ultralytics
```
2. Configure dataset and dataset files in train.py
```python
from ultralytics import YOLO
import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
if __name__ == '__main__':

    # Load a model, Here use our model file
    model = YOLO('LGP-YOLO.yaml')

    # Train the model, You can use your own datasets file, such as tt100k.yaml
    model.train(data='Datasets/tt100k.yaml', epochs=200, batch=8, imgsz=640, device=0)

    # Evaluate model performance on the validation set, make sure the yaml file same as datasets file
    metrics = model.val(data='Datasets/tt100k.yaml', imgsz=640, batch=1, device=0)
```


### Citation
If use our model, please consider citing:
```sh
@article{zhang2026lightweight,
  title={A Lightweight Granular Perception Feature Pyramid Network with Context-aware for Small Traffic Sign Detection},
  author={Zhang, Yan and Bi, Dengfeng and Huang, Qingqing and Han, Yan and Zhao, Minghang},
  journal={Expert Systems with Applications},
  pages={131885},
  year={2026},
  publisher={Elsevier}
}
```


### Contact Us
If you have any questions or intend to cooperate, feel free to contact us anytime.

Email:s240331138@stu.cqupt.edu.cn



