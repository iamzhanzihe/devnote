---
title:前端開發學習筆記-CSS
vlook-doc-lib:
- [筆記網站跳轉](index.html?target=_self "快速挑轉到想要的網頁")
- [前端開發學習筆記★HTML](web_HTML.html?target=_self "網頁開發學習筆記★HTML")
- [前端開發學習筆記★CSS](web_CSS.html?target=_self "網頁開發學習筆記★CSS")
- [前端開發學習筆記★JS](web_JS.html?target=_self "網頁開發學習筆記★JS")
- [前端開發學習筆記★WebAPI](web_WebAPI.html?target=_self "網頁開發學習筆記★JS")
- [前端開發學習筆記★AJAX](web_AJAX.html?target=_self "網頁開發學習筆記★JS")
- [前端開發學習筆記★React](web_React.html?target=_self "網頁開發學習筆記★React")
---

######  ~VLOOK™~ *[<kbd>![](icon/vlook-hollow-dark.svg) VLOOK ![](icon/icon-more.svg)</kbd>](https://github.com/MadMaxChow/VLOOK)*<br>前端開發學習筆記-CSS<br>──<br><u>簡介</u><br>*本篇筆記是使用[<kbd>![](icon/Typora.svg) Typora</kbd>](https://typora.io/)及[<kbd>![](icon/markdown.svg) Markdown</kbd>](https://markdown.tw/)<br>結合GitHub開源模版撰寫而成並導出成HTML*<br>**JamesZhan**<br>*不允許複製下載`僅供閱覽`* *版本日期`2025年6月1日`*

[TOC]

# 什麼是CSS

**CSS** 全名是 **Cascading Style Sheets**（階層樣式表），是用來**控制網頁外觀和版面配置**的語言

* 用鍵值對的方式呈現
* 屬性和值之間用冒號(:)分開，多個屬性之間用分號(;)隔開
* CSS中的注釋：`/*書寫注釋的內容*/`

```html
<title>CSS 初體驗</title> 
<style>
 /* 選擇器 { } */
  p {
   /* CSS 屬性 */
    color: red;
  }
</style>
<p>體驗 CSS</p>
```

## CSS引入方式

*^tab^*

> **內部樣式表：學習使用**
>
> CSS 程式碼寫在 `<style>` 標籤裡面
>
> ```html
> <!DOCTYPE html>
> <html lang="en">
> 
> <head>
>     <meta charset="UTF-8">
>     <meta name="viewport" content="width=device-width, initial-scale=1.0">
>     <title>Document</title>
>     <style>
>         input {
>             width: 100%;
>             height: 50px;
>         }
>     </style>
> </head>
> 
> <body>
>     輸入文字：<input type="text">
>     輸入文字：<input type="password">
> </body>
> 
> </html>
> ```

> **外部樣式表：開發使用**
>
> 1. 建立一個副檔名為.css的檔案
>
>    *==my.css==*
>
>    ```css
>    input {
>        width: 100%;
>        height: 50px;
>    }
>    ```
>
> 2. 在 HTML 使用 `<link>` 標籤引入
>
>    ```html
>    <!DOCTYPE html>
>    <html lang="en">
>          
>    <head>
>        <meta charset="UTF-8">
>        <meta name="viewport" content="width=device-width, initial-scale=1.0">
>        <title>Document</title>
>        <link rel="stylesheet" href="./mycss.css">
>    </head>
>          
>    <body>
>        輸入文字：<input type="text">
>        輸入文字：<input type="password">
>    </body>
>          
>    </html>
>    ```

> **行內樣式：配合 JavaScript 使用**
>
> CSS 寫在標籤的 `<style>` 屬性值裡
>
> ```html
> <!DOCTYPE html>
> <html lang="en">
> 
> <head>
>     <meta charset="UTF-8">
>     <meta name="viewport" content="width=device-width, initial-scale=1.0">
>     <title>Document</title>
>     <!-- <link rel="stylesheet" href="./mycss.css"> -->
> </head>
> 
> <body>
>     輸入文字：<input type="text" style="width: 100%; height: 50px;">
>     輸入文字：<input type="password" style="width: 100%; height: 50px;">
> </body>
> 
> </html>
> ```

# 基本選擇器

CSS 選擇器就像是**指路標**，告訴 CSS「要對哪些 HTML 元素套用樣式」。可以把它想像成在人群中**指名道姓**叫某個人

*==選擇器的基本概念==*

```css
選擇器 {
    樣式屬性: 值;
}
```

## 標籤選擇器

* 標籤選擇器：使用標籤名作為選擇器 → 選中同名標籤設定相同的樣式
* 例如：p, h1, div, a, img......

> [!caution]
>
> 標籤選擇器無法做差異化的呈現，只要被選中的標籤就會變成該樣式

```html
<style>
  p {
    color: red;   
  }
</style>
```

## 類選擇器

* 作用：尋找標籤，差異化設定標籤的顯示效果
* 步驟：
  1. 定義類選擇器 → `.類名`
  2. 使用類選擇器 → 標籤新增 ` class="類名"`

```html
<style>
  /* 定義類選擇器 */   
  .red {
    color: red;
  }
</style>
<!-- 使用類選擇器 -->
<div class="red">這是 div 標籤</div> 
<div class="red size">div 標籤</div>
```

