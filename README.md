# Flight Ticket MCP Server

一个基于模型上下文协议(MCP)的航空机票查询服务器。该服务器为AI助手提供标准化的航班实时动态查询功能接口。

## 概述

Flight Ticket MCP Server 实现了供航空机票相关查询操作的工具和资源。它作为AI助手与航空服务系统之间的桥梁，专注于航班实时动态查询功能。

该服务器采用模块化架构，将核心功能、工具和实用程序分离，使其具有高度的可维护性和可扩展性。

## 功能特性

### 航班实时动态查询
- 根据航班号和日期查询航班详细信息
- 实时航班动态和状态信息
- 代码共享航班号显示
- 航班时刻表和机型信息
- 机场和航站楼信息
- 准点率统计
- 值机柜台和登机口信息
- 餐食和行李托运信息
- 天气预报
- 联系电话信息

### 航班路线查询
- 根据出发地、目的地和出发日期查询可用航班
- 支持282个国内城市和机场代码
- 智能城市名称解析（支持城市名、机场代码、完整格式）
- 实时航班价格和航班时刻信息
- 航空公司和机型信息
- 航站楼和登机口信息
- 价格统计和航空公司分布
- 格式化输出结果

## 技术架构

### 核心模块 (Core)
- 航班数据处理

### 工具模块 (Tools)
- 航班实时动态查询工具

### 实用工具 (Utils)
- 数据验证和格式化
- 日期时间处理
- API客户端封装

## 支持的传输协议

本服务器支持三种传输协议：

1. **sse** - Server-Sent Events（默认，适用于Web应用）
2. **stdio** - 标准输入输出（适用于Claude Desktop）
3. **streamable-http** - 可流式HTTP（适用于HTTP客户端）

## 安装

### 前置要求
- Python 3.11 或更高版本
- pip 包管理器

### 基本安装
```bash
# 克隆或下载项目
cd FlightTicketMCPServer

# 安装依赖
pip install -r requirements.txt
```

## 启动方式

### 1. 直接启动（默认SSE模式）

```bash
# 使用主启动文件（默认启动SSE模式，监听127.0.0.1:8000）
python flight_ticket_server.py

# 或者直接运行main.py
python main.py
```

### 2. 调试模式启动

```bash
# 启用调试模式，会输出详细日志
set MCP_DEBUG=true
python flight_ticket_server.py

# Linux/macOS
export MCP_DEBUG=true
python flight_ticket_server.py
```

### 3. 不同传输协议启动

#### SSE模式（默认）
```bash
# 直接启动，使用默认SSE配置（127.0.0.1:8000）
python flight_ticket_server.py
```

#### stdio模式
```bash
# Windows
set MCP_TRANSPORT=stdio
python flight_ticket_server.py

# Linux/macOS
export MCP_TRANSPORT=stdio
python flight_ticket_server.py
```

#### HTTP模式
```bash
# Windows
set MCP_TRANSPORT=streamable-http
set MCP_HOST=127.0.0.1
set MCP_PORT=8000
python flight_ticket_server.py

# Linux/macOS
export MCP_TRANSPORT=streamable-http
export MCP_HOST=127.0.0.1
export MCP_PORT=8000
python flight_ticket_server.py
```

### 4. 环境变量配置

#### 使用 .env 文件（推荐）

项目提供了 `.env.example` 文件作为配置模板：

1. **复制配置模板**：
   ```bash
   # 复制配置模板
   cp .env.example .env
   ```

2. **编辑配置文件**：
   打开 `.env` 文件，根据需要修改配置值：
   ```env
   # MCP服务器配置
   MCP_TRANSPORT=sse
   MCP_HOST=127.0.0.1
   MCP_PORT=8000
   MCP_SSE_PATH=/sse
   
   # 日志配置
   LOG_LEVEL=INFO
   LOG_FILE_PATH=logs/flight_server.log
   LOG_MAX_SIZE=10
   LOG_BACKUP_COUNT=5
   
   # 开发配置
   MCP_DEBUG=false
   ```

