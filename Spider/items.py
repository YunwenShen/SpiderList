# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaseItem(scrapy.Item):
    # 城区
    region = scrapy.Field()
    # 商圈
    board = scrapy.Field()
    # 楼盘
    estate = scrapy.Field()
    # 物业地址
    address = scrapy.Field()
    # 朝向
    direction = scrapy.Field()
    # 装修程度
    decoration = scrapy.Field()

    # 标题
    title = scrapy.Field()
    # 几房
    countF = scrapy.Field()
    # 几厅
    countT = scrapy.Field()
    # 几卫
    countW = scrapy.Field()
    # 几阳
    countY = scrapy.Field()
    # 面积
    area = scrapy.Field()

    # 租金
    price = scrapy.Field()
    # 出租方式
    leaseMode = scrapy.Field()
    # 支付方式
    payWay = scrapy.Field()
    # 房屋经纪人
    houseAgent = scrapy.Field()
    # 房屋经纪人电话
    houseAgentTel = scrapy.Field()
    # 查看次数
    viewTimes = scrapy.Field()
    # 总楼层
    totalFloor = scrapy.Field()
    # 所在楼层
    currentFloor = scrapy.Field()

    # 爬取网站的名称
    websiteName = 'lianjia'
    # 爬取房源的详细链接
    detailUrl = scrapy.Field()
    # 上架时间
    launchDate = scrapy.Field()
    # 最近更新时间
    updateDate = scrapy.Field()
    # 爬取时间
    createDate = scrapy.Field()


class AddressItem(scrapy.Item):
    """
    房源的城市、城区、商圈、楼盘
    """
    city = scrapy.Field()
    region = scrapy.Field()
    board = scrapy.Field()
    estate = scrapy.Field()
    cityPinyin = scrapy.Field()
    regionPinyin = scrapy.Field()
    boardPinyin = scrapy.Field()
    estatePinyin = scrapy.Field()


class LianJiaItem(BaseItem):
    # 是否有床
    hasBed = scrapy.Field()
    # 是否有空调
    hasAirConditioner = scrapy.Field()
    # 是否有冰箱
    hasRefrigerator = scrapy.Field()
    # 是否有洗衣机
    hasWasher = scrapy.Field()
    # 是否有热水器
    hasWaterHeater = scrapy.Field()
    # 是否有油烟机
    hasCookerHood = scrapy.Field()
    # 是否有燃气
    hasGas = scrapy.Field()
    # 是否有衣柜
    hasWardrobe = scrapy.Field()
    # 是否有桌椅
    hasTableChair = scrapy.Field()
    # 是否有沙发
    hasSofa = scrapy.Field()
    # 是否有消防器材
    hasFireEquipment = scrapy.Field()
    # 是否有wifi
    hasWifi = scrapy.Field()
    # 是否有电视
    hasTv = scrapy.Field()
    # 是否有微波炉
    hasMicroWaveOven = scrapy.Field()
    # 是否有暖气
    hasHeating = scrapy.Field()
    # 是否有电梯
    hasLift = scrapy.Field()