> [!note]
>
> * 類名自訂，不要用純數字或中文，儘量用英文命名，多個單詞之間可以用 `-` 連結
> * 一個類選擇器可以供多個標籤使用
> * 一個標籤可以使用多個類名，類名之間用**空格**隔開，例如：`news-hd`

## id選擇器

* 作用：尋找標籤，差異化設定標籤的顯示效果
* 場景：id 選擇器一般**配合 JavaScript 使用**，很少用來設定 CSS 樣式步驟：
  1. 定義 id 選擇器 → `#id名`
  2. 使用 id 選擇器 → 標籤新增 `id= "id名"`

> [!caution]
>
> 同一個 id 選擇器在一個頁面只能使用一次

```html
<style>
  /* 定義 id 選擇器 */   
  #red {
    color: red;
  }
</style>
<!-- 使用 id 選擇器 -->
<div id="red">這是 div 標籤</div>
```

## 通用選擇器

* 作用：尋找頁面所有標籤，設定相同樣式
* 瀏覽器自動尋找頁面所有標籤，設定相同的樣式

> [!note]
>
> 通用選擇器通常用於**清除標籤的默認樣式**，例如：標籤默認的外邊距、內邊距
>
> ![ClShot 2025-09-01 at 22.14.55@2x](web_CSS.assets/ClShot 2025-09-01 at 22.14.55@2x.png)

```html
<style>
    * {
			margin: 0;
			padding: 0;
		}
</style>
```

## 練習

使用合適的選擇器，繪製兩個正方形

|        屬性名        |       作用       |
| :------------------: | :--------------: |
|      **width**       |  設定元素的寬度  |
|      **height**      |  設定元素的高度  |
| **background-color** | 設定元素的背景色 |

![ClShot 2025-09-01 at 22.22.07@2x](web_CSS.assets/ClShot 2025-09-01 at 22.22.07@2x.png)

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .brown {
            background-color: brown;
            width: 100px;
            height: 100px;
        }

        .orange {
            background-color: orange;
            width: 200px;
            height: 200px;
        }
    </style>
</head>

<body>
    <div class="brown">div1</div>
    <div class="orange">div2</div>
</body>

</html>
```

# 字體樣式

|     描述     |        屬性         |
| :----------: | :-----------------: |
|   字體大小   |    **font-size**    |
|   字體粗細   |   **font-weight**   |
|   字體傾斜   |   **font-style**    |
|     行高     |   **line-height**   |
|    字體族    |   **font-family**   |
| 字體複合屬性 |      **font**       |
|   文本縮進   |   **text-indent**   |
|   文本對齊   |   **text-align**    |
|    修飾線    | **text-decoration** |
|     顏色     |      **color**      |

## font-size 字體大小

文字尺寸，PC 端網頁最常用的單位 `px`

> [!note]
>
> Google瀏覽器默認字號是16px

> [!caution]
>
> `font-size` 屬性後面必須要有單位，否則不會生效

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>字體大小</title>
  <style>
    p {
      font-size: 20px;
    }
  </style>
</head>

<body>
  <p>測試文字的大小</p>
</body>

</html>
```

## font-weight 字體粗細

---

> **數字(開發使用)**
>
> | 描述 | 數值 |
> | ---- | ---- |
> | 正常 | 400  |
> | 加粗 | 700  |

> **關鍵字**
>
> | 描述 | 關鍵字 |
> | ---- | ------ |
> | 正常 | normal |
> | 加粗 | bold   |



- normal 正常字體，相當於數值400
- bold 粗體，相當於數值700

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>字體粗細</title>
  <style>
    h3 {
      font-weight: 700;
    }

    p {
      font-weight: 400;
    }
  </style>
</head>

<body>
  <h3>測試文字</h3>
  <p>測試文字</p>
</body>

</html>
```

## font-style 文字格式

* 作用：清除文字默認的傾斜效果
* 屬性值：
  * 正常（不傾斜）：normal 
  * 傾斜：italic

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    em {
      font-style: normal;
    }

    p {
      font-style: italic;
    }
  </style>
</head>

<body>
  <em>測試文字</em>
  <p>測試文字</p>
</body>

</html>
```

## line-height 行高

* 作用：設定多行文字的間距
* 屬性值：
  * 數字 + px
  * 數字（當前標籤font-size屬性值的**倍數**）

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    p {
      line-height: 2;
    }
  </style>
</head>

<body>
  <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Repudiandae dignissimos praesentium eveniet dolore, quam
    aliquid quos saepe sed corporis vitae eaque sequi quidem, doloribus, ipsa quod. Repudiandae eum voluptatem neque?
  </p>
</body>

