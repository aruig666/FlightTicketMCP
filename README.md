# Flight Ticket MCP Server

一个基于模型上下文协议(MCP)的航空机票查询服务器。该服务器为AI助手提供标准化的航班实时动态查询功能接口。

## 概述

Flight Ticket MCP Server 实现了供航空机票相关查询操作的工具和资源。它作为AI助手与航空服务系统之间的桥梁，专注于航班实时动态查询功能。

该服务器采用模块化架构，将核心功能、工具和实用程序分离，使其具有高度的可维护性和可扩展性。

## 功能特性

### 航班路线查询
- 根据出发地、目的地和出发日期查询可用航班
- 支持282个国内城市和机场代码
- 智能城市名称解析（支持城市名、机场代码、完整格式）
- 实时航班价格和航班时刻信息
- 航空公司和机型信息
- 航站楼和登机口信息
- 价格统计和航空公司分布
- 格式化输出结果

### 航班中转路线查询
- 根据出发地、中转地、目的地查询联程航班
- 支持自定义最小和最大中转时间（默认2-5小时）
- 智能筛选符合中转时间要求的航班组合
- 提供完整的两段航程信息
- 支持国内外航线中转查询
- 详细的中转时间计算和验证

### 天气信息查询
- **按经纬度查询**：精确地理位置天气查询
- **按城市名查询**：支持主要城市直接查询
- 支持历史、当前和未来天气数据
- 提供温度、湿度、风速、天气状况等详细信息
- 自动处理时区和日期范围
- 支持武汉、北京、上海等主要城市预设

### 日期时间工具  
- 获取当前系统日期（YYYY-MM-DD格式）
- 获取当前系统日期时间（YYYY-MM-DD HH:mm:ss格式）
- 为其他功能提供标准化的日期时间支持
- 自动处理时区和格式转换

### 实时航班跟踪 (OpenSky Network)
- **实时航班状态查询**：基于OpenSky Network的全球航班实时追踪
- **航班呼号搜索**：支持通过航班呼号查询实时位置和状态
- **机场周边航班**：查询指定机场20公里范围内的所有航班
- **区域航班查询**：查询任意地理区域内的航班分布
- **批量航班跟踪**：同时监控多个航班的实时状态
- **免费数据源**：使用OpenSky Network免费API，无需密钥注册

### 数据处理与智能化
- **智能城市解析**：支持多种城市输入格式（城市名、机场代码、完整格式）
- **参数验证**：全面的输入参数验证和错误处理
- **结果格式化**：统一的JSON格式输出，便于AI助手解析
- **错误恢复**：完善的异常处理和降级机制
- **日志记录**：详细的操作日志和调试信息

## 技术架构

### 核心模块 (Core)
- 航班数据模型和结构定义
- 机场、航空公司、航班、价格等数据模型
- 航班中转和座位配置数据结构

### 工具模块 (Tools)
- **航班搜索工具** (`flight_search_tools.py`) - 航班路线查询功能
- **航班中转工具** (`flight_transfer_tools.py`) - 多段航程和中转查询  
- **天气查询工具** (`weather_tools.py`) - 基于经纬度和城市的天气查询
- **日期时间工具** (`date_tools.py`) - 日期时间获取和处理
- **实时航班跟踪工具** (`simple_opensky_tools.py`) - 基于OpenSky Network的实时航班追踪

### 实用工具 (Utils)
- **城市字典** (`cities_dict.py`) - 282个城市和机场代码映射
- **数据验证器** (`validators.py`) - 输入参数验证和格式检查
- **日期工具** (`date_utils.py`) - 日期格式化和时区处理
- **API客户端** (`api_client.py`) - HTTP请求封装和错误处理

### MCP集成层
- **FastMCP服务器** - 基于FastMCP框架的MCP协议实现
- **多传输协议支持** - stdio、SSE、HTTP传输协议
- **工具注册管理** - 统一的工具注册和调用机制
- **环境配置管理** - 灵活的配置和环境变量支持

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
cd FlightTicketMCP

# 安装依赖
pip install -r requirements.txt

# 安装OpenSky Network API（实时航班跟踪）
pip install python-opensky
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

