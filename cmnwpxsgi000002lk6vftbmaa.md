---
title: "Windows MySQL 備份與排程備份（透過指令列方式）"
datePublished: Mon Feb 27 2017 03:53:59 GMT+0000 (Coordinated Universal Time)
cuid: cmnwpxsgi000002lk6vftbmaa
slug: windows-mysql
canonical: https://medium.com/@abc12207/windows-mysql-%E5%82%99%E4%BB%BD%E8%88%87%E6%8E%92%E7%A8%8B%E5%82%99%E4%BB%BD-%E9%80%8F%E9%81%8E%E6%8C%87%E4%BB%A4%E5%88%97%E6%96%B9%E5%BC%8F-8dfec04ce0f7
cover: https://cdn-images-1.medium.com/max/800/0*3gZKLBFqyKZiXZII.png

---

---

windows-mysql-backups-and-scheduled-backups-command-line

![](https://cdn-images-1.medium.com/max/800/0*3gZKLBFqyKZiXZII.png)

MySQL 不如 SQL Server 有著 SQL Server Agent 來幫忙處理排程等事項，因此若要針對 MySQL 進行排程備份不外乎兩種方法：

1. 安裝第三方備份排程程式
2. 自行撰寫 Script 透過 Windows 排程定期執行

第一種方法需要安裝額外程式，優點是十分簡單，且通常都有已經撰寫好的 GUI 介面，但我比較不喜歡的一點是通常此類程式都為常駐程式，且要求授權（經費拮据）；目前 MySQL Administrator 免費版也已不支援自動備份排程功能(新版又已支援排程備份)，因此為了解救此問題，只好自己土炮 MySQL 自動備份排程了

`20160710 更新：現在官方所出的管理軟體已有免費支援備份`

大概的步驟為：先透過指令的方式進行備份，再將這指令透過 Windows 排程進行定期執行，這樣就達到我們所想要的效果了

1. 手動備份指令碼

可透過命令提示視窗執行

示範畫面：

![](https://cdn-images-1.medium.com/max/800/0*KSk9TatjVG58cgrP.png)

示範畫面

2. 自動排程備份

(1) 備份指令碼

因為排程備份的關係，要避免檔案名稱重複而導致覆蓋檔案問題，所以檔案名稱一定要透過變數產生，才不會發生檔案名稱相同，導致新的備份檔案蓋掉舊的備份檔案

(2) 設定排程執行

設定排程執行 Windows 就有內建非常方便的`工作排程器`，只要透過滑鼠點一點設定一下，即可方便完成排成設定

首先先開啟工作排程器：

![](https://cdn-images-1.medium.com/max/800/0*xVgndc-X_T0TGJ3i.png)

開啟工作排程器

![](https://cdn-images-1.medium.com/max/800/0*HpleY_sRhMHXVv3_.png)

開啟工作排程器

新增一基本工作：

![](https://cdn-images-1.medium.com/max/800/0*kdCKSetZAfqdymIa.png)

新增一基本工作

![](https://cdn-images-1.medium.com/max/800/0*Yn-3Ltm1mGBZpnuT.png)

新增一基本工作

![](https://cdn-images-1.medium.com/max/800/0*nqPi2xi6NFQgfOWM.png)

新增一基本工作

![](https://cdn-images-1.medium.com/max/800/0*-fy-BmOUuxd4Lxy8.png)

新增一基本工作

![](https://cdn-images-1.medium.com/max/800/0*pIj-jjaj-p_aKM4Y.png)

新增一基本工作

![](https://cdn-images-1.medium.com/max/800/0*x67saIzawYix169Z.png)

新增一基本工作

![](https://cdn-images-1.medium.com/max/800/0*4RXaTQXGb_dAEDh0.png)

新增一基本工作

通過以上步驟，即可完成透過 Windows 工作排程器來定時啟動備份指令

完成畫面如下：

![](https://cdn-images-1.medium.com/max/800/0*ZAx98LOgB9JVmnjS.png)

完成畫面