# -*- coding: utf-8 -*-
# @Time    : 2019/10/28 5:45 PM
# @Author  : Python小学僧
# @File    : 世界地图.py
# @Software: PyCharm

from pyecharts.charts import Map
from pyecharts import options as opts

from Map_tables.data_tools import attr, value

data = []
for index in range(len(attr)):
    city_info = [attr[index], value[index]]
    data.append(city_info)

print(data)

def map_world():
    c = (
        Map()
        .add("世界地图", data , "world")
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Map-世界地图"),
            visualmap_opts=opts.VisualMapOpts(max_=100),
        )
    )
    return c


c = map_world()
c.render(path="./html_files/世界地图.html")