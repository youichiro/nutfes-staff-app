## account

- [x] カスタムユーザモデルの作成
- [x] ログイン画面、アカウント作成画面のスタイル
- [x] 表示権限(login_require)
- [x] staff権限
- [ ] 学生番号のバリデーション


## manual

- [x] 対応マニュアルPDFの表示


## message

- 今年度は実装しない


## shift

- [x] エクセルからシフト取得&DB保存
- [x] 全体シフトの表示(shift_list.html)
- [x] 個別シフトの表示(shift_detail.html)
- [x] 個別シフト画面に他のシフトのリンクを貼る
- [x] ログインユーザのシフトを表示
- [x] 現在時刻のシフトを強調
- [x] 時間軸の固定化
- [ ] 局を結合して表示
- [ ] スタイル微修正


## timetable

- [x] エクセルからタイムテーブル取得&DB保存
- [x] 表示

## ページング

- `/`: `home.html`
- `account/login`: `login.html`
- `account/registration`: `registration.html`
- `shift/`: `shift_list.html`
- `shift/<id>/`: `shift_detail.html`
- `shift/my_shift`: `shift_detail.html`
- `manual/`: `manual_links.html`
- `timetable/`: `timetable_list.html`


## 初期作業

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata fixtures/departments.json
python manage.py shift_registration
python manage.py timetable_registration
python manage.py collectstatic
```