def is_leaf(element, data_list):
    """
    判断元素是否是层级数据中的末级数据（无下级元素）。

    参数:
        element (str): 需要判断的元素，如 '1' 或 '1.1'
        data_list (list): 层级数据列表，如 ['1', '1.1', '1.2', '2']

    返回:
        bool: 如果是末级数据返回 True，否则返回 False
    """
    for item in data_list:
        # 检查是否存在以当前元素开头且后接"."的元素（即下级元素）
        if item['wbs_no'].startswith(element + '.'):
            return False  # 发现下级元素，不是末级
    return True  # 无下级元素，是末级数据


data = [
    {
        "wbs_no": "1",
        "is_lesf": ""
    },
    {
        "wbs_no": "1.1",
        "is_lesf": ""
    },
    {
        "wbs_no": "1.1.1",
        "is_lesf": ""
    },
    {
        "wbs_no": "2",
        "is_lesf": ""
    },
    {
        "wbs_no": "3",
        "is_lesf": ""
    },
    {
        "wbs_no": "3.1",
        "is_lesf": ""
    }
]

for elem in data:
    result = is_leaf(elem['wbs_no'], data)
    status = "末级数据" if result else "非末级数据"
    elem['is_lesf']=status
print(data)