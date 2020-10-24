# -*- coding: utf-8 -*-

def post_params_check(content):
    """
    发帖参数检查
    """
    if not isinstance(content, dict):
        return "title", False
    if 'title' in content and isinstance(content['title'], str) and 1 <= len(content['title']) <= 64:
        if 'content' in content and isinstance(content['content'], str) and 15 <= len(content['content']) <= 256:
            return "ok", True
        else:
            return "content", False
    else:
        return "title", False