3. **配置说明**：
   - `.env` 文件包含敏感配置，不会被提交到版本控制
   - `.env.example` 是安全的模板文件，可以提交到Git
   - 环境变量优先级：系统环境变量 > .env文件 > 程序默认值

#### 直接设置环境变量

如果不使用 `.env` 文件，也可以直接设置环境变量：

支持的环境变量：

| 变量名 | 描述 | 默认值 | 可选值 |
|--------|------|--------|--------|
| `MCP_TRANSPORT` | 传输协议类型 | `sse` | `stdio`, `sse`, `streamable-http` |
| `MCP_HOST` | 服务器主机地址 | `127.0.0.1` | 任何有效IP地址 |
| `MCP_PORT` | 服务器端口 | `8000` | 1-65535 |
| `MCP_PATH` | HTTP路径 | `/mcp` | 任何有效路径 |
| `MCP_SSE_PATH` | SSE路径 | `/sse` | 任何有效路径 |
| `MCP_DEBUG` | 调试模式 | `false` | `true`, `false`, `1`, `0` |
| `LOG_LEVEL` | 日志级别 | `INFO` | `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL` |
| `LOG_FILE_PATH` | 日志文件路径 | `logs/flight_server.log` | 任何有效路径 |
| `LOG_MAX_SIZE` | 日志文件最大大小(MB) | `10` | 正整数 |
| `LOG_BACKUP_COUNT` | 日志备份数量 | `5` | 正整数 |
| `FASTMCP_LOG_LEVEL` | FastMCP日志级别 | `INFO` | `DEBUG`, `INFO`, `WARNING`, `ERROR` |

### 5. 启动验证

启动成功后，您会看到类似输出：

```
Transport: sse
Logging enabled - logs will be saved to logs/ directory
Flight Ticket MCP Server starting...
Transport: sse
All tools registered successfully
Starting SSE transport on 127.0.0.1:8000/sse
```

### 6. 日志文件

服务器启动后会在 `logs/` 目录下生成以下日志文件：

- `flight_server.log` - 一般日志（INFO级别及以上）
- `flight_server_error.log` - 错误日志（ERROR级别）
- `flight_server_debug.log` - 调试日志（仅在调试模式下生成）

### 7. 停止服务器

- **stdio模式**: 按 `Ctrl+C` 停止
- **HTTP/SSE模式**: 按 `Ctrl+C` 或发送SIGTERM信号

## 使用方法

### 与Claude Desktop配置

1. 安装完成后，将服务器添加到Claude Desktop配置文件中：

```json
{
  "mcpServers": {
    "flight-ticket-server": {
      "command": "python",
      "args": ["D:\\FlightTicketMCPServer\\flight_ticket_server.py"],
      "env": {
        "MCP_TRANSPORT": "sse",
        "MCP_HOST": "127.0.0.1",
        "MCP_PORT": "8000"
      }
    }
  }
}
```

