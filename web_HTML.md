---
title:前端開發學習筆記-HTML
vlook-doc-lib:
- [筆記網站跳轉](index.html?target=_self "快速挑轉到想要的網頁")
- [前端開發學習筆記★HTML](web_HTML.html?target=_self "網頁開發學習筆記★HTML")
- [前端開發學習筆記★CSS](web_CSS.html?target=_self "網頁開發學習筆記★HTML")
- [前端開發學習筆記★JS](web_JS.html?target=_self "網頁開發學習筆記★HTML")

---

######  ~VLOOK™~ *[<kbd>![](icon/vlook-hollow-dark.svg) VLOOK ![](icon/icon-more.svg)</kbd>](https://github.com/MadMaxChow/VLOOK)*<br>前端開發學習筆記-HTML<br>──<br><u>簡介</u><br>*本篇筆記是使用[<kbd>![](icon/Typora.svg) Typora</kbd>](https://typora.io/)及[<kbd>![](icon/markdown.svg) Markdown</kbd>](https://markdown.tw/)<br>結合GitHub開源模版撰寫而成並導出成HTML*<br>**JamesZhan**<br>*不允許複製下載`僅供閱覽`* *版本日期`2025年6月11日`*

[TOC]

# 什麼是web前端

前端開發，主要的職責就是將資料以好看的樣式呈現出來。說白了，就是開發網頁

* 網頁由哪些部分組成 ?
    * 文字、圖片、音訊、視訊、超連結、表格等等
* 我們看到的網頁，背後的本質是什麼 ?
    * 前端程式設計師寫的前端程式碼 
* 前端的程式碼是如何轉換成使用者眼中的網頁的 ?
    * 通過瀏覽器解析和渲染成使用者看到的網頁
    * 瀏覽器中對程式碼進行解析和渲染的部分，稱為**瀏覽器核心**

市面上的瀏覽器非常多，比如：IE、Firefox、safari、GoogleChrome等等。 而且我們電腦上安裝的瀏覽器可能都不止一個

但是**不同的瀏覽器核心不同，對於相同的前端程式碼解析的效果也會存在差異**。 因此會造成一個問題，同一段前端程式，不同瀏覽器展示出來的效果是不一樣的，這個使用者體驗就很差了。而我們想達到的效果則是，即使使用者使用的是不同的瀏覽器，解析同一段前端程式碼，最終展示出來的效果都是相同的。
要想達成這樣一個目標，我們就需要定義一個統一的**web標準**

## web標準

**Web標準**也稱為**網頁標準**，由一系列的標準組成，大部分由W3C（ World Wide Web Consortium，全球資訊網協會）負責制定。由三個組成部分：

