# -*- coding: utf-8 -*-
# @Time    : 2019/10/28 5:45 PM
# @Author  : Python小学僧
# @File    : 中国地图.py
# @Software: PyCharm


from pyecharts import options as opts
from pyecharts.charts import Map
from Map_tables.data_tools import *

data = []
for index in range(len(provice)):
    city_info = [provice[index], values[index]]
    data.append(city_info)


def map_base():
    c = (
        Map()
        .add("中国地图",data, "china")
        # is_show 是否显示城市标签
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
         .set_global_opts(title_opts=opts.TitleOpts(title="Map-基本示例"))
    )
    return c


# c = map_base()
# c.render(path="./html_files/中国地图.html")

def map_visualmap():
    c = (
        Map()
        .add("中国地图", data, "china")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Map-VisualMap（分段型）"),
                # is_piecewise ：是否分段显示
            visualmap_opts=opts.VisualMapOpts(max_=100, is_piecewise=True),
        )
    )
    return c

c = map_visualmap()
c.render(path="./html_files/中国地图2.html")