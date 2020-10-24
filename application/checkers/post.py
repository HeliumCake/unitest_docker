# -*- coding: utf-8 -*-

def post_params_check(title=None, content=None):
    """
    发帖参数检查
    """
    if isinstance(title, str) and 1 <= len(title) <= 64:
        if isinstance(content, str) and 15 <= len(content) <= 256:
            return "ok", True
        else:
            return "content", False
    else:
        return "title", False
