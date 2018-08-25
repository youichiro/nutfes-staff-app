# nutfes-staff-app 設計書

## 機能
1. ログイン機能
2. メッセージ機能
3. シフト確認機能
4. 対応マニュアル確認機能
5. 来場者数カウント機能

## ログイン機能
局員のユーザ情報の管理を行う機能を実装する.  
局員にはまず最初にユーザ登録を行ってもらう.  
以下のユーザ情報を入力してもらう.

- 学籍番号 (ex. s163127)
- 名前
- 学年 (ex. M1)
- 局・部門 (ex. 総務局-情報処理部門)
- 電話番号 (ex. 090-0000-0000)
- パスワード

ユーザ登録以降はログイン時に学籍番号とパスワードを入力してもらう.

### 設計

```
app: account

model: 
  User:
    student_id: char
    name: char
    grade: choice
    department: choice
    phone_number: char
    password: password
  Department:
    name: char

pages:
  /login: ログイン画面
  /logout: ログアウト画面
  /registration: ユーザ登録画面
```

## メッセージ機能
局員がメッセージを本部に送信する機能と, 本部がメッセージを閲覧・返信する機能を実装する.  
局員側は以下の情報を入力する.

- 本文
- 重要度ラベル (要対応, 報告, 確認, その他, なし)

メッセージ送信時に, 以下の情報を付与して送信する.

- ユーザ情報(Userモデル)

本部側は送信されたメッセージを閲覧し、必要に応じて返信する.  
受信するメッセージの例: \[要対応\]メインステージ前で熱中症の疑いがあるお客さんが倒れています.(技大太郎)(企画局)\[13:05\]

### 設計

```
app: message

models:
  Message:
    user: User
    text: text
    importance: choice
    created_at: datetime
  Reply:
    user: User
    message: Message
    text: text
    created_at: datetime

pages:
  /form: メッセージフォーム画面
  /view: メッセージ・返信閲覧画面
  /reply_form: 返信フォーム画面
```


## シフト確認機能
各局員のシフトおよび全体のシフトを確認することができる機能を作る.
まず、局員のシフト情報を文字するモデルを作成する.
次に、シフトスプレッドシートからセル情報を読み取り、モデルに保存するスクリプトを作成する.
最後に、ユーザ情報を元にシフトを表示させる.

### 設計

```
app: shift

models:
  Shift:
    user: char
    day: char (first or second)
    weather: char (sun or rain)
    _0600: char (ex. MTG)
    _0630: char
    ...
    _2330: char
    
pages:
  /<int: user_id>: 局員のシフト表示画面
  /whole: 全体のシフト表示画面
```
