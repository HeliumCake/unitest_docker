# -*- coding: utf-8 -*-

def reply_post_params_check(content=None, replyId=0):
    """
    回帖参数检查
    """
    print(content)
    print(replyId)
    if isinstance(content, str) and 15 <= len(content) <= 256:
        if isinstance(replyId, int) and replyId >= 0:
            return "ok", True
        else:
            return "replyId", False
    else:
        return "content", False
