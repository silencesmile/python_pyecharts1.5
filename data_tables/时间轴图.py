# -*- coding: utf-8 -*-
# @Time    : 2019/10/29 3:27 PM
# @Author  : Python小学僧
# @File    : 时间轴图.py
# @Software: PyCharm

from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Bar, Page, Pie, Timeline


def timeline_bar():
    x = Faker.choose()
    tl = Timeline()
    for i in range(2015, 2020):
        bar = (
            Bar()
            .add_xaxis(x)
            .add_yaxis("商家A", Faker.values())
            .add_yaxis("商家B", Faker.values())
            .set_global_opts(title_opts=opts.TitleOpts("某商店{}年营业额".format(i)))
        )
        tl.add(bar, "{}年".format(i))
    return tl

timeline = timeline_bar()
timeline.render("./html_files/时间轴图.html")