# MCP测试仓库

这是一个示例仓库，包含了多个使用Model Context Protocol (MCP)协议的应用示例。MCP是一个允许应用程序与大型语言模型（如Claude）交互的协议。

## 仓库内容

本仓库包含以下示例：

1. **BMI计算服务**：一个完整的MCP应用示例，可以计算BMI指数并提供健康建议
2. **简单计算服务**：一个基础的MCP服务示例，展示基本的工具定义和使用
3. **时间服务**：一个使用TypeScript的MCP服务示例

## 快速开始

### 安装依赖

```bash
pip install -r requirements.txt
```

### 运行BMI计算服务

```bash
python app.py
```

服务将在 http://localhost:8000 上启动。

### 与Claude集成

要将BMI服务与Claude Desktop集成，可以使用:

```bash
fastmcp install app.py
```

或复制`claude_desktop_config.json`到Claude Desktop的配置目录。

## 文件说明

- `app.py`: 主要的BMI计算服务应用
- `server.py`: 简单MCP服务器示例
- `requirements.txt`: 项目依赖
- `claude_desktop_config.json`: Claude Desktop集成配置
- `操作指引.md`: 详细的操作指南
- `bmi_service/`: BMI计算服务的独立实现
- `src/services/`: 其他服务实现示例

## 更多信息

详细的使用说明和操作步骤请参考[操作指引](./操作指引.md)文档。

## 关于MCP

MCP（Model Context Protocol）是一个允许应用程序与大型语言模型交互的协议，提供三种基本功能：
- **资源（Resources）**：应用程序控制的上下文数据
- **工具（Tools）**：模型可以调用的函数
- **提示（Prompts）**：用户控制的交互模板

更多信息请参考：
- [MCP GitHub仓库](https://github.com/modelcontextprotocol/python-sdk)
- [fastmcp GitHub仓库](https://github.com/jlowin/fastmcp)