</html>
```

> [!important]
>
> 行高 = 上間距 + 下間距 + 文字的高度
>
> 但是這樣不方便計算，所以行高的測量方法從**一行文字的最頂端量到下一行文字的最頂端**
>
> ![ClShot 2025-09-01 at 23.18.49@2x](web_CSS.assets/ClShot 2025-09-01 at 23.18.49@2x.png)

> [!note]
>
> 單行文字垂直居中技巧：**行高屬性值等於盒子高度屬性值**
>
> **只適用於單行文字**_~rd~_
>
> ![ClShot 2025-09-01 at 23.30.31@2x](web_CSS.assets/ClShot 2025-09-01 at 23.30.31@2x.png)
>
> ```html
> <!DOCTYPE html>
> <html lang="en">
> 
> <head>
>   <meta charset="UTF-8">
>   <meta name="viewport" content="width=device-width, initial-scale=1.0">
>   <title>Document</title>
>   <style>
>     div {
>       background-color: skyblue;
>       height: 100px;
> 
>       line-height: 100px;
>     }
>   </style>
> </head>
> 
> <body>
>   <div>
>     測試文字
>   </div>
> </body>
> 
> </html>
> ```

## font-family 字體

**font-family** 是 CSS 中用來指定文字字體的屬性，它可以設定多個字體名稱作為備選方案

> [!note]
>
> font-family屬性值可以書寫多個字型名，各個字型名用逗號隔開，執行順序是從**左向右依次尋找**
>
> font-family 屬性**最後**設定一個字型族名，網頁開發建議使用**無襯線字型**
>
> ![ClShot 2025-09-02 at 23.43.49@2x](web_CSS.assets/ClShot 2025-09-02 at 23.43.49@2x.png)

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    div {
      font-family: Georgia, 'Times New Roman', Times, sans-serif;
    }
  </style>
</head>

<body>
  <div>
    測試文字
  </div>
</body>

</html>
```

## font 複合屬性

* 使用場景：設定網頁文字公共樣式
* 複合屬性：屬性的簡寫方式，**一個屬性對應多個值的寫法**，各個屬性值之間用**空格**隔開

> [!caution]
>
> font: 是否傾斜  是否加粗  字號/行高 字型（**必須按順序書寫**）
>
> 字號和字型值必須書寫，否則 font 屬性不生效 

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    div {
      font: italic 700 20px/1.5 "Arial", sans-serif;
    }
  </style>
</head>

<body>
  <div>
    測試文字
  </div>
</body>

</html>
```

## text-indent 內容縮排

**text-indent** 是用來設定**段落首行縮排**的 CSS 屬性，只影響每個段落的第一行文字

* 數字 + px
* **數字 + em（推薦：1em = 當前標籤的字號大小）**

>[!note]
>
>使用em屬性來控制內容縮進，無論字體大小有無變化，都可以字適應調整

![ClShot 2025-09-02 at 23.58.13@2x](web_CSS.assets/ClShot 2025-09-02 at 23.58.13@2x.png)

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    div {
      text-indent: 2em;
    }
  </style>
</head>

<body>
  <div>
    測試文字測試文字測試文字測試文字測試文字測試文字測試文字		測試文字測試文字測試文字測試文字測試文字測試文字測試文字		測試文字測試文字測試文字測試文字測試文字測試文字測試文字		測試文字測試文字測試文字測試文字測試文字測試文字測試文字		測試文字測試文字測試文字測試文字測試文字
  </div>
</body>

</html>
```

## text-align 內容對齊方式

* 使用場景：控制內容水平對齊方式
* 屬性值：
  * left：左對齊(默認)
  * center：居中對齊
  * right：右對齊

> [!note]
>
> text-align本質是控制**內容**的對齊方式，屬性要設定給內容的父級
>
> ![ClShot 2025-09-03 at 00.05.12@2x](web_CSS.assets/ClShot 2025-09-03 at 00.05.12@2x.png)
>
> 可以看到是控制文字的內容，h1標籤的位置及大小是沒有改變的

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    h1 {
      text-align: center;
    }
  </style>
</head>

<body>
  <h1>一級標題</h1>
</body>

</html>
```

## text-decoration 內容修飾線

**text-decoration** 是用來為文字添加**裝飾線條**的 CSS 屬性，包括下劃線、上劃線、刪除線等效果

|     屬性值     |  效果  |        描述        |        常見用途        |
| :------------: | :----: | :----------------: | :--------------------: |
|     `none`     |   無   |  移除所有文字裝飾  |   清除連結預設下劃線   |
|  `underline`   | 下劃線 | 在文字下方添加線條 |   連結、強調重要文字   |
| `line-through` | 刪除線 | 在文字中間添加橫線 | 表示已刪除或作廢的內容 |
|   `overline`   | 上劃線 | 在文字上方添加線條 | 特殊設計效果、標題裝飾 |

![ClShot 2025-09-03 at 00.13.38@2x](web_CSS.assets/ClShot 2025-09-03 at 00.13.38@2x.png)

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    a {
      text-decoration: none;
    }

    div {
      text-decoration: underline;
    }

    p {
      text-decoration: line-through;
    }

    span {
      text-decoration: overline;
    }
  </style>
</head>

<body>
  <a href="https://www.google.com">Google</a>
  <div>div標籤</div>
  <p>p標籤</p>
  <span>span標籤</span>
</body>

</html>
```

## color 文字顏色

|  顏色表示方式  |       屬性值       |                說明                |         使用場景         |
| :------------: | :----------------: | :--------------------------------: | :----------------------: |
|   顏色關鍵字   |    顏色英文單詞    |        red, green, blue...         |         學習測試         |
|   rgb表示法    |   `rgb(r, g, b)`   | r,g,b表示紅綠藍三原色，取值：0-255 |           了解           |
|   rgba表示法   | `rgba(r, g, b, a)` |       a表示透明度，取值：0-1       | 開發使用，實現**透明色** |
| 十六進制表示法 |     `#RRGGBB`      | #000000, #ffcc00，簡寫：#000, #fc0 | 開發使用（從設計稿複製） |

