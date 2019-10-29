# -*- coding: utf-8 -*-
# @Time    : 2019/10/28 5:15 PM
# @Author  : Python小学僧
# @File    : 省份地图.py
# @Software: PyCharm

from pyecharts.charts import Map
from pyecharts import options as opts

# 城市 -- 指定省的城市 xx市

from Map_tables.data_tools import city, values2

data = []
for index in range(len(city)):
    city_info = [city[index], values2[index]]
    data.append(city_info)

print(data)

# 方法二 设置地图参数
def base_info():
    map = Map()
    # 注意：这里是"河南' 不能是河南省
    map.add("河南省地图",data, "河南")
    map.set_global_opts(
            title_opts=opts.TitleOpts(title="Map-河南省地图"),
            visualmap_opts=opts.VisualMapOpts(max_=10))

    return map


c = base_info()
c.render(path="./html_files/河南省地图.html")