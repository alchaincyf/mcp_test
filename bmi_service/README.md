# BMI计算服务 - MCP示例

这是一个使用Model Context Protocol (MCP) 实现的BMI计算服务，基于fastmcp库。

## 功能

- 根据用户提供的身高和体重计算BMI（体质指数）
- 提供BMI分类和健康建议
- 基于MCP协议，可与大型语言模型（如Claude）集成

## 安装

```bash
pip install fastmcp
```

## 使用方法

该服务提供两种使用方式：

1. 作为独立服务运行
2. 与Claude Desktop集成

### 独立服务运行

```bash
python app.py
```

这将启动MCP服务器在默认端口8000上。

### Claude Desktop集成

```bash
fastmcp install app.py
```

这将注册服务到Claude Desktop，允许Claude直接调用BMI计算工具。

## 提供的工具

### calculate_bmi

计算BMI指数的工具，接受以下参数：
- `height`: 身高（厘米）
- `weight`: 体重（千克）

返回计算得到的BMI值（保留两位小数）。

## 提供的提示模板

### health_advice

提供健康建议的提示模板，根据用户的BMI值生成相应的健康建议。

## BMI分类标准

- 低于18.5: 体重过轻
- 18.5-24.9: 正常范围
- 25.0-29.9: 超重
- 30.0及以上: 肥胖

## 计算公式

BMI = 体重(kg) / (身高(m) ^ 2)

## 关于MCP

MCP（Model Context Protocol）是一个允许应用程序与大型语言模型交互的协议，提供三种基本功能：
- 资源（Resources）：应用程序控制的上下文数据
- 工具（Tools）：模型可以调用的函数
- 提示（Prompts）：用户控制的交互模板