>[!note]
>
>只要屬性值為顏色，都可以使用上述四種顏色表示方式，例如：背景色

![ClShot 2025-09-03 at 20.36.56@2x](web_CSS.assets/ClShot 2025-09-03 at 20.36.56@2x.png)

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    div {
      color: red;
    }

    p {
      color: rgb(0, 0, 255);
    }

    span {
      color: rgba(0, 255, 0);
    }

    h1 {
      color: #0000ff;
    }
  </style>
</head>

<body>
  <div>div標籤</div>
  <p>p標籤</p>
  <span>span標籤</span>
  <h1>h1標籤</h1>
</body>

</html>
```

# F12開發人員選項

**F12 開發人員選項**（也稱為開發者工具、DevTools）是瀏覽器內建的一套強大工具，專門用於網頁開發、除錯和分析

|      方法      | 操作                                                         |
| :------------: | ------------------------------------------------------------ |
|   **快捷鍵**   | 按 `F12` 鍵                                                  |
|  **右鍵選單**  | 右鍵點擊網頁 → 選擇「檢查」或「檢查元素」                    |
| **瀏覽器選單** | Chrome: 更多工具 → 開發人員工具 Firefox: 工具 → 網頁開發者 → 開發者工具 |
| **快捷鍵組合** | `Ctrl + Shift + I` (Windows/Linux) `Cmd + Option + I` (Mac)  |

![ClShot 2025-09-03 at 21.05.45@2x](web_CSS.assets/ClShot 2025-09-03 at 21.05.45@2x.png)

# 複合選擇器

**複合選擇器**是將多個基本選擇器組合使用，以更精確地選中特定元素的選擇器。它能讓我們更靈活地控制樣式應用範圍

![ClShot 2025-09-03 at 21.21.36@2x](web_CSS.assets/ClShot 2025-09-03 at 21.21.36@2x.png)

## 後代選擇器

==選中某元素的所有後代元素，包含兒子、孫子……==

> [!important]
>
> 父選擇器  子選擇器 { CSS 屬性}，父子選擇器之間用**空格**隔開

![ClShot 2025-09-03 at 21.26.37@2x](web_CSS.assets/ClShot 2025-09-03 at 21.26.37@2x.png)

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>後代選擇器</title>
  <style>
    div span {
      color: red;
    }
  </style>
</head>

<body>
  <span>span標籤</span>
  <div>
    <span>div裡的span標籤</span>
    <div>
      <span>div裡的div裡的span標籤</span>
    </div>
  </div>
</body>

</html>
```

## 子代選擇器

選中某元素的子代元素（最近的子級)

>[!important]
>
>父選擇器 > 子選擇器 { CSS 屬性}，父子選擇器之間用 **>** 隔開

![ClShot 2025-09-03 at 21.29.43@2x](web_CSS.assets/ClShot 2025-09-03 at 21.29.43@2x.png)

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>子代選擇器</title>
  <style>
    div > span {
      color: red;
    }
  </style>
</head>

<body>
  <span>span標籤</span>
  <div>
    <span>div裡的span標籤</span>
    <p>
      <span>div裡的p裡的span標籤</span>
    </p>
  </div>
</body>

</html>
```

## 群組選擇器

選中多組標籤設定相同的樣式

> [!important]
>
> 選擇器1, 選擇器2, …, 選擇器N { CSS 屬性}，選擇器之間用 **,** 隔開
>
> 最後一個值**不**能加逗號

![ClShot 2025-09-03 at 21.34.10@2x](web_CSS.assets/ClShot 2025-09-03 at 21.34.10@2x.png)

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>群組選擇器</title>
  <style>
    span,
    div,
    p {
      color: red;
    }
  </style>
</head>

<body>
  <span>span標籤</span>
  <div>div標籤</div>
  <p>p標籤</p>
</body>

</html>
```

## 交集選擇器

選中同時**滿足多個條件**的元素

> [!important]
>
> 選擇器1選擇器2 { CSS 屬性}，選擇器之間**連寫**，沒有任何符號

![ClShot 2025-09-03 at 21.39.08@2x](web_CSS.assets/ClShot 2025-09-03 at 21.39.08@2x.png)

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>交集選擇器</title>
  <style>
    p.box {
      color: red;
    }
  </style>
</head>

<body>
  <p class="box">p 標籤，使用了類選擇器 box</p>
  <p>p 標籤</p>
  <div class="box">div 標籤，使用了類選擇器 box</div>
</body>

</html>
```

## 偽類選擇器

偽類表示元素狀態，選中元素的某個狀態設定樣式，例如：滑鼠懸停狀態：**選擇器:hover { CSS 屬性 }**

---

>![ClShot 2025-09-03 at 22.05.41@2x](web_CSS.assets/ClShot 2025-09-03 at 22.05.41@2x.png)

> ![ClShot 2025-09-03 at 22.05.52@2x](web_CSS.assets/ClShot 2025-09-03 at 22.05.52@2x.png)

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>偽類選擇器</title>
  <style>
    a:hover {
      color: red;
    }
  </style>
</head>

<body>
  <a href="https://www.google.com">Google</a>
</body>

</html>
```

