---
title: "[鐵人賽] Azure Data Service - Day 03 - Cognitive Service - 辨識 - Face API"
datePublished: Thu Oct 18 2018 11:35:46 GMT+0000 (Coordinated Universal Time)
cuid: cmnwpzxzc000c02lkg4f0fx0q
slug: azure-data-service-day-03-cognitive-service-face-api
canonical: https://medium.com/@abc12207/%E9%90%B5%E4%BA%BA%E8%B3%BD-azure-data-service-day-03-cognitive-service-%E8%BE%A8%E8%AD%98-face-api-4958dc469d0e
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1776070400179/8dfa5e88-5ce9-4762-b71a-b9959f57abe7.jpeg

---

---

### [IT 鐵人賽] Azure Data Service - Day 03 - Cognitive Service - 辨識 - Face API

#### Azure Data Service - Day 03 - Cognitive Service - Vision - Face API

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070400179/8dfa5e88-5ce9-4762-b71a-b9959f57abe7.jpeg)

上一篇我們介紹了讓電腦看圖說故事，那這篇我們就要來介紹更需要具體細節的部分：Face API。

Cognitive Service 針對臉部辨識的部分提供了以下的功能

* 臉部驗證
  檢查兩張臉部是屬於同一個人的可能性。API 會傳回信心分數，顯示兩張臉部是屬於同一個人的可能性。
* 臉部偵測
  偵測影像中的一或多張人臉，並取得影像臉部位置所在的臉部矩形及臉部屬性，該屬性內含以機器學習為基礎的臉部特徵預測。可用的臉部屬性功能 包括：年齡、表情、性別、姿勢、微笑及鬍子，以及影像中每張臉部的 27 個地標。
* 表情辨識
  臉部 API 現在與表情辨識整合，並傳回影像中每個臉部之一組表情的信心分數，例如生氣、藐視、厭惡、恐懼、快樂、不表意見、憂傷及驚奇。這些表情已知可跨文化普遍地與特定臉部表情溝通。

---

**範例網站介紹**

Face API 可以分成兩大部分，第一個是針對單一臉部做偵測，可以得知這些臉部的相關資訊，甚至是情緒的部分；另一個則是針對多個臉部，用來比對這多的臉部是否為相同人，簡單來說就是認臉。

我們先來看一下官網的範例，後面再來實際用程式動手做

* [偵測影像中的臉部](https://azure.microsoft.com/zh-tw/services/cognitive-services/face/#detection)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070402778/ff8ac5a0-ac3b-4bb6-b1bd-0ec2a67ef3fe.png)

這邊就用是大家的老婆：新垣結衣，來做為範例一下；這是一張「逃避可恥但有用」的劇照，可以看出它辨識出新垣結衣是女生，年紀只有 20 歲！不虧是大家的老婆；甚至還有是否有戴眼鏡以表情等資訊。

* [辨識影像中的情感](https://azure.microsoft.com/zh-tw/services/cognitive-services/face/#recognition)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070404742/1ee236e7-61a1-4cba-bd18-89f962f219dc.png)

在這個範例中就可以看到這是完全針對情緒的參數去做顯示，Cognitive Service 會給每個情緒都有一個分數，最高的分數通常就是結果；以這張來說，新垣結衣被判斷為目前表情情緒是中立。

* [影像中類似臉部的辨識與分組](https://azure.microsoft.com/services/cognitive-services/face/#verification)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070406767/d4b2ead2-556d-45c3-b892-7c504c36af9c.png)

這邊我特地找了「周杰倫」不同時期的照片來測試一下，左邊那張是近期的照片，右邊則是周杰倫超年輕時候的照片。

可以看到其實還是辨識的出來，只是信心程度沒有很高

> 沒有說信心程度很低就為不可能，有可能正解的信心程度為 0.4，但是其他選項的信心程度只有 0.1，所以最佳解仍為正解。

---

**實際動手做**

介紹完範例後，又到了動手做時間，廢話已經說很多，就直接進入 Coding 階段吧

> 在 Azure Portal 上建立 API Key 與新增專案的部分已於上一篇講解過，所以這邊就不騙篇幅了

這次要新增：人臉辨識 API Key

新增完專案後，首先先來安裝 Nuget 套件：Microsoft.Azure.CognitiveServices.Vision.Face

此 Nuget 套件已經有實作 .NET Standard 所以 .NET Core 也可以使用

現在只有 Preview 版本，所以後面要指定版本號

```
dotnet add package Microsoft.Azure.CognitiveServices.Vision.Face -v 2.2.0-preview
```

如果是使用 Package Explorer

```
Install-Package Microsoft.Azure.CognitiveServices.Vision.Face -Version 2.2.0-preview
```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070408443/a3bf3c64-3a6a-435e-be42-a8825121168f.png)

* 示範臉部偵測與表情辨識

我這邊程式就直接使用從 Url 方式來拿到圖片的方式，這邊照片就使用剛剛的範例照片

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070410417/14cd03da-0873-4268-b606-c715a8bc253d.jpeg)

先把相關變數設定好，像是 API Key 跟 ImageUrl，我把 apiKey 放在 appsettings.json 裡

接下來我們就把 `FaceClient` 給 New 起來，並根據 Azure Portal 上之資訊設定 `Endpoint`

> 因為這次安裝的 SDK 為 Preview 狀態，所以 EndPoint 不能這定成跟 Azure Portal 上顯示的一樣，要設為： https://[location].api.cognitive.microsoft.com/；參考：<https://github.com/Azure/azure-sdk-for-net/issues/4534>

設定完後，在把圖片送出去之前還有最後一步，就是設定你要取得那些資訊欄位，我在這邊就把所有的欄位加進來

都設定完成後，我們就可以把圖片送出去做辨識啦

結果如下

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070412523/9bd45ffc-f8b5-4599-aece-7a46c7418223.png)

完整範例程式：[https://github.com/MoneyYu/2019ItHelpData](https://github.com/MoneyYu/2019ItHelpData/tree/master/Day01-02%20Computer%20Vision)

---

下一篇來講影片索引器