---
title: "Surface 系列螢幕 3:2 低解析度選項"
datePublished: Tue Sep 04 2018 08:53:09 GMT+0000 (Coordinated Universal Time)
cuid: cmnwpzqbu000902l100xg2hwu
slug: surface-32
canonical: https://medium.com/@abc12207/surface-%E7%B3%BB%E5%88%97%E8%9E%A2%E5%B9%95-3-2-%E4%BD%8E%E8%A7%A3%E6%9E%90%E5%BA%A6%E9%81%B8%E9%A0%85-725481d1293
cover: https://cdn-images-1.medium.com/max/800/0*DKa7obLt8jOehxt0

---

---

#### Surface Device Display Resolution 3:2 Alternate Options

![](https://cdn-images-1.medium.com/max/800/0*DKa7obLt8jOehxt0)

我手頭上有兩台 Surface 裝置，Surface Pro 4 與 Surface Book 2，Surface 裝置的螢幕我覺得實在很不錯，PixelSense 是個好東西，不過對我來說有時候螢幕解析度太高也是個困擾，除了介面元素都會變小以外，也會稍微多耗點資源，所以我通常都習慣把解析度調低一點

不過 Surface 系列螢幕比例通常是 3:2，而 Windows 現在沒有辦法很好的支援，所以找不到低 3:2 解析度選項，這邊就就介紹如何把這些解析度加入選項

其實有兩種方式，第一種方式是透過 Intel 繪圖驅動程式修改，第二種則是透過修改機碼，這邊先介紹第二種方式，方便又快速

#### 透過修改機碼方式

首先先下載此 reg 檔案：<http://bit.ly/2Q3SEdX>

下載完成後開啟此機碼檔案

![](https://cdn-images-1.medium.com/max/800/1*LUINoHLe8FHPQ51WSvA0rw.png)

點選確定執行(若對檔案內容有疑慮的話就請不要執行)

執行完畢後，請重新開機

這樣解析度選項應該就會有很多 3:2 的選項

![](https://cdn-images-1.medium.com/max/800/1*Aim96_kUGYwD8FyvjFRKng.png)

#### 參考

[**Surface [Book/Book2/Pro3/Pro4/Pro2017] - high-dpi multi-monitor optimization regkey for alternate…**
*Setting up a live Surface demo using the scaling tweak and Vertical Surface Docks at the Seattle Maker Faire (EMP…*dancharblog.wordpress.com](https://dancharblog.wordpress.com/2015/10/26/surface-book-and-surface-pro-4-high-dpi-multi-monitor-optimization-regkey-for-alternate-32-aspect-ratio-resolutions/ "https://dancharblog.wordpress.com/2015/10/26/surface-book-and-surface-pro-4-high-dpi-multi-monitor-optimization-regkey-for-alternate-32-aspect-ratio-resolutions/")