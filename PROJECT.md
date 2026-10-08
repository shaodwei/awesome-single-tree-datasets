# 实测单木库项目

目标：保存真实扫描及配套论文/文档，建立可追溯的单木实例化参考库与 Awesome 目录。

- 数据来源：[目录](catalog/datasets.csv)，原始数据登记：[datasets.csv](.research/datasets.csv)。
- 下载：P0 校验完成，P1/P2 后台进行；TreeScanPL10K P3 已登记，等待当前批次后执行。
- 当前任务：完成大包下载与失败补下，逐包提取 native ID，再逐木做完整性、尺度和坐标 QA；未开展树几何重建。
- 方法与运行：[methods.csv](.research/methods.csv)、[runs.csv](.research/runs.csv)。启动时尚未提交 Git，因此初始运行注明 dirty。
- 大文件与论文保存在外部数据根目录；本机路径见 ignored `.research/paths.local.yaml`。存储身份见 [storage.csv](.research/storage.csv)。
- 已有源目录不删除、不修改；个人原始样地点云按引用登记。生成 NPZ/Blender/程序叶片不计入实测库。
- 只有下载成功且大小/官方校验值一致的文件进入 raw。逐木几何 QA 尚未完成，不能称全部可直接实例化。
