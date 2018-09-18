# Line Bot作製
## 使用サービス
- [Line deveroper登録](https://developers.line.me/ja/)
- [実行環境](https://developers.google.com/apps-script/)

## 手順
- Line developersでプロバイダーを作成
- 作成したプロバイダーでMessaginAPIを作成
- google app script(gas)でプロジェクトを作成
- 作成したプロジェクトをウェブアプリケーション（API）として実行できるように設定　※アクセスして出来るユーザを全員（特命含む）にする事
- MessagingAPIの設定で以下を設定
    - Webhook送信ー利用する
    - WebhookURL-googleスプレッドシートで作成したプロジェクトプロジェクトのウェブアプリケーションURL
- 以下コードをgasのプロジェクトをに追加
```
function doGet(){
  return ContentService.createTextOutput("success");
}
```
- MessageAPIから接続確認
- 確認が出来たら完了
