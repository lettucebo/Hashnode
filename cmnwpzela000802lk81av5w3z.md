---
title: "Nuget 套件封裝之相依版本設定"
datePublished: Mon Apr 13 2026 04:56:03 GMT+0000 (Coordinated Universal Time)
cuid: cmnwpzela000802lk81av5w3z
slug: nuget
canonical: https://medium.com/@abc12207/nuget-%E5%A5%97%E4%BB%B6%E5%B0%81%E8%A3%9D%E4%B9%8B%E7%9B%B8%E4%BE%9D%E7%89%88%E6%9C%AC%E8%A8%AD%E5%AE%9A-319cfac6ee2e
cover: https://cdn-images-1.medium.com/max/800/0*BECtlD1BQ14FPn0K.png

---

---

Nuget dependencies version setting

![](https://cdn-images-1.medium.com/max/800/0*BECtlD1BQ14FPn0K.png)

平常有將需要用到的工具發佈為 nuget 套件的習慣，在 ASP.NET MVC 中很常用到的分頁套件：[X.PagedList](https://www.nuget.org/packages/X.PagedList/) 中，其 [X.PagedList.MVC](https://www.nuget.org/packages/X.PagedList.Mvc/) 最近遇到了最新版本有重大改變的問題，所以之前針對 Bootstrap4 所寫的輔助工具([X.PagedList.Mvc.Bootstrap4](https://www.nuget.org/packages/X.PagedList.Mvc.Bootstrap4/))就失效了，被網友開了 Issue，最後決定要跟著 X.PagedList 版本走，但遇到了在 7.2.X 之前是一種版本，7.5.X 之後要換另外一個版本套件的問題，需要在 Nuget 封裝時就設定好，避免誤用錯誤版本

這邊就紀錄一下要如何在 Nuget 套件中設定其相依版本之條件

簡單來說，是透過一連串符號來代表是需要：大於、小於還是等於，然後數字就代表是甚麼版本

甚麼都沒有輸入，就代表至少要大於等於所指定之版本
例如：7.2，代表就是相依套件之版本 ≥ 7.2

若需要小於或等於所指定之版本，則不太依樣，需要用 (] 包住，並於左邊加入逗號
例如：(,7.2]，代表依套件之版本 ≤ 7.2

用括號包起來且加上逗號則代表不包含等於，大於或是小於則由逗號放在哪邊決定，若逗號放在左邊代表小於，右邊代表大於
例如：(7.2,)，代表相依套件之版本 > 7.2
(,7.2)，代表相依套件之版本 < 7.2

若需要強制指定特定版本時，則可以使用 [] 組合
例如：[7.2]，代表相依套件之版本 == 7.2

若要指定版本區間則是將兩個版本用 () 或是 [] 包起來，並於中間加入逗號
例如： [7.2,7.5]，代表 7.2 ≤ x ≤ 7.5
(7.2,7.5)，代表 7.2 < x < 7.5
[7.2,7.5)，代表 7.2 ≤ x < 7.5
(7.2,7.5]，代表 7.2 < x ≤ 7.5

特此紀錄一下，方便之後用到

[**NuGet 封裝版本的參考**
*確切的指定版本號碼和範圍而定的 NuGet 封裝，並安裝相依性的方式在其他封裝的詳細資訊。*docs.microsoft.com](https://docs.microsoft.com/zh-tw/nuget/reference/package-versioning "https://docs.microsoft.com/zh-tw/nuget/reference/package-versioning")