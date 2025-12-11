import json
import ast
# 原始字符串数据
data_str = """
{'FBillTypeID': {'FNUMBER': 'XSDD01_SYS'}, 'FBillNo': 'NO202501112', 'FCustId': {'FNumber': 'CUST0003'}, 'FSalerId': {'FNumber': '002_GW000055_1'}, 'F_qdmy_Base': {'FNUMBER': 'S-202501068'}, 'FSaleOrderFinance': {'FSettleCurrId': {'FNumber': 'PRE001'}, 'FExchangeTypeId': {'FNumber': 'HLTX01_SYS'}, 'FExchangeRate': 1}, 'FSaleOrderEntry': [{'FMaterialId': {'FNumber': 'S-202501068'}, 'FQty': 1.0, 'FTaxPrice': 0, 'FEntryTaxRate': 13.0, 'F_THPE_ZBJE': 0}]}
"""
# 将字符串转换为Python字典
data_dict = ast.literal_eval(data_str)
# 转换为格式化的JSON字符串
json_output = json.dumps(
    data_dict,
    # indent=2,
    ensure_ascii=False  # 保留中文显示
)
# 输出到控制台
print(json_output)