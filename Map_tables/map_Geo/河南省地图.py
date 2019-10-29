# -*- coding: utf-8 -*-
# @Time    : 2019/10/28 5:15 PM
# @Author  : Python小学僧
# @File    : 省份地图.py
# @Software: PyCharm

from pyecharts.charts import Geo
from pyecharts import options as opts

# 城市 -- 指定省的城市 xx市
from pyecharts.globals import ChartType
from Map_tables.data_tools import city, values2

data = []
for index in range(len(city)):
    city_info = [city[index], values2[index]]
    data.append(city_info)

print(data)
# [['郑州市', 1.07], ['安阳市', 3.85], ['洛阳市', 6.38], ['濮阳市', 8.21], ['南阳市', 2.53], ['开封市', 4.37], ['商丘市', 9.38], ['信阳市', 4.29], ['新乡市', 6.1]]

# 方法二 设置地图参数
def base_info():
    geo = Geo()
    geo.add_schema(maptype="河南")  # 加入自定义的点，格式为
    # 地图形式 type_=ChartType.HEATMAP
    geo.add("geo",data, type_=ChartType.EFFECT_SCATTER)
    # is_show：是否显示经纬度
    geo.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    geo.set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=10),
            title_opts=opts.TitleOpts(title="Geo-河南省地图"))

    return geo

c = base_info()
c.render(path="./html_files/河南省地图.html")