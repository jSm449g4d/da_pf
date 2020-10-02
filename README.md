# コーディングテスト
数字⇔漢数字の変換APIです

## URL
https://dapf-tlnesjcoqq-an.a.run.app/

## 動作画面
![1](https://github.com/jSm449g4d/da_pf/blob/main/assets/kan2num.png)  
![2](https://github.com/jSm449g4d/da_pf/blob/main/assets/num2kan.png)  

## 使い方
https://dapf-tlnesjcoqq-an.a.run.app/v1/number2kanji/{数字}  
https://dapf-tlnesjcoqq-an.a.run.app/v1/kanji2number/{漢字}  
{数字}や{漢字}に目的の数値を入力してください  
※漢数字について、「壱百」「壱拾」等と入力してください。

## 使用技術   
### エディタ
- VSCode  
### インフラ  
- ローカル開発環境: Windows10 & anaconda + Waitress/Flask  
- 環境: GCP(Cloudbuild, CloudRun) + Debian + Waitress/Flask  
### バックエンド  
- Flask(Python)
### その他  
- Docker
- bootstrap4
- fontawesome
