package com.spring.week01.prac;

public class Course {
//    public String title;
//    public String tutor;
//    public int days;

    private String title;
    private String tutor;
    private int days;

    public void setTitle(String title) {
        this.title = title;
    }

    public void setTutor(String tutor) {
        this.tutor = tutor;
    }

    public void setDays(int days) {
        this.days = days;
    }

    public String getTitle() {
        return this.title;
    }

    public String getTutor() {
        return this.tutor;
    }

    public int getDays() {
        return this.days;
    }
}
