# 問題

ある学校でテストを行い、試験結果のCSVファイルがあります。
データを集計して指定した生徒の
・合計点数と教科毎の点数
・順位（全体、科目毎）
をコンソールに出力してください。

CSVファイルは「生徒ID,国語点数,数学点数,英語点数」の順に並んでいます。
各データは以下のルールとします。
・生徒IDは「先頭アルファベット1文字+5桁の数字」（例:A00001）
・国語点数は「正の整数、0以上100以下、データなしの場合は空白」(例:10)
・数学点数は「正の整数、0以上100以下、データなしの場合は空白」(例:10)
・英語点数は「正の整数、0以上200以下、データなしの場合は空白」(例:10)
データの1行は以下のようになります。
A00001,10,10,10

レコード件数は最大1000としてください。
生徒IDは重複することがないものとしてください。

本問題はPythonで実装してください。

出力例
ユーザー名:A00001
合計,5位,150点
国語,10位,50点
数学,10位,50点
英語,10位,50点

