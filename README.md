# Awesome Single-Tree Datasets

真实扫描单木数据目录，用于单木实例化的几何参考、结构分析与独立验证。

A curated catalog of **real measured tree scans** and their associated papers and documentation. Synthetic trees, procedural foliage and simulated laser scans are excluded from the measured library. Scan-derived QSMs are companion reconstructions, not additional observations.

核验日期：2026-10-08。此目录索引原作者数据，不托管第三方数据或论文。源记录的文件清单、下载大小与校验值见 [download_queue.json](catalog/download_queue.json) 和 [additional_queue.json](catalog/additional_queue.json)。获取状态是本机核验快照，不代表源站长期可用。

## 优先使用的实测单木资源

优先级 A：已具备较直接的单木结构/语义或实测验证参考；B：扩大树种、地区和形态覆盖；C：需要筛选、切分、访问申请或进一步核验。优先级针对本项目的单木实例化用途，不是数据集质量排名。

| 数据源 | 实测范围与口径 | 结构与配套 | 来源 / 论文 | 数据许可 |
|---|---|---|---|---|
| **A · Tropical leaf–wood TLS** | TLS; 148 trees; Australia | XYZ; leaf=0 / wood=1; manually annotated | [数据](https://zenodo.org/records/13759407) · [论文](https://doi.org/10.1016/j.isprsjprs.2025.06.023) | CC-BY-4.0 |
| **A · BCI tropical TLS + QSM** | TLS; 201 trees; 176 trees with QSM; Panama | Separate leaf/wood point clouds; repeated QSM fits | [数据](https://zenodo.org/records/15395386) · 论文关联待核验 | CC-BY-4.0 |
| **A · Quebec hardwood MLS + destructive reference** | MLS; 98 trees; Canada | LAZ; QSM; destructive volume; DBH; field measurements | [数据](https://zenodo.org/records/21515256) · 论文关联待核验 | CC-BY-4.0 |
| **A · HuashuTrees** | TLS; 159 biological trees; 318 seasonal scans; China, Nanjing | Paired leaf-on/leaf-off; field traits; labelled attributes | [数据](https://zenodo.org/records/19621699) · [论文](https://doi.org/10.1038/s41597-026-08199-8) | dataset license not specified in API; verify source terms |
| **A · Demol destructive validation TLS** | TLS; 65 trees; Belgium | Clean scan clouds; QSM; destructive biomass/density | [数据](https://zenodo.org/records/4557401) · [论文](https://doi.org/10.1007/s00468-020-02067-7) | CC-BY-4.0 |
| **B · EucFACE individual trees + QSM** | TLS; 116 trees in associated study; release membership needs inspection; Australia | Individual tree clouds; QSM; analysis code | [数据](https://zenodo.org/records/16019825) · [论文](https://doi.org/10.1016/j.agrformet.2025.110708) | CC-BY-4.0 |
| **B · Wytham Woods** | TLS, leaf-off; 876 released trees; 835 in paper analysis; United Kingdom | PLY scan clouds; optimal QSM; analysis | [数据](https://zenodo.org/records/7307956) · [论文](https://doi.org/10.1002/2688-8319.12197) | CC-BY-4.0 |
| **B · TreeML-Data** | TLS, leaf-off; 3755 individual trees; Germany, Munich | Point clouds; QSM; graphs; transforms; tree/QSM attributes | [数据](https://doi.org/10.6084/m9.figshare.c.6788358.v1) · [论文](https://doi.org/10.1038/s41597-023-02873-x) | CC0 |
| **B · BioDiv3DTrees** | TLS / ULS; 4952 point clouds; 3386 QSMs; source study areas | Scan clouds; species labels; QSM; graphs | [数据](https://doi.org/10.25625/8PB1IF) · [论文](https://doi.org/10.1038/s41597-025-06421-7) | CC-BY-4.0 |
| **B · FOR-species20K** | TLS / MLS / ULS; over 20000 point clouds; multi-region collection | Species metadata; mixed scanning modalities | [数据](https://zenodo.org/records/13255198) · [论文](https://doi.org/10.1111/2041-210X.14503) | GPL-3.0-or-later (record) |
| **B · Central European segmented TLS trees** | TLS; 3618 segmented scan clouds; Czech Republic | Leaf-on/off scans; measured traits; structural metadata | [数据](https://doi.org/10.48700/datst.xkadt-0cb92) · [论文](https://doi.org/10.1016/j.dib.2026.113021) | CC-BY-NC-4.0 |
| **C · SYSSIFOSS / PyTreeDB source collection** | TLS / ULS / ALS; source releases across 12 forest plots; no aggregate unique count claimed; Germany | Matched scan modalities; traits; acquisition metadata | [数据](https://doi.org/10.1594/PANGAEA.942856) · [论文](https://doi.org/10.5194/essd-14-2989-2022) | see PANGAEA source record |
| **C · TreeScanPL10K** | TLS plot clouds with tree IDs; 10417 segmented trees in 272 plots; Poland | treeID; treeSP; completelyInside; tree/plot summaries | [数据](https://zenodo.org/records/19127709) · [论文](https://doi.org/10.1038/s41597-026-07269-1) | CC-BY-4.0 |
| **C · IRLTrees3D** | Real-image photogrammetry / 3D reconstruction; tree subset needs source inventory; Ireland | Images; scan-derived geometry; reconstruction benchmark | [数据](https://IRLTrees3D.reliable-ai.org) · [论文](https://openaccess.thecvf.com/content/ICCV2025W/SEA/papers/Chai_IRLTrees3D_A_3D_Reconstruction_Dataset_of_Trees_ICCVW_2025_paper.pdf) | data terms unverified |
| **C · Shivalik Himalaya leaf–wood lidar** | TLS / ALS; restricted file inventory unavailable; India | Leaf/wood classification and field references | [数据](https://zenodo.org/records/15362444) · [论文](https://doi.org/10.1038/s41597-026-06674-w) | CC-BY-4.0 metadata; restricted data access |

## 器官扫描与实例分割补充

这些资源有真实观测依据，但部位范围或标注目的不同，不与完整单木混合统计。

- [Järvselja measured conifer shoots](https://doi.org/10.17632/rs3f6trdvw.1) — 10 measured shoots; Measured needle/shoot STL; source images. Organ-level geometry only; cannot be counted as complete trees. Helpful for needle/shoot reference.
- [TreeLearn real forest benchmark](https://github.com/ecker-lab/TreeLearn) — 156 manually annotated benchmark trees; 6665 automatically labelled training trees; Instance segmentation labels; raw plot clouds. Separate manual benchmark from automatic pseudo-labels. Source data: https://doi.org/10.25625/VPMPID and https://doi.org/10.25625/QUTUWU . Paper preprint arXiv:2309.08471.
- [DigiForests](https://www.ipb.uni-bonn.de/data/digiforest-dataset/) — longitudinal plots; no unique tree count claimed; Stem/crown and instance labels; repeated surveys; field traits. Repeated observations of the same plots are not new trees. Project research document saved; bibliography of data release papers needs completion.
- [TreeScope](https://treescope.org/) — over 1800 reference stems; Stem mapping and reference measurements. Stem detection reference, not an assured whole-crown library. Associated paper arXiv:2310.02162.


## 用于单木实例化时的筛选

1. 对精细枝干/冠层结构，先查看 TLS/高密度 MLS 与完整性证据；ULS/ALS 可作为树冠形状或观测验证，逐木判定能否描述细枝。
2. 需要叶/木参考时，先检查 tropical leaf–wood、BCI、HuashuTrees。需要木质结构与独立体积/生物量验证时，检查 Quebec、Demol 与对应 QSM。
3. 同木跨季节数据保留配对；叶落季扫描没有观测到叶片，不能把后加程序叶片当作实测叶冠。Czech 的生成叶片模型与虚拟 ALS 全部排除于实测库。
4. 区分“整棵树已分割”与“几何无缺失”。遮挡、扫描密度与边界截断都需逐木 QA。TreeScanPL10K 的 completelyInside 只描述树冠是否被样地边界截断。
5. 保留 native tree ID、样地、采集时间、单位和坐标变换；同木的 leaf/wood、点云/QSM/graph、不同拟合和季节不是新增树。
6. FOR-species20K 等合集可能收录其他源；未建立跨源身份映射前，不汇总“全库独立树总数”。

逐源限制和季节/许可说明见 [机器可读目录](catalog/datasets.csv)。单木数据结构见 [实例登记规范](docs/INSTANCE_SCHEMA.md)，纳入标准见 [收录政策](docs/INCLUSION_POLICY.md)。

## 下载与存储

批次 P0 为小型扫描包及属性/说明；P1 为核心点云及相关轻量结构；P2 为大型 QSM；P3 为 TreeScanPL10K 后续批次。当前表按源发布包保留格式。**混合包中的非实测内容不纳入索引**。

下载器支持断点续传、官方大小/MD5 核对及 SHA-256 登记，校验失败保留于隔离目录。原始数据不能被覆盖。使用说明见 [下载工作流](docs/DOWNLOAD_WORKFLOW.md)。受限访问和失败文件见本机生成的手动清单，保持源许可和访问条件。

本仓库只放目录、引用、配置和代码。论文全文、原始点云、压缩包、路径和运行日志保存在独立数据盘。关联文档下载不等于有权重新发布其全文。

## 补充或纠错

新增资源请提交官方数据链接、测量方式、原始数据许可、关联论文、文件大小/校验值及计数口径；同时说明是否含模拟内容或与已有合集重叠。见 [CONTRIBUTING.md](CONTRIBUTING.md)。

目录和本仓库原创代码按 MIT 许可；第三方数据、论文及文档遵守各自许可。