>[!note]
>
>|    選擇器    |     作用     |        說明        |
>| :----------: | :----------: | :----------------: |
>|  **:link**   |    訪問前    |  未被訪問過的連結  |
>| **:visited** |    訪問後    |  已被訪問過的連結  |
>|  **:hover**  |   鼠標懸停   | 鼠標懸停在元素上時 |
>| **:active**  | 點擊時(激活) |  正在被點擊的瞬間  |
>
>如果要給超連結設定以上四個狀態，需要按 **LVHA** 的順序書寫，工作中通常一個 a 標籤選擇器設定超連結的樣式， hover狀態特殊設定 

# CSS特性

## 繼承性

- 子元素會自動繼承父元素的某些 CSS 屬性
- 主要繼承文字相關屬性：`color`、`font-family`、`font-size`、`line-height` 等
- 不繼承佈局相關屬性：`width`、`height`、`margin`、`padding`、`border` 等

> [!caution]
>
> 如果標籤有默認文字樣式會繼承失敗。 例如：a 標籤的顏色、標題的字型大小

![ClShot 2025-09-03 at 23.07.10@2x](web_CSS.assets/ClShot 2025-09-03 at 23.07.10@2x.png)

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>疊層性</title>
  <style>
    div {
      color: red;
      font-weight: 700;
    }
  </style>
</head>

<body>
  <div>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Veritatis dolor expedita pariatur reiciendis! Corrupti
      ea qui aut esse, corporis vitae nihil repellendus ipsam, odit fugit explicabo fugiat aperiam illum officia!</p>
    <a href="https://www.google.com">Google</a>
  </div>
</body>

</html>
```



## 疊層性

- 當多個 CSS 規則作用於同一元素時，會按照特定順序進行覆蓋
- 後面的樣式會覆蓋前面的樣式（相同優先級情況下）
- 遵循「後來者居上」原則

![ClShot 2025-09-03 at 23.05.29@2x](web_CSS.assets/ClShot 2025-09-03 at 23.05.29@2x.png)

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>疊層性</title>
  <style>
    div {
      color: red;
      font-weight: 700;
    }

    div {
      color: blue;
      font-size: 30px;
    }
  </style>
</head>

<body>
  <div>div標籤</div>
</body>

</html>
```



## 優先級

- 決定當多個規則衝突時，哪個規則會被採用
- 優先級從高到低：
  1. `!important`
  2. 行內樣式 (`style="..."`)
  3. ID 選擇器 (`#id`)
  4. 類別選擇器 (`.class`)、屬性選擇器、偽類
  5. 元素選擇器 (`div`、`p`)
  6. 通用選擇器 (`*`)

> [!note]
>
> 選中標籤的範圍越大，優先順序越低

> **複合選擇器-疊加計算**
>
> CSS 優先級使用四位數字來計算：**(a, b, c, d)**
>
> - **a**: 行內樣式 (`style=""`) = 1000
> - **b**: ID 選擇器 (`#id`) = 100
> - **c**: 類別/屬性/偽類選擇器 (`.class`, `[attr]`, `:hover`) = 10
> - **d**: 元素選擇器 (`div`, `p`, `span`) = 1
>
> 1. 從**左向右**依次比較選個數，同一級個數多的優先順序高，如果個數相同，則向後比較
> 2. **!important 權重最高**
> 3. 繼承權重最低

*^tab^*

> **範例1**
>
> ```html
> <!DOCTYPE html>
> <html lang="en">
> 
> <head>
>   <meta charset="UTF-8">
>   <meta name="viewport" content="width=device-width, initial-scale=1.0">
>   <title>優先級</title>
>   <style>
>     .c1 .c2 div {
>       color: bule;
>     }
> 
>     div #box3 {
>       color: green;
>     }
> 
>     #box1 .c3 {
>       color: orange;
>     }
>   </style>
> </head>
> 
> <body>
>   <div id="box1" class="c1">
>     <div id="box2" class="c2">
>       <div id="box3" class="c3">
>         測試這行內容的顏色
>       </div>
>     </div>
>   </div>
> </body>
> 
> </html>
> ```
>
> * `.c1 .c2 div`：(0, 0, 2, 1)
> * `div #box3`：(0, 1, 0, 1)
> * `#box1 .c3`：(0, 1, 1, 0)
>
> *==第一輪比較==*
>
> ```less
> .c1 .c2 div  →  (0, 0, 2, 1)  ← 第一位: 0
> div #box3    →  (0, 1, 0, 1)  ← 第一位: 0  
> #box1.c3     →  (0, 1, 1, 0)  ← 第一位: 0
> ```
>
> *==第二輪比較==*
>
> ```less
> .c1 .c2 div  →  (0, 0, 2, 1)  ← 第二位: 0  ❌
> div #box3    →  (0, 1, 0, 1)  ← 第二位: 1  ✅
> #box1.c3     →  (0, 1, 1, 0)  ← 第二位: 1  ✅
> ```
>
> *==第三輪比較==*
>
> ```less
> div #box3    →  (0, 1, 0, 1)  ← 第三位: 0  ❌
> #box1.c3     →  (0, 1, 1, 0)  ← 第三位: 1  ✅ 獲勝！
> ```