#### 航班路线查询
- "查询重庆到广州明天的航班"
- "搜索上海到北京后天的所有航班"
- "查看深圳飞成都2024年7月20日的航班价格"
- "北京到三亚的航班有哪些选择"
- "帮我找一下成都到杭州下周二的航班信息"

#### 航班中转查询
- "查询北京经香港到纽约的中转航班"
- "搜索上海经迪拜到伦敦的联程航班，中转时间3-6小时"
- "查找广州经新加坡到悉尼的航班，最短中转2小时"
- "北京到洛杉矶，经东京中转的航班有哪些"

#### 天气信息查询
- "查询北京今天和明天的天气情况"
- "上海的天气怎么样"
- "查询纬度39.9042，经度116.4074的天气"（北京坐标）
- "武汉本周的天气预报"
- "查询重庆2024年7月15日到7月17日的天气"

#### 日期时间查询
- "今天是几号"
- "现在的日期和时间是什么"
- "帮我获取当前日期"

#### 实时航班跟踪（OpenSky Network）
- "查询中国国航CCA1234航班的实时状态"
- "北京首都机场周边现在有哪些航班"
- "查看上海浦东机场30公里范围内的航班"
- "搜索所有中国国航(CCA)的实时航班"
- "查询珠三角地区正在飞行的航班"
- "帮我跟踪CCA1234和CSN5678两个航班的位置"

#### 综合查询示例
- "我要从成都飞北京，明天出发，顺便告诉我北京的天气"
- "查询上海到广州的航班，还有广州的天气情况"
- "帮我规划从重庆到东京的行程，需要中转，并查看目的地天气"
- "查询CCA1234航班状态，还有北京首都机场的实时航班情况"

## API参考

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

### 航班中转路线查询
```python
getTransferFlightsByThreePlace(from_place, transfer_place, to_place, min_transfer_time, max_transfer_time)
```

输入参数：
- `from_place`: 出发地城市名称或机场代码 (如: "北京", "BJS")
- `transfer_place`: 中转地城市名称或机场代码 (如: "香港", "HKG")  
- `to_place`: 目的地城市名称或机场代码 (如: "纽约", "NYC")
- `min_transfer_time`: 最小中转时间（小时），默认2.0小时
- `max_transfer_time`: 最大中转时间（小时），默认5.0小时

输出信息：
- 符合条件的中转航班组合列表
- 第一段航程详细信息（出发地到中转地）
- 第二段航程详细信息（中转地到目的地）
- 实际中转时间计算
- 航班号、时间、机场等详细信息

### 天气信息查询

#### 按经纬度查询
```python
getWeatherByLocation(latitude, longitude, start_date, end_date)
```

输入参数：
- `latitude`: 纬度 (如: 39.9042)
- `longitude`: 经度 (如: 116.4074)
- `start_date`: 开始日期 (YYYY-MM-DD格式)，可选
- `end_date`: 结束日期 (YYYY-MM-DD格式)，可选

#### 按城市名查询
```python
getWeatherByCity(city_name, start_date, end_date)
```

输入参数：
- `city_name`: 城市名称 (如: "北京", "上海", "武汉")
- `start_date`: 开始日期 (YYYY-MM-DD格式)，可选
- `end_date`: 结束日期 (YYYY-MM-DD格式)，可选

输出信息：
- 天气状况描述
- 温度信息（最高温、最低温、当前温度）
- 湿度、风速、风向
- 降水概率和降水量
- 日出日落时间
- 紫外线指数

### 日期时间工具
```python
getCurrentDate()  # 获取当前日期（YYYY-MM-DD格式）
```

输出信息：
- 当前系统日期字符串

### 实时航班跟踪（OpenSky Network）

#### 航班状态查询
```python
getFlightStatus(flight_number, date)  # 根据航班号查询实时状态
```

输入参数：
- `flight_number`: 航班呼号或航空公司代码 (如: "CCA1234", "CCA", "CSN")
- `date`: 日期参数（OpenSky仅支持实时数据，此参数被忽略）

输出信息：
- 匹配的航班列表
- 实时位置（经度、纬度、高度）
- 飞行状态（空中飞行、地面停留、滑行等）
- 飞行速度（地面速度、垂直速度）
- 航班基本信息（呼号、国家、真航迹角）

