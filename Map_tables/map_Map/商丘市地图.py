# -*- coding: utf-8 -*-
# @Time    : 2019/10/28 5:46 PM
# @Author  : Python小学僧
# @File    : 商丘市地图.py
# @Software: PyCharm

from pyecharts.charts import Map
from pyecharts import options as opts

# 城市 -- 指定省的城市 xx市

from Map_tables.data_tools import quxian, values3

data = []
for index in range(len(quxian)):
    city_info = [quxian[index], values3[index]]
    data.append(city_info)

print(data)


def map_shangqiu():
    c = (
        Map()
        .add("商丘-Map", data, "商丘")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Map-商丘地图"),
            visualmap_opts=opts.VisualMapOpts(max_=10),
        )
    )
    return c

c = map_shangqiu()
c.render(path="./html_files/商丘地图.html")