# -*- coding: utf-8 -*-
# @Time    : 2019/10/29 3:15 PM
# @Author  : Python小学僧
# @File    : Calendar_日历图.py
# @Software: PyCharm

import datetime
import random

from pyecharts import options as opts
from pyecharts.charts import Calendar


def calendar_base():
    begin = datetime.date(2017, 1, 1)
    end = datetime.date(2017, 12, 31)
    data = [
        [str(begin + datetime.timedelta(days=i)), random.randint(1000, 25000)]
        for i in range((end - begin).days + 1)
    ]

    c = (
        Calendar()
        .add("", data, calendar_opts=opts.CalendarOpts(range_="2017"))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Calendar-2017年微信步数情况"),
            # 显示工具类
            toolbox_opts = opts.ToolboxOpts(orient="horizontal", pos_left="80%"),
            visualmap_opts=opts.VisualMapOpts(
                max_=25000,
                min_=500,
                orient="horizontal",
                is_piecewise=True,
                pos_top="230px",
                pos_left="100px",
            ),
        )
    )
    return c

calendar = calendar_base()
calendar.render("./html_files/Calendar_日历图.html")