#### 机场周边航班查询
```python
getAirportFlights(airport_code, flight_type)  # 查询机场周边航班
```

输入参数：
- `airport_code`: 机场代码 (如: "PEK", "PVG", "CAN", "CTU", "SZX")
- `flight_type`: 航班类型（兼容性参数，OpenSky返回所有航班）

支持的机场（50+个中国主要机场）：

**一线城市及直辖市**：
- PEK: 北京首都国际机场, PKX: 北京大兴国际机场
- PVG: 上海浦东国际机场, SHA: 上海虹桥国际机场  
- CAN: 广州白云国际机场, SZX: 深圳宝安国际机场
- CKG: 重庆江北国际机场, TSN: 天津滨海国际机场

**省会城市及重要城市**：
- CTU: 成都双流国际机场, TFU: 成都天府国际机场
- KMG: 昆明长水国际机场, XIY: 西安咸阳国际机场
- HGH: 杭州萧山国际机场, NKG: 南京禄口国际机场
- WUH: 武汉天河国际机场, CSX: 长沙黄花国际机场
- TAO: 青岛流亭国际机场, XMN: 厦门高崎国际机场
- FOC: 福州长乐国际机场, NNG: 南宁吴圩国际机场
- 以及其他30+个省会城市和重要城市机场

**重要旅游城市**：
- SYX: 三亚凤凰国际机场, HAK: 海口美兰国际机场
- DLC: 大连周水子国际机场, YNT: 烟台蓬莱国际机场
- HFE: 合肥新桥国际机场, WNZ: 温州龙湾国际机场
- 以及更多旅游城市机场

输出信息：
- 机场坐标信息
- 30公里范围内的所有航班
- 航班状态分布统计
- 详细的航班位置和速度信息

#### 区域航班查询
```python
getFlightsInArea(min_lat, max_lat, min_lon, max_lon)  # 查询指定区域航班
```

输入参数：
- `min_lat`: 最小纬度
- `max_lat`: 最大纬度
- `min_lon`: 最小经度
- `max_lon`: 最大经度

输出信息：
- 边界框内的所有航班
- 按国家统计的航班分布
- 每架航班的详细实时信息

#### 批量航班跟踪
```python
trackMultipleFlights(flight_numbers, date)  # 批量跟踪多个航班
```

输入参数：
- `flight_numbers`: 航班号或航空公司代码列表 (如: ["CCA", "CSN", "CES"])
- `date`: 日期参数（OpenSky仅支持实时数据）

输出信息：
- 每个查询的详细结果
- 总航班统计信息
- 成功查询的数量统计


## 开发

### 项目结构
```
FlightTicketMCP/
├── core/                   # 核心业务逻辑
│   ├── __init__.py
│   └── flights.py          # 航班数据模型
├── tools/                  # MCP工具实现
│   ├── __init__.py
│   ├── date_tools.py       # 日期时间工具
│   ├── flight_search_tools.py # 航班搜索工具
│   ├── flight_transfer_tools.py # 航班中转工具
│   ├── simple_opensky_tools.py # OpenSky实时航班追踪
│   └── weather_tools.py    # 天气查询工具
├── utils/                  # 实用工具函数
│   ├── __init__.py
│   ├── api_client.py       # HTTP请求客户端
│   ├── cities_dict.py      # 城市机场代码映射
│   ├── date_utils.py       # 日期处理工具
│   └── validators.py       # 输入验证器
├── examples/               # 示例和演示代码
│   ├── opensky_demo.py     # OpenSky功能演示
│   └── simple_opensky_demo.py # 简化版演示
├── logs/                   # 日志文件目录
├── main.py                 # MCP服务器主入口
├── flight_ticket_server.py # 服务器启动脚本
├── mcp-config.json         # MCP配置示例
├── pyproject.toml          # 项目配置
├── requirements.txt        # 项目依赖
├── LICENSE                 # 开源协议
└── README.md               # 项目文档
```

### 日志和调试

- 日志文件位置：`logs/` 目录
- 启用调试模式：设置 `MCP_DEBUG=true`
- 查看实时日志：`tail -f logs/flight_server.log`



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
