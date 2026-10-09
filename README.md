# Awesome Single-Tree Datasets

**真实扫描单木数据、关联论文与使用边界。** 为单木实例化、枝干结构分析和独立验证提供可追溯的参考来源。

![Measured scans](https://img.shields.io/badge/data-real_measured_scans-2E7D32)
![Sources](https://img.shields.io/badge/catalog-19_sources-1565C0)
![Checked](https://img.shields.io/badge/review-2026--10--09-455A64)

A curated catalog of real measured tree scans and their papers/documentation. Scan-derived QSMs and graphs are companion reconstructions. Synthetic trees, procedural foliage and simulated scans are excluded from the measured library.

[快速选源](#快速选源) · [核心数据集](#核心数据集) · [补充资源](#补充资源) · [使用与计数](#用于单木实例化时的筛选) · [获取状态](docs/ACQUISITION_STATUS.md) · [手动清单](catalog/manual_downloads.csv) · [下载工作流](docs/DOWNLOAD_WORKFLOW.md)

> **当前获取快照 · 2026-10-09**：82 个源包或配套文件，391.3 GB；81 个通过官方校验，1 个仅验证旧副本一致性。15 份论文 / 研究文档 PDF 已归档，含预印本、作者稿和项目文档。BioDiv3DTrees 的 TLS、ULS、Graphs 三包仍未取得。
>
> 这些是获取与完整性记录；逐木几何 QA、跨源去重和独立树总数仍待建立。第三方数据与论文全文保存于独立归档，本仓库提供索引与来源链接。

## 快速选源

| 参考目的 | 优先检查 | 使用前确认 |
|---|---|---|
| 叶 / 木分离及结构参考 | Tropical leaf–wood、BCI、HuashuTrees | 原始标签、季节配对、遮挡与坐标单位 |
| 枝干体积 / 生物量独立验证 | Quebec、Demol、Wytham、EucFACE | 实测参照与 QSM 的对应 ID、研究样本边界 |
| 扩大树种与形态覆盖 | TreeML、FOR-species20K、Czech | 合集重复、物种标签、许可及混合包排除项 |
| 样地内单木实例与边界 | TreeScanPL10K、SYSSIFOSS、TreeLearn | 逐木提取、边界截断、人工与自动标注区别 |
| 针叶 / 枝梢器官几何 | Järvselja shoots | 部位尺度；不能计为整树 |

## 核心数据集

15 个核心候选。A / B / C 表示本项目使用优先级：直接结构或验证参考 / 扩大覆盖 / 需要筛选或申请；不是数据质量排名。**“已核验所选源包”只指当前队列，不能推导源站所有文件均已收齐或每棵树几何完整。**

| 数据源 · 范围 | 发布口径 | 来源 / 论文 | 数据许可 | 获取快照 |
|---|---|---|---|---|
| **A · Tropical leaf–wood TLS**<br>TLS · Australia | 148 trees | [数据](https://zenodo.org/records/13759407) · [论文](https://doi.org/10.1016/j.isprsjprs.2025.06.023) | CC-BY-4.0 | 已核验所选源包 |
| **A · BCI tropical TLS + QSM**<br>TLS · Panama | 201 trees; 176 trees with QSM | [数据](https://zenodo.org/records/15395386) · 论文关联待核验 | CC-BY-4.0 | 已核验所选源包 |
| **A · Quebec hardwood MLS + destructive reference**<br>MLS · Canada | 98 trees | [数据](https://zenodo.org/records/21515256) · 论文关联待核验 | CC-BY-4.0 | 已核验所选源包 |
| **A · HuashuTrees**<br>TLS · China, Nanjing | 159 biological trees; 318 seasonal scans | [数据](https://zenodo.org/records/19621699) · [论文](https://doi.org/10.1038/s41597-026-08199-8) | dataset license not specified in API; verify source terms | 已核验所选源包 |
| **A · Demol destructive validation TLS**<br>TLS · Belgium | 65 trees | [数据](https://zenodo.org/records/4557401) · [论文](https://doi.org/10.1007/s00468-020-02067-7) | CC-BY-4.0 | 已核验所选源包 |
| **B · EucFACE individual trees + QSM**<br>TLS · Australia | 116 trees in associated study; release membership needs inspection | [数据](https://zenodo.org/records/16019825) · [论文](https://doi.org/10.1016/j.agrformet.2025.110708) | CC-BY-4.0 | 已核验所选源包 |
| **B · Wytham Woods**<br>TLS, leaf-off · United Kingdom | 876 released trees; 835 in paper analysis | [数据](https://zenodo.org/records/7307956) · [论文](https://doi.org/10.1002/2688-8319.12197) | CC-BY-4.0 | 已核验所选源包 |
| **B · TreeML-Data**<br>TLS, leaf-off · Germany, Munich | 3755 individual trees | [数据](https://doi.org/10.6084/m9.figshare.c.6788358.v1) · [论文](https://doi.org/10.1038/s41597-023-02873-x) | CC0 | 已核验所选源包 |
| **B · BioDiv3DTrees**<br>TLS / ULS · source study areas | 4952 point clouds; 3386 QSMs | [数据](https://doi.org/10.25625/8PB1IF) · [论文](https://doi.org/10.1038/s41597-025-06421-7) | CC-BY-4.0 | 部分：QSM / 说明；扫描包待补 |
| **B · FOR-species20K**<br>TLS / MLS / ULS · multi-region collection | over 20000 point clouds | [数据](https://zenodo.org/records/13255198) · [论文](https://doi.org/10.1111/2041-210X.14503) | GPL-3.0-or-later (record) | 已核验所选源包 |
| **B · Central European segmented TLS trees**<br>TLS · Czech Republic | 3618 segmented scan clouds | [数据](https://doi.org/10.48700/datst.xkadt-0cb92) · [论文](https://doi.org/10.1016/j.dib.2026.113021) | CC-BY-NC-4.0 | 已核验所选源包 |
| **C · SYSSIFOSS / PyTreeDB source collection**<br>TLS / ULS / ALS · Germany | source releases across 12 forest plots; no aggregate unique count claimed | [数据](https://doi.org/10.1594/PANGAEA.942856) · [论文](https://doi.org/10.5194/essd-14-2989-2022) | see PANGAEA source record | 待选择 / 获取 |
| **C · TreeScanPL10K**<br>TLS plot clouds with tree IDs · Poland | paper: 10417 trees / 7465 species-labelled; released summary: 10447 unique source-file/treeID rows / 7468 labelled; 272 plots | [数据](https://zenodo.org/records/19127709) · [论文](https://doi.org/10.1038/s41597-026-07269-1) | CC-BY-4.0 | 已核验所选源包 |
| **C · IRLTrees3D**<br>Real-image photogrammetry / 3D reconstruction · Ireland | tree subset needs source inventory | [数据](https://IRLTrees3D.reliable-ai.org) · [论文](https://openaccess.thecvf.com/content/ICCV2025W/SEA/papers/Chai_IRLTrees3D_A_3D_Reconstruction_Dataset_of_Trees_ICCVW_2025_paper.pdf) | data terms unverified | 待选择 / 获取 |
| **C · Shivalik Himalaya leaf–wood lidar**<br>TLS / ALS · India | restricted file inventory unavailable | [数据](https://zenodo.org/records/15362444) · [论文](https://doi.org/10.1038/s41597-026-06674-w) | CC-BY-4.0 metadata; restricted data access | 访问受限 |

<details>
<summary>展开逐源结构与使用限制</summary>

- **Tropical leaf–wood TLS** — XYZ; leaf=0 / wood=1; manually annotated。Leaf/wood geometry reference; retain official train/test splits.
- **BCI tropical TLS + QSM** — Separate leaf/wood point clouds; repeated QSM fits。Leaf and wood files represent the same tree; QSM replicates are not additional trees. Record links no specific paper; paper attribution unresolved.
- **Quebec hardwood MLS + destructive reference** — LAZ; QSM; destructive volume; DBH; field measurements。Join by native Tree ID. Associated manuscript named in Readme.docx; publication DOI not supplied by current record.
- **HuashuTrees** — Paired leaf-on/leaf-off; field traits; labelled attributes。Do not count both seasons or sample/full-release overlap twice. Article license does not establish dataset license.
- **Demol destructive validation TLS** — Clean scan clouds; QSM; destructive biomass/density。QSM is measured-scan reconstruction of wood. Archive MAT file count is not a tree population count.
- **EucFACE individual trees + QSM** — Individual tree clouds; QSM; analysis code。Distinguish paper analysis population from all released files.
- **Wytham Woods** — PLY scan clouds; optimal QSM; analysis。Download PLY once; TXT is another representation of the same trees. Study boundary exclusions explain count difference.
- **TreeML-Data** — Point clouds; QSM; graphs; transforms; tree/QSM attributes。40 urban survey projects; graphs and QSM are companion derivatives. Keep original coordinate transformations.
- **BioDiv3DTrees** — Scan clouds; species labels; QSM; graphs。TLS/ULS and derivatives may overlap by tree. Large QSM archive is lower download priority; do not add counts across representations.
- **FOR-species20K** — Species metadata; mixed scanning modalities。Aggregates other datasets: cross-source overlap must be checked. Crown/branch completeness varies. Test species labels withheld. Dev metadata contains Weiser_2022a (226), Weiser_2022b (2580), Calders_2022 (661), likely linked to SYSSIFOSS/Wytham; tree-by-tree identity matching pending.
- **Central European segmented TLS trees** — Leaf-on/off scans; measured traits; structural metadata。Only SEGMENTED_TREES belongs to measured library. Exclude 273 procedural foliage reconstructions and 15718 simulated ALS scenes. Seasonal clouds are not necessarily distinct trees. Acquired subset and full ZIP overlap; retained release-file bytes include both, not independent observations.
- **SYSSIFOSS / PyTreeDB source collection** — Matched scan modalities; traits; acquisition metadata。PyTreeDB indexes these sources; it is not an independent measured population. Select detailed TLS trees for geometry, preserve matching ULS/ALS as validation.
- **TreeScanPL10K** — treeID; treeSP; completelyInside; tree/plot summaries。Select completelyInside=1 for uncropped crowns; plot boundary flag does not guarantee absence of scan occlusion. Must extract by plot + treeID. Paper and released table counts differ; no explanation inferred. Released summary has 9525 rows with completely_inside=1.
- **IRLTrees3D** — Images; scan-derived geometry; reconstruction benchmark。Project endpoint unavailable during check. Include only tree objects and distinguish photographs/mesh/3DGS; no automatically verified data yet. ICCVW 2025 paper available.
- **Shivalik Himalaya leaf–wood lidar** — Leaf/wood classification and field references。File access restricted. User must request/download through official access mechanism; paper is open. Source lookup resolved to version record 17566270; original requested record 15362444 retained as source pointer.

</details>

## 补充资源

器官、茎干及分割基准与完整单木分开登记。重复观测、自动标签和派生模型保持各自口径。

| 数据源 | 范围与限制 | 获取快照 |
|---|---|---|
| [Järvselja measured conifer shoots](https://doi.org/10.17632/rs3f6trdvw.1) | 10 measured shoots。Organ-level geometry only; cannot be counted as complete trees. Helpful for needle/shoot reference. | 器官包；仅旧副本一致性 |
| [TreeLearn real forest benchmark](https://github.com/ecker-lab/TreeLearn) | 156 manually annotated benchmark trees; 6665 automatically labelled training trees。Separate manual benchmark from automatic pseudo-labels. Source data: https://doi.org/10.25625/VPMPID and https://doi.org/10.25625/QUTUWU . Paper preprint arXiv:2309.08471. | 待选择 / 获取 |
| [DigiForests](https://www.ipb.uni-bonn.de/data/digiforest-dataset/) | longitudinal plots; no unique tree count claimed。Repeated observations of the same plots are not new trees. Project research document saved; bibliography of data release papers needs completion. | 待选择 / 获取 |
| [TreeScope](https://treescope.org/) | over 1800 reference stems。Stem detection reference, not an assured whole-crown library. Associated paper arXiv:2310.02162. | 待选择 / 获取 |


## 用于单木实例化时的筛选

1. 对精细枝干/冠层结构，先查看 TLS/高密度 MLS 与完整性证据；ULS/ALS 可作为树冠形状或观测验证，逐木判定能否描述细枝。
2. 需要叶/木参考时，先检查 tropical leaf–wood、BCI、HuashuTrees。需要木质结构与独立体积/生物量验证时，检查 Quebec、Demol 与对应 QSM。
3. 同木跨季节数据保留配对；叶落季扫描没有观测到叶片，不能把后加程序叶片当作实测叶冠。Czech 的生成叶片模型与虚拟 ALS 全部排除于实测库。
4. 区分“整棵树已分割”与“几何无缺失”。遮挡、扫描密度与边界截断都需逐木 QA。TreeScanPL10K 的 completelyInside 只描述树冠是否被样地边界截断。
5. 保留 native tree ID、样地、采集时间、单位和坐标变换；同木的 leaf/wood、点云/QSM/graph、不同拟合和季节不是新增树。
6. FOR-species20K 等合集可能收录其他源；未建立跨源身份映射前，不汇总“全库独立树总数”。

逐源限制和季节/许可说明见 [机器可读目录](catalog/datasets.csv)。单木数据结构见 [实例登记规范](docs/INSTANCE_SCHEMA.md)，纳入标准见 [收录政策](docs/INCLUSION_POLICY.md)。

## 下载与存储

按原作者发布包保留文件名和来源；论文、README、字段字典、许可及校验记录逐源配套。P0、P1/P2、TreeScanPL10K P3 已结束；BioDiv 三个失败包及受限 / 待选择源见 [手动补充清单](catalog/manual_downloads.csv)。

下载器支持断点续传、官方大小 / MD5 核对及 SHA-256 登记，校验失败进入隔离目录。保持原始数据只读、单下载器与 1 TiB 磁盘余量。脚本的锁管理依赖 Windows AgentHub；部署要求与手动文件核验见 [工作流](docs/DOWNLOAD_WORKFLOW.md)。

| 索引 | 内容 |
|---|---|
| [数据源目录](catalog/datasets.csv) / [JSON](catalog/datasets.json) | 科学范围、许可、论文与限制 |
| [获取快照](catalog/acquisition_status.json) | 分源获取状态、文件数、字节数；不是树数 |
| [下载队列](catalog/download_queue.json) / [P3 队列](catalog/additional_queue.json) | 选定源文件、官方校验值与大小 |
| [引用库](catalog/references.bib) | 已登记文献；未解析的关联保持未知 |
| [整体复核](docs/REVIEW_2026-10-09.md) | 证据范围、已修正项和后续 QA |

## 补充或纠错

提交官方数据链接、真实测量方式、原始数据许可、关联论文、文件校验及计数口径；说明模拟内容和跨源重复。参见 [CONTRIBUTING.md](CONTRIBUTING.md)。

目录与原创代码按 [MIT](LICENSE) 许可；第三方数据、论文和文档遵守各自许可。取得论文全文不等于可以重新发布全文。
