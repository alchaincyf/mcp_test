import { MCP } from '@modern/mcp-service';

export async function getCurrentLondonTime() {
  try {
    const response = await MCP.time.getCurrentTime({
      timezone: 'Europe/London'
    });
    
    return {
      time: response.currentTime,
      timezone: response.timezone,
      timestamp: response.timestamp
    };
  } catch (error) {
    console.error('获取伦敦时间失败:', error);
    throw error;
  }
}