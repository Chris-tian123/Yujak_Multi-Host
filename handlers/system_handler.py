import psutil

class SystemHandler:
    @staticmethod
    def get_system_status():
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()
        return f"CPU Usage: {cpu_usage}%\n Memory Usage: {memory_info.percent}%"