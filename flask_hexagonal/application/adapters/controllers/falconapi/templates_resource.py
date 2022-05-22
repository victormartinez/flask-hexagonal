import json
from http import HTTPStatus

import falcon


class ListTemplatesResource:

    def on_get(self, req, resp):
        resp.text = json.dumps({
            "success": True,
            "code": HTTPStatus.OK,
            "message": "[Falcon] List of Templates",
            "data": [{}],
        }, ensure_ascii=False)
        resp.status = falcon.HTTP_200