2. 配置文件位置：
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`

3. 重启Claude Desktop以加载配置。

### 不同传输协议的配置

#### SSE模式（默认）
```json
{
  "mcpServers": {
    "flight-ticket-server": {
      "command": "python",
      "args": ["D:\\FlightTicketMCPServer\\flight_ticket_server.py"],
      "env": {
        "MCP_TRANSPORT": "sse",
        "MCP_HOST": "127.0.0.1",
        "MCP_PORT": "8000",
        "MCP_SSE_PATH": "/sse"
      }
    }
  }
}
```

#### stdio模式
```json
{
  "mcpServers": {
    "flight-ticket-server": {
      "command": "python",
      "args": ["D:\\FlightTicketMCPServer\\flight_ticket_server.py"],
      "env": {
        "MCP_TRANSPORT": "stdio"
      }
    }
  }
}
```

#### HTTP模式
```json
{
  "mcpServers": {
    "flight-ticket-server": {
      "command": "python",
      "args": ["D:\\FlightTicketMCPServer\\flight_ticket_server.py"],
      "env": {
        "MCP_TRANSPORT": "streamable-http",
        "MCP_HOST": "127.0.0.1",
        "MCP_PORT": "8000",
        "MCP_PATH": "/mcp"
      }
    }
  }
}
```

### 示例操作

配置完成后，您可以要求Claude执行以下操作：

#### 航班实时动态查询
- "查询CA3401航班2024年6月12日的实时动态"
- "查询MU5678航班今天的详细信息"  
- "查看CZ1234航班明天的起飞时间和航站楼信息"

#### 航班路线查询
- "查询重庆到广州明天的航班"
- "搜索上海到北京后天的所有航班"
- "查看深圳飞成都2024年7月20日的航班价格"
- "北京到三亚的航班有哪些选择"

## API参考

### 航班实时动态查询
```python
searchFlightsByNumber(fnum, date)  # 根据航班号和日期查询航班详细信息和实时动态
```

输入参数：
- `fnum`: 航班号 (如: CA3401)
- `date`: 航班起飞日期 (YYYY-MM-DD格式)

输出信息：
- 航班号和代码共享航班号
- 执飞航空公司
- 起飞和到达机场及航站楼
- 起飞和到达时间
- 执飞机型和飞行时长
- 航程距离和准点率
- 值机柜台和登机口
- 餐食和行李托运信息
- 天气预报
- 联系电话

### 航班路线查询
```python
searchFlightRoutes(departure_city, destination_city, departure_date)  # 根据出发地、目的地和日期查询可用航班
```

输入参数：
- `departure_city`: 出发城市名称或机场代码 (如: "重庆", "CKG", "重庆(CKG)")
- `destination_city`: 目的地城市名称或机场代码 (如: "广州", "CAN", "广州(CAN)")
- `departure_date`: 出发日期 (YYYY-MM-DD格式)

输出信息：
- 航班列表（包含航班号、航空公司、起飞到达时间、机场、航站楼、价格）
- 价格统计（最低价、最高价、平均价）
- 航空公司分布统计
- 格式化的查询结果输出
- 支持的城市：282个国内城市和机场

支持的城市格式：
- 城市名：上海、北京、重庆、广州等
- 机场代码：SHA、BJS、CKG、CAN等
- 完整格式：上海(SHA)、北京(BJS)等

## 开发

### 项目结构
```
FlightTicketMCPServer/
├── flight_ticket_server/
│   ├── core/              # 核心业务逻辑
│   ├── tools/             # MCP工具实现
│   ├── utils/             # 实用工具函数
│   └── main.py            # 服务器入口点
├── office_flight_ticket_server/  # 额外模块
├── tests/                 # 测试文件
├── logs/                  # 日志文件目录
├── pyproject.toml         # 项目配置
├── requirements.txt       # 项目依赖
├── flight_ticket_server.py # 主启动文件
├── mcp-config.json        # MCP配置示例
└── README.md              # 项目文档
```

### 测试

```bash
# 运行所有测试
python -m pytest tests/ -v

# 运行基本功能测试
python -m pytest tests/test_basic.py -v

# 运行特定测试
python -m pytest tests/test_basic.py::TestFlightSearch::test_searchFlightsByNumber -v
```

### 日志和调试

- 日志文件位置：`logs/` 目录
- 启用调试模式：设置 `MCP_DEBUG=true`
- 查看实时日志：`tail -f logs/flight_server.log`

## 故障排除

### 常见问题

1. **端口被占用**
   ```bash
   # 更改端口
   set MCP_PORT=8001
   python flight_ticket_server.py
   ```

2. **导入错误**
   ```bash
   # 确保在正确的目录
   cd FlightTicketMCPServer/flight_ticket_server
   python flight_ticket_server.py
   ```

3. **权限问题**
   ```bash
   # 检查文件权限
   ls -la flight_ticket_server.py
   chmod +x flight_ticket_server.py
   ```

### 日志分析

查看日志文件了解详细错误信息：
```bash
# 查看一般日志
cat logs/flight_server.log

# 查看错误日志
cat logs/flight_server_error.log

# 实时监控日志
tail -f logs/flight_server.log
```

## 许可证

MIT License - 查看 [LICENSE](LICENSE) 文件获取详细信息。

## 贡献

欢迎提交Issue和Pull Request来改进这个项目。

## 支持

如果您遇到问题或有功能建议，请在GitHub上创建Issue。
