
import pandas as pd

df = pd.DataFrame({
    "银行名称": ["中国银行", "建设银行", "地方银行A"],
    "资本": [120, 90, 50],
    "风险加权资产": [1000, 1000, 1000]
})

df.to_excel("banks.xlsx", index=False)
print("banks.xlsx 已重新生成")