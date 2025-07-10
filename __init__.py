"""
Flight Ticket MCP Server - 航空机票预订和管理服务器

一个基于模型上下文协议(MCP)的航空机票服务，提供:
- 航班搜索和查询
- 机票预订和管理  
- 订单处理和查询
- 乘客信息管理

版本: 1.0.0
作者: Your Name
"""

__version__ = "1.0.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

from . import core, tools, utils

__all__ = ["core", "tools", "utils"] 