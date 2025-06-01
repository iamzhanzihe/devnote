---
title:前端開發學習筆記-HTML
vlook-doc-lib:
- [筆記網站跳轉](index.html?target=_self "快速挑轉到想要的網頁")
- [前端開發學習筆記★HTML](web_HTML.html?target=_self "網頁開發學習筆記★HTML")
- [前端開發學習筆記★CSS](web_CSS.html?target=_self "網頁開發學習筆記★HTML")
- [前端開發學習筆記★JS](web_JS.html?target=_self "網頁開發學習筆記★HTML")

---

######  ~VLOOK™~ *[<kbd>![](icon/vlook-hollow-dark.svg) VLOOK ![](icon/icon-more.svg)</kbd>](https://github.com/MadMaxChow/VLOOK)*<br>前端開發學習筆記-HTML<br>──<br><u>簡介</u><br>*本篇筆記是使用[<kbd>![](icon/Typora.svg) Typora</kbd>](https://typora.io/)及[<kbd>![](icon/markdown.svg) Markdown</kbd>](https://markdown.tw/)<br>結合GitHub開源模版撰寫而成並導出成HTML*<br>**JamesZhan**<br>*不允許複製下載`僅供閱覽`* *版本日期`2025年6月1日`*

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

* HTML標籤屬性

    - HTML屬性一般都出現在HTML標籤中，是HTML標籤的一部分

    - 標籤可以有屬性，包含了額外訊息，屬性一定要在雙引號中，標籤可以有多個屬性

    - 常見屬性名和屬性值成對出現 `<標籤名 屬性名1="屬性值" 屬性名2="屬性值"></標籤名>`

* HTML注釋

    - 格式 : `<!--我是HTML的注釋-->`

    - 方便其他工程師了解此代碼，且以後對程式的更動修改較為輕鬆

    - 注釋的內容不會被執行

* HTML的代碼格式

    - 空白鍵和換行在執行時都不會起作用，所以在編寫HTML文件時，可以使用且必須遵守代碼排版和縮進，以便於閱覽修改

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

## 元素規範

*^tab^*

> **塊狀元素**
>
> 主要用來搭建網站建構，頁面佈局，承載內容
>
> * 總是從新的行開始
> * 可以設置寬度、高度、內外邊距等屬性，默認是100%寬度
>
> 常見的標籤：
>
> * `div`：架構、結構
> * `p` ：段落
> * `h1~h6`：標題
> * `ol`：有序列表 → 配合`li` 去使用
> * `ul`：無序列表 → 配合`li` 去使用
> * `hr`：水平線
> * `noscript`：瀏覽器禁止JavaScript時會顯示的內容
> * `table`：表格
> * `form`：表單
> * `pre` ：預格式化文本，保留文本中的空格、換行，通常使用在code上

> **行內元素**
>
> 加強用戶內容顯示，增加細節
>
> * 和其他元素都在一行顯示
> * 寬度、高度、內外邊距等屬性都是不可修改的，寬度就是文字的寬度
>
> 常見的標籤：
>
> * `span`：文本中的一小節內容
> * `a`：超連結(跳轉頁面)
> * `code`：代碼文本
> * `em`：斜體(強調作用)
> * `i`：斜體，常用在圖標
> * `strong`：粗體(強調作用)
> * `b`：粗體
> * `label`：搭配`input`標籤使用

> **行內塊元素**
>
> 加強用戶內容顯示，增加細節
>
> * 和其他元素都在一行顯示
> * 可以設置寬度、高度、內外邊距等屬性
> * 寬度就是文字的寬度，可以修改
>
> 常見的標籤：
>
> * `input`：輸入標籤，配合`form`表單使用
> * `textarea`：多行文本輸入
> * `select`：定義選擇列表，配合`option`使用
> * `img`：圖片

> **HTML開發規範**
>
> 1. 塊狀元素與塊狀元素同等級，行內元素與行內元素同等級
>
>     ```html
>     	<div>
>     		<!--符合規範 同等級下span、a標籤都是行內元素-->
>     		<span></span>
>     		<span></span>
>     		<a></a>
>     	</div>
>     	
>     	<div>
>     		<!--不符合規範 同等級下span標籤是行內元素 p標籤是塊狀元素-->
>     		<span></span>
>     		<p></p>
>     		<p></p>
>     	</div>
>     ```
>
> 2. 塊狀元素可以包含行內元素或某些塊元素，但是行內元素只能包含行內元素不能包含塊狀元素
>
>     ```html
>     <div>
>     		<!--符合規範 塊狀元素div可以包含行內元素span-->
>     		<span></span>
>     </div>
>     
>     <span>
>     		<!--符合規範 行內元素span只能包含行內元素不能包含塊狀元素-->
>     		<span></span>
>     </span>
>     
>     <span>
>     		<!--不符合規範 行內元素span只能包含行內元素不能包含塊狀元素div-->
>     		<div></div>
>     </span>
>     ```
>
> 3. 特殊的塊狀元素只能包含行內元素，不能包含塊狀元素
>
>     ```html
>     h1 h2 h3 h4 h5 h6 p dt
>     
>     <p>
>     	<!--不符合規範 特殊塊狀元素p不能包含塊狀元素div-->
>     	<div></div>
>     </p>
>     
>     <h1>
>     	<!--不符合規範 特殊塊狀元素h1不能包含塊狀元素p-->
>     	<p></p>
>     </h1>
>     ```
>
> 4. `li`標籤可以包含`div`標籤，因為`li`和`div`標籤都是裝載內容的容器
>
>     ```html
>     <ul>
>     	<li>
>     		<div></div>
>     	</li>
>     </ul>
>     ```

## head常見標籤

# The End<br>*Written by JamesZhan*<br><sub>若是內容有錯誤歡迎糾正 *[<kbd>![](icon/gmail.svg?fill=text) Email</kbd>](mailto:henry16801@gmail.com?subject="內容錯誤糾正(非錯誤糾正可自行更改標題)")*</sub>