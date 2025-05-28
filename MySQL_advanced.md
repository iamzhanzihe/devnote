---
title: MySQL學習筆記
vlook-header-dup: 增;查;改;刪;練習資料
vlook-doc-lib:
- [快速的筆記網站跳轉](index.html?target=_self "可以快速挑轉到想要的網頁")
- [MySQL資料庫★基礎](MySQL_basic.html?target=_self "MySQL資料庫★基礎")
- [MySQL資料庫★進階](MySQL_advanced.html?target=_self "MySQL資料庫★進階")
- [MySQL資料庫★營運](MySQL_ops.html?target=_self "MySQL資料庫★營運")

---

###### 


[TOC]

###### MySQL學習筆記<br>**JamesZhan**<br>*不允許複製下載`僅供閱覽`*_~Og~_ *版本日期`2025年5月26日`*_~Gn~_

# 事務、視圖、觸發器

## 事務

* 什麼是事務?
    * 資料庫事務通常指對資料庫進行讀或寫的一個操作過程。
    * 為資料庫操作提供了一個從失敗中恢復到正常狀態的方法，同時提供了資料庫即使在異常狀態下仍能保持一致性的方法
    * 當多個應用程式在並行訪問資料庫時，可以在這些應用程式間提供一個隔離方法，防止彼此的操作互相干擾
* 事務的特性（ACID）
    * 原子性(Atomicity)：事務必須是原子工作單元，一個事務中的所有語句要就全做，否則一個都不做
    * 一致性(Consistency)：讓資料保持邏輯上的“合理性”
    * 隔離性(Isolation)：如果多個事務同時並行執行，彷彿每個事務各自獨立執行一樣
    * 持久性(Durability)：一個事務執行成功，則對資料來說應該是一個明確的硬碟資料更改（而不僅僅是記憶體中的變化）。

> [!WARNING]
>
> 要使用事務的話，表引擎要為innodb引擎

* 事務的開啟：`begin;` `start transaction;`
* 事務的提交：`commit;`
* 事務的回滾：`rollback;`

*==創建帳戶表模擬轉帳==*

```sql
create table account (
	id tinyint(5) zerofill auto_increment primary key comment 'id編號',
	name varchar(20) default null comment '客戶姓名',
	money decimal(10,2) not null comment '帳戶金額',
)engine=innodb charset=utf8;
```

