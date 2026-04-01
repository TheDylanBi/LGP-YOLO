LGP-YOLO: A lightweight granular perception feature pyramid network with context-awareness for small traffic sign detection


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
