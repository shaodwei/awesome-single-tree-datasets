# 获取状态与配套文档

核对日期：2026-10-09。以下为一次归档获取快照；源站后续版本及可用性可能变化。只记录所选发布文件，不声称整站收齐。

82 个不同归档目标，391,297,450,898 bytes（391.3 GB，364.4 GiB）；81 个有官方校验记录，1 个 Järvselja 器官包仅有旧源 / 副本 SHA-256 一致性。历史导入与后续获取按相同归档目标去重，官方验证记录优先。

| 数据源 | 获取状态 | 文件数 | GB | 论文 / 文档状态 |
|---|---|---:|---:|---|
| [Tropical leaf–wood TLS](https://zenodo.org/records/13759407) | 已核验所选源包 | 1 | 0.255 | pdf_saved |
| [BCI tropical TLS + QSM](https://zenodo.org/records/15395386) | 已核验所选源包 | 2 | 1.449 | unresolved_relationship |
| [Quebec hardwood MLS + destructive reference](https://zenodo.org/records/21515256) | 已核验所选源包 | 7 | 0.332 | unresolved_relationship |
| [HuashuTrees](https://zenodo.org/records/19621699) | 已核验所选源包 | 16 | 13.169 | pdf_saved |
| [Demol destructive validation TLS](https://zenodo.org/records/4557401) | 已核验所选源包 | 3 | 0.143 | pdf_saved |
| [EucFACE individual trees + QSM](https://zenodo.org/records/16019825) | 已核验所选源包 | 1 | 9.621 | pdf_saved |
| [Wytham Woods](https://zenodo.org/records/7307956) | 已核验所选源包 | 3 | 40.991 | pdf_saved |
| [TreeML-Data](https://doi.org/10.6084/m9.figshare.c.6788358.v1) | 已核验所选源包 | 8 | 71.865 | pdf_saved |
| [BioDiv3DTrees](https://doi.org/10.25625/8PB1IF) | 部分：QSM / 说明；扫描包待补 | 3 | 108.025 | pdf_saved |
| [FOR-species20K](https://zenodo.org/records/13255198) | 已核验所选源包 | 3 | 27.200 | pdf_saved |
| [Central European segmented TLS trees](https://doi.org/10.48700/datst.xkadt-0cb92) | 已核验所选源包 | 3 | 23.452 | fulltext_xml_saved_pdf_pending |
| [SYSSIFOSS / PyTreeDB source collection](https://doi.org/10.1594/PANGAEA.942856) | 待选择 / 获取 | 0 | 0.000 | pdf_saved |
| [TreeScanPL10K](https://zenodo.org/records/19127709) | 已核验所选源包 | 31 | 94.421 | pdf_saved |
| [IRLTrees3D](https://IRLTrees3D.reliable-ai.org) | 待选择 / 获取 | 0 | 0.000 | pdf_saved |
| [Shivalik Himalaya leaf–wood lidar](https://zenodo.org/records/15362444) | 访问受限 | 0 | 0.000 | pdf_saved |
| [Järvselja measured conifer shoots](https://doi.org/10.17632/rs3f6trdvw.1) | 器官包；仅旧副本一致性 | 1 | 0.374 | missing_pdf |
| [TreeLearn real forest benchmark](https://github.com/ecker-lab/TreeLearn) | 待选择 / 获取 | 0 | 0.000 | pdf_saved |
| [DigiForests](https://www.ipb.uni-bonn.de/data/digiforest-dataset/) | 待选择 / 获取 | 0 | 0.000 | pdf_saved |
| [TreeScope](https://treescope.org/) | 待选择 / 获取 | 0 | 0.000 | pdf_saved |

配套已归档 15 份 PDF，含正式论文、作者稿、预印本和 DigiForests 项目研究文档；不称为 15 篇同行评审论文。Czech 论文已有全文 XML，PDF 待补；Järvselja 论文 PDF 待补；BCI、Quebec 的论文关联仍未完全解析。各源 README、许可及字段信息按可获得程度保存；缺失信息保持未知。

## 失败与访问缺口

BioDiv3DTrees 的 `TLS.tar.zst`、`ULS.tar.zst`、`Graphs.tar.zst` 在批次中返回 HTTP 503，已列入 [手动清单](../catalog/manual_downloads.csv)，不继续无限重试。目前 BioDiv 已获得 QSM 与说明 / 标签，不能作为已获得的真实扫描点云库使用。

SYSSIFOSS、IRLTrees3D、TreeLearn、DigiForests、TreeScope 仍需源文件选择或访问；Shivalik 数据访问受限。数据源许可与论文开放许可分别登记；HuashuTrees 数据许可未由当前 API 明确确认。

## 解释边界

- 文件数、点云数量、ZIP 成员和生物树个体不是同一口径；不汇总跨源独立树总数。
- 所有源均待逐木几何 QA、单位 / 坐标检查及 native-ID 映射；官方校验只证明传输完整性。
- 873 条旧点云成员索引为部分源的索引；TreeScan 的 282 个容器成员包含 Excel XML，不是 282 个单木扫描。
- `tools/status.py` 的 `current_batch_failures` 仅描述当前活跃批次；无活跃进程时为空不代表历史失败已解决。历史缺口以上述手动清单及完成摘要为准。
- 此次复核核对完成摘要、归档登记和当前文件大小，未重新读取并散列全部 391.3 GB，也未进行解压或几何验证。

## 发布表与论文口径差异

TreeScanPL10K 论文报告 10,417 棵树、7,465 条物种标签；当前下载的 `individual_tree_summary.csv` 有 10,447 行，按 `(source_file, treeID)` 复合键无重复，其中 7,468 行的 species 不为 `unknown`，9,525 行的 `completely_inside=1`。以上是源表行数及字段统计，不能证明跨样地生物个体已去重；差异原因未知，保留两种口径。

Czech 的完整包与旧 subset 同时保留，391.3 GB 包含这些重复表示的文件字节。FOR-species20K 开发元数据含 Weiser_2022a / Weiser_2022b / Calders_2022 等源标识；与 SYSSIFOSS、Wytham 的具体同木关系需进一步核对。
