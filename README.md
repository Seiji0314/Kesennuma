# Kesennuma

## stellar.py
気仙沼観望会のワークショップに用いる星をプロットするためのコードです。

### 使い方
1. コードをダウンロードする

  コマンドラインからなら

  ```
  git clone https://github.com/Seiji0314/Kesennuma.git
  ```

  手でやるなら画面右上のこちらからダウンロード

3. stellar.py のパラメータを確認・編集する

  stellar.py 内の以下の箇所を編集して適切なパラメータにして下さい。

  flux_const：プロットの大きさ

  magnitude_limit：何等星まで表示するか

  season：どの季節を表示するか
  
  ```
  #input your parameter
  
  flux_const = 15 
  
  magnitude_limit = 4
  
  season = 'fa'　#　'sp','su','fa','wi'
  ```
  
3. コードを実行する
   
  ```
  python stellar.py
  ```

  画像が "fig/north_"+season+"_wh_"+str(f0)+"_"+str(mag_lim)+".png" で出力されます。


