---
title: "[IT 鐵人賽] Azure Data Service - Day 04 - Cognitive Service - 辨識 - Video Indexer"
datePublished: Fri Oct 19 2018 15:02:44 GMT+0000 (Coordinated Universal Time)
cuid: cmnwq0bq1000q02jl8n3y0r7o
slug: it-azure-data-service-day-04-cognitive-service-video-indexer
canonical: https://medium.com/@abc12207/it-%E9%90%B5%E4%BA%BA%E8%B3%BD-azure-data-service-day-04-cognitive-service-%E8%BE%A8%E8%AD%98-video-indexer-470c10253ba1
cover: https://cdn-images-1.medium.com/max/800/0*EE5isZJChS0iTa8D.png

---

---

#### Azure Data Service - Day 04 - Cognitive Service - Vision - Video Indexer

![](https://cdn-images-1.medium.com/max/800/0*EE5isZJChS0iTa8D.png)

前面幾篇都是介紹靜態影像的辨識與分析，那這篇就來到針對影片來做處理。

Cognitive Service 針對影片辨識的部分提供了：Video Indexer

它整合了許多功能，在這邊列出一些比較重要的功能：

* 語系偵測
  可以自動偵測出這個影片是屬於哪個語系，目前支援： English, Spanish, French, German, Italian, Chinese (Simplified), Japanese, Russian, and Portuguese (Brazilian)。
* 語音轉字幕
  透過 Cognitive Service 語音轉文字的技術，將所有語音轉為字幕，並提供不同的字幕檔格式；如果影片的內容是屬於特殊領域或是發音較為特殊，也可以透過 Custom Speech 的方式來增進辨識率。
* 降噪
  透過 Skype 的過濾器，濾除像是電話噪音或是背景雜音。
* 角色分析
  可以知道哪個角色在何時說了那些話、語速如何，將這些資訊變成結構化資料提供搜尋。
* 文字辨識 (OCR)
  透過 OCR 的方式辨識影片有出現的任何文字。
* 擷取品牌資訊
  除了透過 OCR 辨識品牌文字以外，也會透過影像辨識品牌的 LOGO。

> 提供的功能實在很多，詳細請看：<https://docs.microsoft.com/zh-tw/azure/cognitive-services/video-indexer/video-indexer-overview>

> Video Indexer 是個 SaaS 服務，所以這次就沒有 Coding 的部分，但是它還是有提供 API 可以讓你自己來串接，從上傳檔案到取得分析完的結果。

---

我們直接開啟網站：<https://www.videoindexer.ai/>，點選「登入」，如果沒有帳號就自己註冊啦

![](https://cdn-images-1.medium.com/max/800/1*pqQvheA3xz7NOhzQAM3Czw.png)
> 直接免費試用，如果要付費再透過 Azure 付費就好

登入完後就可以看到以下畫面

![](https://cdn-images-1.medium.com/max/800/1*ucbpqCk0d2ZAVlgDb8ZDNg.png)

我就使用 Microsoft Ignite 2018 的其中一段影片作為範例：<https://www.youtube.com/watch?v=5quEOAM_jnc>

![](https://cdn-images-1.medium.com/max/800/1*VinvTqDjmD4maxDm77cRgg.png)

點選上傳來上傳影片檔案

* Video source language
  可以手動選擇影片的語系，也可以切成自動偵測。
* Privacy
  選擇影片的隱私設定，分為公開跟私密。
* Indexing preset
  可以指定音訊要處理的方式，有 Default、Audio only 與 Noise reduction。
* Streaming quality
  選擇影片的編碼方式，有單一編碼、適應性編碼或者是不編碼。

![](https://cdn-images-1.medium.com/max/800/1*F_z5KVV6rh3ZIa2dwBWNpA.png)

按下送出後就會開始進行處理。

![](https://cdn-images-1.medium.com/max/800/1*aRVjS-bmNVONeuiF-1rRCw.png)

處理完畢就回如上圖所顯示，直接點開 Play，來看看相關資訊。

![](https://cdn-images-1.medium.com/max/800/1*t10ipHHbuL0fPwuAjOaEyw.png)

可以在上圖看到 Overview 介面，下面來一一介紹。

![](https://cdn-images-1.medium.com/max/800/1*5Q8rDeNEITPyr6JxO4ewHw.png)

首先先來看看影片的播放介面，這就是一般常見的播放介面。

一號紅框是它轉換完成的字幕，英文基本上都是很準的。

二號紅框是影片編碼率，如果在編碼時就有指定自適應性編碼率，就可以有多個編碼品質可以選擇。

![](https://cdn-images-1.medium.com/max/800/1*1oMkeJ27wne5rDcGMF3RKw.png)

在人員區塊中，它會秀出所有有在影片中出現的人，如果是名人的話，甚至會自動幫你標記出他是誰，除此之外，在下方有一時間軸，有在影片中出現的時間都會標成黑色，點選後就影片就會自動跳到時間區段。

![](https://cdn-images-1.medium.com/max/800/1*4pywX_XCbYSaORgEH-BBAg.png)

這邊會自動判斷出影片中所有的關鍵字，把它一一列出來，同樣的，下方也提供時間軸，有出現關鍵字的時間區段會標為黑色，點選後讓影片可以快進到該關鍵字出現的時間區段。

![](https://cdn-images-1.medium.com/max/800/1*88mXUGtOPH4CGM4Ky5aVrA.png)

這區是提供所有場景的 TAG 列表，同樣的會在下面時間軸顯示有出現的時間區段，點選後會自動跳的影片的該時間區段。

![](https://cdn-images-1.medium.com/max/800/1*2vZt1JAjoPKogf4qnzjA5g.png)

這邊會顯示所有有在影片裡面偵測到不論是文字或者是商標的品牌，都會顯示在這邊。

![](https://cdn-images-1.medium.com/max/800/1*o7I3FouHr6YXFpRmMnj4og.png)

也會整合情緒偵測，偵測在影片的每個時間裡的情緒表現為何，把它做成時間軸來顯示。

![](https://cdn-images-1.medium.com/max/800/1*kuSUkKRi99Gil9w5rC9CoQ.png)

最後就是整合了智慧縮圖技術，它會自動尋找精彩焦點自動截圖。

---

![](https://cdn-images-1.medium.com/max/800/1*WP2Jz4JXnNLNF4OzSPFafw.png)

切到另一個頁籤：「Timeline」，這邊主要就是依據時間一一把不論是字幕或者是有在影片中被辨認出來的關鍵字或人物顯示出來

---

**小結**

透過上面的介紹，我們可以看到 Video Indexer 其實是把 Cognitive Service 所提供的不同服務集大成在這一個服務裡。

---

下一篇來介紹一下針對影片與圖片所提供的「內容仲裁」服務。