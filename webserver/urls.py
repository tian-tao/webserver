from handlers.health import HealthHandler
url_patterns = [
    (r"/health", HealthHandler),
]
