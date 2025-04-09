import pandas as pd
import random

# CSVファイルを読み込む
csv_path = 'data/products.csv'
df = pd.read_csv(csv_path)

# 在庫状況の選択肢
stock_options = ['あり', '残りわずか', 'なし']

# 各商品にランダムに在庫状況を割り当てる
df['stock_status'] = [random.choice(stock_options) for _ in range(len(df))]

# 更新したデータをCSVファイルに保存
df.to_csv(csv_path, index=False)

print(f"CSVファイル '{csv_path}' に stock_status 列を追加しました")
print(f"合計 {len(df)} 件の商品に対して在庫状況を割り振りました")
print("\n在庫状況の内訳:")
print(df['stock_status'].value_counts())