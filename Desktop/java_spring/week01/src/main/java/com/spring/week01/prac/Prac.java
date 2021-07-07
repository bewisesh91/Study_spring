package com.spring.week01.prac;

import java.util.ArrayList;
import java.util.List;

public class Prac {
    public static void printInfo() {
        String title = "웹개발의 봄 Spring";
        String tutor = "Spring Pro";
        int weeks = 5;
        float ratings = 5.0f;

        System.out.println("제목: " + title);
        System.out.println("튜터: " + tutor);
        System.out.println("주차: " + weeks);
        System.out.println("별점: " + ratings);
    }


    public static void main(String[] args) {
        System.out.println("Hello, World");
        System.out.println("Hello, Java");

        List<String> myList = new ArrayList<>();
        String course1 = "웹개발의 봄 Spring";
        String course2 = "프론트엔드의 꽃 React";

        myList.add(course1);
        myList.add(course2);

        System.out.println(myList);
        System.out.println(myList.get(0));
        myList.remove(1);
        System.out.println(myList);

        printInfo();
    }
}
