from handlers.health import HealthHandler
from handlers.wechat import WeChatTokenHandler
url_patterns = [
    (r"/health", HealthHandler),
    (r"/sync", WeChatTokenHandler),
]
