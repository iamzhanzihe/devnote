package org.example;

import java.time.LocalDate;
import java.time.Period;
import java.time.format.DateTimeFormatter;

public class UserService {

    /**
     * 給定一個字串，計算出該字串的長度
     * @param input 輸入字串
     */
    public Integer getLength(String input){
        if (input == null) {
            throw new IllegalArgumentException("輸入字串不能為空");
        }
        return input.length();
    }

    /**
     * 給定一個身分證字號，計算出該用戶的性別
     * @param idCard 身分證字號 (格式: A123456789)
     */
    public String getGender(String idCard){
        if (idCard == null || idCard.length() != 10) {
            throw new IllegalArgumentException("無效的身分證字號");
        }

        // 台灣身分證字號第2碼為性別碼：1為男性，2為女性
        char genderCode = idCard.charAt(1);
        if (genderCode == '1') {
            return "男";
        } else if (genderCode == '2') {
            return "女";
        } else {
            throw new IllegalArgumentException("無效的性別碼");
        }
    }
}
