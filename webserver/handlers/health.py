from handlers.base import BaseHandler

import logging
import json
logger = logging.getLogger(__name__)

class HealthHandler(BaseHandler):
    is_healty = True
    def get(self):
        cmd = self.get_argument("action", default=None, strip=True)
        if cmd is not None:
            if cmd.lower() == "open":
                HealthHandler.is_healty = True
            elif cmd.lower() == "fail":
                HealthHandler.is_healty = False

        if not HealthHandler.is_healty:
            msg = "Not healthy"
        else:
            msg = "Healty"

        resp = json.dumps({"msg": msg, "health": HealthHandler.is_healty,
                           "action": cmd})
        self.write(resp)
        self.flush()

