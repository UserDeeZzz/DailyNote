## 日志系统

### redo log 重做日志

![](https://s1.ax1x.com/2020/08/24/dyNyOH.png)

`InnoDB`引擎独有的物理日志 记录数据页变更 保证异常重启提交记录不丢失的机制

这种能力叫作`crash safe`

同时完成事务组提交`GTID` 减少随机写入磁盘次数 redo log持久化并且顺序写入

保证事务的持久性

- `writepos` 写入点
- `checkpoint` 清除点

`writepos`到`checkpoint`之间是可以写入的空白部分 当`writepos`追上`checkpoint`则无法更新

`innodb_flush_log_at_trx_commit`这个参数设置成1的时候，每次事务的redo log都直接持久化到磁盘

### undo log 回滚日志

用于事务失败回滚

保证事务的原子性

实现`MVCC`多版本控制

### bin log 归档日志

server层 记录语句原始逻辑的逻辑日志 追加写 用于和relay log主从复制

### 两阶段提交

在这被行数据在内存中被修改前，写入`undo log`

![](https://static001.geekbang.org/resource/image/2e/be/2e5bff4910ec189fe1ee6e2ecc7b4bbe.png)

1. `redo log`存在，`binlog`不存在 ，`undo log`回滚
2. `redo log`存在，`binlog`存在，`redo log`提交

