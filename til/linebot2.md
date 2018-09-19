# LineBot作成
## 使用API
- SpreadsheetApp
    -  スプレッドシート関連のAPI※デバッグで使用
    - openById(id)
        - 引数で指定したidのスプレッドシートを開く
    - getSheetByName(name)
        - 引数で指定したnameのシートを取得する
    - appendRow(text)
        - 行を追加し、textを入力する

- JSON
    - JSONを扱う
    - parse
        - JSONで記載されている値を区切る

- UrlFetchApp
    - GETまたはPOSTを行なう
    - fetch(url,text)
        - POST通信でurlにtextを送信する


## 実相ソース
```
var channel_access_token = "MessageAPIのtoken";
var spreadsheet = SpreadsheetApp.openById("スプレッドシートのID");

function doPost(e){
  var webhookData = JSON.parse(e.postData.contents).events[0];
  var message,replyToken;
  
  message = webhookData.message.text;
  replyToken = webhookData.replyToken;
  return sendLineMessageFromReplyToken(replyToken,message);
}

function sendLineMessageFromReplyToken(token,replyText){
  appendToSheet("sendLineMessagein");
  var url = "https://api.line.me/v2/bot/message/reply";
  appendToSheet("headers");
  var headers = {
    "Content-Type" : "application/json; charset=UTF-8",
    "Authorization" : "Bearer " + channel_access_token
  };
  appendToSheet("postData");
  var postData = {
    "replyToken" : token,
    "messages" : [{
      "type" : "text",
      "text" : replyText
    }]
  };
  appendToSheet("options");
  var options = {
    "method" : "POST",
    "headers" : headers,
    "payload" : JSON.stringify(postData)
  };
  
  appendToSheet("return");
  return UrlFetchApp.fetch(url,options);
}
  
function appendToSheet(text){
  var sheet = spreadsheet.getSheetByName('webhook');
  sheet.appendRow([text]);
}
```