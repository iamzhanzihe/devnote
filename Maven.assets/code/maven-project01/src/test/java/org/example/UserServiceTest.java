package org.example;

import org.junit.jupiter.api.Test;

public class UserServiceTest  {

    @Test
    public void testGetGender(){
        String gender = new UserService().getGender("C123456789");
    }
}
