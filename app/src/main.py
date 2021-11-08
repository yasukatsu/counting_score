import os 
import sys
# 取り急ぎは気にしないで良いWarningが出るため非表示対応
import warnings
warnings.simplefilter('ignore', FutureWarning)
import pandas as pd
import validation

class const:
   DIR_PATH = "/app/csv_data/"
   MAX_LENGTH = 1000
   REQ_PARAMS = 3

class error:
    NOT_EXIST_FILE = "ファイルが存在しません。"
    INVALID_PARAM = "引数を"+str(const.REQ_PARAMS)+"つ指定してください。"
    MAX_LENGTH_OVER = "最大件数を超過しています。"
    INVALID_CSV = "CSVデータが不正です: "
    NOT_EXIST_STUDENT = "存在しない生徒IDです。"
    DUPLICATE_STUDENT = "重複する生徒IDがあります。"


def calculation(data, student_id, column):
    if column == "":
        total_score = data.sum(axis=1)
        total_rank = data.sum(axis=1).rank(method='min', ascending=False)
        return int(total_rank[student_id]), total_score[student_id]

    else:
        score = data[column]
        rank = data[column].rank(method='min', ascending=False)
        return int(rank[student_id]), score[student_id]

# 引数を取得
args = sys.argv
if len(args) != const.REQ_PARAMS:
    print(error.INVALID_PARAM)
    sys.exit()

file_name = args[1]
file_path = const.DIR_PATH + file_name

if not os.path.exists(file_path):
    print(error.NOT_EXIST_FILE)
    sys.exit()

csv_input = pd.read_csv(file_path, index_col=0)
if len(csv_input) > const.MAX_LENGTH:
    print(error.MAX_LENGTH_OVER)
    sys.exit()

# 空白のセルを0埋め
data = csv_input.fillna(0).astype('int', errors='ignore')

# バリデーションチェック
ok, err = validation.exec(data.to_dict(orient='list'))
if not ok:
    print(error.INVALID_CSV, err)
    sys.exit()

if len(data[data.duplicated()]) > 0:
    print(error.DUPLICATE_STUDENT)
    sys.exit()

student_id = args[2]
if student_id not in data.index:
    print(error.NOT_EXIST_STUDENT)
    sys.exit()

print("ユーザー名:", student_id)

rank, score = calculation(data, student_id, "")
print("合計,"+str(rank)+"位,"+str(score)+"点")

rank, score = calculation(data, student_id, "国語点数")
print("国語,"+str(rank)+"位,"+str(score)+"点")

rank, score = calculation(data, student_id, "数学点数")
print("数学,"+str(rank)+"位,"+str(score)+"点")

rank, score = calculation(data, student_id, "英語点数")
print("英語,"+str(rank)+"位,"+str(score)+"点")

