# -*- coding: utf-8 -*-

def reply_post_params_check(content):
    """
    回帖参数检查
    """
    if not isinstance(content, dict):
        return "content", False
    if 'content' in content and isinstance(content['content'], str) and 15 <= len(content['content']) <= 256:
        if 'replyId' in content:
            if isinstance(content['replyId'], int) and content['replyId'] >= 0:
                return "ok", True
            else:
                return "replyId", False
        else:
            return "ok", True
    else:
        return "content", False
