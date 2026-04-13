---
title: "Azure Data Service - Day 02 - Cognitive Service - 辨識 - Computer Vision - 01"
datePublished: Mon Apr 13 2026 04:56:37 GMT+0000 (Coordinated Universal Time)
cuid: cmnwq04u1000702jr7eyzcrfh
slug: azure-data-service-day-02-cognitive-service-computer-vision-01
canonical: https://medium.com/@abc12207/azure-data-service-day-02-cognitive-service-%E8%BE%A8%E8%AD%98-computer-vision-01-c795092ef396
cover: https://cdn-images-1.medium.com/max/800/1*BFAg5LjBKcu2RqsBpi9hGw.png

---

---

### [IT 鐵人賽] Azure Data Service - Day 02 - Cognitive Service - 辨識 - Computer Vision

![](https://cdn-images-1.medium.com/max/800/1*BFAg5LjBKcu2RqsBpi9hGw.png)

在一般常用的 AI 領域中，電腦視覺肯定是非常常被使用的服務類型，而且其應用類型也很多，從最常見的人臉辨識到自訂的物件偵測等等。

當然我們可以自幹這些服務，但是因為這些服務太常見而且廣被應用，所以大部分雲端提供商都有提供已經建立好的模型直接可以使用，這樣我們就沒有必要花時間一直做別人做過的事情。

---

Cognitive Service 在電腦視覺中提供了以下服務：

* 分析影像
  這項功能會傳回在影像中找到的視覺化內容資訊。使用標記、特定領域模型及四種語言描述，從容地識別內容並將其加上標籤。套用成人 / 猥褻設定，以協助您偵測潛在成人內容。識別圖片中的影像類型及色彩配置。
* 辨識名人和地標
  辨識超過 200,000 名來自商業界、政界、體壇及娛樂圈的名人，以及世界各地 9,000 個自然與人工地標。
* 文字辨識
  使用光學字元辨識 (OCR) 來偵測影像中的文字，然後將辨識出的字詞擷取到電腦可讀取的字元資料流中。分析影像，進而偵測內嵌的文字、產生字元資料流並啟用搜尋。替文字照相，省下複製文字所需的時間及精力。
* 近乎即時分析影片
  近乎即時分析影片：從裝置擷取視訊框架，然後將其傳送至您所選的 API 呼叫，即可對您的視訊檔案使用任何一項電腦視覺 API。更快從影片取得結果。
* 產生縮圖
  依據任何影像，產生高品質且具儲存體效益的縮圖，並修改影像以最符合您的大小、圖形和樣式需求。套用智慧裁剪，產生出外觀比例與原始影像不同的縮圖，同時保留所關注的區域。

---

在開始前，要先跟大家介紹一個觀念，就是：**AI 幾乎沒有辦法 100% 的肯定它所辨認出來的結果是絕對正確**，除非你拿的照片本來就是已經訓練過的照片也明確地跟它講這是甚麼東西。

因此你只要是在使用訓練完的模型所得到的結果，通常都會附上一個數值：**信心程度** (不同家會有不同的名字，意義相同)，它會給它所辨認出來的結果評一個分數，這個分數介於 0 ~ 1 之間，通常都不會看到 0 或 1，因為凡事都有可能，但是凡事也都有不可能。

所以在下面的範例中，都會看到一個欄位：confidence 或是 score，這都代表 AI 對於它所給出的結果之信心程度。

---

**範例網站介紹**

簡單來說就是讓電腦來看圖說故事，他可以分析這張照片的內容並轉換為文字輸出回來，除了看圖說故事以外，如果圖片內含有人臉，它也會整合已經有的服務 (臉部辨識)，並把這些資訊一併輸出。

我們先來看一下官網的範例，後面再來實際用程式動手做

* [辨識影像中的場景及活動](https://azure.microsoft.com/services/cognitive-services/computer-vision/#analyze)

![](https://cdn-images-1.medium.com/max/800/1*FP-s9dQqp_X2c_IKYqa3oQ.png)

點開連結後，就會直接到範例網站裡

一號紅框是讓你看現在用的圖片是哪張，如果圖片裡有人臉，它也會在上面把人臉標記出來，並顯示相關資訊。

二號紅框則是辨識完後的結果檢視，Cognitive Service 辨識完後都會將結果用 JSON 格式回傳，而這邊就是把 JSON 結果視覺化出來，讓您看有哪些參數可以使用。

三號紅框則是讓你選擇範例圖片或是你也可以用自己的圖片，不論是透過 URL 或是電腦上傳的方式均可。

可以看到說明欄位裡有一屬性：text，這就是它會把它變成一句話來說明這張圖片，例如：a group of people posing for a photo

* [辨識影像中的名人與地標](https://azure.microsoft.com/services/cognitive-services/computer-vision/#celebrities-landmarks)

![](https://cdn-images-1.medium.com/max/800/1*a7HLaivrHhTMLOkCEwjezw.png)

這個服務可以拿來辨識全球大部分名人，像上面的圖片我就是自己上傳一張「周杰倫」的照片為範例，可以在右邊的 JSON 結果上看到它也正確的辨認出了他就是周杰倫，除了人以外，地標也是可以的，範例網站上有一張羅馬競技場的照片，他也的確辨認的出來，我這邊就不再多做截圖了。

* [影像中的光學字元辨識 (OCR)](https://azure.microsoft.com/services/cognitive-services/computer-vision/#text)

![](https://cdn-images-1.medium.com/max/800/1*Nu1DMrRRXdXEk_chg60ZbQ.png)

就是很常見的文字辨識，OCR 的全名是 Optical Character Recognition，光學字元辨識，在這服務它使用了深度學習演算法，提供了更好的辨識率，像是大小字等等，已經**支援中文辨識，但是，目前辨識率沒有很好**。

* [手寫辨識](https://azure.microsoft.com/zh-tw/services/cognitive-services/computer-vision/#handwriting)

![](https://cdn-images-1.medium.com/max/800/1*rNlcQfD-gYOglaFcU5_hzQ.png)

其實就還是文字辨識，只是有針對手寫的字跡做調教。

---

**實際動手做**

Cognitive Service 提供了 C#、Node.js、Python、Java 與 Ruby SDK (服務涵蓋範圍略有不同)，如果你所愛的語言不在上面，不用擔心，Cognitive Service 全程提供的 RESTful API 使用，其實 SDK 也只是幫你把呼叫 RESTful API 的動作包起來而已。

> 如果沒有對應的 SDK 可以參考：<https://westus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fa>

在開始前，我們要先到 Azure Portal 上建立一個「電腦視覺 API」資源

> 也可以直接在 Cognitive Service 點選「免費試用」

![](https://cdn-images-1.medium.com/max/800/1*lnFJZW0ZKj7LnMAPcUQi6Q.png)![](https://cdn-images-1.medium.com/max/800/1*ds8d2crX52P4BiO-mnFBBQ.png)

1. 點選建立資源
2. 於搜尋中輸入：「Computer Vision」
3. 點選「電腦視覺」
4. 點選「建立」

![](https://cdn-images-1.medium.com/max/800/1*jAgxvy-83FPsYXdlK96o_w.png)

填寫相關資訊後點選建立

![](https://cdn-images-1.medium.com/max/800/1*EYTt9OhxdrvR3rPXOIScZw.png)

建立完成後，我們需要取得金鑰(Key)，按照上圖步驟來開啟金鑰頁面，取得金鑰後，我們先暫時存著，等等會用到。

接下來就輪到程式部分啦，這邊為了方便起見，我的專案類型使用 Console 專案，實際上任何專案類型都不會有影響。

先在命令列上輸入 `dotnet new console` 來新增 Console 專案

新增完專案後，第一件事就是來安裝相關的 Nuget 套件：Microsoft.Azure.CognitiveServices.Vision.ComputerVision

此 Nuget 套件已經有實作 .NET Standard 所以 .NET Core 也可以使用

```
dotnet add package Microsoft.Azure.CognitiveServices.Vision.ComputerVision
```

如果是使用 Package Explorer

```
Install-Package Microsoft.Azure.CognitiveServices.Vision.ComputerVision
```

![](https://cdn-images-1.medium.com/max/800/1*fZFI8P9jYfrphjVrGHNuzw.png)

我這邊程式就直接使用 Url 方式來拿到圖片，就不示範存取本機圖片了

先把相關變數設定好，像是 API Key 跟 ImageUrl，我把 apiKey 放在 appsettings.json 裡，圖片我就偷懶用一下蘋果日報的圖片

![](https://cdn-images-1.medium.com/max/800/0*pINZCte-v4t9ZtQ5.jpg)

接下來我們就把 `ComputerVisionClient` 給 New 起來，並根據 Azure Portal 上之資訊設定 `Endpoint`

![](https://cdn-images-1.medium.com/max/800/1*9qHfYgklmDztSaJlQxj6DA.png)

設定完後，在把圖片送出去之前還有最後一步，就是設定你要取得那些資訊欄位，我在這邊就只設定四個欄位

詳細欄位資訊如下

都設定完成後，我們就可以把圖片送出去做辨識啦

結果如下

![](https://cdn-images-1.medium.com/max/800/1*hohNLdQFxG8cKTQc7LT0-Q.png)
> 影片分析其實也是使用相同的方式，只是要將影片切成 Frame，然後再送出去做辨識

完整範例程式：[https://github.com/MoneyYu/2019ItHelpData](https://github.com/MoneyYu/2019ItHelpData/tree/master/Day01-02%20Computer%20Vision)