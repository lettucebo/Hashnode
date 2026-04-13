---
title: "政府共通平台之搜尋關鍵字HighLight"
datePublished: Mon Feb 27 2017 03:29:46 GMT+0000 (Coordinated Universal Time)
cuid: cmnwpught000h02jlczda6zny
slug: highlight
canonical: https://medium.com/@abc12207/%E6%94%BF%E5%BA%9C%E5%85%B1%E9%80%9A%E5%B9%B3%E5%8F%B0%E4%B9%8B%E6%90%9C%E5%B0%8B%E9%97%9C%E9%8D%B5%E5%AD%97highlight-af228905b5cc
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1776058153109/75c18544-7189-4d73-bf6d-9363650c40b0.png

---

---

common-platform-of-the-government-search-keyword-highlight

問題為：查詢結果關鍵字沒有被標示出來，如下圖所示。

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776058153109/75c18544-7189-4d73-bf6d-9363650c40b0.png)

### 解決辦法

#### 1. 將下列 JavaScript 加入 `<head></head>` 中

#### 2. 再將下列 JavaScript 加入 `<body></body>` 的最底部

highlight 傳遞的三個參數分別為：

* document.getElementById(‘inputText’)：抓取id為inputText的div，inputText可自行修改。
* ‘<%= queryWord %>’：queryWord為關鍵字變數，也可自行設定變數。
* ‘highlight’：style名稱，可自行編輯想要表示的顏色或形式，此範例的highlight的style為黃色底。

#### 3. 佈署想要 highlight 的區塊

### 完成畫面

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776058154974/cf0b7752-cfe7-491f-bae7-7a4f74e04398.png)

完成畫面