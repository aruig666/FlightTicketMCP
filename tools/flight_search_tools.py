"""
Flight Search Tools - 航班实时动态查询工具

提供根据航班号查询航班详细信息和实时动态的功能
"""

from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
import json
import random
import logging

# 初始化日志器
logger = logging.getLogger(__name__)


def searchFlightsByNumber(fnum: str, date: str) -> Dict[str, Any]:
    """
    根据航班号及航班起飞日期查询航班详细信息和实时动态
    
    Args:
        fnum: 航班号 (如: CA3401)
        date: 航班起飞日期 (YYYY-MM-DD格式)
        
    Returns:
        包含航班详细信息和实时动态的字典
    """
    logger.info(f"开始查询航班: {fnum}, 日期: {date}")
    
    try:
        # 验证输入参数
        if not fnum or not date:
            logger.warning(f"无效参数 - 航班号: '{fnum}', 日期: '{date}'")
            return {
                "status": "error",
                "message": "航班号和日期不能为空",
                "error_code": "INVALID_PARAMS"
            }
        
        # 解析日期
        try:
            flight_date = datetime.strptime(date, "%Y-%m-%d")
            logger.debug(f"日期解析成功: {flight_date}")
        except ValueError as e:
            logger.warning(f"日期格式错误: {date}, 错误: {e}")
            return {
                "status": "error",
                "message": "日期格式不正确，请使用YYYY-MM-DD格式",
                "error_code": "INVALID_DATE_FORMAT"
            }
        
        # 模拟根据航班号生成不同的航班信息
        logger.debug(f"生成航班信息: {fnum}")
        flight_info = _generate_flight_info(fnum, date)
        
        # 格式化输出结果
        logger.debug(f"格式化航班结果: {fnum}")
        formatted_result = _format_flight_result(flight_info, date)
        
        result = {
            "status": "success",
            "flight_number": fnum,
            "flight_date": date,
            "flight_info": flight_info,
            "formatted_output": formatted_result,
            "query_time": datetime.now().isoformat()
        }
        
        logger.info(f"航班查询成功: {fnum}, 航线: {flight_info['origin_airport']['name']} -> {flight_info['destination_airport']['name']}")
        return result
        
    except Exception as e:
        logger.error(f"查询航班信息失败: {fnum}, 错误: {str(e)}", exc_info=True)
        return {
            "status": "error",
            "message": f"查询航班信息失败: {str(e)}",
            "error_code": "QUERY_FAILED"
        }


