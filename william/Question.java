package org.william;

public class Question{

    private int question_id;
    private String question_text;
    private String option_one;
    private String option_twe;
    private String option_three;
    private String option_four;
    private String answer;


    public int getId(){
        return question_id;
    }
    public String getQuestion(){
        return question_text;
    }
    public String getOption_one(){
        return option_one;
    }
    public String getOption_twe(){
        return option_twe;
    }
    public String getOption_three(){
        return option_three;
    }
    public String getOption_four(){
        return option_four;
    }
    public String getAnswer(){
        return answer;
    }

    public Question(){

    }
    public Question(int question_id,String question_text,String option_one,String option_twe,String option_three,String option_four,String answer){
        this.question_id   = question_id;
        this.question_text = question_text;
        this.option_one    = option_one;
        this.option_twe    = option_twe;
        this.option_three  = option_three;
        this.option_four   = option_four;
        this.answer        = answer;
    }
    public static void main(String[] args){

    }
}
