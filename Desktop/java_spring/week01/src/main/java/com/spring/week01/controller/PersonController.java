package com.spring.week01.controller;

import com.spring.week01.prac.Person;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class PersonController {
    @GetMapping("/myinfo")
    public Person getPersons() {
        Person person = new Person();
        person.setName("문승현");
        person.setAge(30);
        person.setAddress("서울시");
        person.setJob("개발자");
        return person;
    }
}