*[<kbd>![](icon/logo.svg) W3C  ![](icon/icon-more.svg?fill=text)</kbd>](https://www.w3.org/)*

* **HTML**：負責網頁的==結構==（頁面元素和內容）
* **CSS**：負責網頁的==表現==（頁面元素的外觀、位置等頁面樣式，如：顏色、大小等）
* **JavaScript**：負責網頁的==行為==（互動效果）

## 環境準備

> *[<kbd>![](icon/logo.svg) VScode  ![](icon/icon-download.svg?fill=text)</kbd>](https://code.visualstudio.com/download)* *[<kbd>![](icon/logo.svg) Chrome  ![](icon/icon-download.svg?fill=text)</kbd>](https://www.google.com/intl/zh-TW/chrome/)*

* VScode：編輯器，編寫程式碼

    * Chinese中文包套件
    * Live Server：即時重新載入程式碼，可以讓瀏覽器即時更新

    > [!note]
    >
    > * 介面放大：`ctrl` + `+` 、`command` + `+`
    > * 介面縮小：`ctrl` + `-`、`command` + `-`

* Chrome：瀏覽器，閱讀編寫的程式碼

# 什麼是HTML

HTML: **H**yper**T**ext **M**arkup **L**anguage，超文字標記語言

*[<kbd>![](icon/logo.svg) mdn  web docs  ![](icon/icon-more.svg?fill=text)</kbd>](https://developer.mozilla.org/zh-TW/docs/Web/HTML)*

* 超文字：超越了文字的限制，比普通文字更強大，除了文字資訊，還可以定義圖片、音訊、視訊等內容
* 標記語言：由標籤` <標籤名> `構成的語言
    - HTML標籤都是預定義好的 。例如：使用 `<h1>` 標籤展示標題，使用`<a>`展示超連結，使用`<img>`展示圖片，`<video>`展示視訊
    - HTML程式碼直接在瀏覽器中運行，HTML標籤由瀏覽器解析 

![ClShot 2025-06-01 at 15.29.40@2x](web_HTML.assets/ClShot 2025-06-01 at 15.29.40@2x.png)

## 如何建立HTML

*^tab^*

> **建立文件**
>
> 滑鼠右鍵 -> 新增文字文件 -> 更改檔案類型為.html
>
> > [!caution]
> >
> > 如果建立完HTML文件後依然是文字文件格式，需要將系統中隱藏已知文件類型取消勾選
> >
> > ![ClShot 2025-06-01 at 15.36.54@2x](web_HTML.assets/ClShot 2025-06-01 at 15.36.54@2x.png)

> **編寫HTML架構**
>
> *==HTML結構==*
>
> ```html
> <html>
>      <head>
>           <title>HTML 快速入門</title>
>      </head>
>      <body>
>                 
>      </body>
> </html>
> ```
>
> 其中`<html>`是根標籤，`<head>`和`<body>`是子標籤
>
> * `<head>` : 定義網頁的頭部，用來存放給瀏覽器看的資訊，如：CSS樣式、網頁的標題
> * `<body>` : 定義網頁的主體部分，存放給使用者看的資訊，也是網頁的主體內容，如：文字、圖片、視訊、音訊、表格等

> **在`<body>`中編寫HTML的核心內容**
>
> *==body核心內容==*
>
> ```html
> <html>
>      <head>
>         <title>HTML 快速入門</title>
>      </head>
>      <body>
>         <h1>Hello HTML</h1>
>         <img src="img/1.png">
>      </body>
> </html>
> ```

> **程式碼下載**
>
> *[<kbd>![](icon/logo.svg) 01.  HTML快速入門 ![](icon/icon-download.svg?fill=text)</kbd>](web_HTML.assets/code/第二章.zip)*

## HTML標籤

標籤是HTML最基本的單位，也是重要的組成部分，通常用 `<` 和 `>` 括起來，標籤有兩種形式:

*^tab^*

*==成對標籤==*

```html
<p>內容</p>
```

*==不成對標籤==*

```html
<hr />
```

> [!NOTE]
>
> HTML標籤大小寫問題
>
> 標籤大小寫無關，`<body />`和`<BODY />`視為同樣
> ，**HTML標籤推薦使小寫**

___

> **父子關係（巢狀關係）**
>
> 子級標籤換行且縮排（Tab鍵）
>
> ![1680255766672](web_HTML.assets/1680255766672.png)

> **兄弟關係（並列關係）**
>
> 兄弟標籤換行要對齊
>
> ![1680255775150](web_HTML.assets/1680255775150.png)

* HTML標籤屬性

    - HTML屬性一般都出現在HTML標籤中，是HTML標籤的一部分

    - 標籤可以有屬性，包含了額外訊息，屬性一定要在雙引號中，標籤可以有多個屬性

    - 常見屬性名和屬性值成對出現 `<標籤名 屬性名1="屬性值" 屬性名2="屬性值"></標籤名>`

* HTML注釋

    - 格式 : `<!--我是HTML的注釋-->`
    - 方便其他工程師了解此代碼，且以後對程式的更動修改較為輕鬆，**注釋的內容不會被執行**

    > [!note]
    >
    > 在 VS Code 中，**新增 / 刪除**註釋的快速鍵：**Ctrl + /**

* HTML的代碼格式

    - 空白鍵和換行在執行時都**不會起作用**，所以在編寫HTML文件時，可以使用且必須遵守代碼排版和縮進，以便於閱覽修改

    - 任何的空白鍵、換行、TAB都只會被視為一個空格

* HTML中的特殊符號

    * 這些特殊符號無法直接輸入顯示在瀏覽器上，會被誤認為是代碼當中的一部分，需在HTML文本中以`&`開頭，以`;`結尾

    *==HTML中的特殊符號==*

    ```html
    &nbsp; 空格
    &gt; >
    &lt; <
    ```

# HTML主結構

## 聲明標籤

*==聲明標籤==*

```html
<!DOCTYPE html> <!--聲明標籤-->
<html>
<!--頭部標籤-->
    <head>
    </head>
<!--主體標籤-->
    <body>
    </body>
</html>
```



* 最上面聲明`<!DOCTYPE html>`

    * 聲明是文件中的第一部分，位於文件最上面

    - 該標籤是告訴瀏覽器所使用的HTML規範

* 以`<html>`開始，以`</html>`結束，中間包含頭部標籤`<head></head>`及主體標籤`<body></body>`

> [!note]
>
> VS Code 可以快速生成骨架：在 HTML 檔案（.html）中，輸入`!`（英文）配合 Enter / Tab 鍵

## 標題標籤

==用在新聞標題、文章標題、網頁區域名稱、產品名稱等等==

```html
<h1>一級標題</h1>
<h2>二級標題</h2>
<h3>三級標題</h3>
<h4>四級標題</h4>
<h5>五級標題</h5>
<h6>六級標題</h6>
```

顯示特點：

* 文字加粗
* 字號逐漸減小
* 獨佔一行（換行）

> [!note]
>
> 1. h1 標籤在一個網頁中只能用一次，用來放新聞標題或網頁的 logo
> 2. h2 ~ h6 沒有使用次數的限制

## 段落標籤

==用在新聞段落、文章段落、產品描述資訊等等==

```html
<p>段落</p>
```

顯示特點：

* 獨佔一行

* 段落之間存在間隙

    ![ClShot 2025-06-11 at 00.29.08@2x](web_HTML.assets/ClShot 2025-06-11 at 00.29.08@2x.png)

## 換行及水平線

* 換行：`br`
* 水平線：`hr`

> [!note]
>
> 如何區別單標籤還是雙標籤？
>
> 如果今天的內容是**需要保裹住的，那麼就是雙標籤**，換行或是水平線都沒有內容要包住，所以使用單標籤

## 字體格式化標籤

---

> **強調效果**
>
> | 標籤名 |     效果      |
> | :----: | :-----------: |
> | strong |   **加粗**    |
> |   em   |    *傾斜*     |
> |  ins   | <u>下劃線</u> |
> |  del   |  ~~刪除線~~   |

> **一般效果**
>
> | 標籤名 |  效果  |
> | :----: | :----: |
> |   b    |  加粗  |
> |   i    |  傾斜  |
> |   u    | 下劃線 |
> |   s    | 刪除線 |



> [!note]
>
> `strong`、`em`、`ins`、`del` 標籤**語意上**自帶強調含義，在使用或開發的時候通常優先選擇這強調效果

## 圖片標籤

在網頁中插入圖片，src用於指定圖像的位置和名稱，是 `<img>` 的必要屬性

```html
<img  src="圖片的 URL" alt=""替代的文字>
```

> [!note]
>
> * 屬性名="屬性值"
> * 屬性寫在尖括號裡面，標籤名後面，標籤名和屬性之間用空格隔開，不區分先後順序

其他屬性：

|  屬性  |    作用    | 說明                               |
| :----: | :--------: | ---------------------------------- |
|  alt   |  替換文字  | 圖片無法顯示的時候顯示的文字       |
| title  |  提示文字  | 鼠標懸停在圖片上面的時候顯示的文字 |
| width  | 圖片的寬度 | 值為數字，沒有單位                 |
| height | 圖片的高度 | 值為數字，沒有單位                 |

### 相對路徑

==從當前檔案位置出發尋找目標檔案==

* / ： 表示進入某個資料夾裡面          → 資料夾名/
* . ：表示當前檔案所在資料夾           → ./
* ..：表示當前檔案的上一級資料夾   → ../  

![ClShot 2025-06-11 at 01.22.06@2x](web_HTML.assets/ClShot 2025-06-11 at 01.22.06@2x.png)

### 絕對路徑

==從根路徑出發尋找目標檔案==

* Windows 電腦從磁碟機代號(C:、D:)出發
* Mac 電腦從根目錄（/）出發

```html
<img  src="C:\images\mao.jpg">
```

> [!note]
>
> Windows 默認是 \ ，其他系統是 /，建議統一寫為 / 

## 超連結標籤

==點選跳轉到其他頁面==

```html
<a href="https://www.google.com">跳轉到google</a>
```

> [!caution]
>
> href 屬性值是跳轉地址，是超連結的必要屬性

超連結默認是在當前窗口跳轉頁面，新增 **target="_blank"** 實現**新窗口**打開頁面。

開發初期，不確定跳轉地址，則 href 屬性值寫為 **#**，表示**空連結**，頁面不會跳轉，在當前頁面刷新一次

```html
<a href="https://www.google.com">跳轉到google</a>

<!-- 跳轉到本地檔案：相對路徑尋找 --> 
<!-- target="_blank" 新窗口跳轉頁面 --> 
<a href="./01-標籤的寫法.html" target="_blank">跳轉到01-標籤的寫法</a>

<!-- #，表示空連結，不會跳轉 -->
<a href="#">空連結</a>
```

## 音檔

```html
<audio src="音檔的 URL"></audio>
```

|      屬性      |       作用       | 特殊說明                                       |
| :------------: | :--------------: | ---------------------------------------------- |
| src (必須屬性) |     音頻 URL     | 支持格式：MP3、Ogg、Wav                        |
|    controls    | 顯示音頻控制面板 |                                                |
|      loop      |     循環播放     |                                                |
|    autoplay    |     自動播放     | 為了提升用戶體驗，瀏覽器一般會禁用自動播放功能 |

> [!note]
>
> 書寫 HTML5 屬性時，如果屬性名和屬性值相同，可以簡寫為一個單詞
>
> ```html
> <audio src="./media/music.mp3" controls loop autoplay></audio>
> ```
>
> 

## 影片

```html
<video src="影片的 URL"></video>
```

|      屬性      |       作用       | 特殊說明                                       |
| :------------: | :--------------: | ---------------------------------------------- |
| src (必須屬性) |     視頻 URL     | 支持格式：MP4、WebM、Ogg                       |
|    controls    | 顯示視頻控制面板 |                                                |
|      loop      |     循環播放     |                                                |
|     muted      |     靜音播放     |                                                |
|    autoplay    |     自動播放     | 為了提升用戶體驗，瀏覽器支持在靜音狀態自動播放 |

> [!note]
>
> 在瀏覽器中，想要自動播放，必須有 muted 屬性
>
> ```html
> <video src="./media/vue.mp4" controls loop muted autoplay></video>
> ```
>
> 

# The End<br>*Written by JamesZhan*<br><sub>若是內容有錯誤歡迎糾正 *[<kbd>![](icon/gmail.svg?fill=text) Email</kbd>](mailto:henry16801@gmail.com?subject="內容錯誤糾正(非錯誤糾正可自行更改標題)")*</sub>