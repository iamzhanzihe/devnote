---
title: MySQL學習筆記
vlook-header-dup: 增;查;改;刪;練習資料
vlook-doc-lib:
- [快速的筆記網站跳轉](index.html?target=_self "可以快速挑轉到想要的網頁")
- [MySQL資料庫★基礎](MySQL_basic.html?target=_self "MySQL資料庫★基礎")
- [MySQL資料庫★進階](MySQL_advanced.html?target=_self "MySQL資料庫★進階")
---

[TOC]

###### MySQL學習筆記<br>**JamesZhan**<br>*不允許複製下載`僅供閱覽`*_~Og~_

# 什麼是資料庫

## 資料庫是什麼？



資料庫（Database）是按照數據結構來組織、存儲和管理數據的倉庫。每個數據庫都有一個或多個不同的API用於創建、訪問、管理、搜索和複製所保存的數據。

我們也可以將資料庫理解為一些關聯表的集合。資料庫的內容可以包括關於產品的資訊、人員的名單、銷售的數據等。此外，它可以用來存儲圖片、PDF、Word文檔等資訊。資料庫管理系統（DBMS）是能夠提供創建、查詢和管理數據庫的軟體應用程式。

*==RDBMS vs NoSQL==*

|            | 關聯式資料庫(RDBMS)                                          | 非關聯式資料庫(NoSQL)                                        |
| ---------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 定義       | 關聯式資料庫是根據關聯模型來組織和管理數據的資料庫。         | 非關聯式資料庫，也稱為 NoSQL 資料庫，不需要固定的模式，且不需要事先為要存儲的數據建立欄位。 |
| 數據結構   | 數據是以表格的形式來存儲的，每個表格都有自己的欄位（例如名字、地址等）和紀錄（即行）。 | 數據可以以多種方式來存儲，例如鍵值對、文件或者寬列等。       |
| 靈活性     | 較低，嚴格遵循結構化模式                                     | 較高，可以輕鬆調整結構或添加新的屬性                         |
| 查詢語言   | 使用結構化查詢語言（SQL）進行數據查詢。                      | 根據不同的資料庫，可能使用各種不同的查詢語言。               |
| 擴展性     | 垂直擴展，即通過增加單個伺服器的性能（例如增加更多的 CPU 或 RAM）來擴展。 | 水平擴展，即通過增加更多的伺服器來擴展。                     |
| 常見資料庫 | MySQL、oracle、db2                                           | mongodb、redis、memcache                                     |

## 什麼是MySQL?

mysql是一個開放原始碼的關聯式資料庫管理系統，現在是oracle公司旗下的一款產品，由C和C++語言編寫，可移植性高。支援在多種作業系統上安裝，以mysql作為資料庫，linux系統作為作業系統，apache或者nginx作為web伺服器，perl/php/python作為伺服器端的腳本直譯器，就可以搭建起一個免費的網站。被業界稱為LNMP或者LAMP

## 存儲引擎

存儲引擎是資料庫管理系統中負責管理數據和檢索的模塊也就是表的類型，不同的存儲引擎提供了不同的特性

