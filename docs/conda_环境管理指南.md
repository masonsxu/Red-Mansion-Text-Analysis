# Conda 环境管理指南

## 环境导出操作

```bash
# 导出当前环境（跨平台兼容）
conda env export --no-builds | grep -v "prefix" > environment.yml

# 包含系统特定依赖（谨慎使用）
conda env export > environment_full.yml
```

## 环境恢复操作

```bash
# 新建环境
conda env create -f environment.yml

# 更新现有环境
conda env update -f environment.yml --prune
```

## 常见问题处理

### 1. 权限错误

```bash
sudo chown -R $USER:$USER /opt/conda/envs/your_env
```

### 2. 包版本冲突

```bash
conda search package_name --info
conda install package_name=版本号
```

### 3. 多平台兼容

```yaml
# environment.yml 示例
channels:
  - defaults
dependencies:
  - python=3.8
  - pip
  - numpy
  - pip:
      - torch==1.9.0+cu102
```