def _generate_flight_info(fnum: str, date: str) -> Dict[str, Any]:
    """
    根据航班号生成模拟的航班信息
    
    Args:
        fnum: 航班号
        date: 航班日期
        
    Returns:
        航班详细信息字典
    """
    # 根据航班号前缀确定航空公司
    airline_mapping = {
        "CA": {"name": "中国国际航空股份有限公司", "phone": "95583"},
        "MU": {"name": "中国东方航空股份有限公司", "phone": "95530"},
        "CZ": {"name": "中国南方航空股份有限公司", "phone": "95539"},
        "HU": {"name": "海南航空股份有限公司", "phone": "95339"},
        "3U": {"name": "四川航空股份有限公司", "phone": "400-830-0999"},
        "FM": {"name": "上海航空有限公司", "phone": "95530"},
        "9C": {"name": "春秋航空有限公司", "phone": "95524"}
    }
    
    # 获取航班前缀
    prefix = fnum[:2]
    airline_info = airline_mapping.get(prefix, {"name": "示例航空公司", "phone": "400-000-0000"})
    
    # 模拟机场信息
    airports = [
        {"code": "PEK", "name": "北京首都国际机场", "phone": "010-12360/010-85734500"},
        {"code": "SHA", "name": "上海虹桥国际机场", "phone": "021-96990"},
        {"code": "SZX", "name": "深圳宝安国际机场", "phone": "0755-23456789"},
        {"code": "CAN", "name": "广州白云国际机场", "phone": "020-96158"},
        {"code": "CTU", "name": "成都天府国际机场", "phone": "028-85205555"}
    ]
    
    # 随机选择起飞和到达机场
    origin_airport = random.choice(airports)
    destination_airports = [a for a in airports if a != origin_airport]
    destination_airport = random.choice(destination_airports)
    
    # 生成代码共享航班号
    share_codes = [
        f"ZH{random.randint(9100, 9999)}",
        f"SC{random.randint(9000, 9999)}",
        f"KY{random.randint(9600, 9999)}"
    ]
    
    # 机型列表
    aircraft_types = [
        "空客A321-271N neo ACF",
        "波音737-800",
        "空客A320-214",
        "波音787-9",
        "空客A330-200",
        "波音777-300ER"
    ]
    
    # 生成起飞和到达时间
    departure_hour = random.randint(6, 22)
    departure_minute = random.choice([0, 15, 30, 45])
    flight_duration = random.randint(120, 480)  # 2-8小时
    
    departure_time = f"{departure_hour:02d}:{departure_minute:02d}"
    arrival_time_dt = datetime.strptime(departure_time, "%H:%M") + timedelta(minutes=flight_duration)
    arrival_time = arrival_time_dt.strftime("%H:%M")
    
    # 计算飞行时长
    hours = flight_duration // 60
    minutes = flight_duration % 60
    duration_str = f"约{hours}小时{minutes}分" if minutes > 0 else f"约{hours}小时"
    
    # 生成天气信息
    weather_conditions = ["晴", "多云", "阵雨", "小雨", "雾"]
    origin_weather = random.choice(weather_conditions)
    dest_weather = random.choice(weather_conditions)
    
    return {
        "flight_number": fnum,
        "share_codes": share_codes,
        "airline": airline_info,
        "origin_airport": origin_airport,
        "destination_airport": destination_airport,
        "terminal_info": {
            "origin": f"T{random.randint(1, 3)}航站楼",
            "destination": f"T{random.randint(1, 3)}航站楼"
        },
        "schedule": {
            "departure_time": departure_time,
            "arrival_time": arrival_time,
            "duration": duration_str
        },
        "aircraft": random.choice(aircraft_types),
        "distance": random.randint(800, 3000),  # 公里
        "punctuality": {
            "departure": round(random.uniform(85, 98), 2),
            "arrival": round(random.uniform(88, 99), 2)
        },
        "facilities": {
            "checkin_counter": random.choice(["A,B区", "C,D区", "E,F区", "G,H区"]),
            "boarding_gate": f"{random.randint(1, 20)}号门",
            "meal": random.choice(["提供正餐", "提供简餐", "不提供餐食"]),
            "baggage": "请以航空公司规定为准"
        },
        "weather": {
            "origin": f"{origin_weather}，气温{random.randint(15, 35)}/{random.randint(10, 25)}℃",
            "destination": f"{dest_weather}，气温{random.randint(15, 35)}/{random.randint(10, 25)}℃"
        }
    }


def _format_flight_result(flight_info: Dict[str, Any], date: str) -> str:
    """
    格式化航班查询结果为可读的字符串
    
    Args:
        flight_info: 航班信息字典
        date: 航班日期
        
    Returns:
        格式化的航班信息字符串
    """
    # 解析日期
    date_obj = datetime.strptime(date, "%Y-%m-%d")
    formatted_date = date_obj.strftime("%Y年%m月%d日")
    
    # 获取城市名称（从机场名称中提取）
    origin_city = flight_info["origin_airport"]["name"].replace("国际机场", "").replace("机场", "")[:2]
    dest_city = flight_info["destination_airport"]["name"].replace("国际机场", "").replace("机场", "")[:2]
    
    result = f"""以下是{formatted_date}{origin_city}飞{dest_city}的{flight_info['flight_number']}航班详细信息：

航班号：{flight_info['flight_number']}（代码共享：{', '.join(flight_info['share_codes'])}）
执行航空公司：{flight_info['airline']['name']}
起飞机场：{flight_info['origin_airport']['name']} {flight_info['terminal_info']['origin']}
到达机场：{flight_info['destination_airport']['name']} {flight_info['terminal_info']['destination']}
计划起飞时间：{flight_info['schedule']['departure_time']}
计划到达时间：{flight_info['schedule']['arrival_time']}
机型：{flight_info['aircraft']}
飞行时长：{flight_info['schedule']['duration']}
航程距离：{flight_info['distance']}公里
准点率：{flight_info['punctuality']['departure']}%
到港准点率：{flight_info['punctuality']['arrival']}%
值机柜台：{flight_info['facilities']['checkin_counter']}
登机口：{flight_info['facilities']['boarding_gate']}
餐食：{flight_info['facilities']['meal']}
行李托运：{flight_info['facilities']['baggage']}
天气预报：{origin_city}{flight_info['weather']['origin']}；{dest_city}{flight_info['weather']['destination']}
联系电话：{flight_info['airline']['name'][:2]}航{flight_info['airline']['phone']}，{flight_info['origin_airport']['name'][:4]}{flight_info['origin_airport']['phone']}，{flight_info['destination_airport']['name'][:4]}{flight_info['destination_airport']['phone']}"""

    return result


