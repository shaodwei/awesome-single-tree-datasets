# 单木登记与实例化检查

每个实测观测建议记录以下字段；未知项保留 null，不推断成实测值。

| 字段 | 定义 |
|---|---|
| instance_id | 本库稳定 ID，由 dataset release + plot + native tree ID 构成 |
| biological_tree_id | 已有证据确认的同一生物个体；无法跨源确认时保持未解析 |
| observation_id | 同木的采集时间、传感器、季节或扫描组 |
| native_tree_id / plot_id | 源名称与连接字段，不改写原文件 |
| source_file / member | 原始压缩包与成员名；关联校验和 |
| modality / acquisition_date / leaf_state | 测量方式、时间与季节 |
| species / taxonomy_source | 原始树种及命名依据 |
| unit / CRS / transform | 长度单位、坐标系统、到实例原点的显式变换 |
| component | whole-tree / leaf / wood / stem / shoot，避免混淆部位 |
| geometry_kind | measured point cloud / photogrammetric mesh / QSM / graph / 3DGS |
| completeness | source flag、边界截断、主干/树梢/细枝/树冠遮挡的逐项检查 |
| measured_attributes | 现场 DBH/高度/体积等，附单位与方法 |
| derived_attributes | 点云/QSM 推算量，附方法/参数和 parent observation |
| rights / references | 数据许可、论文与说明来源 |
| qa_status | pending / reviewed / excluded，附理由 |

处理后的坐标平移/旋转、切分、重采样、改标签各建立新版本并登记 parent。原始坐标与属性保持在 raw 中。

进入实例化可用子库前应至少检查：点云尺度和轴向、树基/树梢、冠层边界及遮挡、异树混入、叶木标签/树种、匹配 QSM 的单位与坐标。QSM 只代表拟合木质骨架；扫描缺失的叶片不能作为已测叶片补写。材料颜色不是实测光谱。

当前索引是扫描包成员清单和 LAS/LAZ 头信息，未做所有点的几何检查，不能直接等同“可实例化树”清单。