> **範例2**
>
> ```html
> <!DOCTYPE html>
> <html lang="en">
> 
> <head>
>   <meta charset="UTF-8">
>   <meta name="viewport" content="width=device-width, initial-scale=1.0">
>   <title>優先級</title>
>   <style>
>     div p {
>       color: red;
>     }
> 
>     father {
>       color: blue;
>     }
>   </style>
> </head>
> 
> <body>
>   <div class="father">
>     <p class="son">
>       測試這行內容的顏色
>     </p>
>   </div>
> </body>
> 
> </html>
> ```
>
> 因為繼承權重最低所以 `father` 類屬性不生效，文字為紅色

# Emmet寫法

==程式碼的簡寫方式，輸入縮寫 VS Code 會自動生成對應的程式碼==

|       說明       |                 HTML標籤結構                 |   Emmet語法   |
| :--------------: | :------------------------------------------: | :-----------: |
|   **類選擇器**   |          `<div class="box"></div>`           | `標籤名.類名` |
|   **ID選擇器**   |            `<div id="box"></div>`            | `標籤名#id名` |
|   **同級標籤**   |             `<div></div><p></p>`             |    `div+p`    |
|  **父子級標籤**  |             `<div><p></p></div>`             |    `div>p`    |
| **多個相同標籤** | `<span>1</span><span>2</span><span>3</span>` |   `span*3`    |
| **有內容的標籤** |              `<div>內容</div>`               |  `div{內容}`  |

| 說明          | CSS屬性                                                | Emmet語法       |
| ------------- | ------------------------------------------------------ | --------------- |
| **寬度**      | `width`                                                | `w`             |
| **寬度500px** | `width: 500px;`                                        | `w500`          |
| **背景色**    | `background-color`                                     | `bgc`           |
| **多個屬性**  | `width: 200px; height: 100px; background-color: #fff;` | `w200+h100+bgc` |

# 背景樣式

網頁中，使用背景圖實現裝飾性的圖片效果

* 屬性名：**background-image**（bgi）
  * 屬性值：**url**(背景圖 URL)

![ClShot 2025-09-06 at 20.39.09@2x](web_CSS.assets/ClShot 2025-09-06 at 20.39.09@2x.png)

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>背景樣式</title>
  <style>
    div {
      width: 400px;
      height: 300px;
      background-color: pink;

      background-image: url(https://picsum.photos/200/200);
    }
  </style>
</head>

<body>
  <div>div標籤</div>
</body>

</html>
```

> [!note]
>
> 背景圖默認有平鋪（複製）效果，如果背景大小跟圖片大小不同時就會有這種效果

## 平鋪方式

屬性名：**background-repeat**（bgr） 

|     屬性值      |       效果       | 說明                                                         |
| :-------------: | :--------------: | ------------------------------------------------------------ |
| **`no-repeat`** |      不平鋪      | 背景圖片只顯示一次，不重複<br />![ClShot 2025-09-06 at 20.59.30@2x](web_CSS.assets/ClShot 2025-09-06 at 20.59.30@2x.png) |
|  **`repeat`**   | 平鋪（默認效果） | 水平和垂直方向都重複平鋪<br />![ClShot 2025-09-06 at 20.59.43@2x](web_CSS.assets/ClShot 2025-09-06 at 20.59.43@2x.png) |
| **`repeat-x`**  |   水平方向平鋪   | 只在水平（X軸）方向重複<br />![ClShot 2025-09-06 at 20.59.58@2x](web_CSS.assets/ClShot 2025-09-06 at 20.59.58@2x.png) |
| **`repeat-y`**  |   垂直方向平鋪   | 只在垂直（Y軸）方向重複<br />![ClShot 2025-09-06 at 21.00.07@2x](web_CSS.assets/ClShot 2025-09-06 at 21.00.07@2x.png) |

![ClShot 2025-09-06 at 20.54.53@2x](web_CSS.assets/ClShot 2025-09-06 at 20.54.53@2x.png)

## 背景圖位置

屬性名：**background-position**（bgp）

屬性值：水平方向位置 垂直方向位置

* 關鍵字

  |    關鍵字    | 位置 | 說明                  |
  | :----------: | :--: | --------------------- |
  |  **`left`**  | 左側 | 背景圖片靠左對齊      |
  | **`right`**  | 右側 | 背景圖片靠右對齊      |
  | **`center`** | 居中 | 背景圖片水平/垂直居中 |
  |  **`top`**   | 頂部 | 背景圖片靠頂部對齊    |
  | **`bottom`** | 底部 | 背景圖片靠底部對齊    |

* 座標

  * 水平：正數向右；負數向左
  * 垂直：正數向下；負數向上

> [!caution]
>
> * 關鍵字取值方式寫法可以顛倒取值順序
> * 可以只寫一個關鍵字，另一個方向默認為居中；數字只寫一個值表示水平方向，垂直方向為居中

![ClShot 2025-09-06 at 21.13.18@2x](web_CSS.assets/ClShot 2025-09-06 at 21.13.18@2x.png)

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>背景圖位置</title>
  <style>
    div {
      width: 400px;
      height: 300px;
      background-color: pink;

      background-image: url(https://picsum.photos/200/200);
      background-repeat: no-repeat;
      background-position: left center;
      /* background-position: 50px; */
    }
  </style>
</head>

<body>
  <div>div標籤</div>
</body>

</html>
```

## 背景圖縮放

屬性名：**background-size**（bgz)