# 为了保持向后兼容性，保留一些基础函数
def get_flight_status(flight_number: str, date: str) -> Dict[str, Any]:
    """
    获取航班状态（简化版本，调用主要的searchFlightsByNumber函数）
    
    Args:
        flight_number: 航班号
        date: 查询日期
        
    Returns:
        航班状态信息
    """
    return searchFlightsByNumber(flight_number, date)


def check_flight_info(flight_number: str, flight_date: str) -> Dict[str, Any]:
    """
    检查航班信息（别名函数）
    
    Args:
        flight_number: 航班号
        flight_date: 航班日期
        
    Returns:
        航班信息
    """
    return searchFlightsByNumber(flight_number, flight_date)


def search_flights(
    origin: str,
    destination: str, 
    departure_date: str,
    return_date: Optional[str] = None,
    passengers: int = 1,
    class_type: str = "economy"
) -> Dict[str, Any]:
    """
    搜索航班
    
    Args:
        origin: 出发城市/机场代码
        destination: 目的地城市/机场代码  
        departure_date: 出发日期 (YYYY-MM-DD)
        return_date: 返程日期 (可选，YYYY-MM-DD)
        passengers: 乘客数量
        class_type: 舱位等级 (economy/business/first)
        
    Returns:
        包含航班搜索结果的字典
    """
    try:
        # 模拟航班数据
        mock_flights = [
            {
                "flight_id": "CA001",
                "flight_number": "CA001", 
                "airline": "中国国际航空",
                "origin": origin,
                "destination": destination,
                "departure_time": "08:00",
                "arrival_time": "10:30",
                "duration": "2小时30分钟",
                "aircraft": "Boeing 737-800",
                "price": {
                    "economy": 1200,
                    "business": 3600, 
                    "first": 8800
                },
                "available_seats": {
                    "economy": 45,
                    "business": 8,
                    "first": 4
                }
            },
            {
                "flight_id": "MU002",
                "flight_number": "MU002",
                "airline": "中国东方航空", 
                "origin": origin,
                "destination": destination,
                "departure_time": "14:20",
                "arrival_time": "16:55",
                "duration": "2小时35分钟",
                "aircraft": "Airbus A320",
                "price": {
                    "economy": 1180,
                    "business": 3400,
                    "first": 8200
                },
                "available_seats": {
                    "economy": 52,
                    "business": 12,
                    "first": 6
                }
            }
        ]
        
        result = {
            "status": "success",
            "search_params": {
                "origin": origin,
                "destination": destination,
                "departure_date": departure_date,
                "return_date": return_date,
                "passengers": passengers,
                "class_type": class_type
            },
            "flights": mock_flights,
            "total_results": len(mock_flights),
            "search_time": datetime.now().isoformat()
        }
        
        return result
        
    except Exception as e:
        return {
            "status": "error",
            "message": f"航班搜索失败: {str(e)}",
            "error_code": "SEARCH_FAILED"
        }


