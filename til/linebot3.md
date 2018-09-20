#LineBOT作成
## 使用API
- SimpleAPI
    - wikipediaが提供しているAPI。検索したいワードを渡す事でそのページの情報を返す。
## 外部APIの使用
APIを使用する場合、取得できた値を使用できる形に形に変換する必要がある。
今回使用したWikipediaのAPIはxml形式で取得するため、XmlServiceを使用し、parseしやすい形にした後に必要なデータの切り出しをおこなった。

```
function keywordSearchFromWikipedia(word){
  var searchUrl = "http://wikipedia.simpleapi.net/api?keyword="+encodeURIComponent(word);
  var options = {
    "method" : "GET",
    "headers" : {
      "Content-Type" : "application/json; charset=UTF-8"
    }
  };
  var resultRoot = XmlService.parse(UrlFetchApp.fetch(searchUrl,options).getContentText()).getRootElement();
  var item =resultRoot.getChildren("result")[0];
  if(!item){
    Logger.log("OK")
    return false;
  }
  
  var title = item.getChildText("title");
  var body = item.getChildText("body");
  var url = item.getChildText("url");
  var returnText = title + "\r\n" + body + "\r\n" + url;
  Logger.log("OK")
  return returnText;
}

```