![MySQL架構圖](mysql_basic.assets/20.png#80%)

* 查看存儲引擎`show engines;`

![查看存儲引擎](mysql_basic.assets/21.png)

* 指定存儲引擎`create table 資料表名稱(資料欄位 資料類型)engine=存儲引擎`

> [!NOTE]
>
> 預設為InnoDB，因此若使用InnoDB可以不指定存儲引擎



# MySQL安裝 (版本5.7.xx以上)

*^tab^*

> **安裝MySQL ❯**
>
> * 下載並安裝 [*點擊下載`MySQL Community Server`V5.4以上*_~Og~_](https://dev.mysql.com/downloads/mysql/)
>
> ![選擇Community Server](mysql_basic.assets/螢幕擷取畫面 2024-04-01 220044.png)
>
> ![按照對應的版本選擇下載檔案](mysql_basic.assets/ClShot 2025-04-14 at 10.30.00@2x.png)

> **開啟環境變數設定頁 ❯**
>
> 設置環境變數是為了讓系統能夠知道 MySQL 命令的位置，這樣就可以在任何地方執行 MySQL 命令，而不需要指定其完整路徑。這對於開發和管理資料庫來說非常方便
>
> 1. 找出MySQL安裝目錄(建議安裝解壓縮於C槽)
>
> 2. 開啟資料夾後複製文件目錄 例如 *==C:\Program Files\MySQL\MySQL Server 8.4\bin==*
>
> 3. 直接左下角「開始」搜尋環境變數
>
>     ![搜尋環境變數](mysql_basic.assets/1.png)![點擊環境變數按鍵](mysql_basic.assets/螢幕擷取畫面 2024-04-01 174544.png)

> **添加變數 ❯**
>
> 系統變數中找尋PATH並編輯、新增
>
> ![雙擊系統變數裡的Path變數](mysql_basic.assets/螢幕擷取畫面 2024-04-01 174741.png#40%)![新增複製的路徑](mysql_basic.assets/螢幕擷取畫面 2024-04-01 174927.png#40%)

## 加入my.ini至文件中無法登入再嘗試

1. 創立一個任意的文字文件(.txt的副檔名)

2. 輸入以下內容

    *==my.ini==*

    ```bash
    [mysqld]
    port=3306
    basedir=C:\\mysql-5.7.44-winx64
    datadir=C:\\mysql-5.7.44-winx64\\data
    max_connections=200
    max_connect_errors=10
    character-set-server=utf8
    default-storage-engine=INNODB
    default_authentication_plugin=mysql_native_password
    
    [mysql]
    default-character-set=utf8
    [client]
    port=3306
    default-character-set=utf8
    ```

    > [!WARNING]
    >
    > basedir、datadir 都要輸入自己解壓縮後存放檔案的位置

3. 將檔名改成my.ini，放入文件中

    ![my.ini放入安裝資料夾](mysql_basic.assets/螢幕擷取畫面 2024-04-01 220941.png)

4. 以管理員模式在PowerShell執行`mysqld --initialize-insecure --user=mysql`

5. 創建MySQL服務`mysqld --install "MySql57" --defaults-file="C:\\mysql-5.7.44-winx64\\my.ini"`

6. 啟動服務 `net start MySql57`

## 使用PowerShell登入MySQL

1. 輸入 `mysql -uroot -p`
    * 可以使用`-h`指定登入ip，默認是localhost
2. 直接再次按下Enter就可以直接不輸入密碼登入
    - root帳號登入就是管理員的帳號，擁有最高權限
3. 登出 `exit;` or  `quit;`

> [!WARNING]
>
> 在最近幾個版本都需手動新增my.ini檔案才能登入，不然就會卡在 **Access denied for user ‘ODBC‘@‘localhost‘ (using password: NO)**

# 數據類型

## 數值類型

### 整數類型

- tinyint
- smallint
- mediumint
- int
- bigint

> [!TIP]
>
> 1byte = 8 bits

*==整數類型==*

| 類型      | 大小     | 範圍(有符號)                                             | 範圍(無符號)                   |
| --------- | -------- | -------------------------------------------------------- | ------------------------------ |
| tinyint   | 1byte    | (-128, 127)                                              | (0, 255)                       |
| smallint  | 2bytes   | (-32768, 32767)                                          | (0, 65535)                     |
| mediumint | 3bytes   | (-8388608, 8388607)                                      | (0, 16777215)                  |
| int       | interger | 4bytes                                                   | (-2147483648, 2147483647)      |
| bigint    | 8bytes   | (-9,223,372,036,854,775,808,  9,223,372,036,854,775,807) | (0,18,446,744,073,709,551,614) |

> [!WARNING]
>
> 默認的顯示寬度都是在最大值的基礎上加1(因為正負號) 
>
> ==整數類型不需指定顯示寬度「int(3)」，若指定將不影響存儲寬度==
>
> ==整數類型指定寬度都是設定顯示寬度，其餘類型都是設置存儲寬度==

### 浮點數類型

- 單精度浮點數float

    *==單精度浮點數float==*

    ```sql
    float[(M,D)] [unsigned] [zerofill]
    
    M是數字總個數，M最大值=255
    D是小數點後位數，D最大值=30
    ```

- 雙精度浮點數double

    *==雙精度浮點數double==*

    ```sql
    double[(M,D)] [unsigned] [zerofill]
    
    M是數字總個數，M最大值=255
    D是小數點後位數，D最大值=30
    ```

    > [!WARNING]
    >
    > float、double看似一樣，但是佔用的位元數不一樣，精準度也有差

- 最精準浮點數decimal

    *==最精準浮點數decimal==*

    ```sql
    decimal[(M,D)] [unsigned] [zerofill]
    
    M是數字總個數，M最大值=65
    D是小數點後位數，D最大值=30
    ```

    > [!WARNING]
    >
    > 是浮點數中最精準的，但是無法擁有太多位數

## 日期類型

- year (1byte)

    *==year (1byte)==*

    ```sql
    YYYY (1901,2155)
    ```

- date (3bytes)

    *==date (3bytes)==*

    ```sql
    YYYY-MM-DD (1000-01-01, 9999-12-31)
    ```

- time (3bytes)

    *==time (3bytes)==*

    ```sql
    HH:MM:SS (-838:59:59, 838:59:59)
    ```

- datetime (8bytes)

    *==datetime (8bytes)==*

    ```sql
    YYYY-MM-DD HH:MM:SS (1000-01-01 00:00:00, 9999-12-31 23:59:59)
    ```

- timestamp (4bytes)

    *==timestamp (4bytes)==*
    
    ```sql
    YYYY-MM-DD HHMMSS (1970-01-01 00:00:00, 2038-01-19 03:14:07)
    ```

## datetime與timestamp差異

*==datetime vs timestamp==*

| 特性     | datetime   | timestamp  |
| -------- | ---------- | ---------- |
| 存儲空間 | 8bytes     | 4bytes     |
| 表示範圍 | 大         | 小         |
| 存儲時區 | 與時區無關 | 與時區有關 |
| 默認值   | null       | 當前時間   |

## 字符類型

- 固定長度 char
- 可變長度 varchar
- 長文本資料 text

> [!WARNING]
>
>  寬度指的是字符的個數

![字符類型](mysql_basic.assets/2.png)

可以使用`select chat_length(欄位名稱) from 資料表名稱` 查看字符個數



> [!WARNING]
>
> varchar比char多一個byte是因為在資料最前面還會多存儲一個寬度的資料

------

以下分別為char(5)、varchar(5)做出測試，個別都存入’小明(空格)’→3個字符

- char(5)下存的資料:’小明(空格)(空格)(空格)’→5個字符
- varchar(5)下存的資料:’小明(空格)’→3個字符

![char(5)下拿取的資料的長度會忽略掉後面的空格](mysql_basic.assets/3.png) ![varchar(5)下拿取的資料的長度](mysql_basic.assets/4.png)




> [!WARNING]
>
> 存取的長度跟拿取資料的長度不一樣 可以設定資料庫`set sql_mode = 'pad_char_to_full_length';` 讓char現出原形

![設定sql_mode](mysql_basic.assets/5.png)

## 列舉類型與集合類型

- 單選 enum (在給定的一個範圍內選一個值)
- 多選 set (在給定的一個範圍內選擇一個以上的值)

![enum](mysql_basic.assets/6.png)

![set](mysql_basic.assets/7.png)

> [!WARNING]
>
> 若是插入非範圍的值，不會報錯，但是會顯示為空

# 基本SQL語句

## 資料庫語言種類

- DDL 資料庫定義語言:創建、定義資料庫、表 CREATE、DROP、ALTER
- DML 資料庫操縱語言:插入數據INSERT、刪出數據DELETE、更新數據UPDATE、查詢數據SELECT
- DCL 資料庫控制語言:控制用戶權限 GRANT、REVOKE
- `help 指令` 查詢語法

## 系統資料庫

![系統資料庫](mysql_basic.assets/19.png#40%)

- information_schema：虛擬資料庫，存放資料庫啟動後的一些參數，如用戶表訊息、權限訊息...…
- performance_schema：主要用於收集資料庫服務器性能參數，處理查詢請求時發生的各種事件
- mysql：最重要的系統資料庫之一，存儲了 MySQL 伺服器的使用者帳號和權限信息
- sys：MySQL 5.7 版本之後引入的資料庫，用於提供關於 MySQL 實例性能的信息

## 資料庫操作(database)



資料庫就是數據的倉庫，對應到一個資料夾，儲存著一定資料結構的資料，一個資料庫中可能包含著若干個表

*^tab^*

> **增**
>
> - `create database db1 charset utf8;`
> - `create database if not exists db1;` 判斷資料庫是否存在，不存在才創建
>
> > [!NOTE]
> >
> > 命名規則
> >
> > - 可以使用字母、數字、底線、@、#、$
> > - 區分大小寫
> > - 具有唯一性
> > - 不能使用SQL的關鍵字
> > - 最長128個字

> **查**
>
> - 列出所有資料庫`show databases;`
>
> - `show create database db1;` 查看指定資料庫
>
>     ![查看指定資料庫](mysql_basic.assets/9.png)
>
> - `show databases;` 查看所有資料庫
>
>     ![查看所有資料庫](mysql_basic.assets/10.png)

> **改**
>
> * `alter database db1 charset gbk;` 修改指定資料庫的字符集
>
> ![修改字符集](mysql_basic.assets/11.png)

> **刪**
>
> * 刪除資料庫`drop database db1;`

## 資料表操作(table)

每一張資料表，是由行和列組成，每記錄一條資料，資料表就增加一行，每一個欄位有著多個屬性。例如是否允許為空、長度、類型等等

> [!IMPORTANT]
>
> 要先切換到當前資料庫`use db1;` 
>
> 查看當前所在的資料庫`select database();`

*^tab^*

> **增**
>
> *==增加資料表==*
>
> ```sql
> create table student_t(
> 	id int not null,
> 	name varchar(10) not null,
> 	age tinyint
> );
> ```
>
> > [!NOTE]
> >
> > 1. 在同一張資料表中，欄位名字不能相同 
> > 2. [(長度) 約束條件]選填

> **查**
>
> - `show create table t1;` 查看指定資料表
>
>     - `\G` 換行顯示
>    
>        ![查看指定資料表](mysql_basic.assets/12.png)
> 
>- `show tables;` 查看當前資料庫下所有的資料表名稱
> 
>    ![查看當前資料庫下所有的資料表名稱](mysql_basic.assets/13.png)
> 
>- `desc t1;` 查看指定資料表結構
> 
>    ![查看指定資料表結構](mysql_basic.assets/14.png)

> **改**
>
> - 修改表名`alter table 資料表名稱 rename 新資料表名稱;`
>
> - 增加表欄位
>
>     - `alter table 資料表名稱 add 欄位名稱 數據類型 [約束條件];`
>     - `alter table 資料表名稱 add 欄位名稱 數據類型 [約束條件] first;`
>     - `alter table 資料表名稱 add 欄位名稱 數據類型 [約束條件] after 欄位名稱;`
>
> - 修改資料項型態`alter table t1 modify name char(6);` 
>
>     ![修改資料項型態](mysql_basic.assets/螢幕擷取畫面 2024-04-02 015111.png)
>
> - 修改欄位名稱及資料型態`alter table t1 change name NAME char(7);` 
>
>     ![修改欄位名稱及資料型態](mysql_basic.assets/螢幕擷取畫面 2024-04-02 015215.png)

> **刪**
>
> * `drop table t1;`
> * `alter table 資料表名稱 drop 欄位名稱;`

> **複製**
>
> * 複製資料表結構+記錄`create table 新資料表名稱 select * from 將複製的資料表名稱;`
> * 只複製資料表結構
>     * `create table 新資料表名稱 select * from 將複製的資料表名稱 where 1=2;`
>     * `create table 新資料表名稱 like 將複製的資料表名稱`
>
> > [!NOTE]
> >
> > 1=2條件為False，查不到任何記錄

## 操作文件內容(資料內容)

*^tab^*

> **增**
>
> - `insert into t1 values 所有字段資料;`
> - `insert into t1(id,name) values(1,'James1'),(2,'James2'),(3,'James3');`
> - `insert into 表名1 select * from 表名2;` (複製資料)
> - `insert into 表名1（欄位名1，欄位名2） select 欄位名1，欄位名2 from 表名2;` (複製資料)

> **查**
>
> - `select id,name from db1.t1;` 針對指定欄位查看資料內容
>
> - `select * from db1.t1;` 查看所有資料內容
>
>     ![查看資料表](mysql_basic.assets/15.png)

> **改**
>
> - `update t1 set name='SB';` 修改所有name欄位的值
>
>     ![修改所有name欄位的值](mysql_basic.assets/16.png)
>
> - `update t1 set name='Lisa' where id=2;`
>
>     ![修改name欄位id=2的值](mysql_basic.assets/17.png)

> **刪**
>
> - `delete from t1 where id=2;`
>
> - `truncate table 表名`
>
>     ![刪除數據](mysql_basic.assets/18.png)

> [!NOTE]
>
> 問在刪改資料之前，要先怎麼做？
>
> A：會對資料進行備份操作，以防萬一，可以進行資料回退
>
> `delete`、`truncate`、`drop` 這三種共同點都是刪除資料，他們的不同點是什麼?
>
> A：
>
> - `delele` 會把刪除的操作記錄給記錄起來，以便資料回退，不會釋放空間，而且不會刪除定義。
> - `truncate`不會記錄刪除操作，會把表佔用的空間恢復到最初，不會刪除定義
> - `drop`會刪除整張表，釋放表佔用的空間。
>
> 刪除速度：`drop` > `truncate` > `delete`

# 約束條件

## not null 與 default

設置欄位是否可以為空值，若是not null未填入值則使用default值

![原始沒有特別設定的欄位格式](mysql_basic.assets/螢幕擷取畫面 2024-04-05 174956.png)

在gender中設定為not null，default為male

*==gender中設定為not null並且指定預設值==*

```sql
 create table t1(
    id int,
    gender enum('male', 'female') not null default 'male',
    skill set('Java', 'Python', 'C++')
 );
```

![指定預設值](mysql_basic.assets/22.png)

## unique key

設置欄位資料是唯一值

- 單個唯一

    單個欄位的值不能與其他的重複

    ![unique key](mysql_basic.assets/螢幕擷取畫面 2024-04-05 180332.png)

    - 方法1:

        *==方法1:欄位內約束==*

        ```sql
        create table t1(
        	 id int unique,
        	 gender enum('male', 'female') not null default 'male',
        	 skill set('Java', 'Python', 'C++')
        );
        ```

    - 方法2

        *==方法2:欄位外約束==*
        
        ```sql
        create table t1(
        	 id int,
        	 gender enum('male', 'female') not null default 'male',
        	 skill set('Java', 'Python', 'C++'),
        	 unique(id)
        );
        ```

- 聯合唯一

    多個欄位的值不能與其他的重複，舉例:(IP, Port)兩個欄位不能與其他重複否則網路會發生衝突

    ![聯合唯一](mysql_basic.assets/螢幕擷取畫面 2024-04-05 181319.png)

    *==多個欄位的值不能與其他重複==*
    
    ```sql
    create table t1(
    	 id int unique,
    	 ip char(15),
    	 port int,
    	 unique(ip,port)
    );
    ```

## primary key

主鍵是不為空且唯一的資料欄位

- 單一主鍵

    ![單一主鍵](mysql_basic.assets/螢幕擷取畫面 2024-04-05 190046.png)

    *==單一主鍵==*

    ```sql
    create table t1(
    	 id int primary key,
    	 gender enum('male', 'female') not null default 'male',
    	 skill set('Java', 'Python', 'C++')
    );
    ```

- 複合主鍵

    ![複合主鍵](mysql_basic.assets/23.png)

    *==複合主鍵==*
    
    ```sql
    create table t1(
    	 ip char(15),
    	 port int,
    	 primary key(ip, port)
    );
    ```

## foreign key

當所有資訊同時存在一張表時，會有重複儲存的問題，想要進行修改需要整個資料表進行更動，表中財務部門重複儲存，若是財務部門有進行更動，需要多次修改有關於財務部門的所有欄位

*==財物部門表==*

| id   | name  | department | description |
| ---- | ----- | ---------- | ----------- |
| 1    | Alex  | 財務部門   | 控制預算    |
| 2    | Wendy | 開發部門   | 研發新技術  |
| 3    | James | 財務部門   | 控制預算    |

*^tab^*

> **拆分為兩張表**
>
> 1. 先建立被關聯的表，並且保證被關聯的欄位唯一
>
>     *==dep表==*
>
>     | id   | department | description |
>     | ---- | ---------- | ----------- |
>     | 1    | 財務部門   | 控制預算    |
>     | 2    | 開發部門   | 研發新技術  |
>
>     ![dep表](mysql_basic.assets/24.png)
>
>     *==建立dep表==*
>
>     ```sql
>     create table dep(
>        id int primary key,
>        department char(5),
>        description char(50)
>     );
>     ```
>
> 2. 再建立關聯的表
>
>     *==emp表==*
>
>     | id   | name  | department_id(外鍵) |
>     | ---- | ----- | ------------------- |
>     | 1    | Alex  | 1                   |
>     | 2    | Wendy | 2                   |
>     | 3    | James | 1                   |
>
>     ![emp表](mysql_basic.assets/25.png)
>
>     *==建立emp表==*
>     
>     ```sql
>     create table emp(
>        id int primary key,
>        name char(5),
>        department_id int,
>        foreign key(department_id) references dep(id) 
>     	   on delete cascade on update cascade
>     );
>     ```
>
> > [!NOTE]
> >
> > 當被關聯表的數據更動或移除，`on delete cascade on update cascade` 指令會自動更新資料表

> **插入資料**
>
> 1. 先將資料插入被關聯表
>
>     *==資料插入被關聯表==*
>
>     ```sql
>     insert into dep values
>     	(1, "財務部門", "控制預算"),
>     	(2, "開發部門", "研發新技術");
>     ```
>
> 2. 再插入關聯表
>
>     *==資料插入關連表==*
>
>     ```sql
>     insert into emp values
>     	(1, 'Alex', 1),
>     	(2, 'Wendy', 2),
>     	(3, 'James', 1);
>     ```

## auto_increment

自動增加固定的數值，且欄位必須是一個鍵，例如:ID

![auto_increment](mysql_basic.assets/螢幕擷取畫面 2024-04-05 224232.png)

*==auto_increment約束==*

```sql
create table t1(
	 id int primary key auto_increment,
	 name char(16)
);
```

> [!NOTE]
>
> 設定起始值還有變化量 `show variables like 'auto_inc%';`  %是通配符
>
> ![設定起始值還有變化量](mysql_basic.assets/26.png)
>
> auto_increment_increment 變化量
>
> `set session auto_increment_increment=5` 設置變化量
>
> auto_increment_offset 初始值
>
> `set session auto_increment_offset=3`
>
> **!!!注意:變化量≥初始值，設置完必須重新開啟MySQL!!!**

> [!NOTE]
>
> 若是有設置auto_increment，直接使用delete指令清空表中的記錄，auto_increment的當前數值並不會被刪除 
> 需使用`truncate 資料表名稱` 才會重設計數器





# 表之間的關係

## 一對一

一個實體的單個實例可以關聯到另一個實體的單個實例

假設現在有兩張表:

- 客戶(一):一個學生只能是客戶群當中的一個客戶
- 學生(一):一個客戶也只會是一個學生

*==建立一對一資料表==*

```sql
CREATE TABLE customer (
   id INT PRIMARY KEY auto_increment,
   name VARCHAR(20),
   phone char(10) not null
);

CREATE TABLE student (
   id INT PRIMARY KEY auto_increment,
   class_name VARCHAR(20) not null,
   customer_id int unique,
   foreign key(customer_id) references customer(id)
	   on delete cascade
	   on update cascade
);

```

> [!NOTE]
>
> * customer_id一定要是唯一，若是重複就不是一對一關係
> * 使用`on delete cascade on update cascade`來保證資料完整性

*==資料插入一對一資料表==*

```sql
-- 插入 customer 表的四筆資料
INSERT INTO customer (name, phone) VALUES 
('張小明', '0912345678'),
('李小華', '0923456789'),
('王大雄', '0934567890'),
('林美玲', '0945678901');

-- 插入 student 表的四筆資料
INSERT INTO student (class_name, customer_id) VALUES 
('資訊工程系', 1),
('電機工程系', 2),
('企業管理系', 3),
('外國語文系', 4);

```



## 一對多

一個實體的多個實例可以關聯到另一個實體的單一實例

假設現在有兩張表:

- 出版社(一):一本書只會有一個出版社發行
- 書籍(多):一個出版社可能會出版好幾本書

*==建立一對多資料表==*

```sql
CREATE TABLE Publishers (
    publisher_id INT PRIMARY KEY,
    publisher_name VARCHAR(100)
);

CREATE TABLE Books (
    book_id INT PRIMARY KEY,
    publisher_id INT,
    FOREIGN KEY (publisher_id) REFERENCES Publishers(publisher_id)
    	on delete cascade
		on update cascade
);

```

*==資料插入一對多資料表==*

```sql
-- 插入 Publishers 表的兩筆資料
INSERT INTO Publishers (publisher_id, publisher_name) VALUES 
(1, '天下文化'),
(2, '遠流出版');

-- 插入 Books 表的四筆資料
INSERT INTO Books (book_id, publisher_id) VALUES 
(101, 1),
(102, 1),
(103, 2),
(104, 2);

```



## 多對多

一個實體的多個實例可以關聯到另一個實體的多個實例

假設現在有兩張表:

- 作者(多):一本書可以由多個作者同時編寫
- 書籍(多):一個作者可以同時發行多本書

---

- 作者表

    | id   | author |
    | ---- | ------ |
    | 1    | alex   |
    | 2    | james  |
    | 3    | lisa   |
    | 4    | joe    |

- 書籍表

    | id   | book     |
    | ---- | -------- |
    | 1    | 白雪公主 |
    | 2    | 三隻小豬 |
    | 3    | 大野狼   |

*==建立多對多關係表==*

```sql
CREATE TABLE author (
	 id INT PRIMARY KEY auto_increment,
   name VARCHAR(20)
);

CREATE TABLE book (
	 id INT PRIMARY KEY auto_increment,
   name VARCHAR(20)
);
```

> [!NOTE]
>
> 多對多關係中，不可能發生兩張表同時都有外鍵去參考另外一張表，此時要額外去創一張新的表



額外增加一張表

*==作者書籍表==*

| id   | author_id | book_id |
| ---- | --------- | ------- |
| 1    | 1         | 1       |
| 2    | 1         | 3       |
| 3    | 2         | 2       |
| 4    | 2         | 3       |

*==多對多關係額外產生一張關連表==*

```sql
create table AuthorBook(
	id int primary key auto_increment,
	author_id int not null,
	book_id int not null,
	constraint fk_author foreign key(author_id) references author(id)
		on delete cascade
		on update cascade,
	constraint fk_book foreign key(book_id) references book(id)
		on delete cascade
		on update cascade
);
```

*==資料插入一對多資料表==*

```sql
-- 插入作者數據
INSERT INTO author (name) VALUES 
('村上春樹'),
('J.K. 羅琳'),
('金庸'),
('李白'),
('艾蜜莉·狄金森');

-- 插入書籍數據
INSERT INTO book (name) VALUES 
('挪威的森林'),
('海邊的卡夫卡'),
('哈利波特與魔法石'),
('哈利波特與密室'),
('射鵰英雄傳'),
('神鵰俠侶'),
('靜夜思'),
('詩選集');

-- 插入作者與書籍的關聯數據
INSERT INTO AuthorBook (author_id, book_id) VALUES 
(1, 1),  -- 村上春樹 - 挪威的森林
(1, 2),  -- 村上春樹 - 海邊的卡夫卡
(2, 3),  -- J.K. 羅琳 - 哈利波特與魔法石
(2, 4),  -- J.K. 羅琳 - 哈利波特與密室
(3, 5),  -- 金庸 - 射鵰英雄傳
(3, 6),  -- 金庸 - 神鵰俠侶
(4, 7),  -- 李白 - 靜夜思
(5, 8),  -- 艾蜜莉·狄金森 - 詩選集
(4, 8);  -- 李白也與詩選集相關（展示多對多關係）

```



# SELECT 簡單查詢



> ###### 練習資料
>
> ```sql
> /*建立部門表*/
> CREATE TABLE dept(
> deptnu INT PRIMARY KEY comment '部門編號',
> dname VARCHAR(50) comment '部門名稱',
> addr VARCHAR(50) comment '部門地址'
> );
> 
> /*插入dept表資料*/
> INSERT INTO dept VALUES (10, '研發部', '北京');
> INSERT INTO dept VALUES (20, '工程部', '上海');
> INSERT INTO dept VALUES (30, '銷售部', '廣州');
> INSERT INTO dept VALUES (40, '財務部', '深圳');
> 
> ```
>
> ![部門表](mysql_basic.assets/ClShot 2025-04-13 at 18.26.17@2x.png)
>
> ```sql
> /*某個公司的員工表*/
> CREATE TABLE employee(
> empno INT PRIMARY KEY comment '僱員編號',
> ename VARCHAR(50) comment '僱員姓名',
> job VARCHAR(50) comment '僱員職位',
> mgr INT comment '僱員上級編號',
> hiredate DATE comment '僱傭日期',
> sal DECIMAL(7,2) comment '薪資',
> deptnu INT comment '部門編號'
> );
> 
> /*插入emp表資料*/
> INSERT INTO employee VALUES (1009, '唐僧', '董事長', NULL, '2010-11-17', 50000, 10);
> INSERT INTO employee VALUES (1004, '豬八戒', '經理', 1009, '2001-04-02', 29750, 20);
> INSERT INTO employee VALUES (1006, '猴子', '經理', 1009, '2011-05-01', 28500, 30);
> INSERT INTO employee VALUES (1007, '張飛', '經理', 1009, '2011-09-01', 24500,10);
> INSERT INTO employee VALUES (1008, '諸葛亮', '分析師', 1004, '2017-04-19', 30000, 20);
> INSERT INTO employee VALUES (1013, '林俊傑', '分析師', 1004, '2011-12-03', 30000, 20);
> INSERT INTO employee VALUES (1002, '牛魔王', '銷售員', 1006, '2018-02-20', 16000, 30);
> INSERT INTO employee VALUES (1003, '程咬金', '銷售員', 1006, '2017-02-22', 12500, 30);
> INSERT INTO employee VALUES (1005, '後裔', '銷售員', 1006, '2011-09-28', 12500, 30);
> INSERT INTO employee VALUES (1010, '韓信', '銷售員', 1006, '2018-09-08', 15000,30);
> INSERT INTO employee VALUES (1012, '安琪拉', '文員', 1006, '2011-12-03', 9500, 30);
> INSERT INTO employee VALUES (1014, '甄姬', '文員', 1007, '2019-01-23', 7500, 10);
> INSERT INTO employee VALUES (1011, '妲己', '文員', 1008, '2018-05-23', 11000, 20);
> INSERT INTO employee VALUES (1001, '小喬', '文員', 1013, '2018-12-17', 8000, 20);
> ```
>
> ![員工表](mysql_basic.assets/ClShot 2025-04-13 at 19.36.41@2x.png)
>
> ```sql
> /*創建員工薪水等級表*/
> CREATE TABLE salgrade(
> grade INT PRIMARY KEY comment '等級',
> lowsal INT comment '最低薪資',
> higsal INT comment '最高薪資'
> );
> 
> /*插入salgrade表資料*/
> INSERT INTO salgrade VALUES (1, 7000, 12000);
> INSERT INTO salgrade VALUES (2, 12010, 14000);
> INSERT INTO salgrade VALUES (3, 14010, 20000);
> INSERT INTO salgrade VALUES (4, 20010, 30000);
> INSERT INTO salgrade VALUES (5, 30010, 99990);
> ```
>
> ![薪水等級表](mysql_basic.assets/ClShot 2025-04-13 at 18.27.06@2x.png)

## 關鍵字的執行順序

![select查詢順序](mysql_basic.assets/27.png)

## 簡單查詢

*==employee表==*

| id   | name  | salary | department | description |
| ---- | ----- | ------ | ---------- | ----------- |
| 1    | Alex  | 25800  | 財務部門   | 控制預算    |
| 2    | Wendy | 25800  | 開發部門   | 研發新技術  |
| 3    | James | 31400  | 財務部門   | 控制預算    |

*==select簡單查詢==*

```sql
#查詢特定欄位
SELECT id,name,department,discription FROM employee;
SELECT name,salary FROM employee;
SELECT name,salary as emp_salary FROM employee;

#查詢全部欄位
SELECT * FROM employee;
```

> [!NOTE]
>
> 若是有重複資料可以使用`SELECT DISTINCT salary FROM employee;`

*==select運算查詢==*

```sql
SELECT name, salary*12 FROM employee;

#將欄位取別名(as可加可不加)
SELECT name, salary*12 AS Annual_salary FROM employee; 
SELECT name, salary*12 Annual_salary FROM employee;
```



*==正則表達式查詢==*

```sql
SELECT * FROM employee regexp '^ex';
```

*==定義顯示格式==*

```sql
#使用 concat()
SELECT CONCAT('姓名:',name,'年薪:',salary*12) Annual_salary FROM employee;

#使用 concat_ws()，設定每個欄位間的分隔符號
SELECT CONCAT_WS(':',name,salary*12) Annual_salary FROM employee;
```

## Where約束

> [!IMPORTANT]
>
> 不能使用聚合函數，例如：sum(), max()……

- 單條件查詢

    ```sql
    SELECT name FROM employee WHERE department='財務部門';
    ```

- 多條件查詢

    ```sql
    SELECT name FROM employee WHERE department='財務部門' and salary>26000;
    ```

- BETWEEN AND

    ```sql
    #搜尋一個範圍內的數值
    SELECT name,salary FROM employee WHERE salary>=10000 AND salary<=20000;
    SELECT name,salary FROM employee 
            WHERE salary BETWEEN 10000 AND 20000;
            
    SELECT name,salary FROM employee WHERE salary<10000 OR salary>20000;
    SELECT name,salary FROM employee 
            WHERE salary **NOT** BETWEEN 10000 AND 20000;
    ```

- IS NULL

    ```sql
    #判斷某資料內容是否為NULL不能直接使用=
    SELECT name,post_comment FROM employee 
            WHERE post_comment IS NULL;
    ```

- IN

    ```sql
    #搜尋特定值的資料
    SELECT name,salary FROM employee 
            WHERE salary=3000 OR salary=3500 OR salary=4000 OR salary=9000 ;
    SELECT name,salary FROM employee 
            WHERE salary IN (3000,3500,4000,9000) ;
    ```

- 模糊查詢

    - `‘&’`:匹配不限數量的所有字元
    - `‘_’`:僅匹配一個字元

    ```sql
    SELECT * FROM employee 
                WHERE name LIKE 'eg%';
                
    SELECT * FROM employee 
                WHERE name LIKE 'al__';
    ```

## Group by分組

> [!Important]
>
> 分組之後只能使用分組的資料欄位及聚合結果

- 聚合函數使用時需考慮執行順序，進行分組(group by)後才能使用聚合函數

    - max()
    - min()
    - avg()
    - sum()
    - count()

- 分組

    ```sql
    #使用部門進行分組
    select department from employee group by department;
    
    #每個部門有多少員工
    select department,count(id) employee_num from employee group by department;
    
    #每個部門最大、最小、平均、加總薪資
    select department,max(salary) max_salary from employee group by department;
    select department,min(salary) min_salary from employee group by department;
    select department,avg(salary) avg_salary from employee group by department;
    select department,sum(salary) sum_salary from employee group by department;
    ```

- group_concat

    ```sql
    #查詢分組後屬於該組別的所有資料欄位
    select department,group_concat(name) from employee group by department;
    ```

## Having過濾

> [!NOTE]
>
> 執行順序 `where` → `group by` → `having` 



```sql
#查詢各部門包含的員工數<2的崗位名稱，及員工姓名、個數
select department,group_concat(name) emp_name,count(id) as count
   from employee 
   group by department 
   having count(id)<2;
   
#查詢各部門平均薪資>30000的崗位名稱，及平均薪資
select department,avg(salary) 
	from employee group by department
	having avg(salary)>30000;
```

## Order by排序

---

> **asc 上升排序(默認)**
>
> ```sql
> #按照薪水升序排序
> SELECT * FROM employee ORDER BY salary;
> SELECT * FROM employee ORDER BY salary asc;
> ```
>
> 

> **desc 下降排序**
>
> ```sql
> #按照薪水降序排序
> SELECT * FROM employee ORDER BY salary DESC;
> ```
>
> 

## Limit限制資料數量

```sql
#初始位置默認從0開始
SELECT * FROM employee ORDER BY salary DESC LIMIT 3; 

#從0開始往後取5組資料
SELECT * FROM employee ORDER BY salary DESC LIMIT 0,5;
SELECT * FROM employee ORDER BY salary DESC LIMIT 5,5;
SELECT * FROM employee ORDER BY salary DESC LIMIT 10,5;
```



# 子查詢

> ###### 練習資料
>
> *==建立department表==*
>
> ```sql
> create table department(
> 	id int,
> 	name varchar(20) 
> );
> 
> #插入數據
> insert into department values
> 	(200,'技術'),
> 	(201,'人力資源'),
> 	(202,'銷售'),
> 	(203,'營運');
> 
> ```
>
> ![查看department資料表](mysql_basic.assets/ClShot 2025-05-19 at 15.40.39@2x.png)
>
> *==建立employee表==*
>
> ```sql
> create table employee(
> 	id int primary key auto_increment,
> 	name varchar(20),
> 	sex enum('male','female') not null default 'male',
> 	age int,
> 	dep_id int
> );
> 
> #插入數據
> insert into employee(name,sex,age,dep_id) values
> 	('egon','male',18,200),
> 	('alex','female',48,201),
> 	('wupeiqi','male',38,201),
> 	('yuanhao','female',28,202),
> 	('liwenzhou','male',18,200),
> 	('jingliyang','female',18,204);
> 
> ```
>
> ![查看employee資料表](mysql_basic.assets/ClShot 2025-05-19 at 15.42.43@2x.png)

子查詢（Subquery）是嵌套在其他 SQL 查詢中的查詢。子查詢可以出現在 SELECT、INSERT、UPDATE 或 DELETE 語句中，以及在 WHERE 或 HAVING 子句中。子查詢允許創建更為複雜和動態的數據操作和條件判斷

![department資料表及employee表](mysql_basic.assets/29.png)

## IN 關鍵字

*^tab^*

> **練習1**
>
> ###### 查詢平均年齡在25歲以上的部門名
>
> ```mysql
> #分解動作1 -> 查詢平均年齡在25歲以上的部門ID
> select dep_id from employee 
> group by dep_id having avg(age)>25; 
> 
> #分解動作2 -> 查詢部門名稱
> select name from department;
> 
> #合併結果
> select name from department where id in(
>     select dep_id from employee 
> 	group by dep_id having avg(age)>25
> );
> ```

> **練習2**
>
> ###### 查詢技術部門員工的姓名
>
> ```mysql
> #分解動作1 -> 查詢技術部門的ID號
> select id from department where name='技術';
> 
> #分解動作2 -> 查詢員工姓名
> select name from employee; 
> 
> #合併結果
> select name from employee where dep_id in (
>     select id from department where name='技術'
> );
> ```

> **練習3**
>
> ###### 查看不足1人的部門名
>
> ```mysql
> #分解動作1 -> 查詢有人的部門ID號 (從員工表查詢，只要是員工必會有部門)
> select distinct dep_id from employee;
> 
> #分解動作2 -> 查詢部門名稱
> select name from department; 
> 
> #合併結果
> select name from department where id not in (
> 	select distinct dep_id from employee
> ); 
> ```

## 比較、運算符

> **查詢大於所有人平均年齡的員工姓名與年齡**
>
> ```mysql
> #分解動作1 -> 查詢所有人的平均年齡
> select avg(age) from employee;
> 
> #分解動作2 -> 查詢員工名與年齡
> select name, age from employee;
> 
> #合併結果
> select name, age from employee 
>    where age > (select avg(age) from employee);
> ```

## EXIST 關鍵字

> [!NOTE]
>
> `EXISTS`查詢回傳`True`、`False`值

```sql
#查詢技術部門的所有員工
select * from employee
	where EXISTS (select id from department where name='技術')  
```

# SELECT 多表查詢

當需要從兩張或更多的表中查詢數據時，SQL 提供了不同的連接（Join）方式來實現表之間的數據合並

> ###### 練習資料
>
> ```sql
> #建表部門表
> create table department(
> id int,
> name varchar(20) 
> );
> 
> #插入數據
> insert into department values
> (200,'技術'),
> (201,'人力資源'),
> (202,'銷售'),
> (203,'營運');
> 
> #查看資料
> mysql> select * from department;
> +------+--------------+
> | id | name |
> +------+--------------+
> | 200 | 技術 |
> | 201 | 人力資源 |
> | 202 | 銷售 |
> | 203 | 運營 |
> +------+--------------+
> ```
>
> ```sql
> #建立員工表
> create table employee(
> id int primary key auto_increment,
> name varchar(20),
> sex enum('male','female') not null default 'male',
> age int,
> dep_id int
> );
> 
> #插入數據
> insert into employee(name,sex,age,dep_id) values
> ('egon','male',18,200),
> ('alex','female',48,201),
> ('wupeiqi','male',38,201),
> ('yuanhao','female',28,202),
> ('liwenzhou','male',18,200),
> ('jingliyang','female',18,204)
> ;
> 
> #查看資料
> mysql> select * from employee;
> +----+------------+--------+------+--------+
> | id | name | sex | age | dep_id |
> +----+------------+--------+------+--------+
> | 1 | egon | male | 18 | 200 |
> | 2 | alex | female | 48 | 201 |
> | 3 | wupeiqi | male | 38 | 201 |
> | 4 | yuanhao | female | 28 | 202 |
> | 5 | liwenzhou | male | 18 | 200 |
> | 6 | jingliyang | female | 18 | 204 |
> +----+------------+--------+------+--------+
> ```

## **INNER JOIN** 內連結

內連接是最常用的連接類型，它返回兩個表中匹配條件的交集。如果行在兩個表中都有匹配，那麼這些行就會被包括在查詢結果中

```sql
SELECT * from employee 
	INNER JOIN department on employee.dep_id=department.id;
	
SELECT * from employee, department on employee.dep_id=department.id;
```

![INNER JOIN查詢](mysql_basic.assets/Untitled-4895768.png)

## LEFT JOIN 左連結

顯示左表（**`table1`**）的所有行，以及右表（**`table2`**）中匹配的行。如果右表中沒有匹配，則結果中右表的部分將以 **`NULL`** 填充

```sql
SELECT * from employee 
	LEFT JOIN department on employee.dep_id=department.id;
```

![LEFT JOIN查詢](mysql_basic.assets/Untitled (1).png)

## RIGHT JOIN 右連結

顯示右表（**`table1`**）的所有行，以及左表（**`table2`**）中匹配的行。如果左表中沒有匹配，則結果中左表的部分將以 **`NULL`** 填充

```sql
SELECT * from employee 
	RIGHT JOIN department on employee.dep_id=department.id;
```

![RIGHT JOIN查詢](mysql_basic.assets/Untitled (2).png)

## 全外連結

> [!NOTE]
>
> 使用左連結和右連結達成全外連結效果，並使用UNION去除重複記錄

```sql
SELECT * from employee 
	RIGHT JOIN department on employee.dep_id=department.id
	UNION
SELECT * from employee 
	LEFT JOIN department on employee.dep_id=department.id;
```

![全外連結查詢](mysql_basic.assets/Untitled (3).png)

> [!NOTE]
>
> 1. 兩個`select`語句查詢結果的“欄位數”必須一致
> 2. 通常，也應該讓兩個查詢語句的欄位類型具有一致性
> 3. 可以聯合更多的查詢結果
> 4. 用到`order by`排序時，需要加上`limit`（加上最大條數就行），需要對子句用括號括起來 

# SQL實戰練習



> ###### 練習資料
>
> ```sql
> /*建立部門表*/
> CREATE TABLE dept(
> deptnu INT PRIMARY KEY comment '部門編號',
> dname VARCHAR(50) comment '部門名稱',
> addr VARCHAR(50) comment '部門地址'
> );
> 
> /*插入dept表資料*/
> INSERT INTO dept VALUES (10, '研發部', '北京');
> INSERT INTO dept VALUES (20, '工程部', '上海');
> INSERT INTO dept VALUES (30, '銷售部', '廣州');
> INSERT INTO dept VALUES (40, '財務部', '深圳');
> 
> ```
>
> ![ClShot 2025-04-13 at 18.26.17@2x](mysql_basic.assets/ClShot 2025-04-13 at 18.26.17@2x.png)
>
> ```sql
> /*某個公司的員工表*/
> CREATE TABLE employee(
> empno INT PRIMARY KEY comment '僱員編號',
> ename VARCHAR(50) comment '僱員姓名',
> job VARCHAR(50) comment '僱員職位',
> mgr INT comment '僱員上級編號',
> hiredate DATE comment '僱傭日期',
> sal DECIMAL(7,2) comment '薪資',
> deptnu INT comment '部門編號'
> );
> 
> /*插入emp表資料*/
> INSERT INTO employee VALUES (1009, '唐僧', '董事長', NULL, '2010-11-17', 50000, 10);
> INSERT INTO employee VALUES (1004, '豬八戒', '經理', 1009, '2001-04-02', 29750, 20);
> INSERT INTO employee VALUES (1006, '猴子', '經理', 1009, '2011-05-01', 28500, 30);
> INSERT INTO employee VALUES (1007, '張飛', '經理', 1009, '2011-09-01', 24500,10);
> INSERT INTO employee VALUES (1008, '諸葛亮', '分析師', 1004, '2017-04-19', 30000, 20);
> INSERT INTO employee VALUES (1013, '林俊傑', '分析師', 1004, '2011-12-03', 30000, 20);
> INSERT INTO employee VALUES (1002, '牛魔王', '銷售員', 1006, '2018-02-20', 16000, 30);
> INSERT INTO employee VALUES (1003, '程咬金', '銷售員', 1006, '2017-02-22', 12500, 30);
> INSERT INTO employee VALUES (1005, '後裔', '銷售員', 1006, '2011-09-28', 12500, 30);
> INSERT INTO employee VALUES (1010, '韓信', '銷售員', 1006, '2018-09-08', 15000,30);
> INSERT INTO employee VALUES (1012, '安琪拉', '文員', 1006, '2011-12-03', 9500, 30);
> INSERT INTO employee VALUES (1014, '甄姬', '文員', 1007, '2019-01-23', 7500, 10);
> INSERT INTO employee VALUES (1011, '妲己', '文員', 1008, '2018-05-23', 11000, 20);
> INSERT INTO employee VALUES (1001, '小喬', '文員', 1013, '2018-12-17', 8000, 20);
> ```
>
> ![ClShot 2025-04-17 at 19.56.21@2x](mysql_basic.assets/ClShot 2025-04-17 at 19.56.21@2x.png)
>
> ```sql
> /*創建員工薪水等級表*/
> CREATE TABLE salgrade(
> grade INT PRIMARY KEY comment '等級',
> lowsal INT comment '最低薪資',
> higsal INT comment '最高薪資'
> );
> 
> /*插入salgrade表資料*/
> INSERT INTO salgrade VALUES (1, 7000, 12000);
> INSERT INTO salgrade VALUES (2, 12010, 14000);
> INSERT INTO salgrade VALUES (3, 14010, 20000);
> INSERT INTO salgrade VALUES (4, 20010, 30000);
> INSERT INTO salgrade VALUES (5, 30010, 99990);
> ```
>
> ![ClShot 2025-04-13 at 18.27.06@2x](mysql_basic.assets/ClShot 2025-04-13 at 18.27.06@2x.png)

*^tab^*

> **1**
>
> 查出至少有一個員工的部門。顯示部門編號、部門名稱、部門位置、部門人數。
>
> ```sql
> /*先查部門人數*/
> select deptnu,count(*) as total from employee group by deptnu;
> 
> /*再做進階查詢*/
> select dept.deptnu, dept.dname, dept.addr, b.total from dept, 
> 	(select deptnu,count(*) as total from employee group by deptnu) as b 
> 	where dept.deptnu=b.deptnu;
> 	
> /*取別名 讓語句再更精簡*/	
> select a.deptnu, a.dname, a.addr, b.total from dept a, 
> 	(select deptnu,count(*) total from employee group by deptnu) b 
> 	where a.deptnu=b.deptnu;
> ```
>
> ![實戰練習1查詢結果](mysql_basic.assets/ClShot 2025-04-17 at 19.38.29@2x.png)

> **2**
>
> 列出薪水比安琪拉高的所有員工。
>
> ```sql
> select * from employee 
> 	where sal > (select sal from employee where ename = '安琪拉');
> ```
>
> ![實戰練習2查詢結果](mysql_basic.assets/ClShot 2025-04-17 at 19.44.16@2x.png)

> **3**
>
> 列出所有員工的姓名及其直接上級的姓名。
>
> ```sql
> select a.ename, ifnull(b.ename,"Boss") leader from employee a 
> 	left join employee b on a.mgr = b.empno;
> ```
>
> ![實戰練習3查詢結果](mysql_basic.assets/ClShot 2025-04-17 at 19.40.45@2x.png)

> **4**
>
> 列出受僱日期早於直接上級的所有員工的編號、姓名、部門名稱。
>
> ```sql
> select a.empno, a.ename, c.dname from employee a 
> 	left join employee b on a.mgr = b.empno
> 	left join dept c on a.deptnu = c.deptnu
> 	where a.hiredate < b.hiredate;
> ```
>
> ![實戰練習4查詢結果](mysql_basic.assets/ClShot 2025-04-17 at 19.41.10@2x.png)

> **5**
>
> 列出部門名稱和這些部門的員工資訊，同時列出那些沒有員工的部門。
>
> ```sql
> select a.dname, b.* from dept a
> left join employee b on a.deptnu = b.deptnu;
> ```
>
> ![實戰練習5查詢結果](mysql_basic.assets/ClShot 2025-04-17 at 19.41.31@2x.png)

> **6**
>
> - 列出所有文員的姓名及其部門名稱，所在部門的總人數。
>
>     ```sql
>     /*計算部門總數*/
>     select deptnu,count(*) total from employee group by deptnu
>                                                                                                                                                 
>     select a.ename, b.dname, a.job, c.total from employee a, dept b,
>     	(select deptnu,count(*) total from employee group by deptnu) c
>     	where a.deptnu=b.deptnu and a.job='文員' and a.deptnu=c.deptnu;
>     ```
>
> ![實戰練習6查詢結果](mysql_basic.assets/ClShot 2025-04-17 at 19.43.24@2x.png)

> **7**
>
> 列出該種工作最低薪水大於15000的，及從事此工作的員工人數。
>
> ```sql
> select job, count(*) from employee group by job having min(sal)>15000;
> ```
>
> ![實戰練習7查詢結果](mysql_basic.assets/ClShot 2025-04-17 at 19.58.11@2x.png)
>
> > [!IMPORTANT]
> >
> > 
> >
> > ```SQL
> > select job, count(*) from employee where sal > 15000 group by job;
> > ```
> >
> > ==這個跟解答有什麼差異點==_~rd~_
> >
> > * WHERE 子句在分組之前篩選資料，因此只考慮符合條的行
> > * HAVING 子句是在分組之後篩選分組，因此它可以分組的聚合結果進行篩選

> **8**
>
> 列出在銷售部工作的員工的姓名，假定不知道銷售部的部門編號。
>
> ```sql
> /*先查詢銷售部的編號*/
> select deptnu from dept where dname="銷售部";
> 
> select ename from employee where deptnu = (select deptnu from dept where dname="銷售部");
> ```
>
> ![實戰練習8查詢結果](mysql_basic.assets/ClShot 2025-04-17 at 20.15.48@2x.png)

> **9**
>
> 列出與諸葛亮從事相同工作的所有員工及部門名稱。
>
> ```sql
> select job from employee where ename = "諸葛亮"
> 
> select a.ename,b.dname from employee a, dept b 
> 	where a.job = (select job from employee where ename = "諸葛亮") and a.deptnu=b.deptnu;
> ```
>
> ![實戰練習9查詢結果](mysql_basic.assets/ClShot 2025-04-17 at 20.27.23@2x.png)

> **10**
>
> 列出薪水比在部門30工作的員工的薪水還高的員工姓名和薪水、部門名稱。
>
> ```sql
> /*先找出部門30最高的薪水*/
> select max(sal) from employee where deptnu=30;
> 
> select a.ename, a.sal, b.dname from employee a, dept b
> 	where a.deptnu=b.deptnu and a.sal>(select max(sal) from employee where deptnu=30);
> ```
>
> ![實戰練習10查詢結果](mysql_basic.assets/ClShot 2025-04-17 at 20.37.58@2x.png)

> **11**
>
> 列出每個部門的員工數量、平均工資。
>
> ```sql
> select deptnu, count(*), avg(sal) from employee group by deptnu;
> ```
>
> ![實戰練習11查詢結果](mysql_basic.assets/ClShot 2025-04-17 at 20.42.35@2x.png)

> **12**
>
> 列出薪金高於公司平均薪水的所有員工資訊，所在部門名稱，上級領導，工資等級。
>
> ```sql
> /*先找出平均薪水*/
> select avg(sal) from employee;
> 
> select a.*, c.dname, b.ename, d.grade from employee a, employee b, dept c, salgrade d
> 	where a.mgr=b.empno and a.deptnu=c.deptnu 
> 	and a.sal>(select avg(sal) from employee) and a.sal between d.lowsal and d.higsal;
> ```
>
> ![實戰練習12查詢結果](mysql_basic.assets/ClShot 2025-04-17 at 20.51.10@2x.png)

# 權限及密碼

## 限制root用戶登入

在 MySQL 中限制 root 用戶登入的 IP 是一項重要的安全措施，這些設定都放在mysql內建資料庫的user表中

* **防止遠程攻擊**：限制 root 只能從特定 IP（通常是本地 127.0.0.1）登入，可以大幅降低遠程攻擊的風險。如果允許 root 從任何 IP 登入（使用%`萬用字元），則增加了被惡意攻擊的可能性。
* **減少暴力破解風險**：限制登入 IP 可以顯著減少暴力破解密碼的嘗試，因為攻擊者必須先獲得允許連接的 IP 才能開始嘗試破解密碼。
* **最小權限原則**：遵循資安的最小權限原則，root 用戶擁有最高權限，應該限制其使用範圍，只在必要時從安全的位置使用。

*^tab^*

> **建立用戶**
>
> * username：將建立的使用者名稱 
> * host：指定該使用者在哪個主機上可以登入，如果是本地使用者可用localhost，如果想讓該使用者可以從任意遠端主機登入，可以使用萬用字元% 
> * password：該使用者的登入密碼，密碼可以為空
>
> *==建立用戶並指定密碼，可以在任一台遠程主機登入==*
>
> ```sql
> create user 'James'@'%' identified by '1234';
> ```
>
> *==建立用戶不指定密碼，指定在163網段的機器登錄==*
>
> ```sql
> create user 'James'@'163.%.%.%' identified by '';
> ```
>
> 

> **查看用戶及權限表**
>
> * 查看用戶可登入的網段
>
>     * `select user,host from mysql.user where user='root';`
>
>         ![查看用戶](mysql_basic.assets/ClShot 2025-04-21 at 16.32.53@2x.png)
>
> * 查看權限
>
>     * `show grants for 'James'@'%';`
>
>         ![James的用戶權限](mysql_basic.assets/ClShot 2025-04-21 at 16.31.58@2x.png)

> **修改用戶權限表**
>
> 修改mysql資料庫裡的user表，限定本機登入
>
> ```sql
> update mysql.user set host='localhost' where user='root';
> ```
> 

> **刪除指定用戶**
>
> * 刪除使用者
>
>     * `drop user 'James'@'%';`
>
>     * `delete from mysql.user where user='James';`


> [!WARNING]
>
> 每次設定完都必須要刷新權限才會生效`flush privileges;`

## 修改用戶密碼

修改使用者密碼分三種方法

1. `set password for 使用者@ip = password('密碼');`

2. `mysqladmin -u使用者 -p舊密碼 password 新密碼;`

    ![輸入原先密碼，再輸入新密碼](mysql_basic.assets/30.png)

3. `update mysql.user set authentication_string=password('密碼') where user='使用者' and host='ip';`

## 忘記原密碼

當在連接資料庫時MySQL服務器時直接跳過權限驗證，任何用戶都可以在不需密碼的情況下直接登入

*^tab^*

> **services.msc查看服務 ❯**
>
> ![找尋MySQL服務](mysql_basic.assets/螢幕擷取畫面 2024-04-01 230414.png)
>
> 1. 使用Windows+R輸入services.msc查看服務
> 2. 打開終端機，關閉MySQL服務`net stop mysql57`(輸入的服務名稱要相同)
> 3. 跳過權限驗證`mysqld --console --skip-grant-tables --shared-memory` 
>
> > [!WARNING]
> >
> > 需用管理員權限開啟PowerShell或是終端機

> **登入MySQL修改密碼**
>
> 1. 打開終端機，輸入`mysql`便可直接登入
> 2. 修改密碼`update mysql.user set authentication_string=password('密碼') where user='使用者' and host='ip';`
> 3. 刷新權限`flush privileges;`
> 4. 在終端機重新啟動MySQL服務`net start MySql57`

## 授權與回收

*^tab^*

> **授權**
>
> * `grant 權限1,權限2... on 資料庫 to '使用者'`
> * `grant 權限1,權限2... on 資料庫 to '使用者'@'%' identified by 'password';`
>     * `all privilege`：代表所有權限
>     * `*.*`：代表所有資料庫的所有表
>
> *==建立使用者，授予查、修改權限，登錄密碼1234，任一主機登入==*
>
> ```sql
> grant select,update on db1.employee to 'james'@'%' identified by '1234'
> ```

> **回收**
>
> * `revoke all privileges on *.* from 'james'@'%';`(還是可以登入)
> * `revoke select,update on db1.employee from 'james'@'%';`
> * `delete from mysql.user where user='james';`直接刪除這個用戶

> [!WARNING]
>
> 必須要刷新權限才會生效`flush privileges;`

