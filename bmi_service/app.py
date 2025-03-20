from fastmcp import FastMCP

# 创建FastMCP实例
mcp = FastMCP("BMI计算服务")

@mcp.tool()
def calculate_bmi(height: float, weight: float) -> float:
    """
    计算BMI（体质指数）
    
    参数:
    height: 身高（厘米）
    weight: 体重（千克）
    
    返回:
    BMI值（保留两位小数）
    """
    # 将身高从厘米转换为米
    height_in_meters = height / 100
    # 计算BMI
    bmi = weight / (height_in_meters ** 2)
    # 保留两位小数
    bmi = round(bmi, 2)
    return bmi

@mcp.prompt("health_advice")
def bmi_advice(user_query: str) -> str:
    """
    返回用于BMI计算的提示模板
    """
    return f"""
你是一个健康顾问，专门计算并解释BMI指数。

{user_query}

你可以使用calculate_bmi工具来计算BMI。参数需要包括:
- height: 身高（厘米）
- weight: 体重（千克）

BMI分类标准:
- 低于18.5: 体重过轻
- 18.5-24.9: 正常范围
- 25.0-29.9: 超重
- 30.0及以上: 肥胖

请提供用户的BMI值并给出相应的健康建议。
"""

# 注意：FastMCP会自动处理服务器的启动
if __name__ == "__main__":
    # 启动服务器在默认端口8000
    mcp.run()