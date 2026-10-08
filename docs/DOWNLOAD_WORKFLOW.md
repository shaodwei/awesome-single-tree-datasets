# 下载工作流

建议目录：archive_root/raw/<dataset_id>/ 保存校验通过的源包；staging/ 保存断点；documentation/<dataset_id>/ 保存论文、README、字段词典和原始许可；source_metadata/ 保存源记录快照；runs/ 保存下载状态与日志；manual_inbox/<dataset_id>/ 接收人工下载。

原始目录不可覆盖。下载器先检查空间与 AgentHub 的 codex 写锁，再获取单下载器进程锁，最多 2 路下载。空间保留量默认 1024 GiB。源大小与 MD5 通过后计算 SHA-256，原子发布到 raw，追加 MANIFEST.jsonl。HTML 响应不会当成数据。

安装 Python 3 后，持有 archive_root 的 codex 写锁时执行：

```powershell
python tools/library_io.py --queue catalog/download_queue.json --root X:/ResearchData/SingleTreeLibrary --phase P0 --reserve-gib 1024 --budget-gib 400 --release-lock
```

完整批次改为 `--phase P1,P2`；后续 TreeScanPL10K 使用 `--queue catalog/additional_queue.json --phase P3`。不要同时启动第二下载器。Windows 主机如 PATH 上的 Python 不可用，用实际 Python 完整路径。

同一队列可重复执行：已验证的文件重新核对后跳过，未完整文件按服务端 Range 支持续传；校验失败文件隔离。服务端不能可靠续传时重新获取该文件。不要把未完整 `.part` 改成正式文件。

手动下载失败文件放入 manual_inbox/<dataset_id>/<原文件名>；先核对队列大小和官方 MD5。当前后台批次结束后再统一导入，避免与正在写入的文件冲突。数据许可/受限访问通过官方机制处理。

运行状态在 runs/<run_id>/status.json；summary.json 仅在整批结束时产生。部分失败不会伪装为全批完成。机器断电后先确认旧 PID 已消失，再由同一任务处理残留 .downloader.lock 和 AgentHub 锁，保留 staging。

工程实现已做 read-only Claude review，以及有效续传、服务器忽略 Range、错误校验值隔离、已有 raw 冲突保留和路径越界测试。
