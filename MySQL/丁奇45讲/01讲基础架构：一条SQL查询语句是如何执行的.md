## 基础架构

![](https://static001.geekbang.org/resource/image/0d/d9/0d2070e8f84c4801adbfa03bda1f98d9.png)

### Server层

#### 连接器

每个连接开启一个线程

```mysql
show processlist; # 查看连接	
```

长连接 减少建立连接动作 但会造成内存占用

短连接 建立连接频繁比较耗时

解决方案

1. 定期断开长连接
2. version >= 5.7 执行`mysql_reset_connection`释放连接内存

#### 查询缓存

利 执行结果被缓存，相同查询命中缓存直接从内存读取，速度快

弊 查询缓存失效频繁，对一个表更新会造成所有这张表的缓存失效

#### 分析器

词法解析 语法解析 语义解析

#### 优化器

选择索引 选择表连接顺序

#### 执行器

调用引擎接口取数据

## Q&A

```mysql
select * from T where k=1 # 表T不存在k字段 在哪个阶段报错
```

分析器