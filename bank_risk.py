import pandas as pd


def calculate_car(capital, risk_weighted_assets):
    if risk_weighted_assets <= 0:
        return None
    return capital / risk_weighted_assets


def assess_risk_level(car):
    if car is None:
        return "数据错误"
    if car >= 0.10:
        return "低风险"
    elif car >= 0.08:
        return "中等风险"
    elif car >= 0.06:
        return "高风险"
    else:
        return "严重风险"


df = pd.read_excel("banks.xlsx")

df["资本充足率"] = df.apply(
    lambda row: calculate_car(row["资本"], row["风险加权资产"]),
    axis=1
)

df["风险等级"] = df["资本充足率"].apply(assess_risk_level)

df["资本充足率"] = df["资本充足率"].apply(
    lambda x: f"{x:.2%}" if x is not None else "数据错误"
)

df.to_excel("risk_report.xlsx", index=False)

print("分析完成，已生成 risk_report.xlsx")