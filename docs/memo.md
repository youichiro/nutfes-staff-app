## account

- [x] カスタムユーザモデルの作成
- [ ] ログイン画面、アカウント作成画面のスタイル
- [ ] 表示権限(login_require)
- [ ] 学生番号のバリデーション

## manual

- [x] 対応マニュアルPDFの表示

## message

## shift

- [x] エクセルからシフト取得&DB保存
- [x] 全体シフトの表示(shift_list.html)
- [x] 個別シフトの表示(shift_detail.html)
- [ ] 個別シフト画面に他のシフトのリンクを貼る
- [ ] 現在時刻のシフトを強調
- [ ] 時間軸の固定化
- [ ] 局を結合して表示
- [ ] スタイル微修正


## ページング

- `/`: `home.html`
- `account/login`: `login.html`
- `account/registration`: `registration.html`
- `message/`: `message_list.html`
- `message/form/`: `message_form.html`
- `message/<id>/reply_form`: `reply_form.html`
- `shift/`: `shift_list.html`
- `shift/<id>/`: `shift_detail.html`
- `manual/<num>`: Driveのリンク


## 初期作業

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata fixtures/departments.json
python manage.py shift_registration
```