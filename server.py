from mcp.server import Server

# 创建服务器实例，需要提供一个名称
server = Server(name="calculator-server")  # 添加了必需的 name 参数

@server.tool()
def calculate_multiples(number: float) -> dict:
    """
    计算一个数字的2倍和3倍
    
    Args:
        number: 输入的数字
        
    Returns:
        包含2倍和3倍结果的字典
    """
    return {
        "double": number * 2,
        "triple": number * 3
    }

if __name__ == "__main__":
    server.run()