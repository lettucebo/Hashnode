---
title: "政府共通平台之 RSS 網址錯誤問題"
datePublished: Mon Apr 13 2026 04:52:14 GMT+0000 (Coordinated Universal Time)
cuid: cmnwpui1a000i02jlfw0uffem
slug: rss
canonical: https://medium.com/@abc12207/%E6%94%BF%E5%BA%9C%E5%85%B1%E9%80%9A%E5%B9%B3%E5%8F%B0%E4%B9%8B-rss-%E7%B6%B2%E5%9D%80%E9%8C%AF%E8%AA%A4%E5%95%8F%E9%A1%8C-a7dd1f549a3c

---

---

goverment-shared-platform-rss-url-error

共用框架中的RSS雖正常顯示，但內容連結均為localhost(舊網址)

原因為當初在安裝時，因為尚不知道未來網址是什麼，所以當時就已localhost做為安裝url，此網址會被存入設定檔，有的服務會使用此網址當作root url

`說真的，這套由某家廠商寫得真的是漏洞百出，不知道是怎過驗收的，維護到現在我手邊幾乎都不再用了，當然某些機關還是些有再用，如果還有人在維護且有幸看到，lucky`

### 原因

其實發生原因也很簡單，在安裝時因為不知道網址是甚麼，所以先打了localhost，系統就直接使用localhost當作對外網址，而系統後台沒有提供修改介面

### 修正方法

檔案路徑位於：Tomcat 6.0\webapps\xxxxxxxx(管理後台資料夾)\WEB-INF\web.xml

修正以下節點即可