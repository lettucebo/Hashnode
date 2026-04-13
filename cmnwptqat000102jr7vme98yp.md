---
title: "政府共通平台之轉寄好友修復"
datePublished: Mon Apr 13 2026 04:51:38 GMT+0000 (Coordinated Universal Time)
cuid: cmnwptqat000102jr7vme98yp
slug: 5ps5bqc5ywx6yca5bmz5yw5lml6l2j5ae5aw95yl5lu5b6p
canonical: https://medium.com/@abc12207/%E6%94%BF%E5%BA%9C%E5%85%B1%E9%80%9A%E5%B9%B3%E5%8F%B0%E4%B9%8B%E8%BD%89%E5%AF%84%E5%A5%BD%E5%8F%8B%E4%BF%AE%E5%BE%A9-7e7cb12d347e
cover: https://cdn-images-1.medium.com/max/800/0*VSut9Nftl5BzzX80.png

---

---

common-platform-of-the-government-forward-friends-fix

錯誤狀況為：

1. 使用轉寄好友功能時，會發生被 XSS 防護擋下，直接進入警告畫面

![](https://cdn-images-1.medium.com/max/800/0*VSut9Nftl5BzzX80.png)

2. 修復第一項後，點擊寄出，其中 xItem 之值變為 null ，導致 mail 與返回頁面之連結錯誤

![](https://cdn-images-1.medium.com/max/800/0*8ZxHnzpyKZXrvVjU.png)

### Fix 1. 轉寄好友之 XSS 防護

#### 發生原因

預設 XSS 防護模式為阻斷模式意即若視為 XSS 攻擊，則將此 Request 阻擋下來，並顯示警告頁面

![](https://cdn-images-1.medium.com/max/800/0*_wdjrQLTU2vn6jiA.png)

#### 解決方法

預設 XssFilter 模式為阻斷模式，將其修正為過濾模式

### 2. 送出後 xItem 之值變為 null

#### 錯誤畫面

![](https://cdn-images-1.medium.com/max/800/0*GA9FOVPEUEmuzR32.png)

#### 發生原因

範例網址：<http://web.tactri.gov.tw/wSite/sp?xdUrl=/wSite/Forward/Forward.jsp?xItem=6486&ctNode=216&mp=11>

其 `QuerySring` 應為 `xdUrl=/wSite/Forward/Forward.jsp?xItem=6486&ctNode=216&mp=11` 可從中解析出三個參數：

* `xdUrl=/wSite/Forward/Forward.jsp?xItem=6486`
* `ctNode=216`
* `mp=11`

其原始程式卻直接去取得 xItem 之值，導致所得 xItem 值均為 null

#### 解決方法

#### `Javascript`

透過 Javascript 處理 QueryString 取得 xItem 之值

#### `JSP`

原理與 Javascript 相同，透過程式處理取得 xItem 之值

### 修復完成畫面

![](https://cdn-images-1.medium.com/max/800/0*505JC-_U2jgQ-13v.png)

修復畫面