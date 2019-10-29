# -*- coding: utf-8 -*-
# @Time    : 2019/10/28 5:22 PM
# @Author  : Python小学僧
# @File    : 商丘市地图.py
# @Software: PyCharm

from pyecharts.charts import Geo
from pyecharts import options as opts

# 城市 -- 指定省的城市 xx市
from pyecharts.globals import ChartType

# 区县 -- 具体城市内的区县  xx县
from Map_tables.data_tools import quxian, values3

data = []
for index in range(len(quxian)):
    city_info = [quxian[index], values3[index]]
    data.append(city_info)

# 方法二 设置地图参数
def base_info():
    geo = Geo()
    geo.add_schema(maptype="商丘")  # 加入自定义的点，格式为
    # 地图形式 type_=ChartType.HEATMAP
    geo.add("geo",data, type_=ChartType.EFFECT_SCATTER)
    # is_show：是否显示经纬度
    geo.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    geo.set_global_opts(visualmap_opts=opts.VisualMapOpts(),
            title_opts=opts.TitleOpts(title="Geo-商丘市地图"))

    return geo


c = base_info()
c.render(path="./html_files/商丘市地图.html")