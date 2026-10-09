# 实测单木库项目

目标：保存真实扫描及配套文献，建立可追溯的单木实例化参考库与 Awesome 目录。

- 数据来源：[目录](catalog/datasets.csv)，原始数据登记：[datasets.csv](.research/datasets.csv)。
- 下载状态：P0 21/21 完成；P1/P2 批次结束，27 项中 24 项校验通过、3 个 BioDiv3 文件 HTTP 503；TreeScanPL10K P3 已完成 31/31。批次记录见 [.research/runs.csv](.research/runs.csv)。
- 当前归档状态：82 个 release 文件、391,297,450,898 bytes；81 个来源官方校验通过，1 个旧文件仅有历史副本完整性核对。文件数和压缩包成员数不代表树数。
- 后续任务：保留 3 个 BioDiv3 失败文件及访问受限/论文待核实项；完成逐包 native ID 整理、来源去重与逐木几何/尺度/坐标 QA。几何 QA 尚未开展。
- 方法与运行：[methods.csv](.research/methods.csv)、[runs.csv](.research/runs.csv)。运行记录中的路径使用 `${runs_root}` 等占位符；机器路径仅保存在 ignored 本地配置。
- 大文件和论文保存在外部归档根目录；本机路径见 ignored `.research/paths.local.yaml`。存储身份见 [storage.csv](.research/storage.csv)。
- 已有源目录不删除、不修改；个人原始样地点云按引用登记。生成 NPZ/Blender/程序叶片和模拟 LiDAR 不计入实测库。
- 新增下载必须完成官方校验后进入 raw；历史汇集文件的校验依据单独记录。文件存在不等于已通过逐木 QA 或可直接实例化。
- GitHub 已发布：[awesome-single-tree-datasets](https://github.com/shaodwei/awesome-single-tree-datasets)。公开内容为目录、引用和脚本；第三方数据、论文全文与本机路径保存在外部归档。
- 整体复核与历史范围对账见 [复核报告](docs/REVIEW_2026-10-09.md)。TreeScan 论文与发布表口径差异已明确登记；历史排除资产不计入获取统计。
