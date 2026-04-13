---
title: "關閉 Mac 的 SIP (System Integrity Protection)"
datePublished: Wed Jul 11 2018 16:56:50 GMT+0000 (Coordinated Universal Time)
cuid: cmnwpzg50000502l16ypnfhbb
slug: mac-sip-system-integrity-protection
canonical: https://medium.com/@abc12207/%E9%97%9C%E9%96%89-mac-%E7%9A%84-sip-system-integrity-protection-8f679c4fdd9e
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1776070312121/6eb1f82a-c965-4256-83c8-2bee355a5326.jpeg

---

---

#### Mac disable System Integrity Protection (SIP)

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070312121/6eb1f82a-c965-4256-83c8-2bee355a5326.jpeg)

這篇是要簡單介紹 Mac 要如何關閉 SIP (System Integrity Protection)，若是沒有必要，請不要亂關閉安全保護的機制，這篇是為了 VirtualBox 無法在 Mojave 上使用的其中一篇子文章

1. 首先將 Mac 用 Recovery Mode 開機，於重開機時按住 ***Command + R*** 直到 Apple 的 Logo 出現後放開，即可進入復原模式
2. 於上方選單中，點選： Utilities > Terminal，開啟終端機
3. 執行以下語法，用以關閉 SIP

```
csrutil disable
```

4. 重新開機

這樣就完成關閉 SIP 的動作了

若需要確認是否成功，可以執行以下語法

```
ls -lO /System /usr
```

列出的資料夾有 **restricted** 字眼，代表被 SIP 所保護

預設 (= SIP enabled)，以下的資料夾應該都是被 restricted 的 ([Apple Support page](https://support.apple.com/en-us/HT204899))

```
/System
/usr
/bin
/sbin
Apps that are pre-installed with OS X
```

而下列的資料夾則應該是可以自由存取的：

```
/Applications
/Library
/usr/local
```

[**How do I disable System Integrity Protection (SIP) AKA "rootless" on macOs [OS X]**
*Apple has introduced System Integrity Protection, also known as "rootless", with OS X 10.11, El Capitan. I understand…*apple.stackexchange.com](https://apple.stackexchange.com/a/208481 "https://apple.stackexchange.com/a/208481")