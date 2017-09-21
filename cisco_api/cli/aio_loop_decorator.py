# -*- coding: utf-8 -*-

import asyncio
import functools


def aio_loop(fn):
    def aio_loop_decorator(*args, **kwargs):
        loop = asyncio.get_event_loop()
        kwargs['loop'] = loop
        result = fn(*args, **kwargs)
        loop.close()
        return result
    return functools.update_wrapper(aio_loop_decorator, fn)