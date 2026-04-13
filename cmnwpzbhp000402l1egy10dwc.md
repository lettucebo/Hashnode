---
title: "商務版 Office 365 使用 Office Insider 更新版本"
datePublished: Sat Mar 10 2018 00:23:19 GMT+0000 (Coordinated Universal Time)
cuid: cmnwpzbhp000402l1egy10dwc
slug: office-365-office-insider
canonical: https://medium.com/@abc12207/%E5%95%86%E5%8B%99%E7%89%88-office-365-%E4%BD%BF%E7%94%A8-office-insider-%E6%9B%B4%E6%96%B0%E7%89%88%E6%9C%AC-36fc42b3e82f
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1776070294114/f7b0eeee-2e93-4313-8361-6790a5aa714b.png

---

---

#### How Office 365 Business commercial customers can get early access to new Office 2016 features

Office 365 是非常好的服務，更新就像 Windows 會自動定期更新，也有 Insider 計畫，但是 Insider 計畫是針對 Office 365 個人用戶，商務版 Office 365 則無法用同樣方式來套用 Insider 計畫

Office Insider 計畫簡單來說可以讓你更快體驗到每月升級及新功能，但是可能這些新功能還沒達到很穩定的階段

這邊紀錄一下如何讓商務版 Office 365 可以使用 Office Insider

> 如果要讓商務版 Office 365 使用 Office Insider，需要重新安裝 Office

**Step 1. 下載並設定 Office 部署工具**

從 Microsoft 下載中心下載最新 [Office 部署工具 (Office 2016 版本)](https://www.microsoft.com/download/details.aspx?id=49117)。

下載完畢後，執行該檔案 (officedeploymenttool\_xxxx–xxxx.exe) 進行解壓縮動作，指定一個資料夾作為存放空間，如下圖

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070294114/f7b0eeee-2e93-4313-8361-6790a5aa714b.png)

office deployment tool

#### Step 2. 編輯 configuration.xml 設定檔

使用文字編輯器打開 configuration.xml，我這邊使用 Visual Studio Code 開啟

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070296418/b65f7f42-35e1-43aa-9880-b543903cc123.png)

configuration.xml

有幾個關鍵字設定部分

* OfficeClientEdition：Office 安裝版本的位元，可以填 “64” 或 “32”
* Channel：更新頻道，可以選擇接收更新的方式

“Current” 代表正式版本

“ FirstReleaseCurrent” 或 “ InsiderSlow” 代表 Office 測試人員 - 慢

“InsiderFast” 代表 Office 測試人員 - 快

* Channel 可以參考：[Changes to update channels for Microsoft 365 Apps — Deploy Office | Microsoft Docs](https://docs.microsoft.com/en-us/deployoffice/update-channels-changes)
* Product：產品代碼，可參照：[Product IDs that are supported by the Office Deployment Tool for Click-to-Run](https://support.microsoft.com/en-us/help/2842297/product-ids-that-are-supported-by-the-office-deployment-tool-for-click)
* Language：要安裝的語言，可以參照i18n規範

#### Step 3. 進行安裝

編輯完 configuration.xml 後，就可以開始進行安裝了

將 **setup.exe** 和 **configuration.xml** 兩個檔案，複製到要安裝 Office 的電腦。

此電腦必須連線至網際網路，才能安裝 Office。

> 如果電腦已經安裝 Office，請先解除安裝 Office 並重新啟動電腦，再執行下一個步驟。

用系統管理員身分打開命令提示字元，切換目錄至已複製好檔案的資料夾，執行下列命令：

```
Setup.exe /configure configuration.xml
```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070298483/327858e8-6116-46d2-888f-cb53e22c75f5.png)

setup

這指令會將 Office 檔案從網際網路上的 CDN 節點下載到電腦上，並開始安裝。

執行後會出現安裝畫面

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1776070300318/fac0100e-bc59-48e4-9f12-049445eef8a2.png)

Installation

安裝完成後，開啟 Office 應用程式，例如 Word，然後移至 [**檔案** > **帳戶**。在 [**產品資訊**] 區段中，您應該會看到包含 「 Office 內部。 」 文字