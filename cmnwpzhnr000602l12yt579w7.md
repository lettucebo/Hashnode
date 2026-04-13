---
title: "在 Mac OS Mojave 上執行 VirtualBox"
datePublished: Mon Apr 13 2026 04:56:07 GMT+0000 (Coordinated Universal Time)
cuid: cmnwpzhnr000602l12yt579w7
slug: mac-os-mojave-virtualbox
canonical: https://medium.com/@abc12207/%E5%9C%A8-mac-os-mojave-%E4%B8%8A%E5%9F%B7%E8%A1%8C-virtualbox-6b233559dfc5
cover: https://cdn-images-1.medium.com/max/800/1*1FNpoxMvbF5VMapUyXY31Q.png

---

---

#### Run VirtualBOx at Mac OS Mojave

最近將我的 MacBookPro 升級到了 Mac OS Mojave Beta，為了要使用 Dark Mode，不過一升級後就發現無法執行 VirtualBox 了，會出現以下錯誤：

![](https://cdn-images-1.medium.com/max/800/1*1FNpoxMvbF5VMapUyXY31Q.png)

原因是因為 Apple 從 Mojave 開始封鎖所有不到 5.3 版本的 kext，而 VirtualBox 剛好使用的是 5.2 版本的 kext，基本上正式的解決方法只能等 Oracle 官方升級 kext 版本

除了等待 Oracle 官方升級以外，目前現在還有個 Workaround，以下介紹作法

1. 安裝 VirtualBox 5.2 以上的版本，一定要 5.2 以上的版本才可以使用這個 Workaround
2. 關閉 Mac 的 SIP ([System Integrity Protection](https://support.apple.com/en-us/HT204899))，關閉方式可參考此：[關閉 Mac 的 SIP (System Integrity Protection)](https://blog.developer.money/%E9%97%9C%E9%96%89-mac-%E7%9A%84-sip-system-integrity-protection-8f679c4fdd9e)，若本來就已經關閉的可以略過此步驟
3. 執行以下語法，用以將 VirtualBox 的 kext 加入白名單

這樣就可以執行 VirtualBox 了

正式解法還是要等官方出囉

Reference