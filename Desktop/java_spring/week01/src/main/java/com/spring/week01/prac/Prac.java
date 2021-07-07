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

    public static int countFruit(String fruit) {
        List<String> fruits = new ArrayList<>();
        fruits.add("감");
        fruits.add("배");
        fruits.add("감");
        fruits.add("딸기");
        fruits.add("수박");
        fruits.add("메론");
        fruits.add("수박");
        fruits.add("딸기");
        fruits.add("메론");
        fruits.add("수박");
        fruits.add("메론");
        fruits.add("수박");
        fruits.add("감");

        int cnt = 0;
        for (String i :fruits) {
            if (i == fruit) {
                cnt++;
            }
        }
        return cnt;
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

        List<String> fruits = new ArrayList<>();
        fruits.add("감");
        fruits.add("배");
        fruits.add("감");
        fruits.add("딸기");
        fruits.add("수박");
        fruits.add("메론");
        fruits.add("수박");
        fruits.add("딸기");
        fruits.add("메론");
        fruits.add("수박");
        fruits.add("메론");
        fruits.add("수박");
        fruits.add("감");
        System.out.println(fruits);

        for (String fruit : fruits) {
            System.out.println(fruit);
        }

        int age = 20;
        if (age > 19) {
            System.out.println("성인입니다.");
        } else {
            System.out.println("미성년자입니다.");
        }

        int melon = countFruit("메론");
        System.out.println(melon);

        Course course = new Course();
        course.setTitle("웹개발의 봄, spring");
        System.out.println(course.getTitle());
        System.out.println(course.getTutor());

    }
}