* **關鍵字(常用)**_~Rd~_

  * **cover**：等比例縮放背景圖片以完全覆蓋背景區，可能**背景圖片部分看不見**

    ![ClShot 2025-09-06 at 21.33.51@2x](web_CSS.assets/ClShot 2025-09-06 at 21.33.51@2x.png)

  * **contain**：等比例縮放背景圖片以完全裝入背景區，可能**背景區部分空白**

    ![ClShot 2025-09-06 at 21.33.14@2x](web_CSS.assets/ClShot 2025-09-06 at 21.33.14@2x.png)

* **百分比(常用)**_~Rd~_：根據盒子尺寸計算圖片大小

* 數字 + 單位（例如：px）

> [!note]
>
> 圖片比例與盒子比例相同，使用 cover 或 contain 縮放背景圖效果相同

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>背景圖縮放</title>
  <style>
    div {
      width: 400px;
      height: 300px;
      background-color: pink;

      background-image: url(https://picsum.photos/200/200);
      background-repeat: no-repeat;
      background-size: cover;
    }
  </style>
</head>

<body>
  <div>div標籤</div>
</body>

</html>
```

## 背景圖固定

作用：背景不會隨著元素的內容滾動

屬性名：**background-attachment**（bga）

屬性值：**fixed**

> [!note]
>
> 一般背景圖片會隨著滑鼠滾動而移動

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>背景圖固定</title>
  <style>
    body {
      background-image: url(https://picsum.photos/500/500);
      background-repeat: no-repeat;
      background-attachment: fixed;
    }
  </style>
</head>

<body>
  <p>test測試文字</p>
  <p>test測試文字</p>
  <p>test測試文字</p>
  <p>test測試文字</p>
  <p>test測試文字</p>
  <p>test測試文字</p>
  <p>test測試文字</p>
  <p>test測試文字</p>
  <p>test測試文字</p>
  <p>test測試文字</p>
  <p>test測試文字</p>
  <p>test測試文字</p>
  <p>test測試文字</p>
  <p>test測試文字</p>
  <p>test測試文字</p>
  <p>test測試文字</p>
  <p>test測試文字</p>
  <p>test測試文字</p>
  <p>test測試文字</p>
  <p>test測試文字</p>
  <p>test測試文字</p>
  <p>test測試文字</p>
  <p>test測試文字</p>
  <p>test測試文字</p>
  <p>test測試文字</p>
  <p>test測試文字</p>
</body>

</html>
```

## 背景複合屬性

屬性名：**background**（bg）
屬性值：背景色 背景圖 背景圖平鋪方式 背景圖位置/背景圖縮放  背景圖固定（**空格隔開各個屬性值，不區分順序**)

> [!important]
>
> 背景圖位置/背景圖縮放，是使用 **/** 隔開

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>背景複合屬性</title>
  <style>
    div {
      height: 400px;
      width: 500px;
      background: pink url(https://picsum.photos/500/500) no-repeat right center/cover;
    }
  </style>
</head>

<body>
  <div>test測試文字</div>
</body>

</html>
```

# 顯示模式

CSS 的顯示模式（Display Mode）決定了元素在頁面中的排列方式和佔據空間的特性

佈局網頁的時候，需要根據標籤的顯示模式選擇合適的標籤擺放內容

|     特性     | Block 塊狀 | Inline 行內 | Inline-Block 行內塊 |
| :----------: | :--------: | :---------: | :-----------------: |
| **排列方式** |  獨佔一行  |  同行顯示   |      同行顯示       |
| **設置寬度** |   ✅ 可以   |  ❌ 不可以   |       ✅ 可以        |
| **設置高度** |   ✅ 可以   |  ❌ 不可以   |       ✅ 可以        |
| **默認寬度** | 佔滿父容器 | 由內容決定  |     由內容決定      |

## 塊狀(block)元素

![ClShot 2025-09-08 at 14.49.10@2x](web_CSS.assets/ClShot 2025-09-08 at 14.49.10@2x.png)

- **獨佔一行**：每個塊狀元素都會換行顯示
- **可設置寬高**：可以自由設定 `width` 和 `height`
- **默認寬度**：佔滿父容器的整個寬度

*==常見塊狀元素==*

```html
<div>、<p>、<h1>~<h6>、<ul>、<ol>、<li>
<header>、<footer>、<section>、<article>
<form>、<table>、<hr>、<pre>
```



## 行內(inline)用素

![ClShot 2025-09-08 at 14.51.40@2x](web_CSS.assets/ClShot 2025-09-08 at 14.51.40@2x.png)

- **同行顯示**：多個行內元素可以在同一行
- **不可設置寬高**：`width` 和 `height` 無效
- **內容決定大小**：大小由內容決定

*==常見行內元素==*

```html
<span>、<a>、<strong>、<em>、<b>、<i>
<img>、<input>、<button>、<label>
<code>、<small>、<sub>、<sup>
```



## 行內塊(inline-block)元素 

![ClShot 2025-09-08 at 14.54.59@2x](web_CSS.assets/ClShot 2025-09-08 at 14.54.59@2x.png)

- **同行顯示**：可以和其他元素在同一行
- **可設置寬高**：可以設定 `width` 和 `height`
- **內容決定大小**：大小由內容決定

*==常見行內塊元素==*

```html
<img>、<input>、<button>、<select>、<textarea>
```

## 轉換顯示樣式

轉換顯示樣式就是使用 `display` 屬性來**改變元素原本的顯示模式**，讓元素表現得像其他類型的元素一樣

> [!important]
>
> 這只改變**視覺表現**，不改變元素的**語義意義**！

|     屬性值     |  效果  | 詳細說明                             |
| :------------: | :----: | ------------------------------------ |
|    `block`     |  塊級  | 獨佔一行，可設寬高，默認寬度100%     |
| `inline-block` | 行內塊 | 同行顯示，可設寬高，結合兩者優點     |
|    `inline`    |  行內  | 同行顯示，不可設寬高，由內容決定大小 |

常見轉換類型：

1. 塊狀 → 行內

   ```css
   /* 原本的塊狀元素（如 div）變成行內顯示 */
   div {
     display: inline;
   }
   ```

2. 行內 → 塊狀

   ```css
   /* 原本的行內元素（如 span）變成塊狀顯示 */
   span {
       display: block;
   }
   ```

3.  任何元素 → 行內塊

   ```css
   /* 任何元素都可以變成行內塊 */
   .inline-block {
       display: inline-block;
   }
   ```

# 結構偽類選擇器

 CSS 中用來根據元素在 HTML 文檔結構中的位置來選取元素的選擇器。它們能夠精確選擇特定位置的元素，而不需要添加額外的 class 或 id

|      選擇器       | 說明                       | 範例                             |
| :---------------: | :------------------------- | :------------------------------- |
| **:first-child**  | 選擇父元素的第一個子元素   | `li:first-child` - 第一個列表項  |
|  **:last-child**  | 選擇父元素的最後一個子元素 | `li:last-child` - 最後一個列表項 |
| **:nth-child(n)** | 選擇父元素的第 n 個子元素  | `li:nth-child(3)` - 第n個列表項  |

![ClShot 2025-09-09 at 18.39.42@2x](web_CSS.assets/ClShot 2025-09-09 at 18.39.42@2x.png)

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>優先級</title>
  <style>
    li:first-child {
      background-color: red;
    }

    li:last-child {
      background-color: green;
    }
  </style>
</head>

<body>
  <ul>
    <li>li 1</li>
    <li>li 2</li>
    <li>li 3</li>
    <li>li 4</li>
    <li>li 5</li>
    <li>li 6</li>
    <li>li 7</li>
    <li>li 8</li>
    <li>li 9</li>
    <li>li 10</li>
  </ul>
</body>

</html>
```