def get_flight_details(flight_number: str) -> Dict[str, Any]:
    """
    获取航班详细信息
    
    Args:
        flight_number: 航班号
        
    Returns:
        航班详细信息字典
    """
    try:
        # 模拟航班详细信息
        flight_details = {
            "flight_number": flight_number,
            "airline": "中国国际航空",
            "aircraft": "Boeing 737-800", 
            "route": {
                "origin": {
                    "code": "PEK",
                    "name": "北京首都国际机场",
                    "terminal": "T3"
                },
                "destination": {
                    "code": "SHA", 
                    "name": "上海虹桥国际机场",
                    "terminal": "T2"
                }
            },
            "schedule": {
                "departure_time": "08:00",
                "arrival_time": "10:30",
                "duration": "2小时30分钟",
                "timezone": "UTC+8"
            },
            "services": {
                "meal": "早餐",
                "wifi": True,
                "entertainment": True,
                "baggage_allowance": "23kg"
            },
            "seat_configuration": {
                "economy": {
                    "total": 156,
                    "available": 45,
                    "layout": "3-3"
                },
                "business": {
                    "total": 16,
                    "available": 8,
                    "layout": "2-2"
                },
                "first": {
                    "total": 8,
                    "available": 4,
                    "layout": "1-1"
                }
            }
        }
        
        return {
            "status": "success",
            "flight_details": flight_details,
            "query_time": datetime.now().isoformat()
        }
        
    except Exception as e:
        return {
            "status": "error", 
            "message": f"获取航班详情失败: {str(e)}",
            "error_code": "DETAILS_FAILED"
        }


def check_flight_status(flight_number: str, date: Optional[str] = None) -> Dict[str, Any]:
    """
    检查航班状态
    
    Args:
        flight_number: 航班号
        date: 查询日期 (可选，YYYY-MM-DD)
        
    Returns:
        航班状态信息字典
    """
    try:
        # 模拟航班状态
        statuses = ["准时", "延误", "取消", "已起飞", "已降落"]
        current_status = random.choice(statuses)
        
        status_info = {
            "flight_number": flight_number,
            "date": date or datetime.now().strftime("%Y-%m-%d"),
            "current_status": current_status,
            "scheduled_departure": "08:00",
            "actual_departure": "08:15" if current_status == "延误" else "08:00",
            "scheduled_arrival": "10:30", 
            "estimated_arrival": "10:45" if current_status == "延误" else "10:30",
            "gate": "A12",
            "terminal": "T3",
            "delay_reason": "空域管制" if current_status == "延误" else None,
            "last_updated": datetime.now().isoformat()
        }
        
        return {
            "status": "success",
            "flight_status": status_info,
            "query_time": datetime.now().isoformat()
        }
        
    except Exception as e:
        return {
            "status": "error",
            "message": f"查询航班状态失败: {str(e)}",
            "error_code": "STATUS_FAILED"
        }


def get_airport_info(airport_code: str) -> Dict[str, Any]:
    """
    获取机场信息
    
    Args:
        airport_code: 机场代码 (如: PEK, SHA, CAN)
        
    Returns:
        机场信息字典
    """
    try:
        # 模拟机场信息数据库
        airports = {
            "PEK": {
                "code": "PEK",
                "name": "北京首都国际机场",
                "city": "北京",
                "country": "中国",
                "terminals": ["T1", "T2", "T3"],
                "coordinates": {"lat": 40.0801, "lon": 116.5846},
                "timezone": "UTC+8",
                "services": ["免税店", "餐厅", "贵宾室", "WiFi", "充电站"]
            },
            "SHA": {
                "code": "SHA", 
                "name": "上海虹桥国际机场",
                "city": "上海",
                "country": "中国", 
                "terminals": ["T1", "T2"],
                "coordinates": {"lat": 31.1979, "lon": 121.3364},
                "timezone": "UTC+8",
                "services": ["免税店", "餐厅", "贵宾室", "WiFi", "高铁站"]
            },
            "CAN": {
                "code": "CAN",
                "name": "广州白云国际机场", 
                "city": "广州",
                "country": "中国",
                "terminals": ["T1", "T2"],
                "coordinates": {"lat": 23.3924, "lon": 113.2988},
                "timezone": "UTC+8",
                "services": ["免税店", "餐厅", "贵宾室", "WiFi", "地铁站"]
            }
        }
        
        airport_info = airports.get(airport_code.upper())
        
        if airport_info:
            return {
                "status": "success",
                "airport_info": airport_info,
                "query_time": datetime.now().isoformat()
            }
        else:
            return {
                "status": "error",
                "message": f"未找到机场代码 {airport_code} 的信息",
                "error_code": "AIRPORT_NOT_FOUND"
            }
            
    except Exception as e:
        return {
            "status": "error",
            "message": f"获取机场信息失败: {str(e)}",
            "error_code": "AIRPORT_INFO_FAILED"
        } 