*==nth公式==*

|        功能         |       公式       |         說明         | 實際選中的元素    |
| :-----------------: | :--------------: | :------------------: | ----------------- |
|    **偶數標籤**     |       `2n`       |   選擇所有偶數位置   | 2, 4, 6, 8, 10... |
|    **奇數標籤**     | `2n+1` 或 `2n-1` |   選擇所有奇數位置   | 1, 3, 5, 7, 9...  |
|   **5的倍數標籤**   |       `5n`       | 選擇第5、10、15...個 | 5, 10, 15, 20...  |
| **第5個以後的標籤** |      `n+5`       |  從第5個開始到最後   | 5, 6, 7, 8, 9...  |
| **第5個以前的標籤** |      `-n+5`      |    從第1個到第5個    | 1, 2, 3, 4, 5     |

![ClShot 2025-09-09 at 18.42.29@2x](web_CSS.assets/ClShot 2025-09-09 at 18.42.29@2x.png)

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>優先級</title>
  <style>
    li:nth-child(2n+1) {
      background-color: red;
    }
  </style>
</head>

<body>
  <ul>
    <li>li 1</li>
    <li>li 2</li>
    <li>li 3</li>
    <li>li 4</li>
    <li>li 5</li>
    <li>li 6</li>
    <li>li 7</li>
    <li>li 8</li>
    <li>li 9</li>
    <li>li 10</li>
  </ul>
</body>

</html>
```

# 偽元素選擇器

偽元素選擇器是 CSS 中用來**創建和樣式化不存在於 HTML 中的虛擬元素**的特殊選擇器，像是圖中的箭頭

![ClShot 2025-09-09 at 18.51.14@2x](web_CSS.assets/ClShot 2025-09-09 at 18.51.14@2x.png)

|   選擇器    | 說明                                |  位置  |
| :---------: | ----------------------------------- | :----: |
| `E::before` | 在E元素**裡面最前面**添加一個偽元素 | 內容前 |
| `E::after`  | 在E元素**裡面最後面**添加一個偽元素 | 內容後 |

>[!caution]
>
>* 必須設定 **content: ””屬性**，用來設定偽元素的內容，如果沒有內容，則**引號留空**即可
>* 偽元素默認是**行內顯示模式**
>* **權重和標籤選擇器相同**

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>優先級</title>
  <style>
    div::before {
      content: "我";
    }

    div::after {
      content: "吃飯"
    }
  </style>
</head>

<body>
  <div>愛</div>
</body>

</html>
```



# The End<br>*Written by JamesZhan*<br><sub>若是內容有錯誤歡迎糾正 *[<kbd>![](icon/gmail.svg?fill=text) Email</kbd>](mailto:henry16801@gmail.com?subject="內容錯誤糾正(非錯誤糾正可自行更改標題)")*</sub>
